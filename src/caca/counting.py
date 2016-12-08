'''
Created on 07/12/2016

@author: 
'''
import logging
import sys
nivel_log = logging.ERROR
# nivel_log = logging.DEBUG
logger_cagada = None

def cacounting_core(numeros):
    tam_numeros = len(numeros)
    conteo_mayores = []
    mapa_mierda = [0 for _ in range(100)]
    
    for numero_act in numeros:
        mapa_mierda[numero_act] += 1
        
    logger_cagada.debug("el mapa de mierda %s" % mapa_mierda)
    
    conteo_mayores.append(mapa_mierda[0])
    for  idx_num, num_act in enumerate(mapa_mierda[1:], 1):
        conteo_mayores.append(num_act + conteo_mayores[idx_num - 1])
    
    logger_cagada.debug("el conteo caca %s" % conteo_mayores)
    
    return conteo_mayores
    
def cacounting_main():
    lineas = list(sys.stdin)
    numeros = []
    
    for linea in lineas[1:]:
        numeros.append(int(linea.strip().split(" ")[0]))
        
    logger_cagada.debug("los putos numeros %s" % numeros)
    
    ass = cacounting_core(numeros)
    print(" ".join([str(x) for x in ass]))
    

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)   
        cacounting_main()
