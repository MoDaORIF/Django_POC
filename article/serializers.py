from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Article
        fields = (
            "id",
            "title",
            "body",
            "owner",
            "created_at",
        )
