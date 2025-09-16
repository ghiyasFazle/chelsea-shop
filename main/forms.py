from django.forms import ModelForm
from main.models import product

class productForm(ModelForm):
    class Meta:
        model = product
        fields = ["name","description", "category", "thumbnail", "is_featured","price","stock"]