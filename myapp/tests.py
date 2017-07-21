from django.test import TestCase
 
from .models import Entity, RelatedEntity
 
 
class EntityTestCase(TestCase):
    def test_set_children(self):
        related_entity = RelatedEntity.objects.create()
        entity = Entity.objects.create(name='An entity', some_relation=related_entity)
        entity.children.add(Entity.objects.create(name='1st child', some_relation=related_entity))
        entity.children.add(Entity.objects.create(name='2nd child', some_relation=related_entity))
 
        self.assertEquals(entity.children.all()[0].name, '1st child')
        self.assertEquals(entity.children.all()[1].name, '2nd child')
