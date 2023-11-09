from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from .forms import SignupForm
from item.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False).order_by('?')

    paginator = Paginator(items, 3)

    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    template = 'core/index.html'
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories
    }
    return render(request, template, context)


# def signup(request):
#     template = 'core/signup.html'
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login/')
#     else:
#         form = SignupForm()
#     context = {
#         'form': form
#     }
#     return render(request, template, context)


def contact(request):
    template = 'static/contact.html'
    return render(request, template)


def about(request):
    template = 'static/about.html'
    return render(request, template)


def terms(request):
    template = 'static/terms.html'
    return render(request, template)
