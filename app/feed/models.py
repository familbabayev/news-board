from django.db import models


class Post(models.Model):
    """Post model that will be served at the feed"""

    title = models.CharField(max_length=200)
    link = models.CharField(max_length=1000)
    author_name = models.CharField(max_length=200)
    vote_amount = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment model for posts"""

    owner = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author_name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
