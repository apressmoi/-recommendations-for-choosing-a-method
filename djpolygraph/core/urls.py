from django.urls import path
from .views import home,login_view, logout_view, register


app_name = 'core'
urlpatterns = [
    path('', home, name='home-page'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='registration'),
]