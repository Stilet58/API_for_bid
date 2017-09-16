from rest_framework import viewsets
from api_organization.serializers import *
from api_organization.models import *
from rest_framework import filters


class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('credit_organization', 'type_of_a_proposal') #Фильтры по кредитной организации и типу предложения
    search_fields = ('name', 'type_of_a_proposal', 'credit_organization__name') #Поиск по текстовым полям
    ordering_fields = '__all__' #Сортировка по всем полям


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('proposal', 'status',) #Фильтры по названию предложения и статусу заявки
    search_fields = ('form__surname', 'form__first_name', 'form__last_name', 'proposal__name') #Поиск по текстовым полям
    ordering_fields = '__all__' #Сортировка по всем полям


class CreditOrganizationViewSet(viewsets.ModelViewSet):
    queryset = Credit_organization.objects.all()
    serializer_class = CreditOrganizationSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',) #Поиск по текстовым полям
    ordering_fields = '__all__' #Сортировка по всем полям