from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import logout
from .models import NewspaperPDF
from .serializers import NewspaperPDFSerializer

# Create your views here.

class NewspaperPDFListView(generics.ListAPIView):
    queryset = NewspaperPDF.objects.all().order_by('-upload_date')
    serializer_class = NewspaperPDFSerializer

class NewspaperPDFUploadView(generics.CreateAPIView):
    queryset = NewspaperPDF.objects.all()
    serializer_class = NewspaperPDFSerializer
    permission_classes = [permissions.IsAdminUser]

class NewspaperPDFDetailView(generics.RetrieveDestroyAPIView):
    queryset = NewspaperPDF.objects.all()
    serializer_class = NewspaperPDFSerializer
    permission_classes = [permissions.IsAdminUser]

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def admin_logout(request):
    """Logout the admin user"""
    logout(request)
    return Response({'message': 'Admin logged out successfully'}, status=status.HTTP_200_OK)
