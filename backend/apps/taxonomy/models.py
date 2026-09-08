from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, db_index=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_nav_visible = models.BooleanField(default=True)
    color_accent = models.CharField(max_length=32, default='#0066FF', help_text="Hex accent color")

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, db_index=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Subcategories'
        unique_together = ('category', 'slug')
        ordering = ['name']

    def __str__(self):
        return f"{self.category.name} > {self.name}"

class Topic(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, db_index=True)
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    icon_name = models.CharField(max_length=64, blank=True, default='Layers')

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=16, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, db_index=True)
    iso_code = models.CharField(max_length=3, unique=True, help_text="ISO 3166-1 alpha-2 or alpha-3 code")
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name='countries')
    capital = models.CharField(max_length=100, blank=True)
    flag_emoji = models.CharField(max_length=8, blank=True)
    gdp_nominal_usd = models.CharField(max_length=64, blank=True, help_text="e.g. $67.5 Billion")
    population = models.CharField(max_length=64, blank=True, help_text="e.g. 102.5 Million")
    strategic_resources = models.JSONField(default=list, blank=True, help_text="List of strategic resources (Cobalt, Lithium, Gold, etc.)")
    sovereignty_notes = models.TextField(blank=True, help_text="Key national sovereignty and strategic priorities")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.flag_emoji} {self.name}" if self.flag_emoji else self.name
