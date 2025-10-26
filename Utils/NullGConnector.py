import os
from typing import List, Union

import requests
from pydantic import TypeAdapter

from NullgModels.ServerModels import ServerResponseItem
import NullgModels.BattletechModels as BattletechModels
import NullgModels.HardwarModels as HardwarModels
import NullgModels.EquipmentModels as EquipmentModels


class NullGConnector:
    """Client connector for the NullG Tech API.

    This class provides a Python interface to the NullG Tech API, which serves
    Battletech game data including units, equipment, box sets, Master Unit List
    entries, eras, and other game resources. It handles REST API calls,
    response parsing, and automatic model validation using Pydantic.

    The connector supports:
    - Unit searching and retrieval with expansion options
    - Equipment database queries
    - Box set lookups
    - Master Unit List (MUL) searches
    - Era information by year or ID
    - Generic resource reading

    Attributes:
        base_url (str): Base URL for the API endpoint. Defaults to local development
                       server but can be configured for production.

    Examples:
        >>> # Connect to production API
        >>> api = NullGConnector(base_url="https://api.nullg.tech")

        >>> # Search for units
        >>> units = api.search_units({
        ...     "payload": {
        ...         "filter": {"name": "Warhammer", "unitTypeId": 2},
        ...         "project": {"name": 1, "bv": 1}
        ...     }
        ... })

        >>> # Get unit by ID with full expansion
        >>> unit = api.get_unit_by_id({
        ...     "id": "78a802b4-2d25-4750-b6fd-2dad78a88531",
        ...     "expand": True
        ... })

        >>> # Search equipment
        >>> equipment = api.search_equipment({
        ...     "payload": {"filter": {"name": "AC/10 Ammo"}}
        ... })

    Note:
        All methods return lists of parsed Pydantic model objects. The specific
        model type is determined by the API response's itemClass field and
        automatically mapped to the appropriate model from BattletechModels,
        HardwarModels, or EquipmentModels.
    """

    base_url = None
    api_key = None

    def __init__(self, base_url: str = 'http://127.0.0.1:8000', api_key: str = None) -> None:
        """Initialize the NullG API connector.

        Args:
            base_url (str, optional): Base URL for the API endpoint.
                                     Defaults to 'http://127.0.0.1:8000' for local development.
                                     Use 'https://api.nullg.tech' for production.
            api_key (str): API key for authentication. Defaults to None.

        Examples:
            >>> # Local development
            >>> api = NullGConnector()

            >>> # Production API
            >>> api = NullGConnector(base_url="https://api.nullg.tech")
        """
        self.base_url = base_url
        self.api_key = api_key

    def get_unit_by_id(self, params) -> List:
        """Retrieve a specific unit by its unique identifier.

        Fetches a single unit from the database using its UUID. Optionally
        expands related data like equipment details, faction information, etc.

        Args:
            params (dict): Dictionary containing:
                - id (str): UUID of the unit to retrieve
                - expand (bool): Whether to expand nested/related data

        Returns:
            List: List containing the parsed unit model object(s). Type depends
                 on unit type (UnitData, UnitDataExtended, etc.)

        Raises:
            ValueError: If no unit is found with the given ID or if the response
                       is invalid.

        Examples:
            >>> api = NullGConnector()
            >>> params = {
            ...     "id": "78a802b4-2d25-4750-b6fd-2dad78a88531",
            ...     "expand": True
            ... }
            >>> units = api.get_unit_by_id(params)
            >>> print(units[0].name, units[0].model)
        """
        unit_id = params['id']
        expand = params['expand']
        endpoint = f'/v4/unit/find'
        query_params = {'item_id': unit_id, 'expand': expand}
        response = self._make_rest_call(endpoint, params=query_params)
        models = self._parse_items(response)
        return models

    def search_units(self, params) -> List:
        """Search for units using complex filter criteria.

        Performs a filtered search across the unit database using MongoDB-style
        query syntax. Supports filtering by name, type, stats, equipment, and
        nested properties. Can include projection to limit returned fields.

        Args:
            params (dict): Dictionary containing:
                - payload (dict): SearchFilter object as dict with:
                    - filter (dict): MongoDB query filter
                    - project (dict, optional): Field projection
                    - page (int, optional): Page number
                    - itemsPerPage (int, optional): Results per page

        Returns:
            List: List of parsed unit model objects matching the filter criteria.

        Raises:
            ValueError: If no units match the filter or response is invalid.

        Examples:
            >>> # Search for Clan mechs with specific equipment
            >>> params = {
            ...     "payload": {
            ...         "filter": {
            ...             "name": "Warhammer",
            ...             "unitTypeId": 2,
            ...             "totalWar.equipmentList.name": "Heavy PPC"
            ...         },
            ...         "project": {"name": 1, "bv": 1}
            ...     }
            ... }
            >>> units = api.search_units(params)

            >>> # Search with pagination
            >>> params = {
            ...     "payload": {
            ...         "filter": {"techbase": "Clan"},
            ...         "page": 1,
            ...         "itemsPerPage": 20
            ...     }
            ... }
            >>> units = api.search_units(params)
        """
        method = 'post'
        json_data = params['payload']
        endpoint = '/v4/unit/find'
        response = self._make_rest_call(endpoint, json_data=json_data, method=method)
        models = self._parse_items(response)
        return models

    def get_box_set(self, params) -> List:
        """Retrieve box set information by barcode or ID.

        Fetches details about a Battletech product box set, including contained
        miniatures, point values, and product information.

        Args:
            params (dict): Dictionary containing:
                - boxSetId (str): Barcode or unique identifier of the box set

        Returns:
            List: List of BoxsetItem model objects for the specified box set.

        Raises:
            ValueError: If no box set is found with the given ID.

        Examples:
            >>> params = {"boxSetId": "0850011819135"}
            >>> box_sets = api.get_box_set(params)
            >>> for box_set in box_sets:
            ...     print(f"{box_set.name}: {box_set.minPoints}-{box_set.maxPoints} pts")
        """
        box_set_id = params['boxSetId']
        endpoint = f'/v4/boxset/find'
        query_params = {'item_id': box_set_id}
        response = self._make_rest_call(endpoint, params=query_params)
        models = self._parse_items(response)
        return models

    def search_mul(self, params) -> List:
        """Search the Master Unit List (MUL) database.

        Queries the official Master Unit List database for units by various
        criteria including MUL ID, NullG ID, faction availability, and more.

        Args:
            params (dict): Dictionary containing:
                - payload (dict): SearchFilter object with MUL-specific filters

        Returns:
            List: List of MULUnitItem model objects matching the search criteria.

        Raises:
            ValueError: If no MUL entries match the filter.

        Examples:
            >>> # Find MUL entry by NullG unit ID
            >>> params = {
            ...     "payload": {
            ...         "filter": {
            ...             "nullgId": "60febaa9-02a9-4da7-8180-564a35300763"
            ...         }
            ...     }
            ... }
            >>> mul_units = api.search_mul(params)
            >>> print(mul_units[0].mulId, mul_units[0].factions)
        """
        method = 'post'
        json_data = params['payload']
        endpoint = '/v4/mul/find'
        response = self._make_rest_call(endpoint, json_data=json_data, method=method)
        models = self._parse_items(response)
        return models

    def get_eras(self, params) -> List:
        """Retrieve Battletech timeline era information.

        Fetches era data by year, era ID, or custom filter criteria. Eras
        represent time periods in the Battletech universe (e.g., Succession Wars,
        Clan Invasion, Dark Age).

        Args:
            params (dict, optional): Dictionary that can contain:
                - year (int): Get eras active in a specific year
                - eraId (int): Get a specific era by ID
                - payload (dict): SearchFilter for complex era queries
                If None or empty, returns all eras.

        Returns:
            List: List of EraItem model objects.

        Raises:
            ValueError: If no eras match the criteria.

        Examples:
            >>> # Get eras for a specific year
            >>> eras = api.get_eras(params={"year": 3069})
            >>> for era in eras:
            ...     print(f"{era.name}: {era.yearStart}-{era.yearEnd}")

            >>> # Get specific era by ID
            >>> eras = api.get_eras(params={"eraId": 5})

            >>> # Get all eras
            >>> all_eras = api.get_eras(params=None)
        """
        query_params = None
        json_data = None
        method = 'get'
        endpoint = '/v4/eras/find'
        if params is not None:
            if 'year' in params:
                query_params = {'year': params['year']}
            elif 'eraId' in params:
                query_params = {'eraId': params['eraId']}
            elif 'payload' in params:
                json_data = params['payload']
                method = 'post'
        response = self._make_rest_call(endpoint, params=query_params, method=method, json_data=json_data)
        models = self._parse_items(response)
        return models

    def search_equipment(self, params) -> List:
        """Search the equipment database.

        Queries the equipment database for weapons, ammunition, and other
        equipment items using MongoDB-style filters.

        Args:
            params (dict): Dictionary containing:
                - payload (dict): SearchFilter object with equipment-specific filters

        Returns:
            List: List of EquipmentItem model objects matching the search.

        Raises:
            ValueError: If no equipment matches the filter.

        Examples:
            >>> # Search for specific ammo
            >>> params = {
            ...     "payload": {
            ...         "filter": {"name": "AC/10 Ammo"},
            ...         "project": {"name": 1, "item": 1}
            ...     }
            ... }
            >>> equipment = api.search_equipment(params)

            >>> # Search by equipment type
            >>> params = {
            ...     "payload": {
            ...         "filter": {"item.type": "weapon"}
            ...     }
            ... }
            >>> weapons = api.search_equipment(params)
        """
        method = 'post'
        json_data = params['payload']
        endpoint = '/v4/equipment/find'
        response = self._make_rest_call(endpoint, json_data=json_data, method=method)
        return self._parse_items(response)

    def read_resource(self, params) -> List:
        """Read a generic resource list from the API.

        Retrieves reference data lists such as unit types, factions, roles,
        weight classes, and other enumeration-style resources.

        Args:
            params (dict): Dictionary containing:
                - resource (str): Name of the resource to retrieve
                              (e.g., "unit_types", "factions", "roles")

        Returns:
            List: List of resource items (typically BasicItem or dict objects).

        Raises:
            ValueError: If the resource name is invalid or not found.

        Examples:
            >>> # Get list of unit types
            >>> unit_types = api.read_resource(params={"resource": "unit_types"})
            >>> for ut in unit_types:
            ...     print(f"{ut['id']}: {ut['name']}")

            >>> # Get factions list
            >>> factions = api.read_resource(params={"resource": "factions"})
        """
        method = 'get'
        endpoint = f'/v4/resources/list/{params["resource"]}'
        response = self._make_rest_call(endpoint, method=method)
        return self._parse_items(response)

    def _make_rest_call(self, endpoint, params=None, data=None, json_data=None, method='get'):
        """Make an HTTP request to the API.

        Internal method that handles the actual HTTP communication with the API,
        including authentication, headers, and request construction.

        Args:
            endpoint (str): API endpoint path (e.g., '/v4/unit/find')
            params (dict, optional): URL query parameters
            data (any, optional): Form data for the request
            json_data (dict, optional): JSON payload for POST requests
            method (str, optional): HTTP method ('get', 'post', etc.). Defaults to 'get'.

        Returns:
            ServerResponseItem: Parsed response from the API.

        Raises:
            ValueError: If the HTTP method is invalid, response status is not 200,
                       or response format is invalid.

        Note:
            This method includes a hardcoded API key for authentication. In production,
            this should be moved to environment variables or secure configuration.
        """
        url = f'{self.base_url}{endpoint}'
        header = {
            'Content-Type': 'application/json',
            'X-API-Key': self.api_key
        }
        try:
            request_method = getattr(requests, method)
        except AttributeError:
            raise ValueError('Invalid method')

        response = request_method(
            url,
            params=params,
            data=data,
            json=json_data,
            headers=header
        )
        return self._parse_response(response)

    def _parse_response(self, response) -> ServerResponseItem:
        """Parse and validate the HTTP response from the API.

        Internal method that validates the response status and content type,
        then deserializes the JSON into a ServerResponseItem model.

        Args:
            response: requests.Response object from the HTTP call

        Returns:
            ServerResponseItem: Validated Pydantic model containing the response data.

        Raises:
            ValueError: If response status is not 200 or content type is not JSON.
        """
        if response.status_code != 200:
            raise ValueError('Invalid response')
        headers = response.headers
        if 'json' in headers['Content-Type']:
            returnData = ServerResponseItem.model_validate_json(response.text)
            return returnData
        else:
            raise ValueError('Invalid response')

    def _parse_items(self, results: ServerResponseItem) -> List:
        """Parse and validate items from the API response.

        Internal method that extracts items from the ServerResponseItem,
        determines the appropriate Pydantic model class, and validates/parses
        each item into that model type.

        Args:
            results (ServerResponseItem): Parsed API response containing items to process.

        Returns:
            List: List of validated Pydantic model objects of the appropriate type.

        Raises:
            ValueError: If no results are found, item class is invalid, or
                       validation fails.

        Note:
            The item class is automatically determined from the response's itemClass
            field and mapped to models in BattletechModels, HardwarModels, or
            EquipmentModels modules.
        """
        if results.totalItems == 0:
            raise ValueError(
                f'No results found for {results.itemClass} with filter {results.filter}'
            )
        items = results.items
        itemClass = self._get_item_class(results.itemClass)
        adapter = TypeAdapter(List[itemClass])
        models: List[itemClass] = adapter.validate_python(items)
        return models

    def _get_item_class(self, itemClassStr: str) -> Union[object, None]:
        """Resolve item class name to actual Python class.

        Internal method that maps a string class name from the API response
        to the corresponding Pydantic model class.

        Args:
            itemClassStr (str): Name of the class as returned by the API
                              (e.g., 'UnitData', 'EquipmentItem', 'BoxsetItem')

        Returns:
            Union[object, None]: The corresponding Python class object.

        Raises:
            ValueError: If the item class string doesn't match any known model.

        Note:
            Searches for the class in the following order:
            1. BattletechModels module
            2. HardwarModels module
            3. EquipmentModels module
            4. Built-in dict type (for generic responses)
        """
        itemClass = None
        if hasattr(BattletechModels, itemClassStr):
            itemClass = getattr(BattletechModels, itemClassStr)
        elif hasattr(HardwarModels, itemClassStr):
            itemClass = getattr(HardwarModels, itemClassStr)
        elif hasattr(EquipmentModels, itemClassStr):
            itemClass = getattr(EquipmentModels, itemClassStr)
        elif itemClassStr == 'dict':
            itemClass = dict
        else:
            raise ValueError(f'Invalid item class {itemClass}')
        return itemClass