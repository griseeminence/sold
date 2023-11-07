from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Communication
from item.models import Item

from .forms import CommunicationMessageForm


@login_required
def new_communication(request, item_pk):
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

    return render(request, 'communication/new_communication.html', {
        'form': form
    })


@login_required
def inbox(request):
    communications = Communication.objects.filter(members__in=[request.user.id])
    return render(request, 'communication/inbox.html', {
        'communications': communications
    })


@login_required
def detail(request, pk):
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
    return render(request, 'communication/detail.html', {
        'communications': communications,
        'form': form,
    })
