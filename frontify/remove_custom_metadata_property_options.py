# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, Literal, Optional

from pydantic import Field

from .base_model import BaseModel


class RemoveCustomMetadataPropertyOptions(BaseModel):
    remove_custom_metadata_property_options: Optional[
        "RemoveCustomMetadataPropertyOptionsRemoveCustomMetadataPropertyOptions"
    ] = Field(alias="removeCustomMetadataPropertyOptions")


class RemoveCustomMetadataPropertyOptionsRemoveCustomMetadataPropertyOptions(BaseModel):
    custom_metadata_property: (
        "RemoveCustomMetadataPropertyOptionsRemoveCustomMetadataPropertyOptionsCustomMetadataProperty"
    ) = Field(alias="customMetadataProperty")


class RemoveCustomMetadataPropertyOptionsRemoveCustomMetadataPropertyOptionsCustomMetadataProperty(
    BaseModel
):
    id: str
    creator: "RemoveCustomMetadataPropertyOptionsRemoveCustomMetadataPropertyOptionsCustomMetadataPropertyCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "RemoveCustomMetadataPropertyOptionsRemoveCustomMetadataPropertyOptionsCustomMetadataPropertyModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    name: str
    type: "RemoveCustomMetadataPropertyOptionsRemoveCustomMetadataPropertyOptionsCustomMetadataPropertyType"
    help_text: Optional[str] = Field(alias="helpText")
    is_required: bool = Field(alias="isRequired")
    default_value: Optional[Any] = Field(alias="defaultValue")


class RemoveCustomMetadataPropertyOptionsRemoveCustomMetadataPropertyOptionsCustomMetadataPropertyCreator(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class RemoveCustomMetadataPropertyOptionsRemoveCustomMetadataPropertyOptionsCustomMetadataPropertyModifier(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class RemoveCustomMetadataPropertyOptionsRemoveCustomMetadataPropertyOptionsCustomMetadataPropertyType(
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


RemoveCustomMetadataPropertyOptions.model_rebuild()
RemoveCustomMetadataPropertyOptionsRemoveCustomMetadataPropertyOptions.model_rebuild()
RemoveCustomMetadataPropertyOptionsRemoveCustomMetadataPropertyOptionsCustomMetadataProperty.model_rebuild()
