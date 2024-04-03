import sys
from PIL import Image
from rembg import remove

def remover_fundo(caminho_entrada, caminho_saida):
    imagem_original = Image.open(caminho_entrada)
    imagem_sem_bg = remove(imagem_original)
    imagem_sem_bg.save(caminho_saida)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python transparencize.py <caminho_entrada> <caminho_saida>")
        sys.exit(1)

    caminho_entrada = sys.argv[1]
    caminho_saida = sys.argv[2]

    remover_fundo(caminho_entrada, caminho_saida)
