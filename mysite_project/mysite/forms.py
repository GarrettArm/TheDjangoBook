from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='An email')
    message = forms.CharField(widget=forms.Textarea)

    # i don't like this approach.  Django is doing magic by automatically
    # running any def 'clean_{}'format(form fieldname) when validating.
    # It's too magic for python.
    def clean_message(self):
        cd = self.cleaned_data['message']
        word_count = len(cd.split())
        if word_count < 4:
            raise forms.ValidationError('Not enough words')
        return cd
