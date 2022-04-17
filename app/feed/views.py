from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from . import serializers


class PostViewSet(viewsets.ModelViewSet):
    """Post viewset to manage posts in the database"""

    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()

    @action(detail=True, methods=["post"])
    def upvote(self, request, pk):
        """Make an upvote on the post"""
        post = models.Post.objects.filter(id=pk).first()
        serializer = serializers.VoteSerializer(data=request.data)
        if serializer.is_valid():
            post.vote_amount += 1
            post.save()
            return Response(
                {"message": "Post Upvoted"}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class CommentViewSet(viewsets.ModelViewSet):
    """Comment viewset to manage comments in the database"""

    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()

    def get_queryset(self):
        """Get comments for the given post"""
        return models.Comment.objects.filter(owner=self.kwargs["post_pk"])
