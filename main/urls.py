from django.urls import path
from . import views
from .views import (
    MenuListView,
    MenuListView1,
    MenuListView2,
    MenuListView3,
    MenuListView4,
    menuDetail,
    add_to_cart,
    get_cart_items,
    order_item,
    CartDeleteView,
    order_details,
    admin_view,
    item_list,
    pending_orders,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
    pay,
    final,
    update_status,
    end,
    about,
    contact,
    add_reviews, MenuList, MenuListView1, contacted,
)

app_name = "main"

urlpatterns = [
    path('', MenuList.as_view(), name='Hotels'),
    path('home', MenuListView.as_view(), name='home'),
    path('home1', MenuListView1.as_view(), name='home1'),
    path('home2', MenuListView2.as_view(), name='home2'),
    path('contact', contact.as_view(), name='contact'),
    path('contactus', contacted, name='contacted'),
    path('about', about.as_view(), name='about'),
    path('home3', MenuListView3.as_view(), name='home3'),
    path('home4', MenuListView4.as_view(), name='home4'),
    path('dishes/<slug>', views.menuDetail, name='dishes'),
    path('item_list/', views.item_list, name='item_list'),
    path('item/new/', ItemCreateView.as_view(), name='item-create'),
    path('item-update/<slug>/', ItemUpdateView.as_view(), name='item-update'),
    path('item-delete/<slug>/', ItemDeleteView.as_view(), name='item-delete'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.get_cart_items, name='cart'),
    path('remove-from-cart/<int:pk>/', CartDeleteView.as_view(), name='remove-from-cart'),
    path('payment/', views.pay, name='payment'),
    path('done/',views.final,name='done'),
    path('',views.end,name='finish'),
    path('ordered/', views.order_item, name='ordered'),
    path('order_details/', views.order_details, name='order_details'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('pending_orders/', views.pending_orders, name='pending_orders'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update_status/<int:pk>', views.update_status, name='update_status'),
    path('postReview', views.add_reviews, name='add_reviews'),
    path('subscribe/', views.subscribe, name = 'subscribe'),
]
