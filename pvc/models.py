from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=128)
    color = models.CharField(max_length=15)


class PromptTemplate(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    tag = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(db_index=True)


class PromptTemplateVersion(models.Model):
    template = models.ForeignKey(PromptTemplate, on_delete=models.CASCADE)
    version = models.CharField(max_length=7, db_index=True)

    content = models.TextField()
    input_variables = models.CharField()
    is_actual = models.BooleanField(default=False, db_index=True)

    class Meta:
        unique_together = ["template", "version"]


class PVCLog(models.Model):
    log_tag = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE)
    prompt = models.ForeignKey(PromptTemplateVersion, on_delete=models.CASCADE)

    input = models.TextField()
    output = models.TextField()

    created_at = models.DateTimeField(auto_created=True)
