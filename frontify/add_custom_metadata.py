# Generated by ariadne-codegen
# Source: queries-mutations

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class AddCustomMetadata(BaseModel):
    add_custom_metadata: Optional["AddCustomMetadataAddCustomMetadata"] = Field(
        alias="addCustomMetadata"
    )


class AddCustomMetadataAddCustomMetadata(BaseModel):
    parent_ids: List[str] = Field(alias="parentIds")


AddCustomMetadata.model_rebuild()
