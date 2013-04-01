from django.db import models


#Tabla 1:  Desafios propios. 
class Tabla_uno(models.Model):
	nombre = models.CharField(max_length = 15)
    desafio = models.TextField()
    meta = models.TextField()

    def __unicode__(self):
    	return self.nombre

#Tabla 2:
class Tabla_dos(models.Model):
	nombre = models.CharField(max_length = 15)
	
	def __unicode__(self):
		return self.nombre

class Contenido(models.Model):
	pass    


class Departamento(models.Model):
    nombre = models.CharField(max_length = 20)
	
	def __unicode__(self):
		return self.nombre	

#Carreras de la UnACh, que deben llenar el ciclo-calidad.
class Carrera(models.Model):
    nombre = models.CharField(max_length = )

    def __unicode__(self):
        return self.nombre


#Facultades de la UnACh, que deben completar el ciclo-calidad.
class Facultad(models.Model):
    nombre = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.nombre
#Vicerrectorias de la Unach, que participan del ciclo de calidad.
class Vicerrectoria(models.Model):
	nombre = models.CharField(max_length = 20)	

class Funcionario(models.Model):
    nombre = models.CharField(max_length = 30)
    correo = models.EmailField(max_length = 30)
    id_departamento = models.ForeignKey(Departamento)
    
    def __unicode__(self):
        return self.nombre



#Representa el papel a llenar del ciclo de calidad 
class CicloCalidad(models.Model):
    nombre = models.CharField(max_length = 10)
    id_funcionario = models.ForeignKey(Funcionario)
    descripcion = models.CharField(max_length = 30, null = True)
     		
        def __unicode__(self):
            return self.nombre


