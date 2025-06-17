from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login , logout , authenticate
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Record
from .forms import UserRegistrationForm , AddRecordForm



# Create your views here.
def home(request):
    return render(request , 'home.html' , {})



def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddRecordForm(request.POST, request.FILES)  # Correct way
            if form.is_valid():
                form.save()
                messages.success(request, 'Record added successfully')
                return redirect('records_view')
            else:
                messages.error(request, 'Error adding record. Please correct the errors below.')
        else:
            form = AddRecordForm()
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, 'You must login first to access this page!')
        return redirect('login')


def update_record(request, pk):
    current_record = get_object_or_404(Record, pk=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddRecordForm(request.POST, request.FILES, instance=current_record)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record updated successfully')
                return redirect('records_view')
            else:
                messages.error(request, 'Update record failed!')
        else:
            form = AddRecordForm(instance=current_record)
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, 'You have to sign in')
        return redirect('login')



def record_view(request):
        records = Record.objects.all()
        return render(request , 'records_view.html' , {'records' : records})



def record_detail(request , pk):
    # my_record = Record.objects.get(pk=pk)
    record = get_object_or_404(Record , pk = pk)
    return render(request , 'record_detail.html' ,{'record' : record})




@require_http_methods(["DELETE", "POST"])
def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method in ['POST', 'DELETE']:
        record.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('records_view')
    messages.error(request, 'Invalid request method')
    return redirect('record_detail', pk=pk)


def signup_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']

            user = User(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.set_password(password)
            user.save()

            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = UserRegistrationForm()

    return render(request, 'signup_user.html', {'form': form})


# def signup_user(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)  # Don't save yet
#             user.first_name = form.cleaned_data['name']       # map 'name' to first_name
#             user.last_name = form.cleaned_data['last_name']   # map 'last_name'
#             user.email = form.cleaned_data['email']           # map 'email'
#             user.save()                                      # now save all fields
#             messages.success(request, 'Account created successfully')
#             return redirect('login')
#         else:
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f"{field.capitalize()}: {error}")
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'signup_user.html', {'form': form})



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # 'on' if checked

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if remember_me != 'on':
                request.session.set_expiry(0)  # Session expires on browser close
            else:
                request.session.set_expiry(1209600)  # 2 weeks

            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login_user.html')



# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request , 'Login successfully')
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid username or password')
#             return redirect('login')
#     return render(request, 'login_user.html')



def logout_user(request):
    logout(request)
    messages.success(request , 'Logout successfully')
    return redirect('home')




