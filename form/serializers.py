from rest_framework import serializers
from .models import Bookacall, contactform

class bookacallserializer(serializers.ModelSerializer):
    class Meta:
        model = Bookacall
        fields = ['first_name', "last_name", "business_type", "business_name","email", "business_detail"]


class contactformserializer(serializers.ModelSerializer):
    class Meta:
        model = contactform
        fields = ['first_name', "last_name","email", "contact_matter"]