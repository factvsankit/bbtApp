from django.contrib import admin

from metadataapp.models import Event, Plant, Fruit, CropPricing


class EventInline(admin.StackedInline):
    model = Event


class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'season')
    exclude = ('last_changed_by', )
    inlines = [EventInline]

    def save_model(self, request, obj, form, change):
        obj.last_changed_by = request.user.username
        obj.save()


class FruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_changed_by')

    def save_model(self, request, obj, form, change):
        obj.last_changed_by = request.user.username
        obj.save()


admin.site.register(Plant, PlantAdmin)
admin.site.register(Fruit, FruitAdmin)
admin.site.register(CropPricing)
