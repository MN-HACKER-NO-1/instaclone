from django import forms
from .models import post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText,PrependedAppendedText,FormActions,
)
class PostForm(forms.ModelForm):
    helper=FormHelper()
    helper.form_method='POST'
    helper.add_input(Submit('Post', 'Post', css_class='btn_primary'))

    class Meta:
        model=post
        fields=[
            'image',
            'caption'
        ]
