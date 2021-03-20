from django.db import models
import uuid

class TeamMember(models.Model):
    member_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    role = models.CharField(choices=[("admin", "Admin"), ("regular", "Regular")], max_length=10, default="regular")