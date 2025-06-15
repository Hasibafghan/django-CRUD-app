from django.urls import path
from . import views

urlpatterns=[
    path('' , views.home , name='home'),
    path('login/' , views.login_user , name='login'),
    path('logout/' , views.logout_user , name='logout'),
    path('signup/' , views.signup_user , name='signup'),
    path('records_view/' , views.record_view , name='records_view'),
    path('add_record/' , views.add_record , name='add_record'),
    path('record_detail/<int:pk>/' , views.record_detail , name='record_detail'),
    path('delete_record/<int:pk>/' , views.record_delete , name='delete_record'),
]

# if request.method == 'POST':
#         form = AddRecordForm(request.POST or None) #request.FILES
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Record added successfully')
#             return redirect('records_view')
#         else:
#             messages.error(request, 'Error adding record. Please correct the errors below.')
#     else:
#         form = AddRecordForm()

#     return render(request, 'add_record.html', {'form': form})

