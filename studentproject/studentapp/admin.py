from django.contrib import admin
from studentapp.models import stud_det,stud_fee

# Register your models here.
class stud_ref(admin.ModelAdmin):
    pass

admin.site.register(stud_det,stud_ref)
admin.site.register(stud_fee,stud_ref)

