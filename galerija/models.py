from django.db import models

class Album(models.Model):
    title = models.CharField(max_length = 30)
    description = models.CharField(max_length = 256)

    def __str__(self):
        return "Title: {}, Description: {}".format(self.title, self.description)

    class Meta:
        ordering = ('title', )

class Image(models.Model):
    path = models.CharField(max_length = 256, blank = False)
    album = models.ForeignKey(Album, related_name = 'images', on_delete = models.CASCADE)
    title = models.CharField(max_length = 30, blank = True)
    description = models.CharField(max_length = 256, blank = True)

    def __str__(self):
        return "Album: {}, Path: {}, Title: {},   Description: {}".format(self.album.title,
                                                        self.path,self.title,self.description)

    class Meta:
        ordering = ('title', )