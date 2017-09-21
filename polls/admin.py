import os

from django import forms
from django.contrib import admin


# Register your models here.


from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_displayed = ('next_status', 'question_text', 'pub_date')
    change_form_template = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'templates', 'admin', 'new_change_form.html'))

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        if Question.objects.get(id=object_id).state != 'new':
            extra_context['readonly'] = True

        return super(QuestionAdmin, self).change_view(request, object_id, extra_context=extra_context)



admin.site.register(Question, QuestionAdmin)
