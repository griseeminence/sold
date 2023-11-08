from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from item.forms import NewItemForm, EditItemForm
from item.models import Item, Category


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    template = 'item/items.html'

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))  # Выполняет поиск по имени

    context = {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    }
    return render(request, template, context)


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    template = 'item/detail.html'
    context = {
        'item': item,
        'related_items': related_items
    }
    return render(request, template, context)


@login_required
def new_item(request):
    template = 'item/new_item.html'
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.pk)
    else:
        form = NewItemForm()

    context = {'form': form,
               'title': 'New Item'}

    return render(request, template, context)


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    template = 'item/new_item.html'
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    context = {
        'form': form,
        'title': 'Edit item',
    }

    return render(request, template, context)


def category_list(request, category_slug):
    template = 'Item/category_list.html'
    item_by_category = Item.objects.filter(category__slug=category_slug)
    context = {
        'item_by_category': item_by_category,
    }
    return render(request, template, context)
