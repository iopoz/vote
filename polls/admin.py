import os

from django import forms
from django.contrib import admin
# from polls.forms import ReadOnlyAdminFields

# Register your models here.


from polls.models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    change_form_template = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates', 'admin', 'new_change_form.html'))

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}

        if Question.objects.get(id=object_id).state != 'new':
            extra_context['has_delete_permission'] = False
            extra_context['show_delete'] = False
        return super(QuestionAdmin, self).change_view(request, object_id, extra_context=extra_context)

    def get_readonly_fields(self, request, obj=None):
        if obj.state != 'new':
            return ('question_text', 'pub_date',)
        else:
            return super(QuestionAdmin, self).get_readonly_fields(request, obj)

admin.site.register(Question, QuestionAdmin)
