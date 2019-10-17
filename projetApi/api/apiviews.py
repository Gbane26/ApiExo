from rest_framework import viewsets
from rest_framework import filters

from .models import Mois, Module, Chapitre, Cours, Usercourse
from .serializers import *


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class MoisViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Mois.objects.all()
    serializer_class = MoisSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ChapitreViewSet(viewsets.ModelViewSet):
    queryset = Chapitre.objects.all()
    serializer_class = ChapitreSerializer

class CoursViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer


class UsercourseViewSet(viewsets.ModelViewSet):
    queryset = Usercourse.objects.all()
    serializer_class = UsercourseSerializer

