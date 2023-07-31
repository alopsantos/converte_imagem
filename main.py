from PIL import Image
import os

url = input("Informe o caminho completo da pasta onde salvou as imagens: ")

arquivos = os.listdir(url)
print("Informe a extensão das imagens na pasta, não precisa informar o ponto")
extensoes_in = input(
    "exemplo (jpg, webp, png, bmp): ")  # .png
print("Informe a extensão que deseja transformar, não precisa informar o ponto")
extensoes_out = input(
    "Exemplo (jpg, webp, png, bmp): ")  # .bmp

for i in arquivos:

    if extensoes_in == []:
        print(i)

    else:
        extensao = i.split('.')[-1]
        if extensao in extensoes_in:
            file_in = (url+'/'+i)
            img = Image.open(file_in)
            file_out = url + '/' + i.split('.')[0]+'.'+extensoes_out
            img.save(file_out)
