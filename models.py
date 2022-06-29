from django.db import models


# Create your models here.
class BlogPost(models.Model):
    slug = models.SlugField()
    pub_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255, db_index=True)
    summary = models.TextField(db_index=True)
    learned = models.TextField()
    img_url = models.URLField()
    git_url = models.URLField()

    def __str__(self):
        return self.title
