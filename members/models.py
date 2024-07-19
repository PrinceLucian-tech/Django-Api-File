from django.db import models

# Create your models here.
import uuid

class Member(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  first_name = models.Charfield(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(unique=True)
  joined_date = models.DataField(auto_now_add=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"