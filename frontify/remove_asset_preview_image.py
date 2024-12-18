# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import AssetStatusType, CopyrightStatus, TagSource


class RemoveAssetPreviewImage(BaseModel):
    remove_asset_preview_image: Optional[
        "RemoveAssetPreviewImageRemoveAssetPreviewImage"
    ] = Field(alias="removeAssetPreviewImage")


class RemoveAssetPreviewImageRemoveAssetPreviewImage(BaseModel):
    asset: Optional["RemoveAssetPreviewImageRemoveAssetPreviewImageAsset"]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAsset(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["RemoveAssetPreviewImageRemoveAssetPreviewImageAssetModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[
        List[Optional["RemoveAssetPreviewImageRemoveAssetPreviewImageAssetAttachments"]]
    ]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[
        List[Optional["RemoveAssetPreviewImageRemoveAssetPreviewImageAssetTags"]]
    ]
    copyright: Optional["RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCopyright"]
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[
        List[Optional["RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLicenses"]]
    ]
    status: AssetStatusType
    related_assets: (
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssets"
    ) = Field(alias="relatedAssets")
    comments: Optional["RemoveAssetPreviewImageRemoveAssetPreviewImageAssetComments"]
    current_user_permissions: (
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")
    custom_metadata: List[
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCustomMetadata"
    ] = Field(alias="customMetadata")
    location: "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocation"


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetAttachments(BaseModel):
    id: str
    creator: "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetAttachmentsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetAttachmentsModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: Optional[str]
    filename: Optional[str]
    type: Optional[str]
    external_id: Optional[str] = Field(alias="externalId")
    extension: Optional[str]
    size: Optional[Any]
    download_url: Optional[Any] = Field(alias="downloadUrl")


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetAttachmentsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetAttachmentsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetTags(BaseModel):
    value: str
    source: Optional[TagSource]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCopyright(BaseModel):
    status: CopyrightStatus
    notice: Optional[str]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[
            Optional[
                "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItems"
            ]
        ]
    ]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItems(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: (
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsCreator"
    )
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[
        List[
            Optional[
                "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsAttachments"
            ]
        ]
    ]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[
        List[
            Optional[
                "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsTags"
            ]
        ]
    ]
    copyright: Optional[
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsCopyright"
    ]
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[
        List[
            Optional[
                "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsLicenses"
            ]
        ]
    ]
    status: AssetStatusType
    related_assets: (
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsRelatedAssets"
    ) = Field(alias="relatedAssets")
    comments: Optional[
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsComments"
    ]
    current_user_permissions: (
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsCreator(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsModifier(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsAttachments(
    BaseModel
):
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


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsTags(
    BaseModel
):
    value: str
    source: Optional[TagSource]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsCopyright(
    BaseModel
):
    status: CopyrightStatus
    notice: Optional[str]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsLicenses(
    BaseModel
):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsRelatedAssets(
    BaseModel
):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsComments(
    BaseModel
):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItemsCurrentUserPermissions(
    BaseModel
):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetComments(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[
            Optional["RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCommentsItems"]
        ]
    ]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCommentsItems(BaseModel):
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    content: str
    mentioned_users: List[
        Optional[
            "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCommentsItemsMentionedUsers"
        ]
    ] = Field(alias="mentionedUsers")
    is_resolved: bool = Field(alias="isResolved")
    replies: "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCommentsItemsReplies"


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCommentsItemsMentionedUsers(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCommentsItemsReplies(
    BaseModel
):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCurrentUserPermissions(
    BaseModel
):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCustomMetadata(BaseModel):
    typename__: Literal[
        "CustomMetadata", "CustomMetadataValue", "CustomMetadataValues"
    ] = Field(alias="__typename")
    property: (
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCustomMetadataProperty"
    )


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCustomMetadataProperty(
    BaseModel
):
    id: str
    creator: "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCustomMetadataPropertyCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCustomMetadataPropertyModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: str
    type: (
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCustomMetadataPropertyType"
    )
    help_text: Optional[str] = Field(alias="helpText")
    is_required: bool = Field(alias="isRequired")
    default_value: Optional[Any] = Field(alias="defaultValue")


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCustomMetadataPropertyCreator(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCustomMetadataPropertyModifier(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCustomMetadataPropertyType(
    BaseModel
):
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


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocation(BaseModel):
    brand: Optional["RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocationBrand"]
    library: Optional[
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocationLibrary"
    ]
    workspace_project: Optional[
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocationWorkspaceProject"
    ] = Field(alias="workspaceProject")
    folder: Optional[
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocationFolder"
    ]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocationBrand(BaseModel):
    id: str
    name: str


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocationLibrary(BaseModel):
    id: str
    name: Optional[str]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocationWorkspaceProject(
    BaseModel
):
    id: str
    name: Optional[str]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocationFolder(BaseModel):
    id: str
    name: str
    breadcrumbs: List[
        "RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocationFolderBreadcrumbs"
    ]


class RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocationFolderBreadcrumbs(
    BaseModel
):
    id: Optional[str]
    name: Optional[str]


RemoveAssetPreviewImage.model_rebuild()
RemoveAssetPreviewImageRemoveAssetPreviewImage.model_rebuild()
RemoveAssetPreviewImageRemoveAssetPreviewImageAsset.model_rebuild()
RemoveAssetPreviewImageRemoveAssetPreviewImageAssetAttachments.model_rebuild()
RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssets.model_rebuild()
RemoveAssetPreviewImageRemoveAssetPreviewImageAssetRelatedAssetsItems.model_rebuild()
RemoveAssetPreviewImageRemoveAssetPreviewImageAssetComments.model_rebuild()
RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCommentsItems.model_rebuild()
RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCustomMetadata.model_rebuild()
RemoveAssetPreviewImageRemoveAssetPreviewImageAssetCustomMetadataProperty.model_rebuild()
RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocation.model_rebuild()
RemoveAssetPreviewImageRemoveAssetPreviewImageAssetLocationFolder.model_rebuild()
