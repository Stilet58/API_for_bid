from rest_framework import viewsets
from api_partners.serializers import FormSerializer
from api_organization.models import Form


class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
