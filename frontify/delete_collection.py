# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class DeleteCollection(BaseModel):
    delete_collection: Optional["DeleteCollectionDeleteCollection"] = Field(
        alias="deleteCollection"
    )


class DeleteCollectionDeleteCollection(BaseModel):
    id: str


DeleteCollection.model_rebuild()
