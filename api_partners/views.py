from rest_framework import viewsets
from api_partners.serializers import FormSerializer
from api_organization.models import Form
from rest_framework import filters


class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('phone_confirmation',) #Фильтр по статусу телефона
    search_fields = ('surname', 'first_name', 'last_name') #Поиск по текстовым полям
    ordering_fields = '__all__' #Сортировка по всем полям



