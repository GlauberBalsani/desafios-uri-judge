
#MANEIRA LÓGICA DE RESOLVER

#sami = input().split()
#a = int(sami[0])
#b = int(sami[1])
#c = int(sami[2])
#maior = 0

#if a>b and a>c:
#    maior = a
#elif b>a and b>c:
#    maior = b
#else:
#    maior = c

#print(f"{maior} eh o maior")    

sami = input().split()
a = int(sami[0])
b = int(sami[1])
c = int(sami[2])
maior = max(a,b,c)
print(f"{maior} eh o maior")

