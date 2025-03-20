# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, Literal, Optional

from pydantic import Field

from .base_model import BaseModel


class AddCustomMetadataPropertyOptions(BaseModel):
    add_custom_metadata_property_options: Optional[
        "AddCustomMetadataPropertyOptionsAddCustomMetadataPropertyOptions"
    ] = Field(alias="addCustomMetadataPropertyOptions")


class AddCustomMetadataPropertyOptionsAddCustomMetadataPropertyOptions(BaseModel):
    custom_metadata_property: (
        "AddCustomMetadataPropertyOptionsAddCustomMetadataPropertyOptionsCustomMetadataProperty"
    ) = Field(alias="customMetadataProperty")


class AddCustomMetadataPropertyOptionsAddCustomMetadataPropertyOptionsCustomMetadataProperty(
    BaseModel
):
    id: str
    creator: "AddCustomMetadataPropertyOptionsAddCustomMetadataPropertyOptionsCustomMetadataPropertyCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "AddCustomMetadataPropertyOptionsAddCustomMetadataPropertyOptionsCustomMetadataPropertyModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: str
    type: "AddCustomMetadataPropertyOptionsAddCustomMetadataPropertyOptionsCustomMetadataPropertyType"
    help_text: Optional[str] = Field(alias="helpText")
    is_required: bool = Field(alias="isRequired")
    default_value: Optional[Any] = Field(alias="defaultValue")


class AddCustomMetadataPropertyOptionsAddCustomMetadataPropertyOptionsCustomMetadataPropertyCreator(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class AddCustomMetadataPropertyOptionsAddCustomMetadataPropertyOptionsCustomMetadataPropertyModifier(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class AddCustomMetadataPropertyOptionsAddCustomMetadataPropertyOptionsCustomMetadataPropertyType(
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


AddCustomMetadataPropertyOptions.model_rebuild()
AddCustomMetadataPropertyOptionsAddCustomMetadataPropertyOptions.model_rebuild()
AddCustomMetadataPropertyOptionsAddCustomMetadataPropertyOptionsCustomMetadataProperty.model_rebuild()
