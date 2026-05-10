#2) Implementar com funções prontas (Usando Image1.pgm) 

## PARTE A

#2.1 a 2.4) Fazer um programa para realizar o processo de aguçamento (sharpening)
# de imagens, mediante o uso de um Filtro Laplaciano no domínio espacial.
# As entradas do programa devem ser:
# (i) a imagem
# (ii) o tipo de filtro laplaciano

import cv2
import numpy as np

def agucar_laplaciano(imagem, sigma=None):
    """
    Aplica o aguçamento usando filtro Laplaciano (3x3, centro 8).
    Se sigma for passado, aplica suavização Gaussiana antes (Itens 2.2 e 2.3).
    """
    # Se tem sigma, aplica o Gaussiano antes (tamanho do kernel Gaussiano = 3x3)
    if sigma is not None:
        # O (3,3) é o tamanho da janela, e o sigmaX dita a força do desfoque
        img_processada = cv2.GaussianBlur(imagem, (3, 3), sigmaX=sigma)
    else:
        img_processada = imagem.copy()

    # Definir o Kernel Laplaciano (+8 no centro)
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])

    # Aplicar o filtro usando CV_64F (float) para não perder os valores negativos!
    bordas = cv2.filter2D(img_processada, cv2.CV_64F, kernel)

    # Aguçamento: Imagem Original + Bordas
    # Usamos a imagem original crua para somar, assim destacamos os detalhes nela
    imagem_agucada = imagem + bordas

    # Cortar valores fora do limite (0 a 255) e converter de volta para uint8
    imagem_final = np.clip(imagem_agucada, 0, 255).astype(np.uint8)

    return imagem_final, np.clip(bordas, 0, 255).astype(np.uint8) 
    # Retornamos as bordas também para colocar no relatório!
    

def agucar_frequencia(imagem, tipo_filtro = "gaussiano", D0 = 30):
    """
    Realiza o aguçamento do dominio de frequência usando um filtro Passa-Altas.
    tipo_filtro: "ideal" ou "gaussiano"
    D0: Frequência de corte
    """
    
    # Obtendo dimensões da imagem
    M, N = imagem.shape
    
    # FFT e Shift
    F = np.fft.fft2(imagem)
    Fshift = np.fft.fftshift(F)
    
    # Criar o Filtro Passa-Altas
    H = np.zeros((M, N), dtype=np.float32)
    for u in range(M):
        for v in range(N):
            # Distância D(u,v) ao centro
            D = np.sqrt((u - M/2) ** 2 + (v - N/2) ** 2)
            
            if tipo_filtro == "ideal":
                # Filtro Ideal Passa-Altas (Corta a Faca)
                H[u,v] = 0 if D <= D0 else 1
            elif tipo_filtro == "gaussiano":
                # Filtro Gaussiano Passa-Altas (Transição Suave)
                H[u,v] = 1 - np.exp(-(D**2) / (2 * D0**2))

    # Aplicar o filtro e Transformada Inversa
    Gshift = Fshift * H
    img_bordas = np.abs(np.fft.ifft2(np.fft.ifftshift(Gshift)))

    # Aguçamento: Imagem Original + Altas Frequências (Bordas)
    bordas_norm = cv2.normalize(img_bordas, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    
    # Somar com a original evitando estourar o limite de 255
    imagem_agucada = cv2.add(imagem, bordas_norm)
    
    return imagem_agucada, bordas_norm    
    