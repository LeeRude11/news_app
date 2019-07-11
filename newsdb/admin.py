from django.contrib import admin

from .models import SingleNews, NewsTag


class NewsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'get_tags')
    list_filter = ('tags',)

    def get_tags(self, news):
        return ', '.join(tag.name for tag in news.tags.all()) or 'None'

    get_tags.short_description = 'Tags List'

    filter_horizontal = ('tags',)


admin.site.register(SingleNews, NewsAdmin)
admin.site.register(NewsTag)
