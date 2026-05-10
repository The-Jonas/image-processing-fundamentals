import cv2
import numpy as np

def filtro_butterwoth_passa_altas(imagem, D0, n):
    M, N = imagem.shape
    H = np.zeros((M, N), dtype=np.float32)
    
    for u in range(M):
        for v in range(N):
            D = np.sqrt((u - M/2) ** 2 + (v - N/2) ** 2)
            if D == 0:
                H[u,v] = 0
            else:
                H[u,v] = 1 / (1 + (D0 / D) ** (2 * n))
                
    return H 

def filtro_notch_rejeita(imagem, pontos_ruido, D0=10, n=2):
    """
    pontos_ruido: lista de tuplas (u,v) com as coordenadas dos spikes de ruido.
    """  
    M, N = imagem.shape
    H = np.ones((M, N), dtype=np.float32)
    
    for u in range(M):
        for v in range(N):
            for (uk, vk) in pontos_ruido:
                # Distância ao ponto de ruído e seu simétrico
                Dk = np.sqrt((u - M/2 - uk)**2 + (v - N/2 - vk)**2)
                D_neg_k = np.sqrt((u - M/2 + uk)**2 + (v - N/2 + vk)**2)
                
                # Filtro Butterworth Notch Reject
                H[u, v] *= (1 / (1 + (D0 / Dk)**n)) * (1 / (1 + (D0 / D_neg_k)**n))
    
    return H
    
def aplicar_filtro_frequencia(imagem, filtro):
    F = np.fft.fft2(imagem)
    Fshift = np.fft.fftshift(F)
    
    Gshift = Fshift * filtro
    
    G = np.fft.ifftshift(Gshift)
    img_back = np.fft.ifft2(G)
    return np.abs(img_back)