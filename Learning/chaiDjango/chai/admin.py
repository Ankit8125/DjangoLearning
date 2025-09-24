from django.contrib import admin
from .models import ChaiVariety, ChaiCertificate, ChaiReview, Store

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
  model = ChaiReview
  extra = 2 # we cannot give review directly, we have to give reference that for which chai we are giving review. 
  
class ChaiVarietyAdmin(admin.ModelAdmin):
  # Whenever we want to customize or enable/disable features in admin, we will use ModelAdmin
  list_display = ('name', 'type', 'date_added') # It is a tuple. Make sure all the fields mentioned here exist in model, else we will get an error.
  inlines = [ChaiReviewInline] # We have already mentioned foreign key in models.py that is why it is able to connect
  
class StoreAdmin(admin.ModelAdmin):
  list_display = ('name', 'location') # these are clickables
  filter_horizontal = ('chai_varieties',) # If we have 1 field, then we must add a ','  

class ChaiCertificateAdmin(admin.ModelAdmin):
  list_display = ('chai', 'certificate_number')
  
# Now we have to inform which model we have imported and which customized class you have injected on that model
admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
