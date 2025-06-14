from django.urls import path
from . import views

urlpatterns=[
    path('' , views.home , name='home'),
    path('login/' , views.login_user , name='login'),
    path('logout/' , views.logout_user , name='logout'),
    path('signup/' , views.signup_user , name='signup'),
    path('records_view/' , views.record_view , name='records_view'),
    path('record_detail/<int:pk>/' , views.record_detail , name='record_detail'),
    path('delete_record/<int:pk>/' , views.record_delete , name='delete_record'),
]