
#### Processo de Subamostragem ####

#1) Nessa primeira parte, não se pode utilizar nenhuma função pronta, além da função de ler e escrever uma imagem

import cv2              # Para ler e escrever a imagem (somente cv2.imread() e cv2.imwrite())
import numpy as np      # Para tratar a imagem como uma matriz e assim conseguir manipular os pixels da imagem.

#1.1) Uma função que deve retirar metade das linhas da imagem de forma intercalada

def retirar_metade_linhas(imagem):
    # imagem[inicio:fim:passo]
    # Pega somente as linhas de 2 em 2, e o segundo argumento está setado como "faça pra todas as colunas"
    imagem_reduzida = imagem [::2, :]
    return imagem_reduzida
 
#1.2) Uma função que deve retirar metade das colunas da imagem de forma intercalada

def retirar_metade_colunas(imagem):
    # Mesma coisa, só que invertido, já que é pra coluna agora...
    imagem_reduzida = imagem [:, ::2]
    return imagem_reduzida 

#1.3) Uma função que deve chamar os anteriores (1.1 e 1.2) e fazer a imagem ficar com um quarto da quantidade de pixels 

def retirar_metade_colunas_e_linhas(imagem):
    # Simplesmente chamar as duas funções para retirar as linhas e colunas
    # Em uma matriz não importa a ordem, se retirar as linhas ou colunas primeiro, vai resultar no mesmo
    imagem_um_quarto = retirar_metade_colunas(imagem)
    imagem_um_quarto = retirar_metade_linhas(imagem_um_quarto)
    return imagem_um_quarto

#1.4) Duplicar as linhas de uma imagem, criando uma linha que cada pixel seja a media do
# pixel de cima e de baixo (caso não tenha linha em baixo, só copiar a de cima)

def duplicar_linhas(imagem):
    altura, largura = imagem.shape
    # Criamos a matriz com o dobro da altura
    nova_img = np.zeros((altura * 2, largura), dtype=np.uint8)

    for i in range(altura):
        # As linhas que já tinhamos vão ocupar espaços pares na matriz
        nova_img[2*i] = imagem[i]
            
        # Agora preenchemos a linha impár
        # E por isso o índice sempre vai ser (2*i + 1)
        
        if i < altura - 1:
            # Se não for a última linha, calculamos a média
            # OBS: Convertemos pra uint16 pra soma não passar de 255
            cima = imagem[i].astype(np.uint16)
            baixo = imagem[i+1].astype(np.uint16)
            media = (cima + baixo) // 2
            
            nova_img[2*i + 1] = media.astype(np.uint8)
        else:
            # Se não tem linha em baixo, só copia a de cima
            nova_img[2*i + 1] = imagem[i]
            
    return nova_img  

#1.5) Duplicar as colunas de uma imagem - similar a 1.4

def duplicar_colunas(imagem):
    altura, largura = imagem.shape
    # Agora vai ter dobro de largura
    nova_img = np.zeros((altura, largura * 2), dtype=np.uint8)
    
    for i in range(largura):
        # Como agora se trata de colunas, usamos [:, 2*i], na função das linhas omitimos as colunas
        nova_img[:, 2*i] = imagem[:, i]
            
        if i < largura - 1:
            esquerda = imagem[:, i].astype(np.uint16)
            direita = imagem[:, i+1].astype(np.uint16)
            media = (esquerda + direita) // 2
            
            nova_img[:, 2*i + 1] = media.astype(np.uint8)
        else:
            nova_img[:, 2*i + 1] = imagem[:, i]
            
    return nova_img

#1.6) Uma função que aumente o tamanho da imagem usando 1.4 e 1.5    

def aumentar_imagem(imagem):
    # Primeiro dobramos as linhas
    img_maior = duplicar_linhas(imagem)
    # Depois dobramos as colunas do resultado anterior
    img_maior = duplicar_colunas(img_maior)
    
    return img_maior

#1.7 e 1.8 são questões para fins de teste e relátorio 
            
            
            
        
