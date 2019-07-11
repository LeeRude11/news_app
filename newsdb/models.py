from django.db import models


NEWS_IMGS_FOLDER = 'news_images/'
DEF_NEWS_IMG = NEWS_IMGS_FOLDER + 'default.png'


class SingleNews(models.Model):
    heading = models.CharField(max_length=64)
    text = models.TextField()
    image = models.ImageField(
        upload_to=NEWS_IMGS_FOLDER,
        default=DEF_NEWS_IMG
    )
    tags = models.ManyToManyField('NewsTag', blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = 'News'


class NewsTag(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name
