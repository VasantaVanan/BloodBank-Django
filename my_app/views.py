from django.shortcuts import render, redirect
from .forms import RegisterForm, DonerForm
from .models import Doner
from django.views.generic import ListView
# Create your views here.
def home(request):
    return render(request, 'base.html')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = RegisterForm()

    return render(response, 'my_app/register.html', {'form': form})

def doner(request):
    """    def get(self, request, *args, **kwargs):
        form = DonerForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = DonerForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form.save()"""
    form = DonerForm(request.POST or None)
    if form.is_valid():
        form.save()

    content = {'form': form}

    return render(request, 'my_app/doner.html', content)

def donerlist(request):
    posts = Doner.objects.all()
    context = {'posts': posts}

    return render(request, 'my_app/donerlist.html', context)