from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from ..models import Question

# 맨 처음 페이지, 검색 창이랑 로고만 띄우기