from rest_framework import viewsets
from api_organization.serializers import *
from api_organization.models import *


class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class CreditOrganizationViewSet(viewsets.ModelViewSet):
    queryset = Credit_organization.objects.all()
    serializer_class = CreditOrganizationSerializer