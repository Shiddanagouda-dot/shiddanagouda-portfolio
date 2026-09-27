from django.db import models


class Profile(models.Model):
    """The single owner of this portfolio. Only one row is expected to exist."""

    full_name = models.CharField(max_length=120)
    tagline = models.CharField(
        max_length=160,
        help_text="Short role line, e.g. 'Software Engineer (Fresher) — Python / Django / DRF'",
    )
    summary = models.TextField()
    location = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    leetcode_note = models.CharField(max_length=120, blank=True)
    languages_spoken = models.CharField(max_length=200, blank=True)
    resume_file_name = models.CharField(
        max_length=120,
        blank=True,
        default="resume.pdf",
        help_text="File name inside core/static/core/files/ to link as 'Download Resume'.",
    )

    def __str__(self):
        return self.full_name


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    location = models.CharField(max_length=120, blank=True)
    start_year = models.CharField(max_length=10, blank=True)
    end_year = models.CharField(max_length=10, blank=True)
    detail = models.CharField(max_length=200, blank=True, help_text="e.g. CGPA: 8.4")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-end_year"]

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Experience(models.Model):
    role = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.CharField(max_length=40)
    end_date = models.CharField(max_length=40, default="Present")
    bullet_points = models.TextField(
        help_text="One bullet per line."
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def bullets(self):
        return [line.strip() for line in self.bullet_points.splitlines() if line.strip()]

    def __str__(self):
        return f"{self.role} at {self.organization}"


class SkillCategory(models.Model):
    name = models.CharField(max_length=80)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Skill categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    year = models.CharField(max_length=20, blank=True)
    tech_stack = models.CharField(
        max_length=250, help_text="Comma-separated, e.g. 'Django, DRF, PostgreSQL'"
    )
    summary = models.CharField(max_length=250)
    bullet_points = models.TextField(help_text="One bullet per line.", blank=True)
    link = models.URLField(blank=True, help_text="GitHub or live link")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]

    def bullets(self):
        return [line.strip() for line in self.bullet_points.splitlines() if line.strip()]

    def __str__(self):
        return self.title


class Certification(models.Model):
    name = models.CharField(max_length=200)
    provider = models.CharField(max_length=120, blank=True)
    year = models.CharField(max_length=10, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}> — {self.created_at:%Y-%m-%d %H:%M}"
