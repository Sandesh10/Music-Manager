from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})
    
    #The below function is builtin syntax for string representation
    #of this object
    def __str__(self):
        return self.album_title + ' - '+ self.artist


class Song(models.Model):
    #A primary key is needed when each element needs a unique id no.
    #A foreign key is needed when you have sth like Song thats part of something else.
    #Each song is linked to Album. 
    # on delete= models.CASCADE - It means whenever we delete the album, any
    #songs that were linked to that, go ahead and delete the songs.

    album = models.ForeignKey(Album, on_delete= models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


    
    
