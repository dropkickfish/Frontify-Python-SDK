# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, Literal, Optional

from pydantic import Field

from .base_model import BaseModel


class UpdateCustomMetadataProperty(BaseModel):
    update_custom_metadata_property: Optional[
        "UpdateCustomMetadataPropertyUpdateCustomMetadataProperty"
    ] = Field(alias="updateCustomMetadataProperty")


class UpdateCustomMetadataPropertyUpdateCustomMetadataProperty(BaseModel):
    property: "UpdateCustomMetadataPropertyUpdateCustomMetadataPropertyProperty"


class UpdateCustomMetadataPropertyUpdateCustomMetadataPropertyProperty(BaseModel):
    id: str
    creator: "UpdateCustomMetadataPropertyUpdateCustomMetadataPropertyPropertyCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "UpdateCustomMetadataPropertyUpdateCustomMetadataPropertyPropertyModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: str
    type: "UpdateCustomMetadataPropertyUpdateCustomMetadataPropertyPropertyType"
    help_text: Optional[str] = Field(alias="helpText")
    is_required: bool = Field(alias="isRequired")
    default_value: Optional[Any] = Field(alias="defaultValue")


class UpdateCustomMetadataPropertyUpdateCustomMetadataPropertyPropertyCreator(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class UpdateCustomMetadataPropertyUpdateCustomMetadataPropertyPropertyModifier(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class UpdateCustomMetadataPropertyUpdateCustomMetadataPropertyPropertyType(BaseModel):
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


UpdateCustomMetadataProperty.model_rebuild()
UpdateCustomMetadataPropertyUpdateCustomMetadataProperty.model_rebuild()
UpdateCustomMetadataPropertyUpdateCustomMetadataPropertyProperty.model_rebuild()
