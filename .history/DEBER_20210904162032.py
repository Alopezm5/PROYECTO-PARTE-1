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
    def __init__(self,nom="",ruc=0,dire="",tele=0,email="",estado="",profe=""):
        self.nombre=nom
        self.ruc=ruc
        self.direccion=dire
        self.telefono=tele
        self.correo=email
        self.estadocivil=estado
        self.profesion=profe
        self.antiguedad
        self.comision
        self.fechaNomina=
        self.fechaIngreso=

    def empleado(self):
        self.nombre=input("Ingresar nombre del empleado: ")
        self.cedula=int(input("Ingresar numero de cedula del empleado: "))
        self.direccion=input("Ingresar la direccion del empleado: ")
        self.telefono=int(input("Ingresar numero de contacto del empleado: "))
        self.correo=input("Ingresar correo personal del empleado: ")

    def empleadoObrero(self): 
        self.iess=
        self.estadocivil=input("Ingresar estado civil del empleado: ")
        self.antiguedad=float(input("Ingresar valor de antiguedad"))
        self.fechaNomina=input("Ingresar fecha de nomida (formato año-mes-dia): ")
        self.fechaIngreso=input("Ingresar fecha de ingreso (formato año-mes-dia): ")

    def empleadoOficina(self):#falta dos atributo como definicion de oficina
      self.profesion=input("Ingresar profesion del empleado: ")
      self.comision=float(input("Ingresar calor de la comsion: "))

    def mostrarempleado(self):
        print("El empleado: {} con # de C.I. {} \n Con direccion {}, y numero de contacto{}\n Y correo {}".format(self.nombre,self.cedula,self.direccion,self.telefono,self.correo))
        if eleccion==1:
            print("De estado civil",self.estadocivil)
        elif eleccion==2:
            print("Con profesion de",self.profesion)  

class Departamento(Empleado):
    def __init__(self,dep=""):
        self.departamento=dep
    def departa(self):
        self.departamento=input("Ingresar el departamento al que pertenece el empleado: ")

    def mostrarDeparta(self):
        print("El empleado pertenece al departamento de: {}".format(self.departamento))

class Pagos(Empleado):
    def __init__(self, desc=0,desper=0,valhora=0,hotraba=0,extra=0):
        self.descuentos=desc
        self.permisos=desper
        self.valorhora=valhora
        self.horastrabajadas=hotraba
        self.valextra=extra

    def pagoNormal(self):
        self.sueldo=float(input("Ingresar sueldo del trabajador: $"))
        
    def pagoExtra(self):
        self.horasRecargo=int(input("Ingresar horas de recargo: "))
        self.horasExtraordinarias=int(input("Ingresar horas extraordinarias: "))


    def calculoSueldo(self,tt1=0,tt2=0):
        self.valor_hora=self.sueldo/240
        self.sobretiempo= valor_hora * (horasRecargo*0.50+horasExtraordinarias*2)
        self.comEmpOficina =  self.comision*self.sueldo
        self.antiEmpObrero = self.antiguedad*(FechaNomina - FechaIngreso)/365*self.sueldo


        iessEmpleado = Deducciones.iess*(sueldo+sobretiempo)
        prestamoEmpleado = cuota del prestamo
        toting = sueldo+sobretiempo+ comisionEmpOficina+ antiguedadEmpObrero
        totdes = iessEmpleado + prestamoEmpleado
        liquidoRecibir = toting - totdes



    def mostrarSueldo(self):
        print(self.tt1,self.tt2)


emp=Empresa()
emp.datosEmpresa()
emp.mostrarEmpresa()
print("")
emple=Empleado()
emple.empleado()
eleccion=int(input("Va a ingresar un empleado tipo 1. Obreo o 2.Oficina: "))
if eleccion==1:
    emple.empleadoObrero()
elif eleccion==2:
    emple.empleadoOficina()
else:
    print("No selecciono el tipo de empleado")
emple.mostrarempleado()
pag=Pagos()
pag.pagoNormal()
inf=int(input("El trabajador trabajo horas 1.Si o cualquier otro numero.No"))
if inf==1:
    pag.pagoExtra()
else:
    pass    
pag.calculoSueldo()
pag.mostrarSueldo()