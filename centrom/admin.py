from django.contrib import admin
from centrom.models import *


class SpecialtyAdmin(admin.ModelAdmin):
    class Media:#http://djangosnippets.org/snippets/2057/
        js = (#C:\Users\Pedroc\workspacePython\centromedicotondela\centromedico\site_media\javasc\jquery-ui-1.8.15.custom\js
            '/site_media/javasc/jquery-ui-1.8.15.custom/js/jquery-1.5.1.min.js',
            '/site_media/javasc/jquery-ui-1.8.15.custom/js/jquery-ui-1.8.15.custom.js',
            '/site_media/javasc/admin-list-reorder.js',
        )
    list_display = ('position', 'title',)
    list_display_links = ('title',)
    list_editable = ['position']  # 'position' is the name of the model field which holds the posit

    #list_display_links = ('position',)
    


class SubSpecialtyAdmin(admin.ModelAdmin):
    pass


class HealthWorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumb')


class ExamPreparationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(SubSpecialty, SubSpecialtyAdmin)
admin.site.register(HealthWorker, HealthWorkerAdmin)
admin.site.register(ExamPreparation, ExamPreparationAdmin)