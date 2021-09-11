# encoding=utf-8

from enum import Enum, unique
from django.db import models
from scauth.models import AuthUser
from common.models import BaseModel


@unique
class EventStatus(Enum):
    WAIT_CHECK = "WAIT_CHECK"            # 待审核
    WAAIT_SOLUTE = "WAAIT_SOLUTE"        # 待解决
    WAIT_BACK = "WAIT_BACK"              # 待反馈
    FINISH = "FINISH"                    # 已完成


class EventCat(BaseModel):
    name = models.CharField(
        max_length=100,
        default="",
        verbose_name="类别名称",
    )
    detail = models.CharField(
        max_length=512,
        default="",
        verbose_name="类别说明",
    )
    is_active = models.BooleanField(
        default=True, verbose_name="是否是有效"
    )

    class Meta:
        verbose_name = "事件类别表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class Event(BaseModel):
    list_status = [
        status for status in EventStatus
    ]
    status_choices: list = [
        (status.value, status.value)
        for status in EventStatus
    ]
    user = models.ForeignKey(
        AuthUser,
        related_name="event_publish_user",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="事件发布人",
    )
    event_cat = models.ForeignKey(
        EventCat,
        related_name="goods_cat",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="事件分类",
    )
    title = models.CharField(
        max_length=512,
        default="",
        verbose_name="事件标题",
    )
    detail = models.CharField(
        max_length=10000,
        default="",
        verbose_name="事件详情",
    )
    mark = models.CharField(
        max_length=512,
        default="",
        verbose_name="事件备注",
    )
    status = models.CharField(
        max_length=100,
        choices=status_choices,
        default="WAIT_CHECK",
        verbose_name="事件状态",
    )
    views = models.PositiveIntegerField(
        default=0, verbose_name="事件浏览次数"
    )
    is_active = models.BooleanField(
        default=True, verbose_name="是否是有效"
    )

    class Meta:
        verbose_name = "事件表"
        verbose_name_plural = "事件表"

    def __str__(self):
        return self.name

    def as_dict(self):
        return {"id": self.id}


class EventBack(BaseModel):
    user = models.ForeignKey(
        AuthUser,
        related_name="event_back_user",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="反馈人",
    )
    event = models.ForeignKey(
        Event,
        related_name="event_back",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="关联事件",
    )
    content = models.CharField(
        max_length=1024,
        default="",
        blank=True,
        null=True,
        verbose_name="论坛内容",
    )
    views = models.PositiveIntegerField(
        default=0,
        verbose_name="查看次数"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="是否是有效"
    )

    class Meta:
        verbose_name = "事件用户反馈表"
        verbose_name_plural = "事件用户反馈表"

    def __str__(self):
        return self.content

    def as_dict(self):
        return {
            "id": self.id
        }


class EventComment(BaseModel):
    user = models.ForeignKey(
        AuthUser,
        related_name="event_comment_reply_user",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="评论发布者",
    )
    event = models.ForeignKey(
        Event,
        related_name="event_comment_reply",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="关联事件",
    )
    father_forum_cy = models.ForeignKey(
        "EventComment",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="父评论",
    )
    content = models.CharField(
        max_length=1024,
        default="",
        blank=True,
        null=True,
        verbose_name="论坛内容",
    )
    views = models.PositiveIntegerField(
        default=0,
        verbose_name="查看次数"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="是否是有效"
    )

    class Meta:
        verbose_name = "事件评论回复表"
        verbose_name_plural = "事件评论回复表"

    def __str__(self):
        return self.content

    def as_dict(self):
        return {
            "id": self.id
        }
