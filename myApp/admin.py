from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Coordinates


class CorrdinateAdmin(admin.ModelAdmin) :
    model = Coordinates
    list_filter = ('person', )
    list_display = ('get_author', 'lattitude', 'longitude', 'heartRate','id', 'created_at')
    ordering = ('-created_at',)

    def get_author(self, obj):
        return obj.person.get_fullName()
    get_author.short_description = 'Belongs to'
    # get_author.admin_order_field = 'person__firstname'


admin.site.register(Coordinates, CorrdinateAdmin)