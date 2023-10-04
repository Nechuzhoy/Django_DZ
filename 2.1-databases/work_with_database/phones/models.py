from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    image = models.CharField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200, verbose_name="URL")

    def __str__(self):
        return f'{self.name}, {self.image}: {self.price}: {self.release_date}: {self.lte_exists}: {self.slug}'
