from django.contrib import admin
from .models import NewspaperPDF, NewspaperPDFPage
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date.widgets import AdminJalaliDateWidget
from django import forms

class NewspaperPDFAdminForm(forms.ModelForm):
    class Meta:
        model = NewspaperPDF
        fields = '__all__'
        widgets = {
            'date': AdminJalaliDateWidget,
        }

class NewspaperPDFPageInline(admin.TabularInline):
    model = NewspaperPDFPage
    extra = 0

@admin.register(NewspaperPDF)
class NewspaperPDFAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    form = NewspaperPDFAdminForm
    list_display = ('title', 'date', 'upload_date')
    list_filter = ('date',)
    search_fields = ('title',)
    inlines = [NewspaperPDFPageInline]

@admin.register(NewspaperPDFPage)
class NewspaperPDFPageAdmin(admin.ModelAdmin):
    list_display = ('pdf', 'page_number', 'image')
    list_filter = ('pdf',)
