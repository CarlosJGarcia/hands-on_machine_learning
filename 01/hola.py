import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print()
print("Hola, mundo!")
print("Hostname:", hostname)
print("IP Address:", ip)
print("Fin del programa.")
print()

lista = [n for n in range(10)]
print(lista)