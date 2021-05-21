from django.contrib import admin
from .models import Test


class MyModelAdmin(admin.ModelAdmin):
    # Displays timestamps in admin view
    readonly_fields = ('timestamp',)


admin.site.register(
    Test,
    MyModelAdmin
)
