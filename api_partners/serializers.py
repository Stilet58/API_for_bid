from rest_framework import serializers
from api_partners.models import Form


class FormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Form
        fields = ('id', 'surname', 'first_name', 'last_name', 'dob', 'phone_number',
                  'phone_confirmation', 'passport', 'scoring_ball', 'date_of_change', 'date_of_creation')
