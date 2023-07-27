from django import forms
from .widgets import CustomClearableFileInput
from .models import Computers, Reviews


class ComputerForm(forms.ModelForm):

    class Meta:
        model = Computers
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """
    ReviewForm allows the user to comment on a blog post
    """
    class Meta:
        model = Reviews
        fields = ('body',)
