"""
 * El nodo es un objeto con el siguiente esquema
 * nodo: { valor: null, siguiente: null }
"""

class Nodo:
  valor = None
  siguiente = None

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
  num_nodos: 0

  def agregar_al_final(self, valor):
    raise NotImplementedError()

  def agregar_despues_de(self, indice, valor):
    raise NotImplementedError()
    
  def borrar_indice(self, indice):
    raise NotImplementedError()
    
  def contiene(self, valor):
    raise NotImplementedError()

  def valor_de(self, indice):
    raise NotImplementedError()
    
  def imprimir(self):
    raise NotImplementedError()