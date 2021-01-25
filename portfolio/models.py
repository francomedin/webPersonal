from django.db import models

# Create your models here.

class Project(models.Model):
    title= models.CharField(max_length=30,verbose_name="Titulo")
    description=models.TextField(verbose_name="Descripcion")
    image=models.ImageField(verbose_name="Imagen",upload_to="projects")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion") #se añade la hora cuando es creado
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion") #Se actualiza cuando se modifica
    url=models.URLField(null=True,blank=True)
    
    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
        ordering=["-created"]
    
    def __str__(self):
        return self.title