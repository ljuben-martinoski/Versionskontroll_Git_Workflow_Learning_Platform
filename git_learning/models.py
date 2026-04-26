"""
=============================================================================
FILE: models.py
=============================================================================
"""
from django.db import models
from django.utils import timezone


class GitResource(models.Model):
    CATEGORY_CHOICES = [
        ("branching", "Branching Strategies"),
        ("commits", "Commit Conventions"),
        ("collaboration", "Collaboration Practices"),
        ("tools", "Git Tools & Commands"),
        ("general", "General Git Knowledge"),
    ]

    title = models.CharField(max_length=200, help_text="The title of this resource")
    description = models.TextField(help_text="A brief description of what this resource teaches")
    url = models.URLField(blank=True, null=True, help_text="Web link (optional)")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="general")
    is_official = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Git Resource"
        verbose_name_plural = "Git Resources"

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


class LearningNote(models.Model):
    TOPIC_CHOICES = [
        ("branching", "Branching"),
        ("commits", "Commits"),
        ("merging", "Merging"),
        ("pull_requests", "Pull Requests"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES, default="other")
    is_highlighted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Learning Note"
        verbose_name_plural = "Learning Notes"

    def __str__(self):
        return self.title
