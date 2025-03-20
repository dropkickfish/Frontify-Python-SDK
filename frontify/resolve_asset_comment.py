# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel


class ResolveAssetComment(BaseModel):
    resolve_asset_comment: Optional["ResolveAssetCommentResolveAssetComment"] = Field(
        alias="resolveAssetComment"
    )


class ResolveAssetCommentResolveAssetComment(BaseModel):
    comment: Optional["ResolveAssetCommentResolveAssetCommentComment"]


class ResolveAssetCommentResolveAssetCommentComment(BaseModel):
    id: str
    creator: "ResolveAssetCommentResolveAssetCommentCommentCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["ResolveAssetCommentResolveAssetCommentCommentModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    content: str
    mentioned_users: List[
        Optional["ResolveAssetCommentResolveAssetCommentCommentMentionedUsers"]
    ] = Field(alias="mentionedUsers")
    is_resolved: bool = Field(alias="isResolved")
    replies: "ResolveAssetCommentResolveAssetCommentCommentReplies"
    marking: Optional["ResolveAssetCommentResolveAssetCommentCommentMarking"]
    current_user_permissions: (
        "ResolveAssetCommentResolveAssetCommentCommentCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")


class ResolveAssetCommentResolveAssetCommentCommentCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class ResolveAssetCommentResolveAssetCommentCommentModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class ResolveAssetCommentResolveAssetCommentCommentMentionedUsers(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class ResolveAssetCommentResolveAssetCommentCommentReplies(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[Optional["ResolveAssetCommentResolveAssetCommentCommentRepliesItems"]]
    ]


class ResolveAssetCommentResolveAssetCommentCommentRepliesItems(BaseModel):
    id: str
    creator: "ResolveAssetCommentResolveAssetCommentCommentRepliesItemsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "ResolveAssetCommentResolveAssetCommentCommentRepliesItemsModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    content: str
    mentioned_users: List[
        Optional[
            "ResolveAssetCommentResolveAssetCommentCommentRepliesItemsMentionedUsers"
        ]
    ] = Field(alias="mentionedUsers")


class ResolveAssetCommentResolveAssetCommentCommentRepliesItemsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class ResolveAssetCommentResolveAssetCommentCommentRepliesItemsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class ResolveAssetCommentResolveAssetCommentCommentRepliesItemsMentionedUsers(
    BaseModel
):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class ResolveAssetCommentResolveAssetCommentCommentMarking(BaseModel):
    typename__: Literal[
        "Marking", "MultiPageMarking", "SimpleMarking", "VideoMarking"
    ] = Field(alias="__typename")
    position: "ResolveAssetCommentResolveAssetCommentCommentMarkingPosition"
    dimensions: Optional[
        "ResolveAssetCommentResolveAssetCommentCommentMarkingDimensions"
    ]


class ResolveAssetCommentResolveAssetCommentCommentMarkingPosition(BaseModel):
    x: Any
    y: Any


class ResolveAssetCommentResolveAssetCommentCommentMarkingDimensions(BaseModel):
    width: Optional[Any]
    height: Optional[Any]


class ResolveAssetCommentResolveAssetCommentCommentCurrentUserPermissions(BaseModel):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_reply: bool = Field(alias="canReply")


ResolveAssetComment.model_rebuild()
ResolveAssetCommentResolveAssetComment.model_rebuild()
ResolveAssetCommentResolveAssetCommentComment.model_rebuild()
ResolveAssetCommentResolveAssetCommentCommentReplies.model_rebuild()
ResolveAssetCommentResolveAssetCommentCommentRepliesItems.model_rebuild()
ResolveAssetCommentResolveAssetCommentCommentMarking.model_rebuild()
