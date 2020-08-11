from django.db import models

class Employee(models.Model):
    eid - models.charField(max_length = 20)
    ename = models.charField(max_length = 100)
    eemail = models.EmailField()
    econtact = models.charField(max_length = 15)
    class Meta:
        db_table = "employee"
