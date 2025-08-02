from django.urls import path, include
from . import views
urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('insert_data/', views.insert_data, name='insert_data'),
    path('show_page/', views.show_page, name='show_page'),
    path('edit_data/<int:id>/', views.edit_data, name='edit_data'),
    path('update_data/<int:id>/', views.update_data, name='update_data'),
    path('delete_data/<int:id>/', views.delete_data, name='delete_data'),
    
    
    path('', views.register, name='register'),    
    path('register_user/', views.register_user, name='register_user'),
    path('login/', views.login, name='login'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    
]
 
