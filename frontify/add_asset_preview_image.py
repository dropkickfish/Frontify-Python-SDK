# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class AddAssetPreviewImage(BaseModel):
    add_asset_preview_image: Optional["AddAssetPreviewImageAddAssetPreviewImage"] = (
        Field(alias="addAssetPreviewImage")
    )


class AddAssetPreviewImageAddAssetPreviewImage(BaseModel):
    job: "AddAssetPreviewImageAddAssetPreviewImageJob"


class AddAssetPreviewImageAddAssetPreviewImageJob(BaseModel):
    asset_id: str = Field(alias="assetId")


AddAssetPreviewImage.model_rebuild()
AddAssetPreviewImageAddAssetPreviewImage.model_rebuild()