class Rectangle:

	def __init__(self, base, height):
		self.ibase = base
		self.iheight = height

	def area(self):
		return self.ibase * self.iheight

class Square(Rectangle):

	def __init__(self, lado):
		super().__init__(lado, lado)

	def area_sq(self):
		return self.ibase * self.iheight

rect = Rectangle(4, 5)
print('Rectangle:',rect.area())

squa = Square(3)
print('Square:', squa.area_sq())


class Coche:
    neumaticos = 4
    logitud = 120
    estado = False

    def encender(self):
        self.estado = True

    def view_state(self):
        if self.estado:
            return f"Encendido"
        else:
            return f"Apagado"

auto = Coche()
# auto.encender()
print(auto.view_state())