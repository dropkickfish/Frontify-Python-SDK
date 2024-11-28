# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import AssetStatusType, CopyrightStatus, TagSource


class AddAssetLicense(BaseModel):
    add_asset_license: Optional["AddAssetLicenseAddAssetLicense"] = Field(
        alias="addAssetLicense"
    )


class AddAssetLicenseAddAssetLicense(BaseModel):
    asset: Optional["AddAssetLicenseAddAssetLicenseAsset"]
    license: Optional["AddAssetLicenseAddAssetLicenseLicense"]


class AddAssetLicenseAddAssetLicenseAsset(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: "AddAssetLicenseAddAssetLicenseAssetCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["AddAssetLicenseAddAssetLicenseAssetModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[
        List[Optional["AddAssetLicenseAddAssetLicenseAssetAttachments"]]
    ]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[List[Optional["AddAssetLicenseAddAssetLicenseAssetTags"]]]
    copyright: Optional["AddAssetLicenseAddAssetLicenseAssetCopyright"]
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[List[Optional["AddAssetLicenseAddAssetLicenseAssetLicenses"]]]
    status: AssetStatusType
    related_assets: "AddAssetLicenseAddAssetLicenseAssetRelatedAssets" = Field(
        alias="relatedAssets"
    )
    comments: Optional["AddAssetLicenseAddAssetLicenseAssetComments"]
    current_user_permissions: (
        "AddAssetLicenseAddAssetLicenseAssetCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")
    custom_metadata: List["AddAssetLicenseAddAssetLicenseAssetCustomMetadata"] = Field(
        alias="customMetadata"
    )
    location: "AddAssetLicenseAddAssetLicenseAssetLocation"


class AddAssetLicenseAddAssetLicenseAssetCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class AddAssetLicenseAddAssetLicenseAssetModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class AddAssetLicenseAddAssetLicenseAssetAttachments(BaseModel):
    id: str
    creator: "AddAssetLicenseAddAssetLicenseAssetAttachmentsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["AddAssetLicenseAddAssetLicenseAssetAttachmentsModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: Optional[str]
    filename: Optional[str]
    type: Optional[str]
    external_id: Optional[str] = Field(alias="externalId")
    extension: Optional[str]
    size: Optional[Any]
    download_url: Optional[Any] = Field(alias="downloadUrl")


class AddAssetLicenseAddAssetLicenseAssetAttachmentsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class AddAssetLicenseAddAssetLicenseAssetAttachmentsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class AddAssetLicenseAddAssetLicenseAssetTags(BaseModel):
    value: str
    source: Optional[TagSource]


class AddAssetLicenseAddAssetLicenseAssetCopyright(BaseModel):
    status: CopyrightStatus
    notice: Optional[str]


class AddAssetLicenseAddAssetLicenseAssetLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class AddAssetLicenseAddAssetLicenseAssetRelatedAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[Optional["AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItems"]]
    ]


class AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItems(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: "AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[
        List[
            Optional["AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsAttachments"]
        ]
    ]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[
        List[Optional["AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsTags"]]
    ]
    copyright: Optional[
        "AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsCopyright"
    ]
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[
        List[Optional["AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsLicenses"]]
    ]
    status: AssetStatusType
    related_assets: (
        "AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsRelatedAssets"
    ) = Field(alias="relatedAssets")
    comments: Optional["AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsComments"]
    current_user_permissions: (
        "AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")


class AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsAttachments(BaseModel):
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


class AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsTags(BaseModel):
    value: str
    source: Optional[TagSource]


class AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsCopyright(BaseModel):
    status: CopyrightStatus
    notice: Optional[str]


class AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsRelatedAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsComments(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItemsCurrentUserPermissions(
    BaseModel
):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class AddAssetLicenseAddAssetLicenseAssetComments(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[List[Optional["AddAssetLicenseAddAssetLicenseAssetCommentsItems"]]]


class AddAssetLicenseAddAssetLicenseAssetCommentsItems(BaseModel):
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    content: str
    mentioned_users: List[
        Optional["AddAssetLicenseAddAssetLicenseAssetCommentsItemsMentionedUsers"]
    ] = Field(alias="mentionedUsers")
    is_resolved: bool = Field(alias="isResolved")
    replies: "AddAssetLicenseAddAssetLicenseAssetCommentsItemsReplies"


class AddAssetLicenseAddAssetLicenseAssetCommentsItemsMentionedUsers(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class AddAssetLicenseAddAssetLicenseAssetCommentsItemsReplies(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class AddAssetLicenseAddAssetLicenseAssetCurrentUserPermissions(BaseModel):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class AddAssetLicenseAddAssetLicenseAssetCustomMetadata(BaseModel):
    typename__: Literal[
        "CustomMetadata", "CustomMetadataValue", "CustomMetadataValues"
    ] = Field(alias="__typename")
    property: "AddAssetLicenseAddAssetLicenseAssetCustomMetadataProperty"


class AddAssetLicenseAddAssetLicenseAssetCustomMetadataProperty(BaseModel):
    id: str
    creator: "AddAssetLicenseAddAssetLicenseAssetCustomMetadataPropertyCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "AddAssetLicenseAddAssetLicenseAssetCustomMetadataPropertyModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: str
    type: "AddAssetLicenseAddAssetLicenseAssetCustomMetadataPropertyType"
    help_text: Optional[str] = Field(alias="helpText")
    is_required: bool = Field(alias="isRequired")
    default_value: Optional[Any] = Field(alias="defaultValue")


class AddAssetLicenseAddAssetLicenseAssetCustomMetadataPropertyCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class AddAssetLicenseAddAssetLicenseAssetCustomMetadataPropertyModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class AddAssetLicenseAddAssetLicenseAssetCustomMetadataPropertyType(BaseModel):
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


class AddAssetLicenseAddAssetLicenseAssetLocation(BaseModel):
    brand: Optional["AddAssetLicenseAddAssetLicenseAssetLocationBrand"]
    library: Optional["AddAssetLicenseAddAssetLicenseAssetLocationLibrary"]
    workspace_project: Optional[
        "AddAssetLicenseAddAssetLicenseAssetLocationWorkspaceProject"
    ] = Field(alias="workspaceProject")
    folder: Optional["AddAssetLicenseAddAssetLicenseAssetLocationFolder"]


class AddAssetLicenseAddAssetLicenseAssetLocationBrand(BaseModel):
    id: str
    name: str


class AddAssetLicenseAddAssetLicenseAssetLocationLibrary(BaseModel):
    id: str
    name: Optional[str]


class AddAssetLicenseAddAssetLicenseAssetLocationWorkspaceProject(BaseModel):
    id: str
    name: Optional[str]


class AddAssetLicenseAddAssetLicenseAssetLocationFolder(BaseModel):
    id: str
    name: str
    breadcrumbs: List["AddAssetLicenseAddAssetLicenseAssetLocationFolderBreadcrumbs"]


class AddAssetLicenseAddAssetLicenseAssetLocationFolderBreadcrumbs(BaseModel):
    id: Optional[str]
    name: Optional[str]


class AddAssetLicenseAddAssetLicenseLicense(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


AddAssetLicense.model_rebuild()
AddAssetLicenseAddAssetLicense.model_rebuild()
AddAssetLicenseAddAssetLicenseAsset.model_rebuild()
AddAssetLicenseAddAssetLicenseAssetAttachments.model_rebuild()
AddAssetLicenseAddAssetLicenseAssetRelatedAssets.model_rebuild()
AddAssetLicenseAddAssetLicenseAssetRelatedAssetsItems.model_rebuild()
AddAssetLicenseAddAssetLicenseAssetComments.model_rebuild()
AddAssetLicenseAddAssetLicenseAssetCommentsItems.model_rebuild()
AddAssetLicenseAddAssetLicenseAssetCustomMetadata.model_rebuild()
AddAssetLicenseAddAssetLicenseAssetCustomMetadataProperty.model_rebuild()
AddAssetLicenseAddAssetLicenseAssetLocation.model_rebuild()
AddAssetLicenseAddAssetLicenseAssetLocationFolder.model_rebuild()