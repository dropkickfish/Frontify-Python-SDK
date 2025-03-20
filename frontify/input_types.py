# Generated by ariadne-codegen
# Source: public-beta.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import (
    AccountQuerySortByInput,
    AccountQuerySourceTypeInput,
    AssetCommentStatusFilter,
    AssetQueryFilterSortType,
    AssetType,
    BrandQuerySortByInput,
    BrandQuerySourceTypeInput,
    BrandSearchQuerySource,
    ConditionOperator,
    ConditionType,
    CopyrightStatus,
    CreativeExportFormat,
    CreativeExportQuality,
    CreativeTemplateQuerySort,
    CustomMetadataPropertyPositionPlacement,
    CustomMetadataPropertyTypeName,
    LibraryQuerySort,
    MetadataFieldType,
    ProjectPermission,
    WorkspaceProjectQuerySort,
    WorkspaceProjectStateFilter,
)


class AssetCommentQueryInput(BaseModel):
    status: AssetCommentStatusFilter = AssetCommentStatusFilter.ALL


class FolderAssetQueryInput(BaseModel):
    sort_by: Optional[AssetQueryFilterSortType] = Field(alias="sortBy", default=None)


class AssetQueryInput(BaseModel):
    filter: Optional["AssetQueryFilterInput"] = None
    in_folder: Optional["AssetQueryInFolderInput"] = Field(
        alias="inFolder", default=None
    )
    sort_by: Optional[AssetQueryFilterSortType] = Field(alias="sortBy", default=None)
    external_id: Optional[str] = Field(alias="externalId", default=None)
    search: Optional[str] = None
    type: Optional[List[Optional[AssetType]]] = None
    types: Optional[List[Optional[AssetType]]] = None


class AssetQueryFilterInput(BaseModel):
    and_conditions: Optional[List[Optional["AssetQueryFilterConditionInput"]]] = Field(
        alias="andConditions", default=None
    )
    or_conditions: Optional[List[Optional["AssetQueryFilterConditionInput"]]] = Field(
        alias="orConditions", default=None
    )


class AssetQueryFilterConditionInput(BaseModel):
    type: ConditionType
    operator: Optional[ConditionOperator] = ConditionOperator.IS
    value: str
    metadata_field_id: Optional[str] = Field(alias="metadataFieldId", default=None)
    custom_metadata_property_id: Optional[str] = Field(
        alias="customMetadataPropertyId", default=None
    )


class AssetQueryInFolderInput(BaseModel):
    id: str


class AccountQueryInput(BaseModel):
    term: Optional[str] = None
    sort_by: Optional[AccountQuerySortByInput] = Field(
        alias="sortBy", default=AccountQuerySortByInput.RELEVANCE
    )
    filter: Optional["AccountQueryFilterInput"] = None


class AccountQueryFilterInput(BaseModel):
    sources: Optional[List["AccountQuerySourceInput"]] = None


class AccountQuerySourceInput(BaseModel):
    type: AccountQuerySourceTypeInput
    ids: Optional[List[str]] = None


class BrandQueryInput(BaseModel):
    term: Optional[str] = None
    sort_by: Optional[BrandQuerySortByInput] = Field(
        alias="sortBy", default=BrandQuerySortByInput.RELEVANCE
    )
    search_in: Optional[List[Optional[BrandSearchQuerySource]]] = Field(
        alias="searchIn", default_factory=lambda: [BrandSearchQuerySource.EVERYWHERE]
    )
    filter: Optional["BrandQueryFilterInput"] = None


class BrandQueryFilterInput(BaseModel):
    has_tags: Optional[List[Optional[str]]] = Field(alias="hasTags", default=None)
    sources: Optional[List["BrandQuerySourceInput"]] = None
    external_id: Optional[str] = Field(alias="externalId", default=None)


class BrandQuerySourceInput(BaseModel):
    type: BrandQuerySourceTypeInput
    ids: Optional[List[str]] = None


class LibraryQueryInput(BaseModel):
    sort_by: Optional[LibraryQuerySort] = Field(alias="sortBy", default=None)


