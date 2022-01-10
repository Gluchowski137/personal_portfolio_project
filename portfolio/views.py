from django.shortcuts import render
from .models import PortfolioProject
# Create your views here.
def home(request):
    projects = PortfolioProject.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects})
