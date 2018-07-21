from django.contrib import admin

from django.contrib import admin

# Register your models here.
from blood.donor.models import DonorInformation

class DonorInformationAdmin(admin.ModelAdmin):
	""""""
	list_display = ('first_name','last_name','Email','Phone','Age','city', 'group', 'reason')
	list_filter = ('first_name','group')
	search_fields = ('first_name','group')

admin.site.register(DonorInformation, DonorInformationAdmin)

