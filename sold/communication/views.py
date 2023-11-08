from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Communication
from .forms import CommunicationMessageForm
from item.models import Item


@login_required
def new_communication(request, item_pk):
    template = 'communication/new_communication.html'
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    communications = Communication.objects.filter(item=item).filter(members__in=[request.user.id])

    if communications:
        return redirect('communication:detail', pk=communications.first().pk)

    if request.method == 'POST':
        form = CommunicationMessageForm(request.POST)

        if form.is_valid():
            communication = Communication.objects.create(item=item)
            communication.members.add(request.user)
            communication.members.add(item.created_by)
            communication.save()

            communication_message = form.save(commit=False)
            communication_message.communication = communication
            communication_message.created_by = request.user
            communication_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = CommunicationMessageForm()

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def inbox(request):
    communications = Communication.objects.filter(members__in=[request.user.id])
    template = 'communication/inbox.html'
    context = {
        'communications': communications
    }
    return render(request, template, context)


@login_required
def detail(request, pk):
    template = 'communication/detail.html'
    communications = Communication.objects.filter(members__in=[request.user.id]).get(pk=pk)
    if request.method == 'POST':
        form = CommunicationMessageForm(request.POST)

        if form.is_valid():
            communication_message = form.save(commit=False)
            communication_message.communication = communications
            communication_message.created_by = request.user
            communication_message.save()

            communications.save()

            return redirect('communication:detail', pk=pk)
    else:
        form = CommunicationMessageForm()

    context = {
        'communications': communications,
        'form': form,
    }
    return render(request, template, context)
