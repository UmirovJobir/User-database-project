from django.contrib import admin
from .models import User, Document, Additional_document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("user", 'passport', 'CV', 'military_ID', 'reference', 'diplom', 'driving_license')

