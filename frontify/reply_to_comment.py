# Generated by ariadne-codegen
# Source: queries-mutations

from typing import Any, List, Literal, Optional

from pydantic import Field

from .base_model import BaseModel


class ReplyToComment(BaseModel):
    reply_to_comment: Optional["ReplyToCommentReplyToComment"] = Field(
        alias="replyToComment"
    )


class ReplyToCommentReplyToComment(BaseModel):
    reply: "ReplyToCommentReplyToCommentReply"


class ReplyToCommentReplyToCommentReply(BaseModel):
    id: str
    creator: "ReplyToCommentReplyToCommentReplyCreator"
    created_at: Any = Field(alias="createdAt")
    modifier: Optional["ReplyToCommentReplyToCommentReplyModifier"]
    modified_at: Optional[Any] = Field(alias="modifiedAt")
    content: str
    mentioned_users: List[
        Optional["ReplyToCommentReplyToCommentReplyMentionedUsers"]
    ] = Field(alias="mentionedUsers")


class ReplyToCommentReplyToCommentReplyCreator(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class ReplyToCommentReplyToCommentReplyModifier(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


class ReplyToCommentReplyToCommentReplyMentionedUsers(BaseModel):
    typename__: Literal["AccountUser", "User"] = Field(alias="__typename")
    id: str
    email: Any
    name: Optional[str]
    avatar: Optional[Any]


ReplyToComment.model_rebuild()
ReplyToCommentReplyToComment.model_rebuild()
ReplyToCommentReplyToCommentReply.model_rebuild()