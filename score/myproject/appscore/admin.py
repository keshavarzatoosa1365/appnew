from django.contrib import admin
from django.contrib.admin.options import TabularInline
from appscore import models
admin.site.register(models.Mdl_Quize)
admin.site.register(models.Mdl_Result)
class A_admin(admin.TabularInline):
    model=models.Mdl_Answers
    extra=1    

@admin.register(models.Mdl_Question)
class Q_admin(admin.ModelAdmin):
    inlines=[A_admin]   


