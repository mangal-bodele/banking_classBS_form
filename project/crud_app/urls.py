from django.urls import path
from .views import Create_Banking,Show_Banking,Update_Banking,Delete_Banking

urlpatterns = [
    path('create/',Create_Banking.as_view(),name='create_url'),
    path('show/',Show_Banking.as_view(),name='show_url'),
    path('update/<int:pk>/',Update_Banking.as_view(),name='update_url'),
    path('delete/<int:pk>/',Delete_Banking.as_view(),name='delete_url')
]