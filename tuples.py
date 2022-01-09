# Tuples: ordered, immutateble, allows duplicate elements
import sys
import timeit

def main():
    mytuple = ("Max",28,"apple")
    mytuple = tuple(["Max",28,"apple"])
    print(mytuple)
    print(type(mytuple))

# com 1 elemento: mytuple = ("Max",)
    tup = ("Max")
# sem a virgula é salvo com string
    print(type(tup))

    item = mytuple[0] #index
    print(item)

    for i in mytuple:
        print(i)

    if 28 in mytuple:
        print("Yes")
    else:
        print("No")

    mytuple = ("a","p","p","l","e")

    print(len(mytuple))       # 5
    print(mytuple.count('p')) # 2
    print(mytuple.index('l')) # 3

    mylist = list(mytuple)
    print(mylist)

    a = (1,2,3,4,5,6,7,8,9,10)
    print(a[2:5]) # index : 2,3,4
    print(a[1::2]) # passo 2

# abrindo em novas variaveis
    info = ("Max",28,"Boston")
    name, age, city = info
    print(name)
    print(age)
    print(city)

# tuplas ocupam menos memória, uma vantangem para otimizacao
    my_list  = [0,1,2,"Hello",True]
    my_tuple = (0,1,2,"Hello",True)
    print(sys.getsizeof(my_list) ,"bites para a lista")
    print(sys.getsizeof(my_tuple),"bites para a tupla")


    print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=10^8), "tempo listas")
    print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=10^8), "tempo tuplas")


if __name__ == '__main__':
    main()