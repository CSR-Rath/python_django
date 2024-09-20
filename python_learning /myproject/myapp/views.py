from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required(login_url='/login/')
def home(request):
    # Your home page view
    return render(request, 'index.html')


@login_required(login_url='/login/')
def dashboard(request):
    # Your home page view
    return render(request, 'pages/content.html')
