import pytest
from django.urls import reverse
from products.models import Product

# Fixture untuk membuat client yang sudah login
@pytest.fixture
def logged_in_client(client, django_user_model):
    # Buat user baru
    user = django_user_model.objects.create_user(username='testuser', password='testpass')
    
    # Login menggunakan client
    client.login(username='testuser', password='testpass')
    
    return client

# Fixture untuk membuat contoh produk
@pytest.fixture
def create_product():
    return Product.objects.create(name='Test Product', description='Test Description', price=100, stock=10)

@pytest.mark.django_db
def test_add_product_view(logged_in_client):
    # Data untuk produk baru
    product_data = {
        'name': 'New Product',
        'description': 'New Description',
        'price': 200,
        'stock': 5
    }

    # Kirim POST request untuk menambah produk
    response = logged_in_client.post(reverse('add_product'), product_data)

    # Pastikan respons adalah redirect (setelah sukses menambah produk)
    assert response.status_code == 302

    # Pastikan produk baru ditambahkan ke database
    assert Product.objects.filter(name='New Product').exists()

@pytest.mark.django_db
def test_product_list_view(logged_in_client, create_product):
    # Buat request untuk halaman list produk
    response = logged_in_client.get(reverse('product_list'))
    
    # Pastikan respons sukses
    assert response.status_code == 200

    # Pastikan produk yang dibuat ada di respons
    assert 'Test Product' in str(response.content)

@pytest.mark.django_db
def test_add_product_view_without_login(client):
    # Coba akses halaman tambah produk tanpa login
    response = client.get(reverse('add_product'))

    # Pastikan diarahkan ke halaman login
    assert response.status_code == 302
    assert '/accounts/login/' in response.url
