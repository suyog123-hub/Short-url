from django.shortcuts import render, redirect
import pyshorteners
import string
import random
from .models import ShortURL
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,DeleteView,CreateView
@login_required(login_url='signin')
def home(request):
    """Home page - create short URLs and show user's URLs"""
    short_url = ''
    url = ''
    db_short_url = []
    if request.user.is_authenticated:
        db_short_url = ShortURL.objects.filter(user=request.user).order_by('-created_at')
    if request.method == "POST":
        url = request.POST.get('url')
        if not url:
            messages.error(request, "Please enter a URL")
            return render(request, 'index.html', {
                'short_url': short_url,
                'url': url,
                'db_short_url': db_short_url,
            })
        try:
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(url)
            characters = string.ascii_letters + string.digits
            short_key = ''.join(random.choice(characters) for _ in range(6))
            while ShortURL.objects.filter(short_key=short_key).exists():
                short_key = ''.join(random.choice(characters) for _ in range(6))
            if request.user.is_authenticated:
                ShortURL.objects.create(user=request.user,original_url=url,short_key=short_key,short_url=short_url,clicks=0
                )
                messages.success(request, "Short URL created and saved to your account!")
                db_short_url = ShortURL.objects.filter(user=request.user).order_by('-created_at')
            else:
                messages.success(request, f"Your short URL is: {short_url} (Login to save it)")
            
        except Exception as e:
            messages.error(request, f"Error creating short URL: {str(e)}")
    
    context = {
        'short_url': short_url,
        'url': url,
        'db_short_url': db_short_url,
    }
    
    return render(request, 'index.html', context)


