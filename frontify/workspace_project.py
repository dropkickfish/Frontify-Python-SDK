# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import AssetStatusType, CopyrightStatus, TagSource


class WorkspaceProject(BaseModel):
    workspace_project: Optional["WorkspaceProjectWorkspaceProject"] = Field(
        alias="workspaceProject"
    )


class WorkspaceProjectWorkspaceProject(BaseModel):
    id: str
    name: str
    color: Optional["WorkspaceProjectWorkspaceProjectColor"]
    assets: "WorkspaceProjectWorkspaceProjectAssets"
    licenses: Optional[List[Optional["WorkspaceProjectWorkspaceProjectLicenses"]]]
    browse: "WorkspaceProjectWorkspaceProjectBrowse"
    collaborators: Optional["WorkspaceProjectWorkspaceProjectCollaborators"]
    current_user_permissions: (
        "WorkspaceProjectWorkspaceProjectCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")


class WorkspaceProjectWorkspaceProjectColor(BaseModel):
    red: Any
    green: Any
    blue: Any
    alpha: Any


class WorkspaceProjectWorkspaceProjectAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[List[Optional["WorkspaceProjectWorkspaceProjectAssetsItems"]]]


class WorkspaceProjectWorkspaceProjectAssetsItems(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: "WorkspaceProjectWorkspaceProjectAssetsItemsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["WorkspaceProjectWorkspaceProjectAssetsItemsModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[
        List[Optional["WorkspaceProjectWorkspaceProjectAssetsItemsAttachments"]]
    ]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[List[Optional["WorkspaceProjectWorkspaceProjectAssetsItemsTags"]]]
    copyright: Optional["WorkspaceProjectWorkspaceProjectAssetsItemsCopyright"]
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[
        List[Optional["WorkspaceProjectWorkspaceProjectAssetsItemsLicenses"]]
    ]
    status: AssetStatusType
    related_assets: "WorkspaceProjectWorkspaceProjectAssetsItemsRelatedAssets" = Field(
        alias="relatedAssets"
    )
    comments: Optional["WorkspaceProjectWorkspaceProjectAssetsItemsComments"]
    current_user_permissions: (
        "WorkspaceProjectWorkspaceProjectAssetsItemsCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")
    custom_metadata: List[
        "WorkspaceProjectWorkspaceProjectAssetsItemsCustomMetadata"
    ] = Field(alias="customMetadata")
    location: "WorkspaceProjectWorkspaceProjectAssetsItemsLocation"


class WorkspaceProjectWorkspaceProjectAssetsItemsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class WorkspaceProjectWorkspaceProjectAssetsItemsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class WorkspaceProjectWorkspaceProjectAssetsItemsAttachments(BaseModel):
    id: str
    creator: "WorkspaceProjectWorkspaceProjectAssetsItemsAttachmentsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["WorkspaceProjectWorkspaceProjectAssetsItemsAttachmentsModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: Optional[str]
    filename: Optional[str]
    type: Optional[str]
    external_id: Optional[str] = Field(alias="externalId")
    extension: Optional[str]
    size: Optional[Any]
    download_url: Optional[Any] = Field(alias="downloadUrl")


class WorkspaceProjectWorkspaceProjectAssetsItemsAttachmentsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class WorkspaceProjectWorkspaceProjectAssetsItemsAttachmentsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class WorkspaceProjectWorkspaceProjectAssetsItemsTags(BaseModel):
    value: str
    source: Optional[TagSource]


class WorkspaceProjectWorkspaceProjectAssetsItemsCopyright(BaseModel):
    status: CopyrightStatus
    notice: Optional[str]


class WorkspaceProjectWorkspaceProjectAssetsItemsLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class WorkspaceProjectWorkspaceProjectAssetsItemsRelatedAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[Optional["WorkspaceProjectWorkspaceProjectAssetsItemsRelatedAssetsItems"]]
    ]


class WorkspaceProjectWorkspaceProjectAssetsItemsRelatedAssetsItems(BaseModel):
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


class WorkspaceProjectWorkspaceProjectAssetsItemsComments(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[Optional["WorkspaceProjectWorkspaceProjectAssetsItemsCommentsItems"]]
    ]


class WorkspaceProjectWorkspaceProjectAssetsItemsCommentsItems(BaseModel):
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    content: str
    is_resolved: bool = Field(alias="isResolved")


class WorkspaceProjectWorkspaceProjectAssetsItemsCurrentUserPermissions(BaseModel):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class WorkspaceProjectWorkspaceProjectAssetsItemsCustomMetadata(BaseModel):
    typename__: Literal[
        "CustomMetadata", "CustomMetadataValue", "CustomMetadataValues"
    ] = Field(alias="__typename")
    property: "WorkspaceProjectWorkspaceProjectAssetsItemsCustomMetadataProperty"


