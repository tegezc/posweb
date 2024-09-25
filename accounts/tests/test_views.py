import pytest
from django.urls import reverse
from accounts.models import CustomUser  # Ganti auth.User dengan CustomUser

@pytest.mark.django_db
def test_signup_view(client):
    signup_data = {
        'username': 'testuser',
        'password1': 'TestPassword123',
        'password2': 'TestPassword123',
        'first_name': 'Test',
        'email': 'testuser@example.com',
        'phone_number': '1234567890'
    }

    response = client.post(reverse('signup'), signup_data)
    
    # Periksa apakah user berhasil dibuat di database
    user = CustomUser.objects.filter(username='testuser').exists()  # Menggunakan CustomUser
    assert user is True
    assert response.status_code == 302  # Redirect setelah signup sukses

@pytest.mark.django_db
def test_login_view(client):
    # Membuat user untuk pengujian login
    user = CustomUser.objects.create_user(
        username='testuser', 
        password='TestPassword123',
        email='testuser@example.com'
    )

    # Data login
    login_data = {
        'username': 'testuser',
        'password': 'TestPassword123'
    }

    response = client.post(reverse('login'), login_data)
    
    assert response.status_code == 302  # Redirect ke halaman setelah login berhasil

@pytest.mark.django_db
def test_login_view_invalid_credentials(client):
    login_data = {
        'username': 'invaliduser',
        'password': 'invalidpassword'
    }

    response = client.post(reverse('login'), login_data)

    assert 'Invalid username or password.' in response.content.decode('utf-8')  # Pesan kesalahan harus ada
    assert response.status_code == 200  # Tetap di halaman login
