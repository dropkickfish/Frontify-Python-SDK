# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel


class ReopenAssetComment(BaseModel):
    reopen_asset_comment: Optional["ReopenAssetCommentReopenAssetComment"] = Field(
        alias="reopenAssetComment"
    )


class ReopenAssetCommentReopenAssetComment(BaseModel):
    comment: Optional["ReopenAssetCommentReopenAssetCommentComment"]


class ReopenAssetCommentReopenAssetCommentComment(BaseModel):
    id: str
    creator: "ReopenAssetCommentReopenAssetCommentCommentCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["ReopenAssetCommentReopenAssetCommentCommentModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    content: str
    mentioned_users: List[
        Optional["ReopenAssetCommentReopenAssetCommentCommentMentionedUsers"]
    ] = Field(alias="mentionedUsers")
    is_resolved: bool = Field(alias="isResolved")
    replies: "ReopenAssetCommentReopenAssetCommentCommentReplies"
    marking: Optional["ReopenAssetCommentReopenAssetCommentCommentMarking"]
    current_user_permissions: (
        "ReopenAssetCommentReopenAssetCommentCommentCurrentUserPermissions"
    ) = Field(alias="currentUserPermissions")


class ReopenAssetCommentReopenAssetCommentCommentCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class ReopenAssetCommentReopenAssetCommentCommentModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class ReopenAssetCommentReopenAssetCommentCommentMentionedUsers(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class ReopenAssetCommentReopenAssetCommentCommentReplies(BaseModel):
    total: int
    page: int
    limit: int
    has_next_page: bool = Field(alias="hasNextPage")
    items: Optional[
        List[Optional["ReopenAssetCommentReopenAssetCommentCommentRepliesItems"]]
    ]


class ReopenAssetCommentReopenAssetCommentCommentRepliesItems(BaseModel):
    id: str
    creator: "ReopenAssetCommentReopenAssetCommentCommentRepliesItemsCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional[
        "ReopenAssetCommentReopenAssetCommentCommentRepliesItemsModifier"
    ]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    content: str
    mentioned_users: List[
        Optional[
            "ReopenAssetCommentReopenAssetCommentCommentRepliesItemsMentionedUsers"
        ]
    ] = Field(alias="mentionedUsers")


class ReopenAssetCommentReopenAssetCommentCommentRepliesItemsCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class ReopenAssetCommentReopenAssetCommentCommentRepliesItemsModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class ReopenAssetCommentReopenAssetCommentCommentRepliesItemsMentionedUsers(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    name: Optional[str]


class ReopenAssetCommentReopenAssetCommentCommentMarking(BaseModel):
    typename__: Literal[
        "Marking", "MultiPageMarking", "SimpleMarking", "VideoMarking"
    ] = Field(alias="__typename")
    position: "ReopenAssetCommentReopenAssetCommentCommentMarkingPosition"
    dimensions: Optional["ReopenAssetCommentReopenAssetCommentCommentMarkingDimensions"]


class ReopenAssetCommentReopenAssetCommentCommentMarkingPosition(BaseModel):
    x: Any
    y: Any


class ReopenAssetCommentReopenAssetCommentCommentMarkingDimensions(BaseModel):
    width: Optional[Any]
    height: Optional[Any]


class ReopenAssetCommentReopenAssetCommentCommentCurrentUserPermissions(BaseModel):
    can_edit: bool = Field(alias="canEdit")
    can_delete: bool = Field(alias="canDelete")
    can_reply: bool = Field(alias="canReply")


ReopenAssetComment.model_rebuild()
ReopenAssetCommentReopenAssetComment.model_rebuild()
ReopenAssetCommentReopenAssetCommentComment.model_rebuild()
ReopenAssetCommentReopenAssetCommentCommentReplies.model_rebuild()
ReopenAssetCommentReopenAssetCommentCommentRepliesItems.model_rebuild()
ReopenAssetCommentReopenAssetCommentCommentMarking.model_rebuild()
