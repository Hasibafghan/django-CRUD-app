from django.urls import path
from . import views

urlpatterns=[
    path('' , views.home , name='home'),
    path('login/' , views.login_user , name='login'),
    path('logout/' , views.logout_user , name='logout'),
    path('signup/' , views.signup_user , name='signup'),
    path('records_view/' , views.record_view , name='records_view'),
    path('add_record/' , views.add_record , name='add_record'),
    path('update_record/<int:pk>' , views.update_record , name='update_record'),
    path('record_detail/<int:pk>/' , views.record_detail , name='record_detail'),
    path('delete_record/<int:pk>/' , views.record_delete , name='delete_record'),
]

