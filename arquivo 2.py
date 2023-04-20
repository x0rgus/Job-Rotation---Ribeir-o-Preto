texto = input("digite o texto: ")
textoinvertido = []
texto = [x for x in texto]

for letra in texto:
    textoinvertido = [letra] + textoinvertido

textoinvertido = "".join(textoinvertido)
print(f"O texto invertido é: '{textoinvertido}'")

