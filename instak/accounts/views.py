from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


def index(request):
    users = get_list_or_404(User)
    context = {
        'users': users
    }
    return render(request, 'accounts/index.html', context)
