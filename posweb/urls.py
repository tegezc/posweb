from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include URLs from accounts app
    path('products/', include('products.urls')),  # Include URLs from product app
    path('', lambda request: redirect('accounts/login/')),  # Redirect root URL to login
]
