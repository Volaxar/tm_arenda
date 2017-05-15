from django import forms


class ContactForm(forms.Form):
    error_css_class = 'error-field'

    sender = forms.CharField(
        label='Имя',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'size': 20})
    )

    phone = forms.CharField(
        label='Телефон',
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'size': 20})
    )

    mail = forms.EmailField(
        label='E-mail',
        required=False,
        widget=forms.TextInput(attrs={'size': 20})
    )
    
    message = forms.CharField(
        label='Текст сообщения',
        widget=forms.Textarea(attrs={'rows': 8})
    )
