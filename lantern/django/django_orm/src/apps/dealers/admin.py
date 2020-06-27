from django.contrib import admin

# Register your models here.
from apps.dealers.models import Country, City, Dealer


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    pass

    #  def _image(self, obj):
    #     if obj.logo:
    #         return mark_safe(f'<img src="{obj.logo.url}" style="height: 50px">')
    #     return '----'