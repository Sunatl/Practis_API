from django.db import models

class Actor(models.Model):
    act_fname = models.CharField(max_length=50)
    act_iname  = models.CharField(max_length=50)
    act_gender = models.CharField(max_length=50)
    
    def __str__(self):
        return self.act_fname
    
class Director(models.Model):
    dir_fname = models.CharField(max_length=50)
    dir_iname  = models.CharField(max_length=50)
    
    def __str__(self):
        return self.dir_fname
    
class Genres(models.Model):
    gen_title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.dir_title
    
    
class Reviewer(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    time = models.IntegerField()
    lang = models.CharField(max_length=50)
    dt_rel = models.DateField(auto_now=True)
    rel_country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Movie_cast(models.Model):
    act_id = models.ForeignKey(Actor,  on_delete=models.CASCADE)
    mov_id = models.ForeignKey(Movie,  on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return self.role
    
class Movie_direction(models.Model):
    dir_id = models.ForeignKey(Director, on_delete=models.CASCADE)
    mov_id = models.ForeignKey(Movie,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.mov_id.__str__()


class Movie_genres(models.Model):
    gen_id = models.ForeignKey(Genres, on_delete=models.CASCADE)
    mov_id = models.ForeignKey(Movie,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.mov_id.__str__()

class Rating(models.Model):
    rev_id = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    mov_id = models.ForeignKey(Movie,  on_delete=models.CASCADE)
    rev_starts = models.IntegerField()
    num_o_ratings = models.IntegerField()
    
    def __str__(self):
        return self.mov_id.__str__()