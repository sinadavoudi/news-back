from django.urls import path
from .views import NewspaperPDFListView, NewspaperPDFUploadView, NewspaperPDFDetailView, admin_logout

urlpatterns = [
    path('pdfs/', NewspaperPDFListView.as_view(), name='pdf-list'),
    path('pdfs/upload/', NewspaperPDFUploadView.as_view(), name='pdf-upload'),
    path('pdfs/<int:pk>/', NewspaperPDFDetailView.as_view(), name='pdf-detail'),
    path('admin/logout/', admin_logout, name='admin-logout'),
] 