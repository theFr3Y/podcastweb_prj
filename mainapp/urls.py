from django.urls import path
from .views import indexView, login_registerView, contactView, aboutView, logoutView, podcasterslugView

# i dont think it needs an explanation
app_name = 'main'
urlpatterns = [
    path('', indexView, name='index'),
    path('about/', aboutView, name='about'),
    path('login-register/', login_registerView, name='login-register'),
    path('contact/', contactView, name='contact'),
    path('<slug:slug>', podcasterslugView, name='slug'),
    path('logout/', logoutView, name='logout')
]