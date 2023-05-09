from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MyPasswordSetForm
from django.contrib import admin


urlpatterns = [
    path("", views.home),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("category/<slug:value>", views.CategoryView.as_view(), name='category'),
    path("category-title/<value>", views.CategoryTitle.as_view(), name='category-title'),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(), name='product-detail'),
    path("update-profile/", views.ProfileView.as_view(), name='update-profile'),
    path("profile/", views.profile, name='profile'),
    path("update-address/", views.AddressView.as_view(), name='update-address'),
    path("update-address/<int:pk>", views.AddressUpdateView.as_view(), name='address-update'),
    path('address/', views.address, name='address'),

    path('towns', views.get_towns, name='towns'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('show-cart/', views.show_cart, name='show-cart'),
    path('checkout/', views.CheckOutView.as_view(), name='checkout'),

    path('search/', views.search, name='search'),
    path('shop/', views.shop, name='shop'),
    path('wishlist/', views.wishlist_display, name='wishlist'),
    path('paymentdone/', views.make_payment, name='payment'),
    path('orders/', views.orders, name='orders'),

    path('selectedaddress/', views.selected_address),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('pluswishlist/', views.plus_wishlist),
    path('minuswishlist/', views.minus_wishlist),
    path('removewishlist/', views.remove_wishlist),


    # authentication
    path('registration', views.CustomerRegistrationView.as_view(), name='registration'),
    path('accounts/login/', auth_view.LoginView.as_view(
        template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('password-change/', auth_view.PasswordChangeView.as_view(
     template_name='app/password-change.html', form_class=MyPasswordChangeForm,
     success_url='/password-changed'), name='password-change'),
    path('password-changed/', auth_view.PasswordChangeDoneView.as_view(
        template_name='app/password-changed.html'), name='password-changed'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='app/password-reset.html', form_class=MyPasswordResetForm),
        name='password-reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='app/password-reset-done.html'), name='password_reset_done'),
    path('password_rest_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='app/password-reset-confirm.html', form_class=MyPasswordSetForm),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='app/password-reset-complete.html'), name='password_reset_complete')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Maringo Sports Club'
admin.site.site_title = 'Maringo Sports Club'
admin.site.site_index_title = 'Welcome to Maringo Sports Club'





