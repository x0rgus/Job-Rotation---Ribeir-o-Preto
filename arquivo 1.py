numero = int(input("Digite o numero: "))
c=0
a=1
b=1

if numero==0 or numero==1:
    print("Pertence")
else:
    while c<numero:
        c=a+b
        b=a
        a=c
    if c==numero:
        print("Pertence")
    else:
        print("não pertence")