from django.contrib import admin
from .models import Post, Category

# Inline model admin for Category in Post admin
class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'category', 'published_date', 'created_date', 'updated_date', 'content_preview')
    list_filter = ('status', 'category', 'author', 'created_date', 'updated_date')
    search_fields = ('title', 'content', 'author__username', 'category__name')
    list_editable = ('status',)
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
    
    fieldsets = (
        (None, {
            'fields': ('author', 'title', 'content', 'image', 'status', 'category')
        }),
        ('Dates', {
            'fields': ('published_date',)
        }),
    )
    
    inlines = [CategoryInline]

    # Overriding the save_model method to add custom logic when saving objects
    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    # Custom admin action to bulk publish selected posts
    def publish_posts(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "Selected posts have been published.")
    publish_posts.short_description = "Publish selected posts"

    # Adding the custom action to the list of available actions
    actions = [publish_posts]

    # Adding a method to display a preview of the content in the list view
    def content_preview(self, obj):
        return obj.content[:50] + "..."
    content_preview.short_description = 'Content Preview'

# Registering the models with the admin site
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
