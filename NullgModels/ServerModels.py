from NullgModels.EquipmentModels import EquipmentItem
from NullgModels.HardwarModels import *
from NullgModels.BattletechModels import *
from pydantic import BaseModel, ConfigDict, Field

from NullgModels.InnerSphereMapModels import InnerSphereFactionRecord, StarSystemControlHistoryRecord, StarSystem
from NullgModels.UploadModels import UploadUnitData

# -----------------------------
# Allowed MongoDB operators
# -----------------------------
ALLOWED_OPERATORS = {
    "$eq", "$ne", "$gt", "$gte", "$lt", "$lte",
    "$in", "$nin", "$regex", "$exists",
    "$and", "$or", "$nor", "$not"
}

DISALLOWED_OPERATORS = {
    '$merge', '$out'
}

# -----------------------------
# Recursive filter validator
# -----------------------------
def validate_filter(filter_dict: Any):
    """Recursively validate MongoDB filter structure for security.
    
    Ensures that only allowed MongoDB query operators are used in filter
    expressions to prevent potentially dangerous operations.
    
    Args:
        filter_dict: MongoDB filter dictionary, list, or scalar value to validate.
        
    Raises:
        ValueError: If a disallowed operator is found in the filter.
        
    Note:
        This function recursively validates nested structures including
        dictionaries and lists to ensure comprehensive security checking.
    """
    if isinstance(filter_dict, dict):
        for key, value in filter_dict.items():
            # Check for disallowed top-level operators
            if key.startswith("$") and key not in ALLOWED_OPERATORS:
                raise ValueError(f"Operator '{key}' is not allowed.")

            # Recurse into nested dicts or lists
            if isinstance(value, (dict, list)):
                validate_filter(value)
    elif isinstance(filter_dict, list):
        for item in filter_dict:
            validate_filter(item)
    # Scalars (str, int, etc.) are safe

def validate_pipeline(pipeline_list: Any):
    """Recursively validate MongoDB aggregation pipeline structure for security.
    
    Ensures that dangerous aggregation stages like $merge and $out are not
    used in pipeline expressions.
    
    Args:
        pipeline_list: MongoDB pipeline list, dictionary, or nested structure to validate.
        
    Raises:
        ValueError: If a disallowed operator is found in the pipeline.
        
    Note:
        This function prevents write operations in aggregation pipelines
        that could modify the database.
    """
    if isinstance(pipeline_list, dict):
        for key, value in pipeline_list.items():
            # Check for disallowed top-level operators
            if key.startswith("$") and key in DISALLOWED_OPERATORS:
                raise ValueError(f"Aggregate Operator '{key}' is not allowed.")

            # Recurse into nested dicts or lists
            if isinstance(value, (dict, list)):
                validate_pipeline(value)
    elif isinstance(pipeline_list, list):
        for item in pipeline_list:
            validate_pipeline(item)
    # Scalars (str, int, etc.) are safe


class SearchFilter(BaseModel):
    """MongoDB query filter with pagination and projection support.
    
    This model encapsulates a complete MongoDB find() query including
    filtering criteria, field projection, and pagination parameters.
    Used for searching and retrieving data from collections.
    
    Attributes:
        filter: MongoDB query filter using standard MongoDB query syntax.
               Supports comparison, logical, and text search operators.
        project: Optional field projection to control which fields are returned.
                Use 1/True to include fields, 0/False to exclude fields.
        page: Current page number for pagination (1-indexed).
        itemsPerPage: Maximum number of items to return per page.
        
    Examples:
        >>> # Simple equality search
        >>> SearchFilter(filter={"name": "Warhammer"})
        
        >>> # Range query with projection
        >>> SearchFilter(
        ...     filter={"mass": {"$gte": 50, "$lte": 75}},
        ...     project={"name": 1, "mass": 1, "bv": 1},
        ...     page=1,
        ...     itemsPerPage=20
        ... )
        
        >>> # Complex query with logical operators
        >>> SearchFilter(filter={
        ...     "$and": [
        ...         {"techbase": "Inner Sphere"},
        ...         {"bv": {"$gte": 1500}}
        ...     ]
        ... })
        
        >>> # Text search with regex
        >>> SearchFilter(filter={"name": {"$regex": "Atlas"}})
    """
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    filter: Dict = Field(
        description="MongoDB query filter using standard query operators. "
                   "Supports $eq, $ne, $gt, $gte, $lt, $lte, $in, $nin, $regex, "
                   "$exists, $and, $or, $nor, $not. Use dot notation for nested fields.",
        default=dict,
        examples=[
            {"name": "Warhammer"},
            {"totalWar.walkMp": {"$gte": 5}},
            {"$and": [{"alphaStrike.size": 2}, {"alphaStrike.damageShort": {"$gte": 3}}]},
            {"name": {"$regex": "Atlas", "$options": "i"}}
        ])
    project: Optional[Dict[str, Union[int, bool]]] = Field(
        description="MongoDB field projection to control returned fields. "
                   "Use 1 or True to include a field, 0 or False to exclude it. "
                   "By default, all fields are returned. Use dot notation for nested fields.",
        default=None,
        examples=[
            {"name": 1, "totalWar.equipmentList": 1, "alphaStrike": 0},
            {"fullName": 1, "id": 1, "bv": 1},
            {"_id": 0, "name": 1, "mass": 1}
        ])
    page: Optional[int] = Field(
        description="Page number to retrieve (1-indexed). Used for pagination of results.",
        default=1,
        ge=1,
        le=1000,
        examples=[1, 2, 3]
    )
    itemsPerPage: Optional[int] = Field(
        description="Maximum number of items to return per page. Controls page size for pagination.",
        default=50,
        ge=10,
        le=100,
        examples=[10, 20, 50, 100]
    )

    @field_validator("itemsPerPage", mode="before")
    @classmethod
    def validate_items_per_page(cls, v):
        return max(min(v, 100), 1) if v is not None else v

    @field_validator("page", mode="before")
    @classmethod
    def validate_page(cls, v):
        return max(min(v, 1000), 1) if v is not None else v

    def validate_security(self):
        """Validate the filter for security compliance.
        
        Checks that only allowed MongoDB operators are used in the filter
        to prevent potentially dangerous operations.
        
        Raises:
            ValueError: If the filter contains disallowed operators.
        """
        validate_filter(self.filter)


