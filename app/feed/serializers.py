from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):
    """Serializer for post objects"""

    comments = serializers.SerializerMethodField()

    class Meta:
        model = models.Post
        fields = "__all__"
        read_only_fields = ("id", "vote_amount", "created_on")

    def get_comments(self, obj):
        comments = obj.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for comment objects"""

    class Meta:
        model = models.Comment
        fields = "__all__"
        read_only_fields = ("id", "created_on")


class VoteSerializer(serializers.Serializer):
    """Serializer for vote request"""

    vote = serializers.CharField(max_length=5)
