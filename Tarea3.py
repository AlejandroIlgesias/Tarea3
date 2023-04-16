from funciones import verificar
from clases import CorreoException

t=True
while t:
    print("Igrese su correo elecrónico")
    correo=input("> ")
    try:
        verificar(correo)
        if correo=="vicente@eni.es":
            print("Bienvenido Vicente")
        else:
            print("Cuenta bloqueada a causa de un ataque")
        t=False
    except CorreoException:
        
        if correo=="":
            print(" '' es una entrada incorrecta. Introduzca una dirección de correo  electrónico" )
        else:
            print("Una dirección de correo electrónico debe tener el formato xxx@xxx.xx")