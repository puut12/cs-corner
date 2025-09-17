from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ItemsForm, ItemsSizeForm
from main.models import Items
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        items_list = Items.objects.all()
    else:
        items_list = Items.objects.filter(user=request.user)

    context = {
        'app' : 'CS Corner',
        'name': request.user.username,
        'class': 'PBP C',
        'items_list': items_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_items(request):
    form_class = ItemsForm

    if request.method == "POST":
        category = request.POST.get('category')
        if category in ['jersey', 'jaket']:
            form_class = ItemsSizeForm
        form = form_class(request.POST)
        if form.is_valid():
            # form.save()
            items_entry = form.save(commit = False)
            items_entry.user = request.user
            items_entry.save()
            return redirect('main:show_main')
    else:
        form = ItemsForm()

    context = {'form': form}
    return render(request, "create_items.html", context)

@login_required(login_url='/login')
def show_items(request, id):
    items = get_object_or_404(Items, pk=id)
    items.increment_views()

    context = {
        'items': items
    }

    return render(request, "items_detail.html", context)

def show_xml(request):
    items_list = Items.objects.all()
    xml_data = serializers.serialize("xml", items_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    items_list = Items.objects.all()
    json_data = serializers.serialize("json", items_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, items_id):
    try:
        items_item = Items.objects.filter(pk=items_id)
        xml_data = serializers.serialize("xml", items_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Items.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, items_id):
    try:
        items_item = Items.objects.get(pk=items_id)
        json_data = serializers.serialize("json", [items_item])
        return HttpResponse(json_data, content_type="application/json")
    except Items.DoesNotExist:
       return HttpResponse(status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response