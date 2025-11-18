from django.urls import path
from authentication.views import login_flutter, register_flutter, logout_flutter

app_name = 'authentication'

urlpatterns = [
    path('login-flutter/', login_flutter, name='login_flutter'),
    path('register-flutter/', register_flutter, name='register_flutter'),
    path('logout-flutter/', logout_flutter, name='logout_flutter'),
]