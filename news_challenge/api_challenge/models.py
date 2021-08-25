from django.db import models


class Author(models.Model):
    """
    Author Model.
    """
    name = models.CharField(
        max_length=100
    )

    picture = models.URLField()

    def __str__(self):
        return self.name

class Article(models.Model):
    """
    Article Model.
    """

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    category = models.CharField(
        max_length=100
    )

    title = models.CharField(
        max_length=150
    )

    summary = models.CharField(
        max_length=250
    )

    firstParagraph = models.TextField(
        max_length=500
    )

    body = models.TextField()

    def __str__(self):
        return self.title