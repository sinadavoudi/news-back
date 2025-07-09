from rest_framework import serializers
from .models import NewspaperPDF, NewspaperPDFPage

class NewspaperPDFPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewspaperPDFPage
        fields = ['page_number', 'image']

class NewspaperPDFSerializer(serializers.ModelSerializer):
    pages = NewspaperPDFPageSerializer(many=True, read_only=True)
    class Meta:
        model = NewspaperPDF
        fields = ['id', 'title', 'date', 'upload_date', 'pdf_file', 'pages'] 