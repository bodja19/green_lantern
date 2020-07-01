from django.forms import ModelForm
from apps.newsletters.models import Newsletter

class NewsLetterModelForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email"]
