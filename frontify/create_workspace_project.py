# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import AssetStatusType, CopyrightStatus, TagSource, WorkflowStatusEnterRule


class CreateWorkspaceProject(BaseModel):
    create_workspace_project: Optional[
        "CreateWorkspaceProjectCreateWorkspaceProject"
    ] = Field(alias="createWorkspaceProject")


class CreateWorkspaceProjectCreateWorkspaceProject(BaseModel):
    project: "CreateWorkspaceProjectCreateWorkspaceProjectProject"


class CreateWorkspaceProjectCreateWorkspaceProjectProject(BaseModel):
    id: str
    name: str
    color: Optional["CreateWorkspaceProjectCreateWorkspaceProjectProjectColor"]
    assets: "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssets"
    licenses: Optional[
        List[Optional["CreateWorkspaceProjectCreateWorkspaceProjectProjectLicenses"]]
    ]
    workflow: "CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflow"
    browse: "CreateWorkspaceProjectCreateWorkspaceProjectProjectBrowse"
    collaborators: Optional[
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectCollaborators"
    ]
    current_user_permissions: (
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")
    is_archived: bool = Field(alias="isArchived")
    custom_metadata: List[
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectCustomMetadata"
    ] = Field(alias="customMetadata")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectColor(BaseModel):
    red: Any
    green: Any
    blue: Any
    alpha: Any


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[Optional["CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItems"]]
    ]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItems(BaseModel):
    typename__: Literal[
        "Asset", "Audio", "Document", "EmbeddedContent", "File", "Image", "Video"
    ] = Field(alias="__typename")
    id: str
    creator: "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    title: str
    description: Optional[str]
    attachments: Optional[
        List[
            Optional[
                "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsAttachments"
            ]
        ]
    ]
    external_id: Optional[str] = Field(alias="externalId")
    tags: Optional[
        List[
            Optional[
                "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsTags"
            ]
        ]
    ]
    copyright: Optional[
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsCopyright"
    ]
    availability: (
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsAvailability"
    )
    expires_at: Optional[Any] = Field(alias="expiresAt")
    licenses: Optional[
        List[
            Optional[
                "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsLicenses"
            ]
        ]
    ]
    status: AssetStatusType
    related_assets: (
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsRelatedAssets"
    ) = Field(alias="relatedAssets")
    comments: Optional[
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsComments"
    ]
    current_user_permissions: (
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")
    workflow_task: Optional[
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsWorkflowTask"
    ] = Field(alias="workflowTask")
    variants: Optional[
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsVariants"
    ]
    preview_background_color: Optional[
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsPreviewBackgroundColor"
    ] = Field(alias="previewBackgroundColor")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsAttachments(
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


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsTags(BaseModel):
    value: str
    source: Optional[TagSource]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsCopyright(
    BaseModel
):
    status: CopyrightStatus
    notice: Optional[str]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsAvailability(
    BaseModel
):
    from_: Optional[Any] = Field(alias="from")
    to: Optional[Any]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsRelatedAssets(
    BaseModel
):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsComments(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsCurrentUserPermissions(
    BaseModel
):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_download: bool = Field(alias="canDownload")
    can_comment: bool = Field(alias="canComment")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsWorkflowTask(
    BaseModel
):
    id: str
    title: Optional[str]
    description: Optional[str]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsVariants(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItemsPreviewBackgroundColor(
    BaseModel
):
    red: Any
    green: Any
    blue: Any
    alpha: Any


class CreateWorkspaceProjectCreateWorkspaceProjectProjectLicenses(BaseModel):
    id: str
    title: str
    license: str
    add_by_default: bool = Field(alias="addByDefault")
    require_consensus: bool = Field(alias="requireConsensus")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflow(BaseModel):
    id: str
    statuses: List[
        Optional["CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflowStatuses"]
    ]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflowStatuses(BaseModel):
    id: str
    name: str
    color: "CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflowStatusesColor"
    assigned_users: List[
        Optional[
            "CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflowStatusesAssignedUsers"
        ]
    ] = Field(alias="assignedUsers")
    checklist_presets: List[
        Optional[
            "CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflowStatusesChecklistPresets"
        ]
    ] = Field(alias="checklistPresets")
    tasks: "CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflowStatusesTasks"
    enter_rules: List[Optional[WorkflowStatusEnterRule]] = Field(alias="enterRules")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflowStatusesColor(
    BaseModel
):
    red: Any
    green: Any
    blue: Any
    alpha: Any


class CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflowStatusesAssignedUsers(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflowStatusesChecklistPresets(
    BaseModel
):
    id: str
    content: str


class CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflowStatusesTasks(
    BaseModel
):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectBrowse(BaseModel):
    folders: "CreateWorkspaceProjectCreateWorkspaceProjectProjectBrowseFolders"
    assets: "CreateWorkspaceProjectCreateWorkspaceProjectProjectBrowseAssets"


class CreateWorkspaceProjectCreateWorkspaceProjectProjectBrowseFolders(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[
            Optional[
                "CreateWorkspaceProjectCreateWorkspaceProjectProjectBrowseFoldersItems"
            ]
        ]
    ]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectBrowseFoldersItems(BaseModel):
    typename__: Literal["Folder", "SubFolder"] = Field(alias="__typename")
    id: str
    name: str
    created_at: Any = Field(alias="createdAt")
    modified_at: Optional[Any] = Field(alias="modifiedAt")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectBrowseAssets(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectCollaborators(BaseModel):
    users: "CreateWorkspaceProjectCreateWorkspaceProjectProjectCollaboratorsUsers"


class CreateWorkspaceProjectCreateWorkspaceProjectProjectCollaboratorsUsers(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[
            Optional[
                "CreateWorkspaceProjectCreateWorkspaceProjectProjectCollaboratorsUsersItems"
            ]
        ]
    ]
    edges: List[
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectCollaboratorsUsersEdges"
    ]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectCollaboratorsUsersItems(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectCollaboratorsUsersEdges(
    BaseModel
):
    role: str


class CreateWorkspaceProjectCreateWorkspaceProjectProjectCurrentUserPermissions(
    BaseModel
):
    can_create_assets: bool = Field(alias="canCreateAssets")
    can_view_collaborators: bool = Field(alias="canViewCollaborators")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectCustomMetadata(BaseModel):
    typename__: Literal[
        "CustomMetadata", "CustomMetadataValue", "CustomMetadataValues"
    ] = Field(alias="__typename")
    property: (
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectCustomMetadataProperty"
    )


class CreateWorkspaceProjectCreateWorkspaceProjectProjectCustomMetadataProperty(
    BaseModel
):
    id: str
    creator: "CreateWorkspaceProjectCreateWorkspaceProjectProjectCustomMetadataPropertyCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectCustomMetadataPropertyModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: str
    type: (
        "CreateWorkspaceProjectCreateWorkspaceProjectProjectCustomMetadataPropertyType"
    )
    help_text: Optional[str] = Field(alias="helpText")
    is_required: bool = Field(alias="isRequired")
    default_value: Optional[Any] = Field(alias="defaultValue")


class CreateWorkspaceProjectCreateWorkspaceProjectProjectCustomMetadataPropertyCreator(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectCustomMetadataPropertyModifier(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class CreateWorkspaceProjectCreateWorkspaceProjectProjectCustomMetadataPropertyType(
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


CreateWorkspaceProject.model_rebuild()
CreateWorkspaceProjectCreateWorkspaceProject.model_rebuild()
CreateWorkspaceProjectCreateWorkspaceProjectProject.model_rebuild()
CreateWorkspaceProjectCreateWorkspaceProjectProjectAssets.model_rebuild()
CreateWorkspaceProjectCreateWorkspaceProjectProjectAssetsItems.model_rebuild()
CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflow.model_rebuild()
CreateWorkspaceProjectCreateWorkspaceProjectProjectWorkflowStatuses.model_rebuild()
CreateWorkspaceProjectCreateWorkspaceProjectProjectBrowse.model_rebuild()
CreateWorkspaceProjectCreateWorkspaceProjectProjectBrowseFolders.model_rebuild()
CreateWorkspaceProjectCreateWorkspaceProjectProjectCollaborators.model_rebuild()
CreateWorkspaceProjectCreateWorkspaceProjectProjectCollaboratorsUsers.model_rebuild()
CreateWorkspaceProjectCreateWorkspaceProjectProjectCustomMetadata.model_rebuild()
CreateWorkspaceProjectCreateWorkspaceProjectProjectCustomMetadataProperty.model_rebuild()
