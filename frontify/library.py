# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import AssetStatusType, CopyrightStatus, TagSource, WorkflowStatusEnterRule


class Library(BaseModel):
    library: Optional["LibraryLibrary"]


class LibraryLibrary(BaseModel):
    typename__: Literal[
        "DocumentLibrary", "IconLibrary", "Library", "LogoLibrary", "MediaLibrary"
    ] = Field(alias="__typename")
    id: str
    name: str
    color: Optional["LibraryLibraryColor"]
    assets: "LibraryLibraryAssets"
    licenses: Optional[List[Optional["LibraryLibraryLicenses"]]]
    collections: "LibraryLibraryCollections"
    browse: "LibraryLibraryBrowse"
    collaborators: Optional["LibraryLibraryCollaborators"]
    current_user_permissions: "LibraryLibraryCurrentUserPermissions" = Field(
        alias="currentUserPermissions"
    )
    workflow: "LibraryLibraryWorkflow"
    custom_metadata_properties: List["LibraryLibraryCustomMetadataProperties"] = Field(
        alias="customMetadataProperties"
    )
    asset_submission_requests: List["LibraryLibraryAssetSubmissionRequests"] = Field(
        alias="assetSubmissionRequests"
    )


class LibraryLibraryColor(BaseModel):
    red: Any
    green: Any
    blue: Any
    alpha: Any


class LibraryLibraryAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[List[Optional["LibraryLibraryAssetsItems"]]]


