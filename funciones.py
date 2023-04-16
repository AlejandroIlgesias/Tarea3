from clases import CorreoException


def verificar(elmail):
    arroba=elmail.count('@') #cuenta las @ en elmail
    punto=elmail.count('.')
    
    #si hay 0 @ o más de una
    #rfind si la @ esta al final
    #si no hay @ (otra forma de hacerlo)

    if(arroba!=1 or elmail.rfind('@')==(len(elmail)-1) or elmail.find('@')==0):
        raise CorreoException("correo no válido")
    else:
        if (punto==1) and (elmail.rfind(".")>=(elmail.rfind("@")+2)):# COMPARA LAS POSICIONES DEL PUNTO Y EL ARROBA EN LA CADENA
            pass

        else:
            raise CorreoException("correo no válido")