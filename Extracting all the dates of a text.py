#Extracting all the dates of a text
import re

file = r"C:\Users\Cash\Documents\pruebas_python\proyectos\re\cuento con acentos.txt"

with open(file, "r", encoding='utf-8') as f:
    value = f.read()
#     x = value.replace("Ã±", "ñ")
    f.close()
#     print(value)
    
    
value


def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))
        
print(re.findall("[0-9]{1,2}\sde*\s[a-z]*", value))
print(re.findall("[0-9]{1,2}/[0-9]{1,2}/[0-9]{1,2}", value))

