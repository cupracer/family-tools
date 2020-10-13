from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from guardian.admin import GuardedModelAdminMixin

from main.models import User


class GuardedUserAdmin(GuardedModelAdminMixin, UserAdmin):
    pass


class GuardedGroupAdmin(GuardedModelAdminMixin, GroupAdmin):
    pass


admin.site.unregister(Group)

admin.site.register(User, GuardedUserAdmin)
admin.site.register(Group, GuardedGroupAdmin)
