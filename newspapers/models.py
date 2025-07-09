from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from pdf2image import convert_from_path
from django.core.files.base import ContentFile
from io import BytesIO
import os

# Create your models here.

class NewspaperPDF(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    upload_date = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

class NewspaperPDFPage(models.Model):
    pdf = models.ForeignKey(NewspaperPDF, related_name='pages', on_delete=models.CASCADE)
    page_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='pdf_pages/')


@receiver(post_save, sender=NewspaperPDF)
def create_pdf_images(sender, instance, created, **kwargs):
    if created and instance.pdf_file:
        pdf_path = instance.pdf_file.path
        images = convert_from_path(pdf_path, dpi=200)
        for i, image in enumerate(images):
            buffer = BytesIO()
            image.save(buffer, format='PNG')
            page = NewspaperPDFPage(
                pdf=instance,
                page_number=i+1
            )
            page.image.save(f'{instance.id}_page_{i+1}.png', ContentFile(buffer.getvalue()), save=True)
