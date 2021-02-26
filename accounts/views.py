from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterationForm
from django.contrib.auth.models import User
from django.contrib import messages


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
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'You registerd successfully.', 'info')
            return redirect('core:home')
        return render(request, self.template_name, {'form':form})

