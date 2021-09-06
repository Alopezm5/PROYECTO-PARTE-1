class Empresa:
    def __init__(self):
        pass

    def datosEmpresa(self,nom,ruc,dir,tele,ciud,tipEmpr):#3
        self.nombre=nom
        self.ruc=ruc
        self.direccion=dir
        self.telefono=tele
        self.ciudad=ciud
        self.tipoEmpresa=tipEmpr


class Empleado():
    def __init__(self):
        pass

    def empleado(self,nom,ced,dir,tele):
        self.nombre=nom
        self.cedula=ced
        self.direccion=dir
        self.telefono=tele

    def empleadoObrero(self,nom,ced,dir,tele):#falta dos atributo como definicion de obrero 
        self.nombre=nom
        self.cedula=ced
        self.direccion=dir
        self.telefono=tele

    def empleadoOficina(self,nom,ced,dir,tele):#falta dos atributo como definicion de oficina
        self.nombre=nom
        self.cedula=ced
        self.direccion=dir
        self.telefono=tele

class Departamento(2):
    def __init__(self):
        pass

class Pagos():
    def __init__(self):
        pass

    def pagoNormal(self, valhora,hoesti,hotraba):#falta 1 atributo
        self.valorhora=valhora
        self.horaestimada=hoesti
        self.horastrabajadas=hotraba

    def pagoExtra(self, valhora,hoesti,hotraba):#falta 1 atributo
        self.valorhora=valhora
        self.horaestimada=hoesti
        self.horastrabajadas=hotraba

    def Nomina():#faltan 8 atributos incluir cosas del empleado y  sobretiempo
        pass


emp=Empresa()
emp.datosEmpresa()
