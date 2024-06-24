from django.urls import path
from . import views

app_name = 'hw3_app'

urlpatterns = [

    path('', views.index, name='index'),  # вывод главной страницы
    path('client_orders/<int:client_id>', views.client_orders),
]
