from django.contrib import admin
from .models import Status

class AdminStatus(admin.ModelAdmin):
    list_display = ['Month', 'Lead_Type', 'Leads_Priority', 'Lead_Source', 'Market_Place_Subsource', 'Country', 'Business_Potential', 'Company_Size', 'Platform']



admin.site.register(Status, AdminStatus)