from lista_enlazada import ListaEnlazada

lista = ListaEnlazada()

def test_agregar_al_final():
  lista.agregar_al_final(10)
  assert lista.raiz.valor == 10
  assert lista.num_nodos == 1

lista.agregar_al_final(3)
lista.agregar_al_final(2)
lista.agregar_al_final(1)

def test_valor_de():
  assert lista.valor_de(3) == 1
  
def test_agregar_despues_de():
  assert lista.agregar_despues_de(2, 12)
  assert lista.valor_de(3) == 12
  
def test_borrar_indice():
  lista.borrar_indice(0)
  assert lista.valor_de(0) == 3
  lista.borrar_indice(10)
  assert lista.num_nodos == 3
  
def test_contiene():
  assert lista.contiene(12)
  assert not lista.contiene(-1)

def test_imprimir():
  assert lista.imprimir() == "3 => 2 => 12 => 1"