class WorkspaceProjectQueryInput(BaseModel):
    state: Optional[WorkspaceProjectStateFilter] = WorkspaceProjectStateFilter.ALL
    sort_by: Optional[WorkspaceProjectQuerySort] = Field(alias="sortBy", default=None)


class LibraryPageAssetQueryInput(BaseModel):
    term: Optional[str] = None


class CreativeTemplateQueryInput(BaseModel):
    sort_by: Optional[CreativeTemplateQuerySort] = Field(alias="sortBy", default=None)


class AddAssetLicenseInput(BaseModel):
    asset_id: str = Field(alias="assetId")
    license_id: str = Field(alias="licenseId")


class AddAssetMetadataFieldValueInput(BaseModel):
    asset_id: str = Field(alias="assetId")
    metadata_field_id: str = Field(alias="metadataFieldId")
    value: str


class AddAssetPreviewImageInput(BaseModel):
    asset_id: str = Field(alias="assetId")
    file_id: str = Field(alias="fileId")


class AddAssetRelationsInput(BaseModel):
    asset_id: str = Field(alias="assetId")
    related_asset_ids: List[str] = Field(alias="relatedAssetIds")


class AddAssetTagsInput(BaseModel):
    id: str
    tags: Optional[List[Optional["TagInput"]]] = None


class TagInput(BaseModel):
    value: str


class AddCollectionAssetsInput(BaseModel):
    collection_id: str = Field(alias="collectionId")
    asset_ids: List[str] = Field(alias="assetIds")


class AddCustomMetadataInput(BaseModel):
    parent_ids: List[str] = Field(alias="parentIds")
    custom_metadata: List["CustomMetadataInput"] = Field(alias="customMetadata")


class CustomMetadataInput(BaseModel):
    property_id: str = Field(alias="propertyId")
    value: Optional[Any] = None


class AddCustomMetadataPropertyOptionsInput(BaseModel):
    property_id: str = Field(alias="propertyId")
    options: List["AddCustomMetadataPropertyOptionInput"]


class AddCustomMetadataPropertyOptionInput(BaseModel):
    value: str
    is_default: Optional[bool] = Field(alias="isDefault", default=False)


class AddWorkflowChecklistItemInput(BaseModel):
    id: str
    content: str
    assignee_user_id: Optional[str] = Field(alias="assigneeUserId", default=None)


class AddWorkflowChecklistPresetInput(BaseModel):
    id: str
    content: str
    assignee_user_id: Optional[str] = Field(alias="assigneeUserId", default=None)


class AddWorkflowStatusAssigneesInput(BaseModel):
    id: str
    user_ids: List[str] = Field(alias="userIds")


class AddWorkflowTaskAssigneesInput(BaseModel):
    id: str
    user_ids: List[str] = Field(alias="userIds")


class CreateAccountUserInput(BaseModel):
    name: str
    email: Any


class CreateAssetInput(BaseModel):
    project_id: Optional[str] = Field(alias="projectId", default=None)
    file_id: str = Field(alias="fileId")
    title: str
    alternative_text: Optional[str] = Field(alias="alternativeText", default=None)
    is_decorative: Optional[bool] = Field(alias="isDecorative", default=None)
    description: Optional[str] = ""
    external_id: Optional[str] = Field(alias="externalId", default=None)
    copyright: Optional["CreateCopyrightInput"] = None
    tags: Optional[List[Optional["TagInput"]]] = None
    skip_file_metadata: Optional[bool] = Field(alias="skipFileMetadata", default=False)
    directory: Optional[List[Optional[str]]] = None
    parent_id: Optional[str] = Field(alias="parentId", default=None)
    workflow_status: Optional[str] = Field(alias="workflowStatus", default=None)
    availability: Optional["DateTimeRangeInput"] = None
    expires_at: Optional[Any] = Field(alias="expiresAt", default=None)
    author: Optional[str] = ""
    preview_background_color: Optional["RgbaColorInput"] = Field(
        alias="previewBackgroundColor", default=None
    )


class CreateCopyrightInput(BaseModel):
    status: CopyrightStatus = CopyrightStatus.UNKNOWN
    notice: Optional[str] = ""


