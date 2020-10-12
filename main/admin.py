from django.contrib import admin
from django.contrib.auth.models import Group
from guardian.admin import GuardedModelAdmin

from main.models import Team, User


class UserAdmin(GuardedModelAdmin):
    pass


class TeamAdmin(GuardedModelAdmin):
    pass


admin.site.unregister(Group)

admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)
