"""
 * El nodo es un objeto con el siguiente esquema
 * nodo: { valor: null, siguiente: null }
 *
 * Antes de cada función veras las instrucciones de lo
 * que debería de hacer
 *
 * Cuando hagas cambios en ester archivo vas a ver
 * las pruebas que has completado
"""

"""
 * Agregar al final de nuestra lista un nuevo
 * nodo con el valor pasado como parametro
 *
 * Si no hay un nodo en nuestra lista, crear el
 * nodo raiz y ponerle asignarle el valor
 *
 * Para crear un nodo puedes usar la funcion crearNodo
 *
"""

class ListaEnlazada:
  raiz = None
  numNodos: 0

  
  def agregar_al_final(valor):
    raise NotImplementedError()

  
  def agregar_despues_de(indice, valor):
    raise NotImplementedError()
    
  def borrar_indice(indice):
    raise NotImplementedError()
    
  def contiene(valor):
    raise NotImplementedError()

  def valor_de(indice):
    raise NotImplementedError()
    
  def imprimir():
    raise NotImplementedError()