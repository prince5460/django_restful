from django.db import models


# Create your models here.

class BlogArticle(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    author = models.CharField(max_length=20, verbose_name='作者')
    content = models.TextField(verbose_name='文章内容')
    pub_date = models.DateTimeField(verbose_name='时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ("-pub_date",)

    def __str__(self):
        return self.title
