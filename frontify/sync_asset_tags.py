# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import AssetStatusType, CopyrightStatus, TagSource


class SyncAssetTags(BaseModel):
    sync_asset_tags: Optional["SyncAssetTagsSyncAssetTags"] = Field(
        alias="syncAssetTags"
    )


class SyncAssetTagsSyncAssetTags(BaseModel):
    asset: Optional["SyncAssetTagsSyncAssetTagsAsset"]


class SyncAssetTagsSyncAssetTagsAsset(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: "SyncAssetTagsSyncAssetTagsAssetCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["SyncAssetTagsSyncAssetTagsAssetModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[List[Optional["SyncAssetTagsSyncAssetTagsAssetAttachments"]]]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[List[Optional["SyncAssetTagsSyncAssetTagsAssetTags"]]]
    copyright: Optional["SyncAssetTagsSyncAssetTagsAssetCopyright"]
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[List[Optional["SyncAssetTagsSyncAssetTagsAssetLicenses"]]]
    status: AssetStatusType
    related_assets: "SyncAssetTagsSyncAssetTagsAssetRelatedAssets" = Field(
        alias="relatedAssets"
    )
    comments: Optional["SyncAssetTagsSyncAssetTagsAssetComments"]
    current_user_permissions: (
        "SyncAssetTagsSyncAssetTagsAssetCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")
    custom_metadata: List["SyncAssetTagsSyncAssetTagsAssetCustomMetadata"] = Field(
        alias="customMetadata"
    )
    location: "SyncAssetTagsSyncAssetTagsAssetLocation"


class SyncAssetTagsSyncAssetTagsAssetCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class SyncAssetTagsSyncAssetTagsAssetModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class SyncAssetTagsSyncAssetTagsAssetAttachments(BaseModel):
    id: str
    creator: "SyncAssetTagsSyncAssetTagsAssetAttachmentsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["SyncAssetTagsSyncAssetTagsAssetAttachmentsModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: Optional[str]
    filename: Optional[str]
    type: Optional[str]
    external_id: Optional[str] = Field(alias="externalId")
    extension: Optional[str]
    size: Optional[Any]
    download_url: Optional[Any] = Field(alias="downloadUrl")


class SyncAssetTagsSyncAssetTagsAssetAttachmentsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class SyncAssetTagsSyncAssetTagsAssetAttachmentsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class SyncAssetTagsSyncAssetTagsAssetTags(BaseModel):
    value: str
    source: Optional[TagSource]


class SyncAssetTagsSyncAssetTagsAssetCopyright(BaseModel):
    status: CopyrightStatus
    notice: Optional[str]


class SyncAssetTagsSyncAssetTagsAssetLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class SyncAssetTagsSyncAssetTagsAssetRelatedAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[List[Optional["SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItems"]]]


class SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItems(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: "SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[
        List[Optional["SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsAttachments"]]
    ]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[
        List[Optional["SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsTags"]]
    ]
    copyright: Optional["SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsCopyright"]
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[
        List[Optional["SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsLicenses"]]
    ]
    status: AssetStatusType
    related_assets: "SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsRelatedAssets" = (
        Field(alias="relatedAssets")
    )
    comments: Optional["SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsComments"]
    current_user_permissions: (
        "SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")


class SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsAttachments(BaseModel):
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: Optional[str]
    filename: Optional[str]
    type: Optional[str]
    external_id: Optional[str] = Field(alias="externalId")
    extension: Optional[str]
    size: Optional[Any]
    download_url: Optional[Any] = Field(alias="downloadUrl")


class SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsTags(BaseModel):
    value: str
    source: Optional[TagSource]


class SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsCopyright(BaseModel):
    status: CopyrightStatus
    notice: Optional[str]


class SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsRelatedAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsComments(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItemsCurrentUserPermissions(
    BaseModel
):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class SyncAssetTagsSyncAssetTagsAssetComments(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[List[Optional["SyncAssetTagsSyncAssetTagsAssetCommentsItems"]]]


class SyncAssetTagsSyncAssetTagsAssetCommentsItems(BaseModel):
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    content: str
    mentioned_users: List[
        Optional["SyncAssetTagsSyncAssetTagsAssetCommentsItemsMentionedUsers"]
    ] = Field(alias="mentionedUsers")
    is_resolved: bool = Field(alias="isResolved")
    replies: "SyncAssetTagsSyncAssetTagsAssetCommentsItemsReplies"


class SyncAssetTagsSyncAssetTagsAssetCommentsItemsMentionedUsers(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class SyncAssetTagsSyncAssetTagsAssetCommentsItemsReplies(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class SyncAssetTagsSyncAssetTagsAssetCurrentUserPermissions(BaseModel):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class SyncAssetTagsSyncAssetTagsAssetCustomMetadata(BaseModel):
    typename__: Literal[
        "CustomMetadata", "CustomMetadataValue", "CustomMetadataValues"
    ] = Field(alias="__typename")
    property: "SyncAssetTagsSyncAssetTagsAssetCustomMetadataProperty"


class SyncAssetTagsSyncAssetTagsAssetCustomMetadataProperty(BaseModel):
    id: str
    creator: "SyncAssetTagsSyncAssetTagsAssetCustomMetadataPropertyCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["SyncAssetTagsSyncAssetTagsAssetCustomMetadataPropertyModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: str
    type: "SyncAssetTagsSyncAssetTagsAssetCustomMetadataPropertyType"
    help_text: Optional[str] = Field(alias="helpText")
    is_required: bool = Field(alias="isRequired")
    default_value: Optional[Any] = Field(alias="defaultValue")


class SyncAssetTagsSyncAssetTagsAssetCustomMetadataPropertyCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class SyncAssetTagsSyncAssetTagsAssetCustomMetadataPropertyModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class SyncAssetTagsSyncAssetTagsAssetCustomMetadataPropertyType(BaseModel):
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


class SyncAssetTagsSyncAssetTagsAssetLocation(BaseModel):
    brand: Optional["SyncAssetTagsSyncAssetTagsAssetLocationBrand"]
    library: Optional["SyncAssetTagsSyncAssetTagsAssetLocationLibrary"]
    workspace_project: Optional[
        "SyncAssetTagsSyncAssetTagsAssetLocationWorkspaceProject"
    ] = Field(alias="workspaceProject")
    folder: Optional["SyncAssetTagsSyncAssetTagsAssetLocationFolder"]


class SyncAssetTagsSyncAssetTagsAssetLocationBrand(BaseModel):
    id: str
    name: str


class SyncAssetTagsSyncAssetTagsAssetLocationLibrary(BaseModel):
    id: str
    name: Optional[str]


class SyncAssetTagsSyncAssetTagsAssetLocationWorkspaceProject(BaseModel):
    id: str
    name: Optional[str]


class SyncAssetTagsSyncAssetTagsAssetLocationFolder(BaseModel):
    id: str
    name: str
    breadcrumbs: List["SyncAssetTagsSyncAssetTagsAssetLocationFolderBreadcrumbs"]


class SyncAssetTagsSyncAssetTagsAssetLocationFolderBreadcrumbs(BaseModel):
    id: Optional[str]
    name: Optional[str]


SyncAssetTags.model_rebuild()
SyncAssetTagsSyncAssetTags.model_rebuild()
SyncAssetTagsSyncAssetTagsAsset.model_rebuild()
SyncAssetTagsSyncAssetTagsAssetAttachments.model_rebuild()
SyncAssetTagsSyncAssetTagsAssetRelatedAssets.model_rebuild()
SyncAssetTagsSyncAssetTagsAssetRelatedAssetsItems.model_rebuild()
SyncAssetTagsSyncAssetTagsAssetComments.model_rebuild()
SyncAssetTagsSyncAssetTagsAssetCommentsItems.model_rebuild()
SyncAssetTagsSyncAssetTagsAssetCustomMetadata.model_rebuild()
SyncAssetTagsSyncAssetTagsAssetCustomMetadataProperty.model_rebuild()
SyncAssetTagsSyncAssetTagsAssetLocation.model_rebuild()
SyncAssetTagsSyncAssetTagsAssetLocationFolder.model_rebuild()
