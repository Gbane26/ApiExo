from rest_framework import serializers

from .models import *

from drf_dynamic_fields import DynamicFieldsMixin




class UsercourseSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Usercourse
        fields = '__all__'

class CoursSerializer(serializers.ModelSerializer):
    module_usercourse = UsercourseSerializer(many=True, required=False)

    class Meta:
        model = Cours
        fields = '__all__'

class ChapitreSerializer(serializers.ModelSerializer):
    chapitre_cours = CoursSerializer(many=True, read_only=True, required=False)
    
    class Meta:
        model = Chapitre
        fields = '__all__'


class ModuleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    module_chapitre = ChapitreSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Module
        fields = '__all__'


class MoisSerializer(serializers.ModelSerializer):
    mois_module = ModuleSerializer(many=True, required=False)

    class Meta:
        model = Mois
        fields = '__all__'