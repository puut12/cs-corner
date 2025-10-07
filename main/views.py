from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ItemsForm, ItemsSizeForm
from main.models import Items
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from datetime import datetime
from django.db import IntegrityError
from django.core.exceptions import ValidationError

# Create your views here.
@login_required(login_url='/login')
def show_main(request, category_name=None):
    form = ItemsForm()
    context = {
        'app' : 'CS Corner',
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'form': form, 
        'category_name': category_name 
    }
    return render(request, "main.html", context)

def create_items(request):
    if request.method == "POST":
        category = request.POST.get('category')
        if category in ['jersey', 'jaket']:
            form = ItemsSizeForm(request.POST, request.FILES)
        else:
            form = ItemsForm(request.POST, request.FILES)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Product added successfully!')
            return redirect('main:show_main') 
        else:
            pass
    else:
        form = ItemsForm()

    if 'form' not in locals():
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

def get_thumbnail_url(thumbnail_field):
    """Fungsi helper untuk mendapatkan URL thumbnail"""
    if not thumbnail_field:
        return None
    if hasattr(thumbnail_field, 'url'):
        return thumbnail_field.url
    return str(thumbnail_field)

def show_json(request):
    category_name = request.GET.get('category', None)
    items_list = Items.objects.all()

    if category_name and category_name != 'all':
        if category_name == 'apparel':
            items_list = items_list.filter(category__in=['jersey', 'jaket'])
        elif category_name == 'merchandise':
            items_list = items_list.filter(category__in=['poster', 'figur'])
        else:
            items_list = items_list.filter(category=category_name)

    data = [
        {
            'id': str(item.id),
            'name': item.name,
            'price': item.price,
            'description': item.description,
            'thumbnail': get_thumbnail_url(item.thumbnail),
            'category': item.category,
            'is_featured': item.is_featured,
            'size': item.size,
            'items_views': item.items_views,
            'user': item.user.id if item.user else None,
        }
        for item in items_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, items_id):
    try:
        items_item = Items.objects.filter(pk=items_id)
        xml_data = serializers.serialize("xml", items_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Items.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, items_id):
    try:
        item = Items.objects.select_related('user').get(pk=items_id)
        data = {
            'id': str(item.id),
            'name': item.name,
            'price': item.price,
            'description': item.description,
            'thumbnail': get_thumbnail_url(item.thumbnail),
            'category': item.category,
            'is_featured': item.is_featured,
            'size': item.size,
            'items_views': item.items_views,
            'user_username': item.user.username,
        }
        return JsonResponse(data)
    except Items.DoesNotExist:
       return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)     
        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
        
        if form.is_valid():
            form.save()          
            if is_ajax:
                return JsonResponse({"status": "success", "message": "Account created successfully. Please login."}, status=201)
            else:
                return redirect('main:login')
        else:
            if is_ajax:
                return JsonResponse({"status": "error", "message": form.errors}, status=400)     
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                response = JsonResponse({
                    "status": "success",
                    "message": "Login success!"
                })
                response.set_cookie('last_login', str(datetime.now()))
                return response
            else:
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.now()))
                return response
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
             return JsonResponse({
                "status": "error",
                "message": form.errors
            }, status=400)
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_items(request, id):
    items = get_object_or_404(Items, pk=id)

    if items.category in ['jersey', 'jaket']:
        form_class = ItemsSizeForm
    else:
        form_class = ItemsForm
    
    form = form_class(request.POST or None, instance=items)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_items.html", context)

def delete_items(request, id):
    items = get_object_or_404(Items, pk=id)
    items.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
@login_required
def create_items_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        thumbnail = request.POST.get("thumbnail")
        category = request.POST.get("category")
        is_featured = request.POST.get("is_featured") == 'on'
        size = request.POST.get("size")

        if not name or not price:
            return JsonResponse({"status": "error", "message": "Name and price are required."}, status=400)        
        
        new_item = Items(
            name=name, 
            price=price,
            description=description,
            thumbnail=thumbnail,
            is_featured=is_featured,
            size=size,
            user=request.user
        )
        new_item.save()

        return JsonResponse({
            "status": "success",
            "message": "Produk berhasil ditambahkan melalui AJAX."
        }, status=201)
JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

@csrf_exempt
@require_POST
def edit_items_ajax(request, items_id):
    try:
        item = Items.objects.get(pk=items_id)
    except Items.DoesNotExist:
        return HttpResponseNotFound(JsonResponse({"status": "error", "message": "Item tidak ditemukan."}))
    
    item.name = request.POST.get("name")
    item.price = request.POST.get("price")
    item.description = request.POST.get("description")
    item.category = request.POST.get("category")
    item.is_featured = request.POST.get("is_featured") == 'on'
    if item.category in ['jersey', 'jaket']:
        item.size = request.POST.get("size")
    else:
        item.size = None
    try:
        item.full_clean()
        item.save()
    except (ValidationError, IntegrityError, ValueError) as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "success", "message": "Product updated successfully"})

@csrf_exempt
@require_POST 
@login_required
def delete_items_ajax(request, id):
    try:
        item = Items.objects.get(pk=id, user=request.user)
        item.delete()
        return JsonResponse({"status": "success", "message": "Produk berhasil dihapus."}, status=200)
    except Items.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Produk tidak ditemukan atau Anda tidak punya hak akses."}, status=404)