class PipelineFilter(BaseModel):
    """MongoDB aggregation pipeline with pagination support.
    
    This model encapsulates a MongoDB aggregation pipeline for performing
    complex data transformations, analytics, and multi-stage processing.
    Used for advanced queries that require grouping, sorting, joining, or
    statistical calculations.
    
    Attributes:
        pipeline: List of aggregation stages in MongoDB pipeline format.
                 Each stage is a dictionary with a stage operator and its parameters.
        page: Current page number for result pagination.
        itemsPerPage: Maximum number of results to return.
        
    Examples:
        >>> # Group units by faction and count
        >>> PipelineFilter(pipeline=[
        ...     {"$unwind": "$factions"},
        ...     {"$group": {"_id": "$factions", "count": {"$sum": 1}}},
        ...     {"$sort": {"count": -1}}
        ... ])
        
        >>> # Calculate average BV by weight class
        >>> PipelineFilter(pipeline=[
        ...     {"$group": {
        ...         "_id": "$weightClassId",
        ...         "avgBV": {"$avg": "$bv"},
        ...         "count": {"$sum": 1}
        ...     }},
        ...     {"$sort": {"_id": 1}}
        ... ])
        
        >>> # Filter and project in stages
        >>> PipelineFilter(pipeline=[
        ...     {"$match": {"techbase": "Clan"}},
        ...     {"$project": {"name": 1, "bv": 1, "mass": 1}},
        ...     {"$sort": {"bv": -1}},
        ...     {"$limit": 10}
        ... ])
    """
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    pipeline: List[Dict[str, Any]] = Field(
        description="MongoDB aggregation pipeline as a list of stage dictionaries. "
                   "Each stage performs a specific operation (match, group, sort, project, etc.). "
                   "Stages are executed sequentially. Disallowed stages: $merge, $out.",
        default=None,
        examples=[
            [{"$match": {"mass": {"$gte": 50}}}, {"$group": {"_id": "$weightClassId", "count": {"$sum": 1}}}],
            [{"$unwind": "$factions"}, {"$group": {"_id": "$factions", "avgBV": {"$avg": "$bv"}}}]
        ]
    )
    page: Optional[int] = Field(
        description="Page number for pagination of aggregation results (1-indexed).",
        default=1,
        ge=1,
        le=1000
    )
    itemsPerPage: Optional[int] = Field(
        description="Maximum number of aggregation results to return.",
        default=50,
        ge=1,
        le=100
    )

    @field_validator("itemsPerPage", mode="before")
    @classmethod
    def validate_items_per_page(cls, v):
        return max(min(v, 100), 1) if v is not None else v

    @field_validator("page", mode="before")
    @classmethod
    def validate_page(cls, v):
        return max(min(v, 100), 1) if v is not None else v

    def validate_security(self):
        """Validate the pipeline for security compliance.
        
        Checks that no dangerous write operations ($merge, $out) are used
        in the aggregation pipeline.
        
        Raises:
            ValueError: If the pipeline contains disallowed operators.
        """
        validate_pipeline(self.pipeline)


