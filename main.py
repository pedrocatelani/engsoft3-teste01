from triangle.triangle import Triangle

tri = Triangle()

#Autores: Tales, Pedro Catelani e Gustavo Souza
#Ler 3 valores (A, B e C) representando as medidas dos lados

lista_de_teste = [
    (1, 2, 3),
    (3, 4, 5),
    (2, 2, 4),
    (4, 4, 4),
    (5, 3, 3)
]

check = tri.create_triangle(3, 4, 5)
print(check)