import os
class Empresa():
    def __init__(self,nom="",ruc=0,dire="",tele=0,ciud="",tipEmpr=""):
        self.nombre=nom
        self.ruc=ruc
        self.direccion=dire
        self.telefono=tele
        self.ciudad=ciud
        self.tipoEmpresa=tipEmpr

    def datosEmpresa(self):#3
        self.nombre=input("Ingresar nombre de la empresa: ")
        self.ruc=int(input("Ingresar ruc de la empresa: "))
        self.direccion=input("Ingresar la direccion de la empresa: ")
        self.telefono=int(input("Ingresar el numero de telefono de la empresa: "))
        self.ciudad=input("Ingresar ciudad donde esta la empresa: ")
        self.tipoEmpresa=input("Ingresar tipo de empresa publica o privada: ")
    
    def mostrarEmpresa(self):
        print("")
        print("Datos de la Empresa")
        print("La empresa de nombre {}\n De RUC #{} \n Está ubicada en {}\n Se puede comunicar al #{}\n Está empresa esta en la ciudad de {}\n Es una entidad {}".format(self.nombre,self.ruc,self.direccion, self.telefono,self.ciudad, self.tipoEmpresa))

class Empleado(Empresa):
    def __init__(self,nom="",cedu=0,dire="",tele=0,email="",estado="",profe="",anti=0,com=0,fNomina="",fIngreso="",iess=0):
        self.nombre=nom
        self.cedula=cedu
        self.direccion=dire
        self.telefono=tele
        self.correo=email
        self.estadocivil=estado
        self.profesion=profe
        self.antiguedad=anti
        self.comision=com
        self.fechaNomina=fNomina
        self.fechaIngreso=fIngreso
        self.iess=iess

    def empleado(self):
        self.nombre=input("Ingresar nombre del empleado: ")
        self.cedula=int(input("Ingresar numero de cedula del empleado: "))
        self.direccion=input("Ingresar la direccion del empleado: ")
        self.telefono=int(input("Ingresar numero de contacto del empleado: "))
        self.correo=input("Ingresar correo personal del empleado: ")
        self.iess=float(input("Ingresar valor del iees recordar que debe ser porcentuado Ejemplo si quiere decir 20% debe ingresar 0.20"))
        self.fechaNomina=input("Ingresar fecha de nomida (formato año-mes-dia): ")
        self.fechaIngreso=input("Ingresar fecha de ingreso (formato año-mes-dia): ")
        self.antiguedad=float(input("Ingresar valor de antiguedad"))
        self.comision=float(input("Ingresar calor de la comsion: "))

    def empleadoObrero(self): 
        self.estadocivil=input("Ingresar estado civil del empleado: ")

    def empleadoOficina(self):
      self.profesion=input("Ingresar profesion del empleado: ")

    # def mostrarempleado(self):
    #     print("El empleado: {} con # de C.I. {} \n Con direccion {}, y numero de contacto{}\n Y correo {}".format(self.nombre,self.cedula,self.direccion,self.telefono,self.correo))
  

class Departamento(Empleado):
    def __init__(self,dep=""):
        self.departamento=dep
    def departa(self):
        self.departamento=input("Ingresar el departamento al que pertenece el empleado: ")

    def mostrarDeparta(self):
        print("El empleado pertenece al departamento de: {}".format(self.departamento))

class Pagos(Empleado):
    def __init__(self, desc=0,desper=0,valhora=0,hotraba=0,extra=0):
        self.permisos=desper
        self.valorhora=valhora
        self.horastrabajadas=hotraba
        self.valextra=extra
        self.sueldo= suel
        self.horasRecargo= hrecar
        self.horasExtraordinarias=hextra
        self.prestamo= pres
        self.mesCuota= mcou
        self.valor_hora= valho
        self.sobretiempo=sobtiem
        self.comEmpOficina = comofi
        self.antiEmpObrero = antobre
        self.iessEmpleado = iemple
        self.cuotaPrestamo=cuopres
        self.totdes = tot
        self.liquidoRecibir = liquid


    def pagoNormal(self):
        self.sueldo=float(input("Ingresar sueldo del trabajador: $"))
        self.prestamo=float(input("Ingresar monto del prestamo que ha generado el empleado: $"))
        self.mesCuota=("Ingresar meses qa diferir el prestamo: ")
        
    def pagoExtra(self):
        self.horasRecargo=int(input("Ingresar horas de recargo: "))
        self.horasExtraordinarias=int(input("Ingresar horas extraordinarias: "))

    def calculoSueldo(self):
        self.valor_hora=self.sueldo/240
        self.sobretiempo= valor_hora * (horasRecargo*0.50+horasExtraordinarias*2)
        self.comEmpOficina =  self.comision*self.sueldo
        self.antiEmpObrero = self.antiguedad*(FechaNomina - FechaIngreso)/365*self.sueldo
        self.iessEmpleado = self.iess*(self.sueldo+self.sobretiempo)
        self.cuotaPrestamo=self.prestamo/self.mesCuota
        if eleccion==1:
            self.toting = self.sueldo+self.sobretiempo+ self.comEmpOficina
        elif eleccion==2:    
            self.toting = self.sueldo+self.sobretiempo+self.antiEmpObrero
        self.totdes = iessEmpleado + prestamoEmpleado
        self.liquidoRecibir = toting - totdes

    def mostrarSueldo(self):
        print("Arreglar")


emp=Empresa()
emp.datosEmpresa()
emple=Empleado()
emple.empleado()
eleccion=int(input("Va a ingresar un empleado tipo 1. Obreo o 2.Oficina: "))
emple.empleadoObrero()
emple.empleadoOficina()
pag=Pagos()
pag.pagoNormal()   
pag.pagoExtra
pag.calculoSueldo()
pag.mostrarSueldo()
os.system ("cls")

emp.mostrarEmpresa()
print("")
emple.mostrarempleado()
