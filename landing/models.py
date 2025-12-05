from django.db import models
from django.conf import settings

class ImagenGaleria(models.Model):
    titulo = models.CharField(max_length=120)
    imagen = models.ImageField(upload_to='galeria/')
    descripcion = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        db = settings.FIRESTORE_CLIENT
        db.collection("imagenes").document(str(self.id)).set({
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "imagen_url": self.imagen.url if self.imagen else None,
        })

    def delete(self, *args, **kwargs):
        db = settings.FIRESTORE_CLIENT
        db.collection("imagenes").document(str(self.id)).delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=200)
    motivacion = models.CharField(max_length=200)
    estilo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='personajes/')
    detalles = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        db = settings.FIRESTORE_CLIENT
        db.collection("personajes").document(str(self.id)).set({
            "id": self.id,
            "nombre": self.nombre,
            "rol": self.rol,
            "motivacion": self.motivacion,
            "estilo": self.estilo,
            "detalles": self.detalles,
            "imagen_url": self.imagen.url if self.imagen else None,
        })

    def delete(self, *args, **kwargs):
        db = settings.FIRESTORE_CLIENT
        db.collection("personajes").document(str(self.id)).delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        db = settings.FIRESTORE_CLIENT
        db.collection("noticias").document(str(self.id)).set({
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "fecha": self.fecha.isoformat(),
            "imagen_url": self.imagen.url if self.imagen else None,
        })

    def delete(self, *args, **kwargs):
        db = settings.FIRESTORE_CLIENT
        db.collection("noticias").document(str(self.id)).delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Historia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        db = settings.FIRESTORE_CLIENT
        db.collection("historia").document("principal").set({
            "titulo": self.titulo,
            "contenido": self.contenido,
        })

    def delete(self, *args, **kwargs):
        db = settings.FIRESTORE_CLIENT
        db.collection("historia").document("principal").delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.titulo
