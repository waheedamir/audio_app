from django.contrib import admin
from core.models import Song, Audiobook, Podcast, Participants

# Register your models here.

admin.site.register(Song)
admin.site.register(Audiobook)
admin.site.register(Participants)


class ParticipantsInline(admin.TabularInline):
    model = Participants


@admin.register(Podcast)
class ParticipantsAdmin(admin.ModelAdmin):
    inlines = [
        ParticipantsInline
    ]
