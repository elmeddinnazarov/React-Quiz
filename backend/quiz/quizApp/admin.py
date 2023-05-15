
from django.contrib import admin
from .models import Question, Option, Quiz, Report


class OptionInline(admin.TabularInline):
    model = Option

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    
    
admin.site.register(Question, QuestionAdmin)

admin.site.register(Quiz)
admin.site.register(Report)