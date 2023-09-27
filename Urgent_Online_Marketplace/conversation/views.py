from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from items.models import Item
from django.shortcuts import redirect
from .models import Conversation
from .forms import ConversationMessagesForm
# Create your views here.


@login_required(login_url='signin')
def new_conversation(request, item_pk):
    item = Item.objects.get(pk=item_pk)

    if item.created_by == request.user:
        return redirect('index')
    conversation = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    if conversation:
        pass # redirect to conversaton

    if request.method == 'POST':
        form = ConversationMessagesForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('details', pk=item_pk)
    else:
        form = ConversationMessagesForm()
    return render(request, 'conversation/new_conversation.html', {'form': form})


@login_required(login_url='signin')
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required(login_url='signin')
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessagesForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('detail', pk=pk)
    else:
        form = ConversationMessagesForm()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form,
    })
