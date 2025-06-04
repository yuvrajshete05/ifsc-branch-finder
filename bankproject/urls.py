from django.contrib import admin
from django.urls import path
from bankapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/banks/', views.bank_list, name='bank_list'),
    path('api/branches/<str:ifsc>/', views.branch_detail, name='branch_detail'),
]
