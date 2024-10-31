from django.urls import path
from myapp.views import expenditure_list
from . import views

urlpatterns = [
    path('home/', views.home, name='home'), 
    path('expenses/', views.expenses, name='expenses'), 
    path('', views.index, name='index'), 
    path('add-expenditure/', views.add_expenditure, name='add-expenditure'),
    path('expenditure-list/', views.expenditure_list, name='expenditure-list'),
    path('register/', views.register, name='register'), 
    path('users/', views.user_list, name='user-list'),
    path('login/', views.login_view, name='login'),
    
    path('user/expenditure-list/', views.user_expenditure_list, name='user-expenditure-list'),
]
