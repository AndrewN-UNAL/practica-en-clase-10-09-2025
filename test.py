var=input("escribe una frase para editar despues:")
print("esta es tu frase: ", var)
remove=input("que quieres eliminar de esta frase?: ")


print(var.replace(remove,""))

count=input("que letra quieres contar en tu frase?: ")
print("hay ", var.count(count), count, " en tu frase")
print(var.count())
