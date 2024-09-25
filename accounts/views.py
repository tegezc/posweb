from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Login user setelah signup
            return redirect('login')  # Redirect setelah signup berhasil
        else:
            messages.error(request, "Please correct the error below.")  # Menampilkan pesan error
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Ubah ini sesuai dengan URL yang benar
        else:
            messages.error(request, "Invalid username or password.")  # Pesan untuk login gagal
    return render(request, 'accounts/login.html')

@login_required  # Memastikan hanya pengguna yang sudah login yang bisa mengakses halaman home
def home_view(request):
    user = request.user  # Mendapatkan informasi pengguna yang sedang login
    return render(request, 'accounts/home.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('login')
