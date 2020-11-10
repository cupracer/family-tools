from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from supplies.models import Category, Brand, Supply, SupplyItem


class CategoryAdmin(GuardedModelAdmin):
    pass


class BrandAdmin(GuardedModelAdmin):
    pass


class SupplyAdmin(GuardedModelAdmin):
    pass


class SupplyItemAdmin(GuardedModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(SupplyItem, SupplyItemAdmin)
