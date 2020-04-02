from django.db import models


# Create your models here.
class applicant(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    number = models.IntegerField()
    linkedin = models.URLField(default="", max_length=150)
    github = models.URLField(default="", max_length=150)
    about_me =models.TextField(default="About Me",max_length=500)

    POSITIONS = (
        ('Python Developer', 'Python Developer'),
        ('Java Developer', 'Java Developer'),
        ('Web  Developer', 'Web Developer'),
    )
    position = models.CharField(max_length=40, choices=POSITIONS)

    def __str__(self):
        fullName = self.first_name + " " + self.last_name
        return fullName + " --- " + self.position
