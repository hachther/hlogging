from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.template.defaultfilters import linebreaksbr
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from hlogging.models import LoggingUser, LoggingMessage


class LoggingUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'chat_id', 'type')
    list_filter = ('type', )

admin.site.register(LoggingUser, LoggingUserAdmin)


class LoggingMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'level', 'message', 'actions_view')
    readonly_fields = ('html', )
    list_filter = ('user', 'level')
    ordering = ('-date', )

    def actions_view(self, obj):
        info = self.model._meta.app_label, self.model._meta.model_name
        return mark_safe('<a href="{}" target="_blank">View</a>'.format(reverse('admin:%s_%s_view' % info, args=[obj.pk])))

    actions_view.short_description = _('Actions')

    def message(self, obj):
        return linebreaksbr(obj.text)

    message.short_description = _('Message')

    def get_urls(self):
        urls = super(LoggingMessageAdmin, self).get_urls()
        info = self.model._meta.app_label, self.model._meta.model_name
        my_urls = [
            url(r'^(?P<pk>\d+)/view/$', self.admin_site.admin_view(self.view_message, cacheable=True), name='%s_%s_view' % info),
        ]
        return my_urls + urls

    def view_message(self, request, pk):
        obj = LoggingMessage.objects.get(pk=pk)
        return HttpResponse(obj.html)

admin.site.register(LoggingMessage, LoggingMessageAdmin)