class DateTimeRangeInput(BaseModel):
    from_: Optional[Any] = Field(alias="from", default=None)
    to: Optional[Any] = None


class RgbaColorInput(BaseModel):
    red: Any
    green: Any
    blue: Any
    alpha: Any


class CreateAssetCommentInput(BaseModel):
    asset_id: str = Field(alias="assetId")
    content: str
    marking: Optional["MarkingInput"] = None


class MarkingInput(BaseModel):
    position: Optional["MarkingPositionInput"] = None
    dimensions: Optional["MarkingDimensionsInput"] = None
    timeframe: Optional["MarkingTimeframeInput"] = None
    page: Optional[int] = None


class MarkingPositionInput(BaseModel):
    x: Any
    y: Any


class MarkingDimensionsInput(BaseModel):
    width: Any
    height: Any


class MarkingTimeframeInput(BaseModel):
    start: Optional[Any] = None
    end: Optional[Any] = None


class CreatePermissionTokenInput(BaseModel):
    parent_ids: List[str] = Field(alias="parentIds")


class CreateAssetSubmissionsInput(BaseModel):
    token: str
    request_id: str = Field(alias="requestId")
    file_ids: List[str] = Field(alias="fileIds")
    auto_approve: Optional[bool] = Field(alias="autoApprove", default=False)
    submitter: "AssetSubmissionSubmitterInput"
    metadata: Optional["AssetSubmissionMetadataInput"] = None


class AssetSubmissionSubmitterInput(BaseModel):
    name: str
    email: Any


class AssetSubmissionMetadataInput(BaseModel):
    description: Optional[str] = None
    copyright: Optional["AssetSubmissionCopyrightInput"] = None
    custom: Optional[List["AssetSubmissionCustomMetadataInput"]] = None
    workflow_status_id: Optional[str] = Field(alias="workflowStatusId", default=None)


class AssetSubmissionCopyrightInput(BaseModel):
    author: Optional[str] = None
    status: CopyrightStatus = CopyrightStatus.UNKNOWN
    notice: Optional[str] = ""


class AssetSubmissionCustomMetadataInput(BaseModel):
    property_id: str = Field(alias="propertyId")
    value: Any


class CreateAssetVariantInput(BaseModel):
    file_id: str = Field(alias="fileId")
    asset_id: str = Field(alias="assetId")
    key: str


class CreateAttachmentInput(BaseModel):
    parent_id: str = Field(alias="parentId")
    file_id: str = Field(alias="fileId")
    name: str
    external_id: Optional[str] = Field(alias="externalId", default=None)


class CreateCollectionInput(BaseModel):
    parent_id: str = Field(alias="parentId")
    name: str


class CreateCustomMetadataPropertyInput(BaseModel):
    parent_id: str = Field(alias="parentId")
    name: str
    type: "CreateCustomMetadataPropertyTypeInput"
    help_text: Optional[str] = Field(alias="helpText", default="")
    is_required: Optional[bool] = Field(alias="isRequired", default=False)
    default_value: Optional[str] = Field(alias="defaultValue", default=None)
    position: Optional["CustomMetadataPropertyPositionInput"] = None


class CreateCustomMetadataPropertyTypeInput(BaseModel):
    name: CustomMetadataPropertyTypeName
    options: Optional[List["CreateCustomMetadataPropertyTypeOptionInput"]] = None


class CreateCustomMetadataPropertyTypeOptionInput(BaseModel):
    value: str
    is_default: Optional[bool] = Field(alias="isDefault", default=False)


class CustomMetadataPropertyPositionInput(BaseModel):
    target_id: Optional[str] = Field(alias="targetId", default=None)
    placement: CustomMetadataPropertyPositionPlacement


class CreateExternalAssetInput(BaseModel):
    project_id: str = Field(alias="projectId")
    url: Any
    title: str
    description: Optional[str] = ""
    width: Optional[int] = None
    height: Optional[int] = None
    allow_interactions: Optional[bool] = Field(alias="allowInteractions", default=True)
    external_id: Optional[str] = Field(alias="externalId", default=None)
    copyright: Optional["CreateCopyrightInput"] = None
    directory: Optional[List[Optional[str]]] = Field(default_factory=lambda: [])
    expires_at: Optional[Any] = Field(alias="expiresAt", default=None)
    author: Optional[str] = ""


