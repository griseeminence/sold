from django.shortcuts import render, get_object_or_404

from item.models import Item


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {'item': item}
    return render(request, 'item/detail.html', context)