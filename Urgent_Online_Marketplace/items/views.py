from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import NewItemAddForm, EditItemForm
from .models import Item, Category
from django.urls import reverse
from django.db.models import Q

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


@login_required(login_url='signin')
def new_item_add(request):
    if request.method == 'POST':
        form = NewItemAddForm(request.POST, request.FILES)
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


@login_required(login_url='signin')
def delete_item(request, pk):
    item = Item.objects.get(pk=pk, created_by=request.user)
    item.delete()
    messages.success(request, 'Item deleted successful')
    return redirect('dashboard')


@login_required(login_url='signin')
def edit_item(request, pk):

    item = Item.objects.get(pk=pk, created_by=request.user)
    if request.method == 'POST':

        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():

            item.save()
            messages.success(request, 'Item edit successful...')
            return redirect('details', pk=item.id)
        else:
            messages.error(request, 'Check blew errors')

    else:
        form = EditItemForm(instance=item)
    return render(request, 'items/new_item_add.html', {'form': form, 'title': 'Edit item'})


def browser(request):
    query = request.GET.get('query', '')
    category_id = int(request.GET.get('category', 0))
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    if category_id:
        items = items.filter(category_id=category_id)
    if len(items) == 0:
        messages.info(request, "No search item")
    return render(request, 'items/browser.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': category_id,
    })
