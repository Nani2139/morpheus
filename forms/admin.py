from django.contrib import admin
from .models import Form, Question, Option, Response, Answer

class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class FormAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'created_at', 'updated_at')

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ('text', 'question_type', 'form', 'order')
    list_filter = ('form', 'question_type')

admin.site.register(Form, FormAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(Response)
admin.site.register(Answer)
