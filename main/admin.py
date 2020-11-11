from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from guardian.admin import GuardedModelAdminMixin

from main.models import User


class GuardedUserAdmin(GuardedModelAdminMixin, UserAdmin):
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email', 'todoist_api_key')


class GuardedGroupAdmin(GuardedModelAdminMixin, GroupAdmin):
    pass


admin.site.unregister(Group)

admin.site.register(User, GuardedUserAdmin)
admin.site.register(Group, GuardedGroupAdmin)
