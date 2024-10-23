from django.db import models


# The migration adds an 's' at the end of the class name in the view !
class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    author = models.CharField(max_length=100, blank=True, default="")
    body = models.TextField()
    owner = models.ForeignKey(
        "auth.User", related_name="article", on_delete=models.CASCADE
    ) 

    class Meta:
        ordering = ["created_at"]

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
