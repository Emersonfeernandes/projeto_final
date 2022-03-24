from django import forms
from .models import Url_Scraper
from django.forms import widgets
from django.forms import fields

#NESSE ARQUIVO FORMS.PY FICA A CLASSE QUE RECEBER O FORMULARIO
class URLInput(forms.TextInput):
    input_type = 'URL'

class UserForm(forms.Form):
    
    URL = forms.CharField(max_length=100)
    #URL = forms.URLField(widget=URLInput())


    def url_valido(self):
        pass

    #class Meta:
        #model = Url_Scraper
        #fields = ('URL_save',)