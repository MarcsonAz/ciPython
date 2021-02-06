# operacoes com listas       python cap3/listas.py

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0].title())
print(bicycles[-1])

msg = "My first bicycle was a "+bicycles[2].title()+"."
print(msg)

lista31 = ["Marcson","Rafael","Bruno","Marlon","Natan"]
for x in lista31:
    print(x)

# saudacao
for x in lista31:
    print("Olá, "+x+". Seja bem vindo!")

# “Gostaria de ter uma moto Honda”.

veiculo = ["Moto", "Carro"]
marca = ["Honda","BMW"]

import random as rd
for x in lista31:
    a = rd.randint(0, 1)
    b = rd.randint(0, 1)
    print(x.title()+" gostaria de ter um(a) "+veiculo[a]+" "+marca[b])

# modificar elementos da lista

motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
motorcycles.insert(0, 'ducati')
print(motorcycles)

