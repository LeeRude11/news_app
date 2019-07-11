from django.views import generic

from .models import SingleNews


class NewsList(generic.ListView):
    template_name = 'newsdb/news_list.html'
    model = SingleNews


class NewsDetail(generic.DetailView):
    template_name = 'newsdb/news_detail.html'
    model = SingleNews


class NewsByTag(NewsList):

    def get_queryset(self):
        """
        Return News which have the specified tag.
        """
        tag_name = self.kwargs['tag_name']
        return self.model.objects.filter(tags__name=tag_name)

    def get_context_data(self, **kwargs):
        """
        Set page_title using tag.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All news by tag: " + self.kwargs['tag_name']
        return context
