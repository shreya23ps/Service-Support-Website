from django.contrib import admin,messages
from .models import BlogPost, Comment, Contact,Person, ElectoralRoll,PanCardApplication, DeathCertificateApplication, AddressChangeApplication,DrivingLicenseApplication, RationCardApplication, VoterRegistration

admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Contact)

def generate_electoral_rolls_action(modeladmin, request, queryset):
    eligible_people = Person.objects.filter(is_alive=True).exclude(electoralroll__isnull=False)
    for person in eligible_people:
        ElectoralRoll.objects.create(person=person)
    messages.success(request, "Electoral rolls updated with all eligible voters.")

# Define a custom admin class for Person
class PersonAdmin(admin.ModelAdmin):
    list_display = ('aadhaar_number', 'name', 'surname', 'is_alive')
    actions = [generate_electoral_rolls_action]  # Add the custom action to actions list

# Define a custom admin class for ElectoralRoll
class ElectoralRollAdmin(admin.ModelAdmin):
    list_display = ('person',)

# Register the models with their respective admin classes
admin.site.register(Person, PersonAdmin)
admin.site.register(ElectoralRoll, ElectoralRollAdmin)


class PanCardApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'applicant_aadhaar', 'created_at')
    search_fields = ('applicant_name', 'applicant_aadhaar')
    list_filter = ('created_at',)

admin.site.register(PanCardApplication, PanCardApplicationAdmin)
admin.site.register(DeathCertificateApplication)
admin.site.register(AddressChangeApplication)
admin.site.register(DrivingLicenseApplication)
admin.site.register(RationCardApplication)
admin.site.register(VoterRegistration)

