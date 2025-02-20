from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.utils.safestring import mark_safe

from django.forms import TextInput, Textarea
# import locale


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "cargo", "image_tag",)
    
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'90'})},
        models.TextField: {'widget': Textarea(attrs={'rows':6, 'cols':92})},
    }

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:50px; max-height:50px"/>'.format(obj.foto.url))
    image_tag.short_description = 'Foto'