class WorkspaceProjectWorkspaceProjectAssetsItemsCustomMetadataProperty(BaseModel):
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: str
    help_text: Optional[str] = Field(alias="helpText")
    is_required: bool = Field(alias="isRequired")
    default_value: Optional[Any] = Field(alias="defaultValue")


class WorkspaceProjectWorkspaceProjectAssetsItemsLocation(BaseModel):
    brand: Optional["WorkspaceProjectWorkspaceProjectAssetsItemsLocationBrand"]
    library: Optional["WorkspaceProjectWorkspaceProjectAssetsItemsLocationLibrary"]
    workspace_project: Optional[
        "WorkspaceProjectWorkspaceProjectAssetsItemsLocationWorkspaceProject"
    ] = Field(alias="workspaceProject")
    folder: Optional["WorkspaceProjectWorkspaceProjectAssetsItemsLocationFolder"]


class WorkspaceProjectWorkspaceProjectAssetsItemsLocationBrand(BaseModel):
    id: str
    name: str


class WorkspaceProjectWorkspaceProjectAssetsItemsLocationLibrary(BaseModel):
    id: str
    name: Optional[str]


class WorkspaceProjectWorkspaceProjectAssetsItemsLocationWorkspaceProject(BaseModel):
    id: str
    name: Optional[str]


class WorkspaceProjectWorkspaceProjectAssetsItemsLocationFolder(BaseModel):
    id: str
    name: str


class WorkspaceProjectWorkspaceProjectLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class WorkspaceProjectWorkspaceProjectBrowse(BaseModel):
    folders: "WorkspaceProjectWorkspaceProjectBrowseFolders"
    assets: "WorkspaceProjectWorkspaceProjectBrowseAssets"


class WorkspaceProjectWorkspaceProjectBrowseFolders(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[Optional["WorkspaceProjectWorkspaceProjectBrowseFoldersItems"]]
    ]


class WorkspaceProjectWorkspaceProjectBrowseFoldersItems(BaseModel):
    typename__: Literal["Folder", "SubFolder"] = Field(alias="__typename")
    id: str
    name: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    breadcrumbs: List["WorkspaceProjectWorkspaceProjectBrowseFoldersItemsBreadcrumbs"]
    folders: "WorkspaceProjectWorkspaceProjectBrowseFoldersItemsFolders"
    assets: "WorkspaceProjectWorkspaceProjectBrowseFoldersItemsAssets"


class WorkspaceProjectWorkspaceProjectBrowseFoldersItemsBreadcrumbs(BaseModel):
    id: Optional[str]
    name: Optional[str]


class WorkspaceProjectWorkspaceProjectBrowseFoldersItemsFolders(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class WorkspaceProjectWorkspaceProjectBrowseFoldersItemsAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class WorkspaceProjectWorkspaceProjectBrowseAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class WorkspaceProjectWorkspaceProjectCollaborators(BaseModel):
    users: "WorkspaceProjectWorkspaceProjectCollaboratorsUsers"


class WorkspaceProjectWorkspaceProjectCollaboratorsUsers(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[Optional["WorkspaceProjectWorkspaceProjectCollaboratorsUsersItems"]]
    ]


class WorkspaceProjectWorkspaceProjectCollaboratorsUsersItems(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class WorkspaceProjectWorkspaceProjectCurrentUserPermissions(BaseModel):
    can_create_assets: bool = Field(alias="canCreateAssets")
    can_view_collaborators: bool = Field(alias="canViewCollaborators")


WorkspaceProject.model_rebuild()
WorkspaceProjectWorkspaceProject.model_rebuild()
WorkspaceProjectWorkspaceProjectAssets.model_rebuild()
WorkspaceProjectWorkspaceProjectAssetsItems.model_rebuild()
WorkspaceProjectWorkspaceProjectAssetsItemsAttachments.model_rebuild()
WorkspaceProjectWorkspaceProjectAssetsItemsRelatedAssets.model_rebuild()
WorkspaceProjectWorkspaceProjectAssetsItemsComments.model_rebuild()
WorkspaceProjectWorkspaceProjectAssetsItemsCustomMetadata.model_rebuild()
WorkspaceProjectWorkspaceProjectAssetsItemsLocation.model_rebuild()
WorkspaceProjectWorkspaceProjectBrowse.model_rebuild()
WorkspaceProjectWorkspaceProjectBrowseFolders.model_rebuild()
WorkspaceProjectWorkspaceProjectBrowseFoldersItems.model_rebuild()
WorkspaceProjectWorkspaceProjectCollaborators.model_rebuild()
WorkspaceProjectWorkspaceProjectCollaboratorsUsers.model_rebuild()
