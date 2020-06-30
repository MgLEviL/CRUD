from django.contrib import admin
from .models import Note, UserNote

# Register your models here.
class UserNoteAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email",)

    fieldsets = (
            ("User note model", {
                'fields': ('name', 'email')
            }),
        )


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'end_date', 'note', 'attach', 'task', 'tag' ,'type', 'user',)

    fieldsets = (
            ("Note model", {
                'fields': ('end_date', 'note', 'attach', 'task', ('tag', 'type',), 'user',)
            }),
        )
    """
    def time_seconds(self, obj):
        return obj.date.strftime("%d %b %Y %H:%M")
        """

admin.site.register(UserNote, UserNoteAdmin)
admin.site.register(Note, NoteAdmin)
