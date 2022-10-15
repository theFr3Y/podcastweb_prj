from django.contrib import admin
from .models import ContactModel, PodcasterModel , PodcastModel

class PodcasterAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['publish']
    list_display = ['name', 'publish']
    fieldsets = [
        ('podcaster info', {'fields':['name']}),
        ('address(slug)', {'fields':['slug']}),
        ('podcaster picture', {'fields':['pic']}),
        ('status', {'fields':['publish']}),
        ('position(unique)', {'fields':['position']})
    ]

class PodcastAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['date', 'publish']
    list_display = ['title', 'publish', 'date']
    fieldsets = [
        ('podcast info', {'fields':['title', 'content']}),
        ('address(slug)', {'fields':['slug']}),
        ('podcast file', {'fields':['url']}),
        ('podcast picture', {'fields':['pic']}),
        ('podcast status', {'fields':['publish']}),
        ('category field', {'fields':['category']})
    ]

class ContactAdmin(admin.ModelAdmin):
    search_fields = ['firstname', 'lastname']
    list_filter = ['sendtime']
    list_display = ['firstname', 'lastname', 'subject', 'sendtime']
    fieldsets = [
        ('user info', {'fields':['firstname', 'lastname', 'email']}),
        ('content', {'fields':['subject', 'message']}),
    ]


admin.site.register(PodcasterModel, PodcasterAdmin)
admin.site.register(PodcastModel, PodcastAdmin)
admin.site.register(ContactModel, ContactAdmin)
