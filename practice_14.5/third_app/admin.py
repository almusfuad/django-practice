from django.contrib import admin
from third_app.models import ExampleModel, ExampleModel2

# Register your models here.
class AssignmentAdmin(admin.ModelAdmin):
      fields = ('user', 'title','description', 'slug', 'timestamp')
      fieldsets = [
            ('Main Information', {
                  'fields': ('title', 'description')
            }),
            ('Additional Information', {
                  'fields': ('slug','user', 'timestamp')
            }),
      ]

class MyModelAdmin(admin.ModelAdmin):
      fieldsets = [
            ('Main Information', {
                  'fields': ('user', 'title', 'description', 'slug', 'timestamp'),
                  'classes': ('wide'),
                  'description': "Enter the main details of the model.",
                  'collapse': True,
            })
      ]

admin.site.register(ExampleModel ,MyModelAdmin)