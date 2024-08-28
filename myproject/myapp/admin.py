from django.contrib import admin

class MyModelAdmin(admin.ModelAdmin):
    class Media:  
        css = {
             'all': ('myapp/css/custom_admin.css',)
        }