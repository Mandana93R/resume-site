from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Profile(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    job_title = models.CharField(max_length=150, verbose_name='Job Title')
    bio = models.TextField(verbose_name='Biography')
    profile_image = models.ImageField(
        upload_to='profile/',
        verbose_name='Profile Image'
    )
    email = models.EmailField(verbose_name='Email')
    website = models.URLField(blank=True, verbose_name='Website')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Phone Number')
    location = models.CharField(max_length=150, blank=True, verbose_name='Location')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'



class SocialLink(models.Model):
    platform = models.CharField(max_length=50, verbose_name='Platform')
    url = models.URLField(verbose_name='URL')
    icon = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Icon'
    )
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name='Display Order'
    )

    def __str__(self):
        return self.platform

    class Meta:
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'
        ordering = ['display_order']



class Project(models.Model):
    PROJECT_TYPES = [
        ('latest', 'Latest Project'),
        ('other', 'Other Project'),
    ]

    title = models.CharField(max_length=150, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        verbose_name='Project Image'
    )
    project_url = models.URLField(blank=True, verbose_name='Project URL')
    github_url = models.URLField(blank=True, verbose_name='GitHub URL')
    project_type = models.CharField(
        max_length=10,
        choices=PROJECT_TYPES,
        default='latest',
        verbose_name='Project Type'
    )
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name='Display Order'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['display_order']



class Experience(models.Model):
    job_title = models.CharField(max_length=150, verbose_name='Job Title')
    company = models.CharField(max_length=150, verbose_name='Company')
    company_url = models.URLField(blank=True, verbose_name='Company Website')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='End Date'
    )
    is_current = models.BooleanField(
        default=False,
        verbose_name='Currently Working Here'
    )
    description = models.TextField(verbose_name='Description')

    def clean(self):
        if self.is_current and self.end_date:
            raise ValidationError(
                'A current job cannot have an end date.'
            )

        if not self.is_current and not self.end_date:
            raise ValidationError(
                'An end date is required for a previous job.'
            )

        if self.end_date and self.end_date < self.start_date:
            raise ValidationError(
                'End date cannot be earlier than start date.'
            )

    def __str__(self):
        return f'{self.job_title} at {self.company}'

    class Meta:
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experiences'
        ordering = ['-start_date']




class Skill(models.Model):
    SKILL_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    name = models.CharField(max_length=100, verbose_name='Skill Name')
    description = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Description'
    )
    level = models.CharField(
        max_length=20,
        choices=SKILL_LEVELS,
        default='beginner',
        verbose_name='Skill Level'
    )
    proficiency = models.PositiveSmallIntegerField(
        default=50,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
        verbose_name='Proficiency (%)'
    )
    url = models.URLField(blank=True, verbose_name='Related URL')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name='Display Order'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['display_order']



class Testimonial(models.Model):
    author_name = models.CharField(max_length=100, verbose_name='Author Name')
    author_title = models.CharField(max_length=150, verbose_name='Author Title')
    quote = models.TextField(verbose_name='Testimonial')
    author_image = models.ImageField(
        upload_to='testimonials/',
        blank=True,
        verbose_name='Author Image'
    )
    linkedin_url = models.URLField(
        blank=True,
        verbose_name='LinkedIn URL'
    )
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name='Display Order'
    )

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['display_order']


class Education(models.Model):
    degree = models.CharField(max_length=150, verbose_name='Degree')
    institution = models.CharField(
        max_length=150,
        verbose_name='Institution'
    )
    institution_url = models.URLField(
        blank=True,
        verbose_name='Institution Website'
    )
    start_year = models.PositiveSmallIntegerField(
        verbose_name='Start Year'
    )
    end_year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name='End Year'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description'
    )
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name='Display Order'
    )

    def clean(self):
        if self.end_year and self.end_year < self.start_year:
            raise ValidationError(
                'End year cannot be earlier than start year.'
            )

    def __str__(self):
        return f'{self.degree} - {self.institution}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
        ordering = ['display_order']


class Language(models.Model):
    PROFICIENCY_LEVELS = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('native', 'Native'),
    ]

    name = models.CharField(max_length=100, verbose_name='Language')
    proficiency = models.CharField(
        max_length=20,
        choices=PROFICIENCY_LEVELS,
        verbose_name='Proficiency Level'
    )
    stars = models.PositiveSmallIntegerField(
        default=3,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
        verbose_name='Stars'
    )
    display_order = models.PositiveIntegerField(
        default=0,
        verbose_name='Display Order'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ['display_order']


class Conference(models.Model):
    name = models.CharField(max_length=150, verbose_name='Conference Name')
    location = models.CharField(max_length=150, verbose_name='Location')
    event_url = models.URLField(blank=True, verbose_name='Event URL')
    event_date = models.DateField(verbose_name='Event Date')
    description = models.TextField(
        blank=True,
        verbose_name='Description'
    )
    is_active = models.BooleanField(default=True, verbose_name='Is Active')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Conference'
        verbose_name_plural = 'Conferences'
        ordering = ['-event_date']