from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_page),
    path("home/",views.homepage, name='home'),
    path("login/",views.login_view, name='login'),
    path("signup/",views.signup, name='signup'),
    path('logout/', views.LogoutView, name='logout'),
    path('aboutus/',views.aboutus),
    path('services/',views.services),
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.settings_view, name='settings'),

    path('my-listings/', views.my_listings_view, name='my_listings'),
    path('rental-requests/', views.rental_requests_view, name='rental_requests'),

    path('search-properties/', views.search_properties_view, name='search_properties'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('my-rentals/', views.my_rentals_view, name='my_rentals'),
]