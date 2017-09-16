from rest_framework import serializers
from api_organization.models import *


class ProposalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proposal
        fields = ('id', 'name', 'type_of_a_proposal', 'start_date_of_rotation','end_date_of_rotation',
                  'min_scoring_ball', 'max_scoring_ball', 'credit_organization', 'date_of_change', 'date_of_creation')


class BidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bid
        fields = ('id', 'form', 'proposal', 'status', 'date_of_dispatch', 'date_of_creation')


class CreditOrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credit_organization
        fields = ('id', 'name', 'phone',  'date_of_change', 'date_of_creation')