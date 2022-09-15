from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import ContactModel, PodcastModel, PodcasterModel

# path: //(home page)
def indexView(request):
    context = {
        'podcast': PodcastModel.objects.filter(publish=True).order_by('-date'),
        'podcaster': PodcasterModel.objects.filter(publish=True),
        'comment': ContactModel.objects.all()
    }
    return render(request, 'index.html', context)

# path: /login-register/
def login_registerView(request):
    if request.method == 'POST':
        data = request.POST
        if 'reg-username' in data:
            User.objects.create_user(data['reg-username'], data['reg-email'], data['reg-password'])
        if 'log-username' in data:
            username = data['log-username']
            password = data['log-password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:index')
            else:
                return redirect('main:login-register')
    return render(request, 'login-register.html')

# path: /contact/
def contactView(request):
    if request.method == 'POST':
        data = request.POST
        ContactModel.objects.create(firstname = data['firstname'], lastname = data['lastname'], email = data['email'], subject = data['subject'], message = data['message'])
    return render(request, 'contact.html')

# path: /about/
def aboutView(request):
    return render(request, 'about.html')

# path: /<slug>/
def podcasterslugView(request, slug):
    context = {
        'category':get_object_or_404(PodcasterModel, slug = slug)
    }
    return render(request, 'podcaster-slug.html', context)

# path: /logout/
def logoutView(request):
    logout(request)
    return redirect('main:login-register')
    