class Triangle():
    a = None
    b = None
    c = None
    
    def create_triangle(self, a:int, b:int, c:int) -> str:
        if a >= (b + c) or b >= (a + c) or c >= (a + b):
            return "É impossível formar um triangulo com esses valores"
        else:
            self.a = a
            self.b = b
            self.c = c
            return "Triangulo construido"
    
    def triangle_type(self) -> str:
        if self.a == None:
            return "Triangulo ainda não formado"
        
        if self.a == self.b and self.b == self.c:
            return "Triangulo Equilatero"
        elif  self.a == self.b or self.b == self.c or self.a == self.c:
            return "Triangulo Isósceles "
        else:
            return "Triangulo Escaleno"