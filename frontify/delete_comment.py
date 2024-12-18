# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class DeleteComment(BaseModel):
    delete_comment: Optional["DeleteCommentDeleteComment"] = Field(
        alias="deleteComment"
    )


class DeleteCommentDeleteComment(BaseModel):
    id: str


DeleteComment.model_rebuild()
