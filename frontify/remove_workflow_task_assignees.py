# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import AssetStatusType, CopyrightStatus, TagSource, WorkflowStatusEnterRule


class RemoveWorkflowTaskAssignees(BaseModel):
    remove_workflow_task_assignees: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssignees"
    ] = Field(alias="removeWorkflowTaskAssignees")


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssignees(BaseModel):
    workflow_task: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTask"
    ] = Field(alias="workflowTask")


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTask(BaseModel):
    id: str
    assigned_users: List[
        Optional[
            "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssignedUsers"
        ]
    ] = Field(alias="assignedUsers")
    asset: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAsset"
    ]
    title: Optional[str]
    description: Optional[str]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssignedUsers(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAsset(
    BaseModel
):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: (
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCreator"
    )
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[
        List[
            Optional[
                "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetAttachments"
            ]
        ]
    ]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[
        List[
            Optional[
                "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetTags"
            ]
        ]
    ]
    copyright: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCopyright"
    ]
    availability: "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetAvailability"
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[
        List[
            Optional[
                "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLicenses"
            ]
        ]
    ]
    status: AssetStatusType
    related_assets: (
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetRelatedAssets"
    ) = Field(alias="relatedAssets")
    comments: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetComments"
    ]
    current_user_permissions: (
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")
    custom_metadata: List[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCustomMetadata"
    ] = Field(alias="customMetadata")
    workflow_task: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetWorkflowTask"
    ] = Field(alias="workflowTask")
    variants: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetVariants"
    ]
    location: "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLocation"
    preview_background_color: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetPreviewBackgroundColor"
    ] = Field(alias="previewBackgroundColor")


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCreator(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetModifier(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetAttachments(
    BaseModel
):
    id: str
    creator: "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetAttachmentsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetAttachmentsModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: Optional[str]
    filename: Optional[str]
    type: Optional[str]
    external_id: Optional[str] = Field(alias="externalId")
    extension: Optional[str]
    size: Optional[Any]
    download_url: Optional[Any] = Field(alias="downloadUrl")


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetAttachmentsCreator(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetAttachmentsModifier(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetTags(
    BaseModel
):
    value: str
    source: Optional[TagSource]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCopyright(
    BaseModel
):
    status: CopyrightStatus
    notice: Optional[str]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetAvailability(
    BaseModel
):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLicenses(
    BaseModel
):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetRelatedAssets(
    BaseModel
):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[
            Optional[
                "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetRelatedAssetsItems"
            ]
        ]
    ]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetRelatedAssetsItems(
    BaseModel
):
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


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetComments(
    BaseModel
):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[
            Optional[
                "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCommentsItems"
            ]
        ]
    ]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCommentsItems(
    BaseModel
):
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    content: str
    is_resolved: bool = Field(alias="isResolved")


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCurrentUserPermissions(
    BaseModel
):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCustomMetadata(
    BaseModel
):
    typename__: Literal[
        "CustomMetadata", "CustomMetadataValue", "CustomMetadataValues"
    ] = Field(alias="__typename")
    property: "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCustomMetadataProperty"


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCustomMetadataProperty(
    BaseModel
):
    id: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: str
    help_text: Optional[str] = Field(alias="helpText")
    is_required: bool = Field(alias="isRequired")
    default_value: Optional[Any] = Field(alias="defaultValue")


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetWorkflowTask(
    BaseModel
):
    id: str
    title: Optional[str]
    description: Optional[str]
    status: "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetWorkflowTaskStatus"
    checklist_item: (
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetWorkflowTaskChecklistItem"
    ) = Field(alias="checklistItem")


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetWorkflowTaskStatus(
    BaseModel
):
    id: str
    name: str
    enter_rules: List[Optional[WorkflowStatusEnterRule]] = Field(alias="enterRules")


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetWorkflowTaskChecklistItem(
    BaseModel
):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetVariants(
    BaseModel
):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: List[
        Optional[
            "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetVariantsItems"
        ]
    ]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetVariantsItems(
    BaseModel
):
    key: str
    filename: Optional[str]
    download_url: Optional[Any] = Field(alias="downloadUrl")


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLocation(
    BaseModel
):
    brand: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLocationBrand"
    ]
    library: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLocationLibrary"
    ]
    workspace_project: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLocationWorkspaceProject"
    ] = Field(alias="workspaceProject")
    folder: Optional[
        "RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLocationFolder"
    ]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLocationBrand(
    BaseModel
):
    id: str
    name: str


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLocationLibrary(
    BaseModel
):
    id: str
    name: Optional[str]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLocationWorkspaceProject(
    BaseModel
):
    id: str
    name: Optional[str]


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLocationFolder(
    BaseModel
):
    id: str
    name: str


class RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetPreviewBackgroundColor(
    BaseModel
):
    red: Any
    green: Any
    blue: Any
    alpha: Any


RemoveWorkflowTaskAssignees.model_rebuild()
RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssignees.model_rebuild()
RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTask.model_rebuild()
RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAsset.model_rebuild()
RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetAttachments.model_rebuild()
RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetRelatedAssets.model_rebuild()
RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetComments.model_rebuild()
RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetCustomMetadata.model_rebuild()
RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetWorkflowTask.model_rebuild()
RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetVariants.model_rebuild()
RemoveWorkflowTaskAssigneesRemoveWorkflowTaskAssigneesWorkflowTaskAssetLocation.model_rebuild()
