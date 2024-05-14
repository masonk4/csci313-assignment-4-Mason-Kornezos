from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)
class BookInstanceInline (admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
   list_display = ('title', 'author')

   inlines = [BookInstanceInline]
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
     list_filter = ('status', 'due_back')

     fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )