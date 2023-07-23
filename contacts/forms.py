from .models import Contact, PcTechnician
from django import forms


class ContactForm(forms.ModelForm):
    """
    PostForm allows the user to post something of their creation
    """
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message',
        )


class PcTechnicianForm(forms.ModelForm):
    """
    PostForm allows the user to post something of their creation
    """
    class Meta:
        model = PcTechnician
        fields = (
            'name',
            'email',
            'computer_type',
            'message',
        )
