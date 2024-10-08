from django.contrib import admin
from .models import Organization, OrganizationMember, Credits


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'created_at', 'updated_at')
    search_fields = ('name', 'creator__username')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    class OrganizationMemberInline(admin.TabularInline):
        model = OrganizationMember
        extra = 1

    inlines = [OrganizationMemberInline]


@admin.register(OrganizationMember)
class OrganizationMemberAdmin(admin.ModelAdmin):
    list_display = ('organization', 'member', 'added_at')
    search_fields = ('organization__name', 'member__username')
    list_filter = ('added_at',)
    ordering = ('-added_at',)
    readonly_fields = ('added_at',)


@admin.register(Credits)
class CreditsAdmin(admin.ModelAdmin):
    list_display = ('organization', 'credits', 'start', 'end', 'created_at')
    search_fields = ('organization__name',)
    list_filter = ('start', 'end', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('organization', 'credits')
        }),
        ('Validity Period', {
            'fields': ('start', 'end')
        }),
        ('Creation Information', {
            'fields': ('created_at',)
        }),
    )
