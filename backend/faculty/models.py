from django.core.exceptions import ValidationError
from django.db import models
from PIL import Image
import uuid

# Class that allows only 1 instance to be created in a model
class SingletonModel(models.Model):
	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		if not self.pk and self.__class__.objects.exists():
			raise ValidationError(f"Only one instance of {self.__class__.__name__} is allowed.")
		return super().save(*args, **kwargs)


class Message(SingletonModel):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	image = models.ImageField(default="default.png", upload_to="org_chart", null=True, blank=True)
	representative = models.CharField(max_length=20)
	content = models.TextField()

	def __str__(self):
		return f"Message from the {self.representative.capitalize()}"

	def clean(self):
		super().clean()
		if len(self.content) > 800:
			raise ValidationError({'content': 'maximum length is 800 characters.'})

	def save(self, *args, **kwargs):
		self.full_clean()
		super().save(*args, **kwargs)

	class Meta:
		verbose_name = "Message"
		verbose_name_plural = "Message"


class OrgChart(SingletonModel):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	image = models.ImageField(default="default.png", upload_to="org_chart", null=True, blank=True)

	def __str__(self):
		return 'Organizational Chart'


class Faculty(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	image = models.ImageField(default="default.png", upload_to="faculties", null=True, blank=True)
	name = models.CharField(max_length=30, unique=True)
	position = models.CharField(max_length=100, unique=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} - {self.position}"

	# Resizes Image Uploads
	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		if self.image:
			img = Image.open(self.image.path)
			max_size = 500

			if img.height > max_size or img.width > max_size:
				img.thumbnail((max_size, max_size), Image.LANCZOS)
				img.save(self.image.path)

	class Meta:
		verbose_name = "Faculty"
		verbose_name_plural = "Faculties"
		ordering = ['date_added']