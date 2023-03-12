from django.contrib import admin
from todoapi.models import Todo, Contact

# class TodoAdmin(admin.ModelAdmin):
#     fields = ("author", "created_at", "description", "name", "category", "priority", "development_state", "expire_date", "contacts")
#     list_display = ("author", "created_at", "description", "name", "category", "priority", "development_state", "expire_date", "contacts")
#     search_fields = ("hallo",)


# class ContactAdmin(admin.ModelAdmin):
#     fields = ("author", "prename", "lastname", "email", "phonenumber", "color")
#     list_display = ("author", "prename", "lastname", "email", "phonenumber", "color")
#     search_fields = ("hallo",)



admin.site.register(Todo)
admin.site.register(Contact)