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
    

def laplaciano_frequencia(imagem):
    # Obtendo dimensões da imagem
    M, N = imagem.shape
    
    # Transformada de Fourier (FFT) e deslocamento do zero para o centro (shift)
    # Usamos np.fft para facilitar a manipulação do expectro
    
    F = np.fft.fft2(imagem)
    Fshift = np.fft.fftshift(F)
    
    # Criar o Filtro Laplaciano no domínio da frequência H(u,v)
    # H(u,v) = -4 * pi^2 * D(u,v)^2, onde D é a distância ao centro
    P, Q = M, N
    H = np.zeros((P, Q), dtype=np.float32)
    
    for u in range(P):
        for v in range(Q):
            # Distância ao centro do espectro (M/2, N/2)
            dist_centro = (u - P/2) ** 2 + (v - Q/2) ** 2
            H[u, v] = -4 * (np.pi**2) * dist_centro

    # Aplicar o filtro: G(u,v) = H(u,v) * F(u,v)
    G = Fshift * H
    
    # Inverter o Shift e aplicar a Transformada Inversa (IFFT)
    G_ishift = np.fft.ifftshift(G)
    img_back = np.fft.ifft2(G_ishift)
    
    # Pegando somente a parte real (ou a magnitude)
    img_laplaciana = np.abs(img_back)
    
    # Aguçamento: Original - Laplaciano
    # Vamos subtrair para realçar
    img_laplaciana_norm = cv2.normalize(img_laplaciana, None, 0, 255, cv2.NORM_MINMAX)
    
    # Resultado final combinado com a original
    imagem_agucada = imagem.astype(np.float32) + img_laplaciana_norm
    imagem_final = np.clip(imagem_agucada, 0, 255).astype(np.uint8)
    
    return imagem_final, img_laplaciana_norm.astype(np.uint8)     
    