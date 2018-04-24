from rest_framework import serializers, viewsets
from blog import models
from rest_framework.renderers import JSONRenderer


class Utf8JSONRenderer(JSONRenderer):
    charset = 'utf-8'


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BlogArticle
        depth = 1
        fields = ('url', 'title', 'author', 'content', 'pub_date')


class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.BlogArticle.objects.all()
    serializer_class = BlogSerializer
    renderer_classes = (Utf8JSONRenderer,)
