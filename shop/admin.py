from django.contrib import admin
from django.contrib.auth.models import Group, User
from shop.models import Product, Category, Comment, Order

# Register your models here.


if admin.site.is_registered(User):
    admin.site.unregister(User)
if admin.site.is_registered(Group):
    admin.site.unregister(Group)


# admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Order)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    fields = ('title',)
    pass
    # prepopulated_fields = {'slug': ('title',)}