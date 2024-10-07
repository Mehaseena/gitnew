from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('admindashboard/', views.admin_view, name='admin_view'),   
    path('home/',views.home, name='home'),
	path('productlist/', views.product_list, name='product_list'),
	# path('create/', views.product_create, name='product_create'),
    path('details/<int:id>', views.product_details, name='product_details'),
	path('cart/', views.view_cart, name='view_cart'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('orderplace/', views.place_order, name='place_order'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
    path('create-category/', views.create_category, name='create_category'),
    path('create-product/', views.create_product, name='create_product'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
]

