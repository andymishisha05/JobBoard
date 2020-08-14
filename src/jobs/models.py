from django.db import models

# Create your models here.

JOB_TYPES = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
    ("Freelancer", "Freelancer")

)


class Job(models.Model):
    title = models.CharField(max_length=100)
    # Location
    job_type = models.CharField(max_length=15, choices=JOB_TYPES)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=False)
    vacancy = models.IntegerField(default=0)
    salary = models.DecimalField(default=0,max_digits=10,decimal_places=3)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    pass
