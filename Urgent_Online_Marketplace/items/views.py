from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Item

# Create your views here.


def details(request, pk):
    #item = get_object_or_404(Item, pk=pk)
    item = Item.objects.get(id=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'items/details.html', {
        'item': item,
        'related_items': related_items,
    })