class CreateFolderInput(BaseModel):
    parent_id: str = Field(alias="parentId")
    name: str
    description: Optional[str] = None


class CreateLicenseInput(BaseModel):
    project_id: str = Field(alias="projectId")
    title: str
    license: str
    add_by_default: Optional[bool] = Field(alias="addByDefault", default=False)
    require_consensus: Optional[bool] = Field(alias="requireConsensus", default=False)


class CreateMetadataFieldInput(BaseModel):
    project_id: str = Field(alias="projectId")
    label: str
    type: MetadataFieldType = MetadataFieldType.TEXT
    values: Optional[List[Optional["MetadataFieldValuesInput"]]] = None
    default_value: Optional[str] = Field(alias="defaultValue", default=None)
    allow_multiple_values: Optional[bool] = Field(
        alias="allowMultipleValues", default=False
    )
    allow_empty_value: Optional[bool] = Field(alias="allowEmptyValue", default=False)
    is_searchable: Optional[bool] = Field(alias="isSearchable", default=True)
    is_editable: Optional[bool] = Field(alias="isEditable", default=True)
    is_visible: Optional[bool] = Field(alias="isVisible", default=True)


class MetadataFieldValuesInput(BaseModel):
    value: str
    default: Optional[bool] = False


class CreateShareLinkInput(BaseModel):
    parent_id: str = Field(alias="parentId")
    permission_token: str = Field(alias="permissionToken")
    usage_key: str = Field(alias="usageKey")
    expires_at: Optional[Any] = Field(alias="expiresAt", default=None)
    password: Optional[str] = None


class CreateWorkflowStatusInput(BaseModel):
    workflow_id: str = Field(alias="workflowId")
    title: str
    color: Optional["RgbaColorInput"] = None


class CreateAssetWorkflowTaskInput(BaseModel):
    asset_id: str = Field(alias="assetId")
    workflow_status_id: str = Field(alias="workflowStatusId")
    assignee_user_ids: Optional[List[str]] = Field(
        alias="assigneeUserIds", default=None
    )
    status_enter_message: Optional[str] = Field(
        alias="statusEnterMessage", default=None
    )


class CreateWorkspaceProjectInput(BaseModel):
    brand_id: str = Field(alias="brandId")
    name: str


class DeleteAccountUserInput(BaseModel):
    id: str
    delegate_id: str = Field(alias="delegateId")
    account_id: str = Field(alias="accountId")


class DeleteAssetInput(BaseModel):
    id: str


class DeleteAttachmentInput(BaseModel):
    id: str


class DeleteAssetVariantInput(BaseModel):
    asset_id: str = Field(alias="assetId")
    key: str


class DeleteCollectionInput(BaseModel):
    collection_id: str = Field(alias="collectionId")


class DeleteCommentInput(BaseModel):
    id: str


class DeleteCustomMetadataPropertyInput(BaseModel):
    id: str


class DeleteFoldersInput(BaseModel):
    ids: List[str]


class DeleteLicenseInput(BaseModel):
    id: str


class DeleteMetadataFieldInput(BaseModel):
    id: str


class DeleteWorkflowStatusInput(BaseModel):
    id: str


class DeleteWorkflowTaskInput(BaseModel):
    id: str


class EditCommentInput(BaseModel):
    id: str
    content: str


class InstallProjectWebhookInput(BaseModel):
    project_id: str = Field(alias="projectId")
    notification_url: Any = Field(alias="notificationUrl")
    name: str


class InviteProjectUserInput(BaseModel):
    project_id: str = Field(alias="projectId")
    email: Any
    permission: ProjectPermission = ProjectPermission.VIEW
    valid_from: Optional[Any] = Field(alias="validFrom", default=None)
    valid_to: Optional[Any] = Field(alias="validTo", default=None)


class MoveAssetsInput(BaseModel):
    asset_ids: List[str] = Field(alias="assetIds")
    destination_id: str = Field(alias="destinationId")