class DataResultItem(BaseModel):
    """Standardized response wrapper for API query results.
    
    This model provides a consistent structure for all API responses,
    including pagination metadata, result items, and operation status
    information. Used as the return type for all search and retrieval
    endpoints.
    
    Attributes:
        currentPage: Current page number in the result set.
        totalPages: Total number of pages available for the query.
        itemsPerPage: Number of items included per page.
        totalItems: Total count of items matching the query across all pages.
        itemClass: Name of the class/type of items in the results list.
        items: List of result items (type varies based on query).
        status: Operation status indicator (success, failure, etc.).
        message: Human-readable message describing the operation result.
        
    Examples:
        >>> # Successful query with results
        >>> DataResultItem(
        ...     currentPage=1,
        ...     totalPages=5,
        ...     itemsPerPage=50,
        ...     totalItems=237,
        ...     itemClass="UnitData",
        ...     items=[...],  # List of UnitData objects
        ...     status="success",
        ...     message="operation was successful"
        ... )
        
        >>> # Empty result set
        >>> DataResultItem(
        ...     currentPage=1,
        ...     totalPages=0,
        ...     itemsPerPage=50,
        ...     totalItems=0,
        ...     itemClass="UnitData",
        ...     items=[],
        ...     status="success",
        ...     message="No results found"
        ... )
        
        >>> # Error response
        >>> DataResultItem(
        ...     status="failure",
        ...     message="Invalid query operator"
        ... )
    """
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    currentPage: int = Field(
        description="Current page number of results being returned (1-indexed).",
        default=0
    )
    totalPages: int = Field(
        description="Total number of pages available for this query result set.",
        default=0
    )
    itemsPerPage: int = Field(
        description="Number of items included in each page of results.",
        default=50,
        ge=10,
        le=200
    )
    totalItems: int = Field(
        description="Total count of items matching the query criteria across all pages.",
        default=0
    )
    itemClass: str = Field(
        description="Class name of the items contained in the results list "
                   "(e.g., 'UnitData', 'EquipmentItem', 'BasicItem', 'Dict').",
        default=""
    )
    items: List[Union[
        EraItem,
        EquipmentItem,
        UnitData,
        BasicItem,
        MULUnitItem,
        BoxsetItem,
        ElementData,
        UnitDataExtended,
        StarSystem,
        StarSystemControlHistoryRecord,
        InnerSphereFactionRecord,
        Dict]
    ] = Field(
        description="List of result items. Type varies based on the query endpoint. "
                   "Check itemClass field to determine the actual type of items.",
        default=[]
    )
    status: str = Field(
        description="Operation status indicator. Common values: 'success', 'failure', 'not completed'.",
        default="not completed"
    )
    message: str = Field(
        description="Human-readable message describing the operation result or any errors encountered.",
        default="Empty results"
    )


class ServerResponseItem(BaseModel):
    """Generic server response wrapper for non-typed results.
    
    Similar to DataResultItem but returns items as generic dictionaries
    rather than typed model objects. Used for aggregation results and
    other queries where the result structure is dynamic.
    
    Attributes:
        currentPage: Current page number in the result set.
        totalPages: Total number of pages available.
        itemsPerPage: Number of items per page.
        totalItems: Total count of matching items.
        itemClass: Type indicator for the items (typically "Dict").
        items: List of result dictionaries with dynamic structure.
        status: Operation status indicator.
        message: Human-readable status message.
        
    Examples:
        >>> # Aggregation results
        >>> ServerResponseItem(
        ...     currentPage=1,
        ...     totalPages=1,
        ...     itemsPerPage=50,
        ...     totalItems=12,
        ...     itemClass="Dict",
        ...     items=[
        ...         {"_id": 1, "count": 45, "avgBV": 1523},
        ...         {"_id": 2, "count": 67, "avgBV": 1789}
        ...     ],
        ...     status="success",
        ...     message="Aggregation completed"
        ... )
    """
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    currentPage: int = Field(
        description="Current page number of results (1-indexed).",
        default=0
    )
    totalPages: int = Field(
        description="Total number of pages in the result set.",
        default=0
    )
    itemsPerPage: int = Field(
        description="Number of items per page.",
        default=50,
        ge=10,
        le=200
    )
    totalItems: int = Field(
        description="Total count of items across all pages.",
        default=0
    )
    itemClass: str = Field(
        description="Class name indicator, typically 'Dict' for generic responses.",
        default=""
    )
    items: List[Dict] = Field(
        description="List of result dictionaries. Structure varies based on query or aggregation.",
        default=[]
    )
    status: str = Field(
        description="Operation status: 'success', 'failure', etc.",
        default="not completed"
    )
    message: str = Field(
        description="Status message or error description.",
        default="Empty results"
    )


class UploadItem(BaseModel):
    """Container for uploading items to the database.
    
    This model wraps items being uploaded to the API, providing metadata
    about the item type and the items themselves. Used for bulk upload
    operations and data imports.
    
    Attributes:
        itemClass: Class name of the items being uploaded (e.g., "UploadUnitData").
        items: List of items to upload, typed according to itemClass.
        
    Examples:
        >>> # Upload unit data
        >>> UploadItem(
        ...     itemClass="UploadUnitData",
        ...     items=[
        ...         UploadUnitData(name="Custom Mech", mass=75, ...),
        ...         UploadUnitData(name="Another Mech", mass=50, ...)
        ...     ]
        ... )
        
    Note:
        Upload endpoints typically require special API key permissions
        and perform strict validation on uploaded data.
    """
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    itemClass: str = Field(
        description="Model class name indicating the type of items being uploaded. "
                   "Must match the actual type of objects in the items list.",
        default=""
    )
    items: List[Union[UploadUnitData]] = Field(
        description="List of items to upload. Type should match the itemClass field.",
        default=[]
    )
