from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from items.models import Item

# Create your views here.


@login_required(login_url='signin')
def dashboard(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/dashboard.html', {
        'items': items
    })
