class Empresa:
    def __init__(self, epsa_nombre='', epsa_ruc='', epsa_dep=''):
        self.epsa_nombre = epsa_nombre
        self.epsa_ruc = epsa_ruc
        self.epsa_departamento = Departamento(epsa_dep)

    def mostrar_empresa_dep(self):
        print('Empresa "{}"\n -Ruc: {}'.format(self.epsa_nombre, self.epsa_ruc))
        self.epsa_departamento.mostrar_departamento()


class Departamento:
    def __init__(self, dep=''):
        self.departamento = dep

    def mostrar_departamento(self):
        print(' -Departamento de', self.departamento)

    def mostrar_empleados(self, empl=None):
        self.datos_empleado = empl
        print('Empleado "{}"'.format(self.datos_empleado.nombre))
        print(' -Correo Electrónico:', self.datos_empleado.correo)
        print(' -Domicilio:', self.datos_empleado.domicilio)


class Empleado:
    def __init__(self, nom='', cor='', dom=''):
        self.nombre = nom
        self.correo = cor
        self.domicilio = dom


class Sueldo:
    def __init__(self, sldo_base=float, sldo_sobreT=float):
        self.sldo_base = SueldoBase(sldo_base)
        self.sldo_sobreT = sldo_sobreT
        self.sueldo = self.sldo_base.sueldo_base + self.sldo_sobreT
    
    def mostrar_sueldos(self):
        print(' -Sueldo Base: $' + str(self.sldo_base.sueldo_base))
        print(' -Sueldo Sobretiempo: $' + str(self.sldo_sobreT))
        print(' -Sueldo Total: $' + str(self.sueldo))


class SueldoBase:
    def __init__(self, sldo_base=float):
        self.sueldo_base = sldo_base


class SueldoSobreTiempo:
    def __init__(self, hra=int, pago=float):
        self.sueldo_sobretiempo = hra * pago


if __name__ == '__main__':
    # Ingreso de datos
    print('INGRESO DE DATOS')
    # Empresa
    empresa_nom = input('Nombre de la empresa: ').strip()
    empresa_ruc = input('Ruc de la empresa: ').strip()
    empresa_dep = input('Departamento asignado: ').strip()
    # Empleado
    empleado_nom = input('\nNombre del empleado: ').strip()
    empleado_cor = input('Correo Electrónico del empleado: ').strip()
    empleado_dom = input('Domicilio del empleado: ').strip()
    # Sueldo
    while True:
        try:
            sueldo_base = float(input('Sueldo base del empleado: $'))
            break
        except ValueError:
            print('Ingrese un valor correcto.\n')
    calcular_sobre_tiempo = True
    while calcular_sobre_tiempo:
        while True:
            respuesta = input('¿Quiere calcular sueldo por sobretiempo?  (Si/No)\n :').lower().replace(' ', '')
            if respuesta in ('si', 'sí'):
                break
            elif respuesta in ('no'):
                calcular_sobre_tiempo = False
                break
            else: print('\nIngrese una respuesta correcta.')
        if calcular_sobre_tiempo:
            while True:
                try:
                    horas_extras = int(input('Horas extras que trabajo: '))
                    break
                except ValueError:
                    print('Ingrese un valor correcto.\n')
            while True:
                try:
                    pago_hra = float(input('Pago por horas extras: $'))
                    break
                except ValueError:
                    print('Ingrese un valor correcto.\n')
            calcular_sobre_tiempo = False

    # Muestra de datos
    print('\nPAGO DE NOMINA')
    # epsa_jf = Empresa('JothaFer', '0999999999', 'Diseño')
    epsa = Empresa(empresa_nom, empresa_ruc, empresa_dep)
    epsa.mostrar_empresa_dep()

    # empl = Empleado('Luis Díaz', 'ldiaz@hotmail.com', 'Milagro')
    empl = Empleado(empleado_nom, empleado_cor, empleado_dom)

    depar = Departamento()
    depar.mostrar_empleados(empl)

    # sldo_sobreT = SueldoSobreTiempo(5, 2.50)
    sldo_sobreT = SueldoSobreTiempo(horas_extras, pago_hra)

    # sldo = Sueldo(1325.80, sldo_sobreT.sueldo_sobretiempo)
    sldo = Sueldo(sueldo_base, sldo_sobreT.sueldo_sobretiempo)
    sldo.mostrar_sueldos()