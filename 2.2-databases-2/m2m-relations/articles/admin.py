from django.contrib import admin

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, ArticleTags, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class ArticleTagsInlineFormset(BaseInlineFormSet):
    def clean(self):

        if len(self.forms) == 0:
            raise ValidationError('Нет тега!')

        self.count_is_main_tag = 0

        for form in self.forms:
            if self.count_is_main_tag > 0 and form.cleaned_data.get('is_main'):
                raise ValidationError('Основной 1 раздел')
            else:
                if form.cleaned_data.get('is_main'):
                    print(f"{form.cleaned_data.get('tag')} - Основной раздел")
                    self.count_is_main_tag += 1
                else:
                    continue

        return super().clean()


class ArticleTagsInline(admin.TabularInline):
    model = ArticleTags
    formset = ArticleTagsInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ArticleTagsInline]