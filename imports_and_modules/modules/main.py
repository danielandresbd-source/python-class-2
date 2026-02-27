from modules.module_1 import add, subtract, multiply, divide
import modules.module_1 as module_1

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

# adicional
print(module_1.__name__) # imprime el nombre del modulo
print(module_1.__file__) # imprime el path del módulo