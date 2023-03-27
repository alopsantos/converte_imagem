from PIL import Image
import os

url = input("Informe o caminho das imagens: ")

arquivos = os.listdir(url)
extensoes_in = input("Infome a extensao das imagens: ")  # .png
extensoes_out = input("Infome a extensao para qual quer converter: ")  # .bmp
# file_in = ""
# img = Image.open(file_in)

# file_out = ""
# img.save(file_out)

for i in arquivos:
    if extensoes_in == []:
        print(i)

    else:
        extensao = i.split('.')[-1]
        if extensao in extensoes_in:
            file_in = (url+i)
            img = Image.open(file_in)
            file_out = url + i.split('.')[0]+extensoes_out
            img.save(file_out)


# print(pasta)
