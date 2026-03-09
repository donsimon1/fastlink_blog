from django.contrib import admin
from assignments.models import About, SocialLink


# Register your models here.

# this code prevents users from adding more than 1 object of the About model
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        else:
            return False


admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)
