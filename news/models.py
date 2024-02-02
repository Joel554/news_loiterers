from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Editor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    

class Contributor(models.Model):
    name = models.CharField(max_length=100)
    editor = models.ForeignKey(Editor, null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    column_name = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    subheadline = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    contributor = models.ForeignKey(Contributor, null=True, blank=True, on_delete=models.PROTECT)
    image = models.ImageField(null=True, blank=True, upload_to="article_images/")
    content = models.TextField()
    editor = models.ForeignKey(Editor, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.headline
    