class MoveFoldersInput(BaseModel):
    folder_ids: List[str] = Field(alias="folderIds")
    destination_id: str = Field(alias="destinationId")


class MoveWorkflowTaskInput(BaseModel):
    workflow_status_id: str = Field(alias="workflowStatusId")
    workflow_task_ids: List[str] = Field(alias="workflowTaskIds")
    status_enter_message: Optional[str] = Field(
        alias="statusEnterMessage", default=None
    )


class RemoveAssetLicenseInput(BaseModel):
    asset_id: str = Field(alias="assetId")
    license_id: str = Field(alias="licenseId")


class RemoveAssetPreviewImageInput(BaseModel):
    id: str


class RemoveAssetRelationsInput(BaseModel):
    asset_id: str = Field(alias="assetId")
    related_asset_ids: List[str] = Field(alias="relatedAssetIds")


class RemoveAssetTagsInput(BaseModel):
    id: str
    tags: Optional[List[Optional["TagInput"]]] = None


class RemoveCollectionAssetsInput(BaseModel):
    collection_id: str = Field(alias="collectionId")
    asset_ids: List[str] = Field(alias="assetIds")


class RemoveCustomMetadataInput(BaseModel):
    parent_ids: List[str] = Field(alias="parentIds")
    custom_metadata: List["CustomMetadataInput"] = Field(alias="customMetadata")


class RemoveCustomMetadataPropertyOptionsInput(BaseModel):
    property_id: str = Field(alias="propertyId")
    option_ids: List[str] = Field(alias="optionIds")


class RemoveMetadataValueInput(BaseModel):
    id: str


class RemoveWorkflowChecklistItemInput(BaseModel):
    id: str


class RemoveWorkflowChecklistPresetInput(BaseModel):
    id: str


class RemoveWorkflowStatusAssigneesInput(BaseModel):
    id: str
    user_ids: List[str] = Field(alias="userIds")


class RemoveWorkflowTaskAssigneesInput(BaseModel):
    id: str
    user_ids: List[str] = Field(alias="userIds")


class ExportCreativeInput(BaseModel):
    template_id: str = Field(alias="templateId")
    destination: Optional["ExportCreativeDestinationInput"] = None
    variables: Optional[List[Optional["CreativeVariableInput"]]] = None
    options: Optional["ExportCreativeOptionsInput"] = None


class ExportCreativeDestinationInput(BaseModel):
    destination_id: str = Field(alias="destinationId")
    title: str


class CreativeVariableInput(BaseModel):
    key: str
    value: Optional[Any] = None


class ExportCreativeOptionsInput(BaseModel):
    format: Optional[CreativeExportFormat] = None
    quality: Optional[CreativeExportQuality] = None
    has_transparent_background: Optional[bool] = Field(
        alias="hasTransparentBackground", default=None
    )
    has_cropmarks: bool = Field(alias="hasCropmarks", default=False)
    bleed: Optional["ExportCreativeBleedInput"] = None
    pages: Optional[List[int]] = None


class ExportCreativeBleedInput(BaseModel):
    top: float
    right: float
    bottom: float
    left: float


class ReopenAssetCommentInput(BaseModel):
    id: str


class ReplaceAssetInput(BaseModel):
    asset_id: str = Field(alias="assetId")
    file_id: str = Field(alias="fileId")
    skip_file_metadata: Optional[bool] = Field(alias="skipFileMetadata", default=False)


class ReplaceAssetVariantInput(BaseModel):
    file_id: str = Field(alias="fileId")
    asset_id: str = Field(alias="assetId")
    key: str


class ReplaceExternalDataSourceFileInput(BaseModel):
    external_data_source_id: str = Field(alias="externalDataSourceId")
    file_id: str = Field(alias="fileId")


class ReplyToCommentInput(BaseModel):
    id: str
    reply: str


class ResolveAssetCommentInput(BaseModel):
    id: str


class SetCustomMetadataInput(BaseModel):
    parent_ids: List[str] = Field(alias="parentIds")
    custom_metadata: List["CustomMetadataInput"] = Field(alias="customMetadata")


