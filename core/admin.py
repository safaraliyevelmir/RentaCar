from django.contrib import admin

from .models import About, Adress, Condtion, Contact, ContactEmail, ContactInformationPhoneNumber, Quote

admin.site.register(About)
admin.site.register(Condtion)
admin.site.register(ContactInformationPhoneNumber)
admin.site.register(ContactEmail)
admin.site.register(Adress)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['fullname','date']

admin.site.register(Contact,ContactAdmin)
admin.site.register(Quote)
