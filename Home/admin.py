from django.contrib import admin
from Home.models import To_do_List_model, Contacts
# Register your models here.

#  Registering our model to show in admin area.
admin.site.register(To_do_List_model)
admin.site.register(Contacts)