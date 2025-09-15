from django.forms import ModelForm
from main.models import Items

class ItemsForm(ModelForm):
    class Meta:
        model = Items
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured"]

class ItemsSizeForm(ModelForm):
    class Meta:
        model = Items
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "size"]