from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from .forms import UserRegisterationForm, UserLoginForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


class UserRegister(View):
    form_class = UserRegisterationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            Profile.objects.create(user=user)
            messages.success(request, 'You registerd successfully', 'info')
            return redirect('core:home')
        return render(request, self.template_name, {'form':form})


# User registeration whit function base views
""" def user_register(request):
    if request.method == 'GET':
        form = UserRegisterationForm
        return render(request, 'accounts/register.html', {'form':form})
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'You registerd successfully', 'info')
            return redirect('core:home')
        return render(request, 'accounts/register.html', {'form':form})
            
 """

class UserLogin(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in successfully', 'success')
                return redirect('core:home')
            messages.error(request, 'Your username or password is rong!', 'danger')
        return render(request, self.template_name, {'form':form})


class UserLogout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You logged out successfully', 'success')
        return redirect('core:home')


class UserDashboard(LoginRequiredMixin, View):
    template_name = 'accounts/dashboard.html'
    form_class = UserProfileForm

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        form = self.form_class
        return render(request, self.template_name, {'user':user, 'form':form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your image uploaded successfully', 'info')
            return redirect('accounts:dashboard', request.user.username)



 