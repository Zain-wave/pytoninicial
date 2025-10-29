class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def Calcular_area(self):
        return self.base * self.altura
    
base = int(input("Proporciona la base: "))
altura = int(input("Proporciona la altura: "))

rectangulo1 = Rectangulo(base, altura)
print(f"Area rectangulo: {rectangulo1.Calcular_area()} ")