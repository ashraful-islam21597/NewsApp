from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='create_order'),
    path('orderlist/',views.orderlist,name='orderlist')
]