import statistics
from statistics import geometric_mean
trabajadores =  ["Juan Pérez","María García","Carlos López"]
sueldos= []
sueldosAltos= []
sueldosMedios=[]
sueldosBajos= []
election=0
sueldo=0
estadisticas=[]
on=0
con=1

def ADDsueldo(nombre,sueldo):
    trabajador={
        "Nombre":nombre,
        "Sueldo":sueldo
        }
    sueldos.append(trabajador)

while on ==0:
    print("""----- Seleccione una opcion -----
          
          1).Asignar sueldos aleatorios
          2).Clasificar sueldo
          3).Ver estadisticas
          4).Reporte de sueldo
          5).Salir del programa
          """)
    try:
        election=int(input())
    except ValueError:
        print(" solo poede elegir las opciones en pantalla ")
    if election==1:
        for element in trabajadores:
            while sueldo <= 300000 or sueldo>=2500000:
                try:
                    print(" solo cifras entre $300.000 y $2.500.000 ")
                    sueldo=int(input(f"Asigne sueldo de {element}: $"))
                except ValueError:
                    print(" solo cifras entre $300.000 y $2.500.000 ")
                ADDsueldo(element,sueldo)
                print(" sueldo agregados ")
            sueldo=0
    elif election==2:
        for element in sueldos:
            if element["Sueldo"]<800000:
                sueldosBajos.append(element)
            elif element["Sueldo"]>=800000 and element["Sueldo"]<2000000:
                sueldosMedios.append(element)
            elif element["Sueldo"]>=2000000:
                sueldosAltos.append(element)
        print(f" Sueldos Menores a $800.000 ({len(sueldosBajos)})")
        print("Nombre del empleado       sueldo")
        for element in sueldosBajos:
            print(f"{element["Nombre"]}        {element["Sueldo"]}")
        print(f" Sueldos entre $800.000 y $2.000.0000 ({len(sueldosMedios)})")
        print("Nombre del empleado       sueldo")
        for element in sueldosMedios:
            print(f"{element["Nombre"]}        {element["Sueldo"]}")
        print(f" Sueldos Mayores a $2.000.0000 ({len(sueldosAltos)})")
        print("Nombre del empleado       sueldo")
        for element in sueldosAltos:
            print(f"{element["Nombre"]}        {element["Sueldo"]}")
    elif election==3:
        for element in sueldos:
            estadisticas.append(element["Sueldo"])
        print(f"""----- Estadisticas -----
              El sueldo mas bajo: {min(estadisticas)}
              El sueldo mas alto: {max(estadisticas)}
              La media giometrica: {round(geometric_mean(estadisticas))}
 """)
    elif election==4:
        print(""" reporte de sueldo 
            nombre     Sueldo_base    Descuento_de_salud  Descuento_AFP  sueldo_liquido """)
        for element in sueldos:
            print(f"            {element["Nombre"]}  {element["Sueldo"]}  {element["Sueldo"]*0.07:2}  {element["Sueldo"]*0.19:2}   {element["Sueldo"]*0.81:2}")
    elif election==5:
        print("""-----Finalizando Programa-----
              Desarrollado por Eliecer Salgado4
              Rut: 20.356.311-6""")
        on=1