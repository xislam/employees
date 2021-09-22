from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Departments(MPTTModel):
    """model department created for employee data, have structures up to 5 levels"""
    name = models.CharField(max_length=50, verbose_name="name")
    parent_departments = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                                        related_name='children')
    create_date = models.DateField(auto_now_add=True, verbose_name="create_date")

    def save(self, *args, **kwargs):
        if self.parent_departments.get_level() == 5:
            raise ValueError(u'Maximum nesting has been reached!')
        super(Departments, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Departments'
        verbose_name = 'Department'
        ordering = ['name']

    class MPTTMeta:
        order_insertion_by = ['name']
        parent_attr = 'parent_departments'


class Employee(models.Model):
    """employee data and link with the department"""
    full_name = models.CharField(max_length=70, verbose_name="full_name")
    position = models.CharField(max_length=50, verbose_name="position")
    employment_date = models.DateField(verbose_name="employment date")
    size_of_salary = models.IntegerField(verbose_name="size of salary")
    subdivision = models.ForeignKey(Departments, verbose_name="Department", on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True, verbose_name="create_date")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Employee'
        verbose_name = 'Employee'
        ordering = ['full_name']
