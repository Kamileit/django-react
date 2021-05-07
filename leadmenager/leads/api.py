from .models import Lead
from rest_framework import viewsets, permissions
from .serializer import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    permissions_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
