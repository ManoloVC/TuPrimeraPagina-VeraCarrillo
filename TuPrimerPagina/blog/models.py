from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class   Categoria(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__ (self):
        return self.nombre
    
class Post(models.Model):
    titulo=models.CharField(max_length=200)
    contenido =models.TextField()
    fecha_publicacion=models.DateTimeField(auto_now_add=True)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.titulo
    