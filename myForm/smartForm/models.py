from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=10, primary_key=True)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.usn
class Project(models.Model):
    p_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    team_size = models.IntegerField()
    student1_usn = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student1_usn')
    student2_usn = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student2_usn')
    student3_usn = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student3_usn', null=True, blank=True)
    def __str__(self):
        return self.project_name