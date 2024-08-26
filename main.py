from triangle.triangle import Triangle

tri = Triangle()
ctrl = 1

#Autores: Tales, Pedro Catelani e Gustavo Souza
#Ler 3 valores (A, B e C) representando as medidas dos lados

test_list = [
    (1, 2, 3),
    (3, 4, 5),
    (2, 2, 4),
    (4, 4, 4),
    (5, 3, 3)
]

for test_case in test_list:
    print(f'\n--Teste {ctrl}--')
    check = tri.create_triangle(test_case[0],test_case[1],test_case[2])
    print(check)
    print(tri.triangle_type())
    print(tri.perimeter())
    print(tri.area())
    ctrl += 1