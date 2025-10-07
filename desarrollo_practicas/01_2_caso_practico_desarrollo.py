from langdetect import detect

def descifrado_fuerza_bruta_cesar(text):
    words = text.split()
    flag = 1
    limit = 25

    while flag <= limit:
        phrase = []
        for word in words:
            convination = []
            
            for i in word:
                valor_ascii = ord(i)

                if valor_ascii <= 90 and valor_ascii + flag > 90:
                    faltante = valor_ascii + flag - 90
                    letra = chr(ord('A')-1 + faltante)
                elif valor_ascii <= 122 and valor_ascii + flag > 122:
                    faltante = valor_ascii + flag - 122
                    letra = chr(ord('a')-1 + faltante)
                else:
                    valor_ascii += flag
                    letra = chr(valor_ascii)
                
                convination.append(letra)
                    
            palabra = "".join(convination)
            phrase.append(palabra)
            phrase.append(" ")

        texto_descifrado = "".join(phrase)
        lenguaje = detect(texto_descifrado)
        if lenguaje == "es":
            return texto_descifrado, flag

        flag += 1
    return "", -1

if __name__ == "__main__":
    texto_crifrado = input("Escribe el texto a descifrar: ")
    texto_plano, clave = descifrado_fuerza_bruta_cesar(texto_crifrado)

    if clave == -1:
        print("NO se pudo descifrar el texto.")
    else:
        print(f"El texto plano es: {texto_plano} y su clave es {clave}")