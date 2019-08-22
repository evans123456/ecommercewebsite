from django.shortcuts import render
from . import models

# Create your views here.
def item_list(request):
    context = {
        'items': models.Item.objects.all()
    }
    return render(request,'orders/item_list.html',context)