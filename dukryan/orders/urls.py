from django.conf.urls import url, include
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'',views.item_list, name='item_list' ),

]