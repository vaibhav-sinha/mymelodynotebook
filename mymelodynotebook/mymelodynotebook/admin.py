from django.contrib import admin
from mymelodynotebook.models import Song,Ref

class SongAdmin(admin.ModelAdmin):
    pass

admin.site.register(Song, SongAdmin)

class RefAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ref, RefAdmin)
