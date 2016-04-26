from django.db import models

class CourseType(models.Model):
    course_type = models.CharField(max_length=140)

    def __unicode__(self):
        return self.course_type

class Course(models.Model):
    course_type = models.ForeignKey(CourseType)
    name = models.CharField(max_length=140)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    #picture = models.ImageField(upload_to='media/courses/pictures', blank=True, null=True)

    def __unicode__(self):
        return self.name
