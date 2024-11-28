# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import AssetStatusType, CopyrightStatus, TagSource


class UpdateAsset(BaseModel):
    update_asset: Optional["UpdateAssetUpdateAsset"] = Field(alias="updateAsset")


class UpdateAssetUpdateAsset(BaseModel):
    asset: Optional["UpdateAssetUpdateAssetAsset"]


class UpdateAssetUpdateAssetAsset(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: "UpdateAssetUpdateAssetAssetCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["UpdateAssetUpdateAssetAssetModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[List[Optional["UpdateAssetUpdateAssetAssetAttachments"]]]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[List[Optional["UpdateAssetUpdateAssetAssetTags"]]]
    copyright: Optional["UpdateAssetUpdateAssetAssetCopyright"]
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[List[Optional["UpdateAssetUpdateAssetAssetLicenses"]]]
    status: AssetStatusType
    related_assets: "UpdateAssetUpdateAssetAssetRelatedAssets" = Field(
        alias="relatedAssets"
    )
    comments: Optional["UpdateAssetUpdateAssetAssetComments"]
    current_user_permissions: "UpdateAssetUpdateAssetAssetCurrentUserPermissions" = (
        Field(alias="currentUserPermissions")
    )
    custom_metadata: List["UpdateAssetUpdateAssetAssetCustomMetadata"] = Field(
        alias="customMetadata"
    )
    location: "UpdateAssetUpdateAssetAssetLocation"


class UpdateAssetUpdateAssetAssetCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class UpdateAssetUpdateAssetAssetModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class UpdateAssetUpdateAssetAssetAttachments(BaseModel):
    id: str
    creator: "UpdateAssetUpdateAssetAssetAttachmentsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["UpdateAssetUpdateAssetAssetAttachmentsModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: Optional[str]
    filename: Optional[str]
    type: Optional[str]
    external_id: Optional[str] = Field(alias="externalId")
    extension: Optional[str]
    size: Optional[Any]
    download_url: Optional[Any] = Field(alias="downloadUrl")


class UpdateAssetUpdateAssetAssetAttachmentsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class UpdateAssetUpdateAssetAssetAttachmentsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class UpdateAssetUpdateAssetAssetTags(BaseModel):
    value: str
    source: Optional[TagSource]


class UpdateAssetUpdateAssetAssetCopyright(BaseModel):
    status: CopyrightStatus
    notice: Optional[str]


class UpdateAssetUpdateAssetAssetLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class UpdateAssetUpdateAssetAssetRelatedAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[List[Optional["UpdateAssetUpdateAssetAssetRelatedAssetsItems"]]]


class UpdateAssetUpdateAssetAssetRelatedAssetsItems(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: "UpdateAssetUpdateAssetAssetRelatedAssetsItemsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["UpdateAssetUpdateAssetAssetRelatedAssetsItemsModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[
        List[Optional["UpdateAssetUpdateAssetAssetRelatedAssetsItemsAttachments"]]
    ]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[List[Optional["UpdateAssetUpdateAssetAssetRelatedAssetsItemsTags"]]]
    copyright: Optional["UpdateAssetUpdateAssetAssetRelatedAssetsItemsCopyright"]
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[
        List[Optional["UpdateAssetUpdateAssetAssetRelatedAssetsItemsLicenses"]]
    ]
    status: AssetStatusType
    related_assets: "UpdateAssetUpdateAssetAssetRelatedAssetsItemsRelatedAssets" = (
        Field(alias="relatedAssets")
    )
    comments: Optional["UpdateAssetUpdateAssetAssetRelatedAssetsItemsComments"]
    current_user_permissions: (
        "UpdateAssetUpdateAssetAssetRelatedAssetsItemsCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")


class UpdateAssetUpdateAssetAssetRelatedAssetsItemsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class UpdateAssetUpdateAssetAssetRelatedAssetsItemsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class UpdateAssetUpdateAssetAssetRelatedAssetsItemsAttachments(BaseModel):
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


class UpdateAssetUpdateAssetAssetRelatedAssetsItemsTags(BaseModel):
    value: str
    source: Optional[TagSource]


class UpdateAssetUpdateAssetAssetRelatedAssetsItemsCopyright(BaseModel):
    status: CopyrightStatus
    notice: Optional[str]


class UpdateAssetUpdateAssetAssetRelatedAssetsItemsLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class UpdateAssetUpdateAssetAssetRelatedAssetsItemsRelatedAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class UpdateAssetUpdateAssetAssetRelatedAssetsItemsComments(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class UpdateAssetUpdateAssetAssetRelatedAssetsItemsCurrentUserPermissions(BaseModel):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class UpdateAssetUpdateAssetAssetComments(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[List[Optional["UpdateAssetUpdateAssetAssetCommentsItems"]]]


class UpdateAssetUpdateAssetAssetCommentsItems(BaseModel):
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    content: str
    mentioned_users: List[
        Optional["UpdateAssetUpdateAssetAssetCommentsItemsMentionedUsers"]
    ] = Field(alias="mentionedUsers")
    is_resolved: bool = Field(alias="isResolved")
    replies: "UpdateAssetUpdateAssetAssetCommentsItemsReplies"


class UpdateAssetUpdateAssetAssetCommentsItemsMentionedUsers(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class UpdateAssetUpdateAssetAssetCommentsItemsReplies(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class UpdateAssetUpdateAssetAssetCurrentUserPermissions(BaseModel):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class UpdateAssetUpdateAssetAssetCustomMetadata(BaseModel):
    typename__: Literal[
        "CustomMetadata", "CustomMetadataValue", "CustomMetadataValues"
    ] = Field(alias="__typename")
    property: "UpdateAssetUpdateAssetAssetCustomMetadataProperty"


class UpdateAssetUpdateAssetAssetCustomMetadataProperty(BaseModel):
    id: str
    creator: "UpdateAssetUpdateAssetAssetCustomMetadataPropertyCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["UpdateAssetUpdateAssetAssetCustomMetadataPropertyModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: str
    type: "UpdateAssetUpdateAssetAssetCustomMetadataPropertyType"
    help_text: Optional[str] = Field(alias="helpText")
    is_required: bool = Field(alias="isRequired")
    default_value: Optional[Any] = Field(alias="defaultValue")


class UpdateAssetUpdateAssetAssetCustomMetadataPropertyCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class UpdateAssetUpdateAssetAssetCustomMetadataPropertyModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class UpdateAssetUpdateAssetAssetCustomMetadataPropertyType(BaseModel):
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


class UpdateAssetUpdateAssetAssetLocation(BaseModel):
    brand: Optional["UpdateAssetUpdateAssetAssetLocationBrand"]
    library: Optional["UpdateAssetUpdateAssetAssetLocationLibrary"]
    workspace_project: Optional[
        "UpdateAssetUpdateAssetAssetLocationWorkspaceProject"
    ] = Field(alias="workspaceProject")
    folder: Optional["UpdateAssetUpdateAssetAssetLocationFolder"]


class UpdateAssetUpdateAssetAssetLocationBrand(BaseModel):
    id: str
    name: str


class UpdateAssetUpdateAssetAssetLocationLibrary(BaseModel):
    id: str
    name: Optional[str]


class UpdateAssetUpdateAssetAssetLocationWorkspaceProject(BaseModel):
    id: str
    name: Optional[str]


class UpdateAssetUpdateAssetAssetLocationFolder(BaseModel):
    id: str
    name: str
    breadcrumbs: List["UpdateAssetUpdateAssetAssetLocationFolderBreadcrumbs"]


class UpdateAssetUpdateAssetAssetLocationFolderBreadcrumbs(BaseModel):
    id: Optional[str]
    name: Optional[str]


UpdateAsset.model_rebuild()
UpdateAssetUpdateAsset.model_rebuild()
UpdateAssetUpdateAssetAsset.model_rebuild()
UpdateAssetUpdateAssetAssetAttachments.model_rebuild()
UpdateAssetUpdateAssetAssetRelatedAssets.model_rebuild()
UpdateAssetUpdateAssetAssetRelatedAssetsItems.model_rebuild()
UpdateAssetUpdateAssetAssetComments.model_rebuild()
UpdateAssetUpdateAssetAssetCommentsItems.model_rebuild()
UpdateAssetUpdateAssetAssetCustomMetadata.model_rebuild()
UpdateAssetUpdateAssetAssetCustomMetadataProperty.model_rebuild()
UpdateAssetUpdateAssetAssetLocation.model_rebuild()
UpdateAssetUpdateAssetAssetLocationFolder.model_rebuild()