class LibraryLibraryAssetsItems(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: "LibraryLibraryAssetsItemsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["LibraryLibraryAssetsItemsModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[List[Optional["LibraryLibraryAssetsItemsAttachments"]]]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[List[Optional["LibraryLibraryAssetsItemsTags"]]]
    copyright: Optional["LibraryLibraryAssetsItemsCopyright"]
    availability: "LibraryLibraryAssetsItemsAvailability"
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[List[Optional["LibraryLibraryAssetsItemsLicenses"]]]
    status: AssetStatusType
    related_assets: "LibraryLibraryAssetsItemsRelatedAssets" = Field(
        alias="relatedAssets"
    )
    comments: Optional["LibraryLibraryAssetsItemsComments"]
    current_user_permissions: "LibraryLibraryAssetsItemsCurrentUserPermissions" = Field(
        alias="currentUserPermissions"
    )
    custom_metadata: List["LibraryLibraryAssetsItemsCustomMetadata"] = Field(
        alias="customMetadata"
    )
    workflow_task: Optional["LibraryLibraryAssetsItemsWorkflowTask"] = Field(
        alias="workflowTask"
    )
    variants: Optional["LibraryLibraryAssetsItemsVariants"]
    location: "LibraryLibraryAssetsItemsLocation"
    preview_background_color: Optional[
        "LibraryLibraryAssetsItemsPreviewBackgroundColor"
    ] = Field(alias="previewBackgroundColor")


class LibraryLibraryAssetsItemsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class LibraryLibraryAssetsItemsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class LibraryLibraryAssetsItemsAttachments(BaseModel):
    id: str
    creator: "LibraryLibraryAssetsItemsAttachmentsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["LibraryLibraryAssetsItemsAttachmentsModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: Optional[str]
    filename: Optional[str]
    type: Optional[str]
    external_id: Optional[str] = Field(alias="externalId")
    extension: Optional[str]
    size: Optional[Any]
    download_url: Optional[Any] = Field(alias="downloadUrl")


class LibraryLibraryAssetsItemsAttachmentsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class LibraryLibraryAssetsItemsAttachmentsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class LibraryLibraryAssetsItemsTags(BaseModel):
    value: str
    source: Optional[TagSource]


class LibraryLibraryAssetsItemsCopyright(BaseModel):
    status: CopyrightStatus
    notice: Optional[str]


class LibraryLibraryAssetsItemsAvailability(BaseModel):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class LibraryLibraryAssetsItemsLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class LibraryLibraryAssetsItemsRelatedAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[List[Optional["LibraryLibraryAssetsItemsRelatedAssetsItems"]]]


class LibraryLibraryAssetsItemsRelatedAssetsItems(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    external_id: Optional[str] = Field(alias="externalId")
    expires_at: Optional[Any] = Field(alias="expiresAt")
    status: AssetStatusType


class LibraryLibraryAssetsItemsComments(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[List[Optional["LibraryLibraryAssetsItemsCommentsItems"]]]


class LibraryLibraryAssetsItemsCommentsItems(BaseModel):
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    content: str
    is_resolved: bool = Field(alias="isResolved")


class LibraryLibraryAssetsItemsCurrentUserPermissions(BaseModel):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class LibraryLibraryAssetsItemsCustomMetadata(BaseModel):
    typename__: Literal[
        "CustomMetadata", "CustomMetadataValue", "CustomMetadataValues"
    ] = Field(alias="__typename")
    property: "LibraryLibraryAssetsItemsCustomMetadataProperty"


class LibraryLibraryAssetsItemsCustomMetadataProperty(BaseModel):
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: str
    help_text: Optional[str] = Field(alias="helpText")
    is_required: bool = Field(alias="isRequired")
    default_value: Optional[Any] = Field(alias="defaultValue")


class LibraryLibraryAssetsItemsWorkflowTask(BaseModel):
    id: str
    assigned_users: List[
        Optional["LibraryLibraryAssetsItemsWorkflowTaskAssignedUsers"]
    ] = Field(alias="assignedUsers")
    asset: Optional["LibraryLibraryAssetsItemsWorkflowTaskAsset"]
    title: Optional[str]
    description: Optional[str]
    status: "LibraryLibraryAssetsItemsWorkflowTaskStatus"
    checklist_item: "LibraryLibraryAssetsItemsWorkflowTaskChecklistItem" = Field(
        alias="checklistItem"
    )


class LibraryLibraryAssetsItemsWorkflowTaskAssignedUsers(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class LibraryLibraryAssetsItemsWorkflowTaskAsset(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    external_id: Optional[str] = Field(alias="externalId")
    expires_at: Optional[Any] = Field(alias="expiresAt")
    status: AssetStatusType


class LibraryLibraryAssetsItemsWorkflowTaskStatus(BaseModel):
    id: str
    name: str
    enter_rules: List[Optional[WorkflowStatusEnterRule]] = Field(alias="enterRules")


class LibraryLibraryAssetsItemsWorkflowTaskChecklistItem(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class LibraryLibraryAssetsItemsVariants(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: List[Optional["LibraryLibraryAssetsItemsVariantsItems"]]


class LibraryLibraryAssetsItemsVariantsItems(BaseModel):
    key: str
    filename: Optional[str]
    download_url: Optional[Any] = Field(alias="downloadUrl")


class LibraryLibraryAssetsItemsLocation(BaseModel):
    brand: Optional["LibraryLibraryAssetsItemsLocationBrand"]
    library: Optional["LibraryLibraryAssetsItemsLocationLibrary"]
    workspace_project: Optional["LibraryLibraryAssetsItemsLocationWorkspaceProject"] = (
        Field(alias="workspaceProject")
    )
    folder: Optional["LibraryLibraryAssetsItemsLocationFolder"]


class LibraryLibraryAssetsItemsLocationBrand(BaseModel):
    id: str
    name: str


class LibraryLibraryAssetsItemsLocationLibrary(BaseModel):
    id: str
    name: Optional[str]


class LibraryLibraryAssetsItemsLocationWorkspaceProject(BaseModel):
    id: str
    name: Optional[str]


class LibraryLibraryAssetsItemsLocationFolder(BaseModel):
    id: str
    name: str


class LibraryLibraryAssetsItemsPreviewBackgroundColor(BaseModel):
    red: Any
    green: Any
    blue: Any
    alpha: Any


class LibraryLibraryLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class LibraryLibraryCollections(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[List[Optional["LibraryLibraryCollectionsItems"]]]


class LibraryLibraryCollectionsItems(BaseModel):
    id: str
    name: str
    assets: "LibraryLibraryCollectionsItemsAssets"


class LibraryLibraryCollectionsItemsAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class LibraryLibraryBrowse(BaseModel):
    folders: "LibraryLibraryBrowseFolders"
    assets: "LibraryLibraryBrowseAssets"


class LibraryLibraryBrowseFolders(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[List[Optional["LibraryLibraryBrowseFoldersItems"]]]


class LibraryLibraryBrowseFoldersItems(BaseModel):
    typename__: Literal["Folder", "SubFolder"] = Field(alias="__typename")
    id: str
    name: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    breadcrumbs: List["LibraryLibraryBrowseFoldersItemsBreadcrumbs"]
    folders: "LibraryLibraryBrowseFoldersItemsFolders"


class LibraryLibraryBrowseFoldersItemsBreadcrumbs(BaseModel):
    id: Optional[str]
    name: Optional[str]


class LibraryLibraryBrowseFoldersItemsFolders(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class LibraryLibraryBrowseAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class LibraryLibraryCollaborators(BaseModel):
    users: "LibraryLibraryCollaboratorsUsers"


class LibraryLibraryCollaboratorsUsers(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: List[Optional["LibraryLibraryCollaboratorsUsersItems"]]
    edges: List["LibraryLibraryCollaboratorsUsersEdges"]


class LibraryLibraryCollaboratorsUsersItems(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class LibraryLibraryCollaboratorsUsersEdges(BaseModel):
    node: "LibraryLibraryCollaboratorsUsersEdgesNode"
    role: str


class LibraryLibraryCollaboratorsUsersEdgesNode(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class LibraryLibraryCurrentUserPermissions(BaseModel):
    can_create_assets: bool = Field(alias="canCreateAssets")
    can_view_collaborators: bool = Field(alias="canViewCollaborators")
    can_create_collections: bool = Field(alias="canCreateCollections")


class LibraryLibraryWorkflow(BaseModel):
    id: str
    statuses: List[Optional["LibraryLibraryWorkflowStatuses"]]


class LibraryLibraryWorkflowStatuses(BaseModel):
    id: str
    name: str
    color: "LibraryLibraryWorkflowStatusesColor"
    assigned_users: List[Optional["LibraryLibraryWorkflowStatusesAssignedUsers"]] = (
        Field(alias="assignedUsers")
    )
    checklist_presets: List[
        Optional["LibraryLibraryWorkflowStatusesChecklistPresets"]
    ] = Field(alias="checklistPresets")
    tasks: "LibraryLibraryWorkflowStatusesTasks"
    enter_rules: List[Optional[WorkflowStatusEnterRule]] = Field(alias="enterRules")


class LibraryLibraryWorkflowStatusesColor(BaseModel):
    red: Any
    green: Any
    blue: Any
    alpha: Any


class LibraryLibraryWorkflowStatusesAssignedUsers(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class LibraryLibraryWorkflowStatusesChecklistPresets(BaseModel):
    id: str
    content: str
    assigned_user: Optional[
        "LibraryLibraryWorkflowStatusesChecklistPresetsAssignedUser"
    ] = Field(alias="assignedUser")


class LibraryLibraryWorkflowStatusesChecklistPresetsAssignedUser(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class LibraryLibraryWorkflowStatusesTasks(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[List[Optional["LibraryLibraryWorkflowStatusesTasksItems"]]]


class LibraryLibraryWorkflowStatusesTasksItems(BaseModel):
    id: str
    title: Optional[str]
    description: Optional[str]


class LibraryLibraryCustomMetadataProperties(BaseModel):
    id: str
    creator: "LibraryLibraryCustomMetadataPropertiesCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["LibraryLibraryCustomMetadataPropertiesModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: str
    type: "LibraryLibraryCustomMetadataPropertiesType"
    help_text: Optional[str] = Field(alias="helpText")
    is_required: bool = Field(alias="isRequired")
    default_value: Optional[Any] = Field(alias="defaultValue")


class LibraryLibraryCustomMetadataPropertiesCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class LibraryLibraryCustomMetadataPropertiesModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class LibraryLibraryCustomMetadataPropertiesType(BaseModel):
    typename__: Literal[
        "CustomMetadataPropertyType",
        "CustomMetadataPropertyTypeDate",
        "CustomMetadataPropertyTypeLongText",
        "CustomMetadataPropertyTypeMultiSelect",
        "CustomMetadataPropertyTypeNumber",
        "CustomMetadataPropertyTypeSelect",
        "CustomMetadataPropertyTypeText",
        "CustomMetadataPropertyTypeUrl",
    ] = Field(alias="__typename")
    name: str


class LibraryLibraryAssetSubmissionRequests(BaseModel):
    id: str
    creator: "LibraryLibraryAssetSubmissionRequestsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["LibraryLibraryAssetSubmissionRequestsModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    project_id: str = Field(alias="projectId")
    title: str
    description: str
    configuration: Optional[Any]


class LibraryLibraryAssetSubmissionRequestsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class LibraryLibraryAssetSubmissionRequestsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


Library.model_rebuild()
LibraryLibrary.model_rebuild()
LibraryLibraryAssets.model_rebuild()
LibraryLibraryAssetsItems.model_rebuild()
LibraryLibraryAssetsItemsAttachments.model_rebuild()
LibraryLibraryAssetsItemsRelatedAssets.model_rebuild()
LibraryLibraryAssetsItemsComments.model_rebuild()
LibraryLibraryAssetsItemsCustomMetadata.model_rebuild()
LibraryLibraryAssetsItemsWorkflowTask.model_rebuild()
LibraryLibraryAssetsItemsVariants.model_rebuild()
LibraryLibraryAssetsItemsLocation.model_rebuild()
LibraryLibraryCollections.model_rebuild()
LibraryLibraryCollectionsItems.model_rebuild()
LibraryLibraryBrowse.model_rebuild()
LibraryLibraryBrowseFolders.model_rebuild()
LibraryLibraryBrowseFoldersItems.model_rebuild()
LibraryLibraryCollaborators.model_rebuild()
LibraryLibraryCollaboratorsUsers.model_rebuild()
LibraryLibraryCollaboratorsUsersEdges.model_rebuild()
LibraryLibraryWorkflow.model_rebuild()
LibraryLibraryWorkflowStatuses.model_rebuild()
LibraryLibraryWorkflowStatusesChecklistPresets.model_rebuild()
LibraryLibraryWorkflowStatusesTasks.model_rebuild()
LibraryLibraryCustomMetadataProperties.model_rebuild()
LibraryLibraryAssetSubmissionRequests.model_rebuild()
