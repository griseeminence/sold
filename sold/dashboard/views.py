from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from item.models import Item


@login_required
def index(request):
    template = 'dashboard/index.html'
    items = Item.objects.filter(created_by=request.user).order_by('?')
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context = {
        'items': items
    }

    return render(request, template, context)
