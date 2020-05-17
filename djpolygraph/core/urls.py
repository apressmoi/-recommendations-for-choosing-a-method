from django.urls import path
from .views import home,login_view, logout_view, register, calculate_view, send_message_to_email
from .api import RenderChoicesPaper


app_name = 'core'
urlpatterns = [
    path('', home, name='home-page'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', register, name='registration'),
    path('calculate/', calculate_view, name='calculate'),
    path('api/<str:name_product>/', RenderChoicesPaper.as_view(), name='get-papers'),
    path('send-message/', send_message_to_email, name='send-message')
]

