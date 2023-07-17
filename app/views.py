from .forms import createUserForm, loginForm, createLeadForm, updateLeadForm
from .models import Lead
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'app/index.html')


def signup(request):
    form = createUserForm()

    if request.method == "POST":
        form = createUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'form':form}
    return render(request, 'app/signup.html', context=context)


def login(request):
    form = loginForm()

    if request.method == "POST":
        form = loginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    context = {'form':form}
    return render(request, 'app/login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect("login")


@login_required(login_url='login')
def dashboard(request):
    allLeads = Lead.objects.all()
    context = {'leads': allLeads}
    return render(request, 'app/dashboard.html', context=context)


@login_required(login_url='login')
def create(request):
    form = createLeadForm()

    if request.method == "POST":
        form = createLeadForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {'form': form}
    return render(request, 'app/create.html', context=context)


@login_required(login_url='login')
def update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = updateLeadForm(instance=lead)

    if request.method == 'POST':
        form = updateLeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    context = {'form':form}
    return render(request, 'app/update.html', context=context)


@login_required(login_url='login')
def read(request, pk):
    allLeads = Lead.objects.get(id=pk)
    context = {'lead':allLeads}
    return render(request, 'app/read.html', context=context)


@login_required(login_url='login')
def delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("dashboard")