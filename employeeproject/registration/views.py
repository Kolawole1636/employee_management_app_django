from django.shortcuts import render, redirect

from .form import UserRegister
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method=='POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! {username}, You can now login!')
            return redirect('login')

    else:
        form = UserRegister()
    return render(request, 'register.html', {'form': form})
