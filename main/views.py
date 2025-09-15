from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ItemsForm, ItemsSizeForm
from main.models import Items
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    items_list = Items.objects.all()

    context = {
        'app' : 'CS Corner',
        'name': 'Putri Hamidah Riyanto',
        'class': 'PBP C',
        'items_list': items_list
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
            form.save()
            return redirect('main:show_main')
    else:
        form = ItemsForm()

    context = {'form': form}
    return render(request, "create_items.html", context)

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