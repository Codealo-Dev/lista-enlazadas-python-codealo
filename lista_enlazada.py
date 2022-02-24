"""
 * El nodo es un objeto con el siguiente esquema
 * nodo: { valor: null, siguiente: null }
"""

class Nodo:
  valor = None
  siguiente = None

  def __init__(self, valor):
    self.valor = valor

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

  def __init__(self):
    self.raiz = None
    self.num_nodos = 0
  
  def agregar_al_final(self, valor):
    if not self.raiz:
      self.raiz = Nodo(valor)
    else:
      cur = self.raiz
      while cur.siguiente:
        cur = cur.siguiente
      cur.siguiente = Nodo(valor)
    self.num_nodos = self.num_nodos + 1
  
  def agregar_despues_de(self, indice, valor):
    if indice > self.num_nodos:
      return None
    cur_indice = indice
    cur = self.raiz
    while cur_indice > 0:
      cur = cur.siguiente
      cur_indice = cur_indice - 1
    nuevo_nodo = Nodo(valor)
    nuevo_nodo.siguiente = cur.siguiente
    cur.siguiente = nuevo_nodo
    self.num_nodos = self.num_nodos + 1
    
  def borrar_indice(self, indice):
    if indice > self.num_nodos:
      return None

    if indice == 0:
      self.raiz = self.raiz.siguiente  
    else:
      cur_indice = indice
      prev = self.raiz
      cur = prev.siguiente
      while cur_indice > 0:
        prev = cur
        cur = cur.siguiente
        cur_indice = cur_indice - 1
      prev.siguiente = cur.siguiente
    self.num_nodos = self.num_nodos - 1
    
  def contiene(self, valor):
    cur = self.raiz
    while cur.siguiente:
      if cur.valor == valor:
        return True
    return False

  def valor_de(self, indice):
    if indice > self.num_nodos:
      return None
    cur_indice = indice
    cur = self.raiz
    while cur_indice > 0:
      cur = cur.siguiente
      cur_indice = cur_indice - 1
    return cur.valor
    
  def imprimir(self):
    if not self.raiz:
      return ""
    
    resultado = []
    cur = self.raiz
    while cur.siguiente:
      resultado.append(str(cur.valor))
      cur = cur.siguiente
    resultado.append(str(cur.valor))
    return " => ".join(resultado)