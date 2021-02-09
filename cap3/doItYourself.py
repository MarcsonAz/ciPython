# atividades do livro para o leitor resolver

#3.4

convidados = ['Mahomes','Messi','Federer','Lebron','Bernardinho']
print('Olá, estou convidando '+convidados[0]+' para jantar.')
print('Olá, estou convidando '+convidados[1]+' para jantar.')
print('Olá, estou convidando '+convidados[2]+' para jantar.')
print('Olá, estou convidando '+convidados[3]+' para jantar.')
print('Olá, estou convidando '+convidados[4]+' para jantar.')

print('Poxa, o convidado Federer não poderá vir para o jantar')

convidados[2] = 'Guga'

print('Olá, estou convidando '+convidados[0]+' para jantar.')
print('Olá, estou convidando '+convidados[1]+' para jantar.')
print('Olá, estou convidando '+convidados[2]+' para jantar.')
print('Olá, estou convidando '+convidados[3]+' para jantar.')
print('Olá, estou convidando '+convidados[4]+' para jantar.')

print("""Informamos que haverá mais espaços disponíveis nas mesas 
para o jantar. Abaixo seguirá a lista de convidados.""")

convidados.insert(0,'Popó')
convidados.insert(4,'Mojave')
convidados.append('Senna')

for x in convidados:
    print('Olá, estou convidando '+x+' para jantar.')

print("""Informamos que houve um problema com as mesas 
para o jantar, somente teremos dois convidados. Abaixo seguirá a lista de convidados.""")

for x in convidados:
    if x=='Mahomes' or x=='Lebron':
        print('Olá, estou convidando '+x+' para jantar.')
    else:
        print('Olá, eu sinto muito, mas o convidado '+x+' não irá para o jantar.')
        convidados.remove(x)

print(convidados)
