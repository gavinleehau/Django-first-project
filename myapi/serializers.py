from django.db import models
from django.db.models import fields
from rest_framework import serializers
from myapp.models import Reporter

class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields= '__all__'