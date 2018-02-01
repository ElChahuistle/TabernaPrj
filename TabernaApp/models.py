from django.db import models


class Cerveceria(models.Model):
    cerveceria = models.CharField(max_length=30)
    country = models.CharField(max_length=15)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.cerveceria

class TipoCerveza(models.Model):
    tipo = models.CharField(max_length=10)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name='Tipo de Cerveza'
        verbose_name_plural='Tipos de Cervezas'


class Presentacion(models.Model):
    presentacion = models.CharField(max_length=10)

    def __str__(self):
        return self.presentacion

    class Meta:
        verbose_name_plural = 'Presentaciones'


class Cerverza(models.Model):
    CATEGORIAS = [
        ('AR', 'Artesanal'),
        ('IN', 'Industrial')
    ]
    cerveza = models.CharField(max_length=10)
    cerveceria = models.ForeignKey(Cerveceria, on_delete=models.DO_NOTHING)
    tipo = models.ForeignKey(TipoCerveza, on_delete=models.DO_NOTHING)
    categoria = models.CharField(max_length=2, choices=CATEGORIAS, default=models.BLANK_CHOICE_DASH)
    presentaciones = models.ManyToManyField(Presentacion)
    existencia = models.IntegerField(default=0)
    board = models.BooleanField(default=False)

    def hay_existencias(self):
        return True if self.existencia > 0 else False

    def en_board(self):
        return True if Cerverza.objects.filter(board=True).count() <= 8 else False

    def __str__(self):
        return self.cerveza
