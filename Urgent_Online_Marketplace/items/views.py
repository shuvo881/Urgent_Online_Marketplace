from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import NewItemAddForm
from .models import Item
from django.urls import reverse

# Create your views here.


def details(request, pk):
    print('pk: ', pk)
    #item = get_object_or_404(Item, pk=pk)
    item = Item.objects.get(id=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'items/details.html', {
        'item': item,
        'related_items': related_items,
    })

@login_required
def new_item_add(request):
    if request.method == 'POST':
        form = NewItemAddForm(request.POST, request.FILES)
        print("yes: ", request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, 'Item added successful...')
            return redirect('details', pk=item.id)
        else:
            messages.error(request, 'Check blew errors')

    else:
        form = NewItemAddForm()
    return render(request, 'items/new_item_add.html', {'form': form, 'title': 'New item'})