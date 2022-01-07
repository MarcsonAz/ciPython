# Lists: ordered, mutateble, allows duplicate elements

def main():
    mylist = ["banana","cherry","apple"]

    item = mylist[0]
    print(item)

    item = mylist[-1]
    print(item)

    for i in mylist:
        print(i)

    if "banana" in mylist: # testado com lemon -> Não
        print("Sim")
    else:
        print("Não")

    print("Quantos elementos na lista:")
    print(len(mylist))

    mylist.append("lemon") # inserir no fim
    
    mylist.insert(1,"blueberry") # posicao especifica
    print(mylist)

# retorna ultimo valor e o remove da lista
    item = mylist.pop() 
    print(item)
    print(mylist)

#somente remover item especifico
    mylist.remove("cherry")
# para esvaziar a lista mylist.clear()
    print(mylist)

# ordenacao
    mylist.reverse()
# muda a lista original
    mylist.sort() 

# sem alterar original
    newlist = sorted(mylist)

    mylist = [0] * 5
    mylist2 = [1,2,3,4,5]

    newlist = mylist + mylist2  

    print(newlist)

# lista[inicio:fim:passo]
    a = newlist[4:7] 
    print(a)

    print(newlist[:3])
    print(newlist[6:])

# do 2º ao fim, com passo de 2 elementos
    print(newlist[2::2]) 

# outro jeito de reverter lista
    print(newlist[::-1])
    
# copiar
    list_org = ["banana","cherry","apple"]
    list_copy = list_org.copy() # ou list_org[:]

#list comprehension
    a = [1,2,3,4,5]
    b = [i*i for i in a]

    print(a)
    print(b)

if __name__ == '__main__':
    main()