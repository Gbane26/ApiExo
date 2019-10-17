from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


def _register(model, admin_class):
    admin.site.register(model, admin_class)


# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MoisAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'cover',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'description',
        'cover',
        'statut',
        'date_add',
        'date_upd',
    )


class ModuleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'mois',
        'language',
        'image',
        'description',
        'prix',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'mois',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'mois',
        'language',
        'image',
        'description',
        'prix',
        'statut',
        'date_add',
        'date_upd',
    )


class ChapitreAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'module',
        'titre',
        'description',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'module',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'module',
        'titre',
        'description',
        'statut',
        'date_add',
        'date_upd',
    )


class CoursAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'chapitre',
        'titre',
        'video',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'chapitre',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'chapitre',
        'titre',
        'video',
        'statut',
        'date_add',
        'date_upd',
    )


class UsercourseAdmin(admin.ModelAdmin):

    list_display = ('id', 'module', 'user', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'module',
        'user',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'module',
        'user',
        'statut',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Mois, MoisAdmin)
_register(models.Module, ModuleAdmin)
_register(models.Chapitre, ChapitreAdmin)
_register(models.Cours, CoursAdmin)
_register(models.Usercourse, UsercourseAdmin)
