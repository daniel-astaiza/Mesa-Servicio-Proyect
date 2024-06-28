from django.db import models
from django.contrib.auth.models import AbstractUser
#siempre que modifiquemos el models.py debesmos hacer python manage.makemigrations y el python manage.migrate

tipoOficinaAmbiente=[
    ('administrativo', 'administrativo'), ('formacion', 'formacion')
]
tipoUsuario=[
    ('administrativo', 'administrativo'), ('instructor','instructor')
]
estadoCaso=[
    ('solicitada', 'solicitada'),('en proceso', 'en proceso'),('finalizada', 'finalizada')
]
tipoProcedimiento=[
    ('hardware', 'hardware'),('software', 'software'),('', '')
]
tipoSolucion=[
    ('parcial', 'parcial'), ('definitiva','definitiva')
]

class OficinaAmbinete(models.Model):
    Tipo= models.CharField(max_length=15, choices=tipoOficinaAmbiente,
                           db_comment="tipo de oficina")
    Nombre=models.CharField(max_length=40 , unique=True,
                            db_comment="nombre de oficina o del ambiente")
    FechaHoraCreacion=models.DateField(auto_now_add=True,
                                           db_comment="fecha y hora del registro")
    FechaHoraActualizacion=models.DateField(auto_now_add=True,
                                           db_comment="fecha y hora ultima actualizacion")
    def __str__(self) -> str:
        return self.Nombre
    
class User (AbstractUser):
    UserTipo = models.CharField(max_length=15, choices=tipoUsuario ,db_comment="tipo de usuario")
    UserFoto = models.ImageField(
        upload_to=f"fotos/", null=True,blank=True,db_comment="foto del usuario")
    FechaHoraCreacion=models.DateField(auto_now_add=True,
                                           db_comment="fecha y hora del registro")
    FechaHoraActualizacion=models.DateField(auto_now_add=True,
                                           db_comment="fecha y hora ultima actualizacion")
    def __str__(self) -> str:
        return self.username
    
    
class Solicitudes(models.Model):
    solUsuario = models.ForeignKey(User, on_delete=models.PROTECT,
                                   db_comment="hace referencia a el empleado que hace la solicitud")
    solDescripcion = models.TextField(max_length=1000, 
                                      db_comment="texto de describe la solicitud del estado")
    solOficinaAmbiente = models.ForeignKey(OficinaAmbinete, on_delete=models.PROTECT,
                                           db_comment="hace referencia a la oficina o ambiente donde se encuentra el equipo")
    FechaHoraCreacion=models.DateField(auto_now_add=True,
                                           db_comment="fecha y hora del registro")
    FechaHoraActualizacion=models.DateField(auto_now_add=True,
                                           db_comment="fecha y hora ultima actualizacion")
    def __str__(self) -> str:
        return self.solDescripcion
    
    
class Caso(models.Model):
    casSolicitud=models.ForeignKey(Solicitudes, on_delete=models.PROTECT,
                                    db_comment="hace referencia a la solicitud")
    casCodigo= models.CharField(max_length=20 , unique=True , 
                                db_comment="codigo unico del caso")
    casUsuario=models.ForeignKey(User, on_delete=models.PROTECT,
                                 db_comment="empleado del soporte tecnico asignado")
    casEstado=models.CharField(max_length=15 , choices=estadoCaso,
                                db_comment="eleccion del estado del caso"  , default='solicitada')
    FechaHoraActualizacion=models.DateField(auto_now_add=True,
                                db_comment="fecha y hora ultima actualizacion")
    def __str__(self) -> str:
        return self.casCodigo
    


class TipoProcedimiento (models.Model):
    proNombre =models.CharField(max_length=30, unique=True, 
                              db_comment="nombre del procedimiento")
    proDescripcion =models.TextField(max_length=1000,
                                db_comment="texto con la descripcion del procedimiento")
    FechaHoraCreacion=models.DateField(auto_now_add=True,
                             db_comment="fecha y hora del registro")
    FechaHoraActualizacion=models.DateField(auto_now_add=True,
                               db_comment="fecha y hora ultima actualizacion")
    def __str__(self) -> str:
        return self.proNombre

class SolucionCaso(models.Model):
    solCaso=models.ForeignKey(Caso, on_delete=models.PROTECT,
                              db_comment="hace referencia al caso ")
    #hacer la migracion otra vez
    solProcedimiento= models.TextField(max_length=2000,
                                        db_comment="Texto del procedimiento realizado en la solución del caso")
    solTipoSolucion=models.CharField(max_length=20, choices=tipoSolucion,
                                     db_comment="tipo de solucion, si es parcial o definitiva")
    FechaHoraCreacion=models.DateField(auto_now_add=True,
                             db_comment="fecha y hora del registro")
    FechaHoraActualizacion=models.DateField(auto_now_add=True,
                               db_comment="fecha y hora ultima actualizacion")
    def __str__(self) -> str:
        return self.solProcedimiento
    
class SolucionCasoTipoProcedimiento(models.Model):
    solSolucionCaso=models.ForeignKey(SolucionCaso, on_delete=models.PROTECT,
                                      db_comment="hace referencia a la solucion del Caso")
    solTipoProcedimiento=models.ForeignKey(TipoProcedimiento,on_delete=models.PROTECT,
                                           db_comment="hace referencia al tipo de la solucion")
    def __str__(self) -> str:
        return f'{self.solSolucionCaso},{self.solTipoProcedimiento}'
    
    
    

    
    
    



    
    

# Create your models here.
