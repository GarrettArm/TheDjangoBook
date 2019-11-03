from django.forms import ModelForm
from django.forms import ValidationError
from .models import Comment


class ContactForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["subject", "email", "message"]

    def send_email(self):
        pass

    def clean_message(self):
        cd = self.cleaned_data["message"]
        word_count = len(cd.split())
        if word_count < 4:
            raise ValidationError("Not enough words")
        return cd
