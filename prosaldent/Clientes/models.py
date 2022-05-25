from django.db import models

class Cliente(models.Model):
    title = models.CharField(max_length=200, 
        verbose_name="Título")
    subtitle = models.CharField(max_length=200, 
        verbose_name="Subtítulo")
    content = models.TextField(
        verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", 
        upload_to="Clientes")
    created = models.DateTimeField(auto_now_add=True, 
        verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, 
        verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "CLIENTE"
        verbose_name_plural = "CLIENTES"
        ordering = ['-created']

    def __str__(self):
        return self.title
