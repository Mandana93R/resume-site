from django.contrib import admin
from .models import (
    Profile,
    SocialLink,
    Project,
    Experience,
    Skill,
    Testimonial,
    Education,
    Language,
    Conference,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'email', 'updated_at')
    search_fields = ('full_name', 'job_title', 'email')

    def has_add_permission(self, request):
        return not Profile.objects.exists()
        # این متد باعث می‌شود وقتی یک پروفایل ایجاد شد، دکمه افزودن پروفایل جدید از پنل مدیریت حذف شود.اما یک نکته: این روش فقط از طریق Django Admin جلوی ایجاد رکورد دوم را می‌گیرد؛ اگر بخواهیم محدودیت در سطح خود مدل هم برقرار باشد، باید بعداً آن را هم بررسی کنیم.
        # نتیجه:
        # - قبل از ایجاد پروفایل: دکمه Add Profile نمایش داده می‌شود.
        # - بعد از ایجاد اولین پروفایل: دکمه Add Profile حذف می‌شود.
        # - امکان مشاهده و ویرایش پروفایل موجود همچنان برقرار است.
        # یک نکته معماری: این محدودیت فقط در Django Admin اعمال می‌شود، نه در سطح دیتابیس یا سایر روش‌های ایجاد رکورد. برای پروژه فعلی کافی است؛ اگر بعداً نیاز داشتیم محدودیت را در سطح مدل هم اعمال می‌کنیم.

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')
    search_fields = ('platform',)
    list_filter = ('is_active',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'project_type',
        'is_active',
        'display_order',
    )
    list_editable = ('is_active', 'display_order')
    list_filter = ('project_type', 'is_active')
    search_fields = ('title', 'description')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'job_title',
        'company',
        'start_date',
        'end_date',
        'is_current',
    )
    list_editable = ('is_current',)
    list_filter = ('is_current',)
    search_fields = ('job_title', 'company')
    ordering = ('-start_date',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'level',
        'proficiency',
        'is_active',
        'display_order',
    )
    list_editable = ('proficiency', 'is_active', 'display_order')
    list_filter = ('level', 'is_active')
    search_fields = ('name',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'author_name',
        'author_title',
        'is_active',
        'display_order',
    )
    list_editable = ('is_active', 'display_order')
    list_filter = ('is_active',)
    search_fields = ('author_name', 'author_title', 'quote')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'degree',
        'institution',
        'start_year',
        'end_year',
    )
    search_fields = ('degree', 'institution')
    ordering = ('-start_year',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'proficiency',
        'stars',
        'display_order',
    )
    list_editable = ('stars', 'display_order')
    list_filter = ('proficiency',)
    search_fields = ('name',)


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'event_date',
        'is_active',
    )
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('name', 'location')
    ordering = ('-event_date',)