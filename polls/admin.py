import os

from django import forms
from django.contrib import admin
from polls.models import Question, Choice

NEW = 'new'
INP = 'inp'
CLOSED = 'closed'
STATE_CHOICES_FOR_NEW = (
    (NEW, 'new question'),
    (INP, 'in progress'),
)

STATE_CHOICES_FOR_INP = (
    (INP, 'in progress'),
    (CLOSED, 'closed question'),
)

STATE_CHOICES_FOR_CLOSED = (
    (CLOSED, 'closed question'),
)


class StatusForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['state','question_text', 'pub_date']

    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        current_state = self.instance.state

        def next_status():
            if current_state == 'new':
                return STATE_CHOICES_FOR_NEW
            elif current_state == 'inp':
                return STATE_CHOICES_FOR_INP
            elif current_state == 'closed':
                return STATE_CHOICES_FOR_CLOSED
            else:
                return STATE_CHOICES_FOR_NEW
            pass

        self.fields['state'].choices = next_status


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

    # readonly_fields = ('choice_text',)
    def get_readonly_fields(self, request, obj=None):
        try:
            if obj.state != 'new':
                return ('choice_text',)  # ('question_text', 'pub_date', )
            else:
                return super(ChoiceInline, self).get_readonly_fields(request, obj)
        except AttributeError:
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
    form = StatusForm

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}

        if Question.objects.get(id=object_id).state != 'new':
            extra_context['has_delete_permission'] = False
            extra_context['show_delete'] = False
        return super(QuestionAdmin, self).change_view(request, object_id, extra_context=extra_context)

    def get_readonly_fields(self, request, obj=None):
        try:
            if obj.state != 'new':
                return self.readonly_fields + ('question_text', 'pub_date')  # ('question_text', 'pub_date', )
            else:
                return super(QuestionAdmin, self).get_readonly_fields(request, obj)
        except AttributeError:
            return super(QuestionAdmin, self).get_readonly_fields(request, obj)

    # def next_status(self, obj):
    #     if obj.state == 'new':
    #         return
    # next_status.short_name = 'Statuses'
    # next_status.empty_value_display = '???'


    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
