from django.contrib import admin
from django import forms
from django.db.models import Q
import models

class EngineDownloadItemsInline(admin.TabularInline):
    class FormSet(forms.models.BaseInlineFormSet):
        def save_new(self, form, commit=True):
            instance = super(forms.models.BaseInlineFormSet, self).save_new(form, commit=commit)
            instance.folder_type = self.folder_type
            instance.save()
            return instance
        def save_existing(self, form, instance, commit=True):
            instance = form.save(commit=commit)
            instance.folder_type = self.folder_type
            instance.save()
            return form.save(commit=commit)

    fields = ['item_type', 'value', 'count']
    model = models.EngineDownloadItems
    extra = 0

    def queryset(self, request):
        qs = super(admin.TabularInline, self).queryset(request)
        qs = qs.filter(folder_type=self.folder_type)
        return qs

class EngineDownloadItemsResourcesInline(EngineDownloadItemsInline):
    class ResourcesFormSet(EngineDownloadItemsInline.FormSet):
        folder_type = 1
    verbose_name = 'Resources item'
    verbose_name_plural = 'Resources items'
    folder_type = ResourcesFormSet.folder_type
    formset = ResourcesFormSet

class EngineDownloadItemsAssetsInline(EngineDownloadItemsInline):
    class AssetsFormSet(EngineDownloadItemsInline.FormSet):
        folder_type = 2
    verbose_name = 'Assets item'
    verbose_name_plural = 'Assets items'
    folder_type = AssetsFormSet.folder_type
    formset = AssetsFormSet

class EngineAdmin(admin.ModelAdmin):
    inlines = [
        EngineDownloadItemsResourcesInline,
        EngineDownloadItemsAssetsInline,
    ]



admin.site.register(models.Engine, EngineAdmin)
admin.site.register(models.Market)
admin.site.register(models.Language)
admin.site.register(models.TemplateDescription)
admin.site.register(models.Theme)
admin.site.register(models.Description)
admin.site.register(models.Ads)
admin.site.register(models.ThemeAd)
