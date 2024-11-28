# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class UploadFile(BaseModel):
    upload_file: Optional["UploadFileUploadFile"] = Field(alias="uploadFile")


class UploadFileUploadFile(BaseModel):
    id: str
    urls: List[Optional[Any]]


UploadFile.model_rebuild()