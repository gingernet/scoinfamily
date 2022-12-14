#encoding=utf-8

from django.shortcuts import render
from blogs.models import Tag, Category, BaseModel
from common.helpers import paged_items, ok_json
from common.pc_m import judge_pc_or_mobile
from cevent.models import Event
from blogs.models import Article
from tools.models import Tools


def index(request):
    nav_bar = "index"
    user_agt = judge_pc_or_mobile(request.META.get("HTTP_USER_AGENT"))
    lst_event = Event.objects.filter(
        status__in=["WAIT_CHECK", "WAIT_SOLUTE", "WAIT_BACK", "FINISH"]
    ).order_by("-id")[:10]
    lst_arctcle = Article.objects.filter(is_active=True)[:3]
    lst_tools = Tools.objects.filter(is_active=True)[:8]
    if user_agt is False:
        return render(request, 'web/pages/index.html', locals())
    else:
        return render(request, 'web/pages/index.html', locals())
