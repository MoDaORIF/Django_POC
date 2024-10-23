from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(
        source="owner.username"
    )  # Show author's username

    class Meta:
        model = Article
        fields = (
            "id",
            "title",
            "body",
            "owner",
            "created_at",
        )


class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Article.objects.all()
    )

    class Meta:
        model = User
        fields = ("id", "username", "article")
