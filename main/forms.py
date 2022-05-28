
from django import forms
from dataclasses import fields
from .models import *

class DATA_FORM(forms.ModelForm):
    class Meta:
        model = details
        fields = "__all__"
        exclude = ('accepted','uniqueid','fileuploaded',)
        required = False
        
    def __init__(self, *args, **kwargs):
        super(DATA_FORM, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['companyname'].widget.attrs['style'] = 'width:400px; height:30px;'
        self.fields['mail'].widget.attrs['style'] = 'width:400px; height:30px;'
        self.fields['phno'].widget.attrs['style'] = 'width:400px; height:30px;'
        self.fields['targetaudience'].widget.attrs['style'] = 'width:400px; height:30px;'
        self.fields['productname'].widget.attrs['style'] = 'width:400px; height:30px;'
        self.fields['businesstype'].widget.attrs['style'] = 'width:400px; height:30px;'
     

    