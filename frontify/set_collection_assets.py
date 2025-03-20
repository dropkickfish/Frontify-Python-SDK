# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import AssetStatusType, CopyrightStatus, TagSource


class SetCollectionAssets(BaseModel):
    set_collection_assets: Optional["SetCollectionAssetsSetCollectionAssets"] = Field(
        alias="setCollectionAssets"
    )


class SetCollectionAssetsSetCollectionAssets(BaseModel):
    collection: Optional["SetCollectionAssetsSetCollectionAssetsCollection"]


class SetCollectionAssetsSetCollectionAssetsCollection(BaseModel):
    id: str
    name: str
    assets: "SetCollectionAssetsSetCollectionAssetsCollectionAssets"
    current_user_permissions: (
        "SetCollectionAssetsSetCollectionAssetsCollectionCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")


class SetCollectionAssetsSetCollectionAssetsCollectionAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[Optional["SetCollectionAssetsSetCollectionAssetsCollectionAssetsItems"]]
    ]


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItems(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: "SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[
        List[
            Optional[
                "SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsAttachments"
            ]
        ]
    ]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[
        List[
            Optional["SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsTags"]
        ]
    ]
    copyright: Optional[
        "SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsCopyright"
    ]
    availability: (
        "SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsAvailability"
    )
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[
        List[
            Optional[
                "SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsLicenses"
            ]
        ]
    ]
    status: AssetStatusType
    related_assets: (
        "SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsRelatedAssets"
    ) = Field(alias="relatedAssets")
    comments: Optional[
        "SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsComments"
    ]
    current_user_permissions: (
        "SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")
    workflow_task: Optional[
        "SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsWorkflowTask"
    ] = Field(alias="workflowTask")
    variants: Optional[
        "SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsVariants"
    ]
    preview_background_color: Optional[
        "SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsPreviewBackgroundColor"
    ] = Field(alias="previewBackgroundColor")


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsAttachments(BaseModel):
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


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsTags(BaseModel):
    value: str
    source: Optional[TagSource]


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsCopyright(BaseModel):
    status: CopyrightStatus
    notice: Optional[str]


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsAvailability(
    BaseModel
):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsRelatedAssets(
    BaseModel
):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsComments(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsCurrentUserPermissions(
    BaseModel
):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsWorkflowTask(
    BaseModel
):
    id: str
    title: Optional[str]
    description: Optional[str]


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsVariants(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class SetCollectionAssetsSetCollectionAssetsCollectionAssetsItemsPreviewBackgroundColor(
    BaseModel
):
    red: Any
    green: Any
    blue: Any
    alpha: Any


class SetCollectionAssetsSetCollectionAssetsCollectionCurrentUserPermissions(BaseModel):
    can_add_assets: bool = Field(alias="canAddAssets")
    can_remove_assets: bool = Field(alias="canRemoveAssets")


SetCollectionAssets.model_rebuild()
SetCollectionAssetsSetCollectionAssets.model_rebuild()
SetCollectionAssetsSetCollectionAssetsCollection.model_rebuild()
SetCollectionAssetsSetCollectionAssetsCollectionAssets.model_rebuild()
SetCollectionAssetsSetCollectionAssetsCollectionAssetsItems.model_rebuild()
