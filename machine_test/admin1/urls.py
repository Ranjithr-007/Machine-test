from . import views
from django.urls import path

urlpatterns=[
    path('',views.adminlogin, name='admin_login'),
    path('adminhome/',views.adminhome, name='adminhome'),
    path('logout/',views.logout, name='logout'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('adduser/',views.adduser, name='adduser'),
    
]