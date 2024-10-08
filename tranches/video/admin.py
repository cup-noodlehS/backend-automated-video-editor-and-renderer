from django.contrib import admin
from .models import (
    File,
    Font,
    AeVersion,
    VideoTemplate,
    StaticLayer,
    DynamicLayer,
    VideoVariant,
    VideoVariantLayer,
)

# Inline classes for related models
class StaticLayerInline(admin.TabularInline):
    model = StaticLayer
    extra = 0

class DynamicLayerInline(admin.TabularInline):
    model = DynamicLayer
    extra = 0

class VideoVariantLayerInline(admin.TabularInline):
    model = VideoVariantLayer
    extra = 0

# Admin classes for each model
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_at')
    search_fields = ('name', 'url')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Font)
class FontAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'created_at')
    search_fields = ('name', 'file__name')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(AeVersion)
class AeVersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(VideoTemplate)
class VideoTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'status_display', 'creator', 'organization', 'created_at', 'updated_at')
    search_fields = ('name', 'composition_name', 'creator__username', 'organization__name')
    list_filter = ('status', 'created_at', 'updated_at', 'ae_version')
    filter_horizontal = ('fonts',)
    inlines = [StaticLayerInline, DynamicLayerInline]
    ordering = ('-created_at',)

@admin.register(StaticLayer)
class StaticLayerAdmin(admin.ModelAdmin):
    list_display = ('layer_name', 'video_template', 'layer_type_display', 'file')
    search_fields = ('layer_name', 'video_template__name', 'file__name')
    list_filter = ('layer_type', 'video_template')
    ordering = ('video_template', 'layer_name')

@admin.register(DynamicLayer)
class DynamicLayerAdmin(admin.ModelAdmin):
    list_display = ('layer_name', 'display_name', 'video_template', 'layer_type_display', 'value', 'file')
    search_fields = ('layer_name', 'display_name', 'video_template__name', 'value', 'file__name')
    list_filter = ('layer_type', 'video_template')
    ordering = ('video_template', 'layer_name')

@admin.register(VideoVariant)
class VideoVariantAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_template', 'status_display', 'creator', 'created_at', 'updated_at')
    search_fields = ('name', 'video_template__name', 'creator__username', 'job_id')
    list_filter = ('state', 'created_at', 'updated_at', 'video_template')
    inlines = [VideoVariantLayerInline]
    ordering = ('-created_at',)

@admin.register(VideoVariantLayer)
class VideoVariantLayerAdmin(admin.ModelAdmin):
    list_display = ('layer_name', 'video_variant', 'layer_type_display', 'file', 'value')
    search_fields = ('layer_name', 'video_variant__name', 'file__name', 'value')
    list_filter = ('layer_type', 'video_variant')
    ordering = ('video_variant', 'layer_name')
