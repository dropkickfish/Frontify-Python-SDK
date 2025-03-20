# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Literal, Optional

from pydantic import Field

from .base_model import BaseModel


class UpdateWorkflowChecklistItem(BaseModel):
    update_workflow_checklist_item: Optional[
        "UpdateWorkflowChecklistItemUpdateWorkflowChecklistItem"
    ] = Field(alias="updateWorkflowChecklistItem")


class UpdateWorkflowChecklistItemUpdateWorkflowChecklistItem(BaseModel):
    checklist_item: Optional[
        "UpdateWorkflowChecklistItemUpdateWorkflowChecklistItemChecklistItem"
    ] = Field(alias="checklistItem")


class UpdateWorkflowChecklistItemUpdateWorkflowChecklistItemChecklistItem(BaseModel):
    id: str
    content: str
    assigned_user: Optional[
        "UpdateWorkflowChecklistItemUpdateWorkflowChecklistItemChecklistItemAssignedUser"
    ] = Field(alias="assignedUser")


class UpdateWorkflowChecklistItemUpdateWorkflowChecklistItemChecklistItemAssignedUser(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


UpdateWorkflowChecklistItem.model_rebuild()
UpdateWorkflowChecklistItemUpdateWorkflowChecklistItem.model_rebuild()
UpdateWorkflowChecklistItemUpdateWorkflowChecklistItemChecklistItem.model_rebuild()
