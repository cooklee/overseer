from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import LoginForm

from django.contrib.auth.models import User

# Create your views here.
class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'form_generic.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            form = LoginForm()
        return render(request, 'form_generic.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('index')




