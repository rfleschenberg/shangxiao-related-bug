from django.db import models


class Entity(models.Model):
    name = models.CharField(max_length=100)
    parents = models.ManyToManyField('self', related_name='children',
                                     symmetrical=False)
    some_relation = models.ForeignKey('RelatedEntity', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RelatedEntity(models.Model):
    pass
