import os

from django import forms
from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    #readonly_fields = ('choice_text',)
    def get_readonly_fields(self, request, obj=None):
        if obj.state != 'new':
            return ('choice_text',)#('question_text', 'pub_date', )
        else:
            return super(ChoiceInline, self).get_readonly_fields(request, obj)

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}

        if Question.objects.get(id=object_id).state != 'new':
            extra_context['has_delete_permission'] = False
            extra_context['show_delete'] = False
            extra_context['has_add_permission'] = False
        return super(ChoiceInline, self).change_view(request, object_id, extra_context=extra_context)


class QuestionAdmin(admin.ModelAdmin):
    # change_form_template = os.path.abspath(
    #     os.path.join(os.path.dirname(__file__), 'templates', 'admin', 'new_change_form.html'))

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}

        if Question.objects.get(id=object_id).state != 'new':
            extra_context['has_delete_permission'] = False
            extra_context['show_delete'] = False
        return super(QuestionAdmin, self).change_view(request, object_id, extra_context=extra_context)

    def get_readonly_fields(self, request, obj=None):
        if obj.state != 'new':

            return self.readonly_fields + ('question_text', 'pub_date')#('question_text', 'pub_date', )
        else:
            return super(QuestionAdmin, self).get_readonly_fields(request, obj)

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