class SetCollectionAssetsInput(BaseModel):
    collection_id: str = Field(alias="collectionId")
    asset_ids: List[str] = Field(alias="assetIds")


class SyncAssetTagsInput(BaseModel):
    id: str
    tags: Optional[List[Optional["TagInput"]]] = None


class UninstallWebhookInput(BaseModel):
    id: str


class UpdateAssetInput(BaseModel):
    id: str
    data: "UpdateAssetDataInput"


class UpdateAssetDataInput(BaseModel):
    title: Optional[str] = None
    alternative_text: Optional[str] = Field(alias="alternativeText", default=None)
    is_decorative: Optional[bool] = Field(alias="isDecorative", default=None)
    filename: Optional[str] = None
    description: Optional[str] = None
    copyright: Optional["UpdateCopyrightInput"] = None
    expires_at: Optional[Any] = Field(alias="expiresAt", default=None)
    author: Optional[str] = None
    preview_background_color: Optional["RgbaColorInput"] = Field(
        alias="previewBackgroundColor", default=None
    )


class UpdateCopyrightInput(BaseModel):
    status: CopyrightStatus
    notice: Optional[str] = None


class UpdateCollectionInput(BaseModel):
    collection_id: str = Field(alias="collectionId")
    data: "UpdateCollectionDataInput"


class UpdateCollectionDataInput(BaseModel):
    name: str


class UpdateCustomMetadataPropertyInput(BaseModel):
    id: str
    data: "UpdateCustomMetadataPropertyDataInput"


class UpdateCustomMetadataPropertyDataInput(BaseModel):
    name: Optional[str] = None
    type: Optional["UpdateCustomMetadataPropertyTypeInput"] = None
    help_text: Optional[str] = Field(alias="helpText", default=None)
    is_required: Optional[bool] = Field(alias="isRequired", default=None)
    default_value: Optional[str] = Field(alias="defaultValue", default=None)


class UpdateCustomMetadataPropertyTypeInput(BaseModel):
    options: Optional[List["UpdateCustomMetadataPropertyTypeOptionInput"]] = None


class UpdateCustomMetadataPropertyTypeOptionInput(BaseModel):
    id: Optional[str] = None
    value: str
    is_default: Optional[bool] = Field(alias="isDefault", default=False)


class UpdateFolderInput(BaseModel):
    id: str
    data: "UpdateFolderDataInput"


class UpdateFolderDataInput(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class UpdateWorkflowChecklistItemInput(BaseModel):
    id: str
    data: "UpdateWorkflowChecklistItemDataInput"


class UpdateWorkflowChecklistItemDataInput(BaseModel):
    content: Optional[str] = None
    assignee_user_id: Optional[str] = Field(alias="assigneeUserId", default=None)


class UpdateWorkflowChecklistPresetInput(BaseModel):
    id: str
    data: "UpdateWorkflowChecklistPresetDataInput"


class UpdateWorkflowChecklistPresetDataInput(BaseModel):
    content: Optional[str] = None
    assignee_user_id: Optional[str] = Field(alias="assigneeUserId", default=None)


class UpdateWorkflowStatusInput(BaseModel):
    id: str
    data: "UpdateWorkflowStatusDataInput"


class UpdateWorkflowStatusDataInput(BaseModel):
    title: Optional[str] = None
    color: Optional["RgbaColorInput"] = None


class UpdateWorkflowTaskInput(BaseModel):
    id: str
    data: "UpdateWorkflowTaskDataInput"


class UpdateWorkflowTaskDataInput(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class UploadFileInput(BaseModel):
    filename: str
    size: Any
    chunk_size: Optional[Any] = Field(alias="chunkSize", default=104857600)


class CreateBrandInput(BaseModel):
    name: str
    color: Optional["RgbaColorInput"] = None


class DeleteBrandInput(BaseModel):
    id: str


class UpdateBrandInput(BaseModel):
    id: str
    data: "UpdateBrandDataInput"


class UpdateBrandDataInput(BaseModel):
    name: Optional[str] = None
    color: Optional["RgbaColorInput"] = None


class CancelExportCreativesInput(BaseModel):
    ids: List[str]
