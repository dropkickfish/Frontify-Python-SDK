# Generated by ariadne-codegen
# Source: queries-mutations

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class DeleteFolders(BaseModel):
    delete_folders: Optional["DeleteFoldersDeleteFolders"] = Field(
        alias="deleteFolders"
    )


class DeleteFoldersDeleteFolders(BaseModel):
    ids: Optional[List[str]]


DeleteFolders.model_rebuild()
