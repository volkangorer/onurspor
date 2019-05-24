from django.contrib import admin

from .models import Database,Galeri,Duyuru,Haber,PuanDurumu

# Register your models here.

admin.site.register(Galeri) 
admin.site.register(Haber) 
admin.site.register(Duyuru)
admin.site.register(PuanDurumu)


@admin.register(Database)
class DatabaseAdmin(admin.ModelAdmin):

    list_display = ["position","name"]
    list_display_links = ["name"]
    search_fields = ["name"]
    list_filter = ["position"]

    
    class Meta :
        model = Database

