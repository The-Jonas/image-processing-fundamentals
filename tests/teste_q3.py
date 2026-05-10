import os 
import cv2
import numpy as np
from src.question3 import *

def testar_questao3():
    nome_foto = 'assets/moire.tif'
    output_path = "output/q3_results/"
    if not os.path.exists(output_path): os.makedirs(output_path)
    
    img = cv2.imread(nome_foto, 0)
    M, N = img.shape
    
    # 4 pares de pontos (8 coordenadas) para cumprir o item 3.2 do roteiro
    pontos = [
        (38, 30), (-38, -30),   # Par 1
        (42, -32), (-42, 32),   # Par 2
        (76, 60), (-76, -60),   # Par 3 (Harmônico)
        (84, -64), (-84, 64)    # Par 4 (Harmônico)
    ]
    
    # Salvar Original (Item 3.1)
    cv2.imwrite(os.path.join(output_path, "3_1_imagem_original.jpg"), img)

    print("-> Aplicando Notch SEM padding...")
    # Usamos n=4 porque o roteiro exige explicitamente
    h_notch_sem = filtro_notch_rejeita(img, pontos, D0=10, n=4)
    img_limpa_sem = aplicar_filtro_frequencia(img, h_notch_sem)
    img_limpa_sem_norm = cv2.normalize(img_limpa_sem, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    
    print("-> Extraindo detalhes com Butterworth...")
    # A sua função clássica para os detalhes do carro
    h_bw = filtro_butterwoth_passa_altas(img_limpa_sem, D0=30, n=4)
    detalhes = aplicar_filtro_frequencia(img_limpa_sem, h_bw)
    detalhes_norm = cv2.normalize(detalhes, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    print("-> Aplicando Notch COM padding ...")
    # Lógica de padding isolada no teste para preservar as suas funções do src/
    img_padded = np.zeros((2 * M, 2 * N), dtype=np.float32)
    img_padded[0:M, 0:N] = img
    pontos_padded = [(u * 2, v * 2) for u, v in pontos]
    
    h_notch_com = filtro_notch_rejeita(img_padded, pontos_padded, D0=20, n=4)
    img_limpa_com = aplicar_filtro_frequencia(img_padded, h_notch_com)
    img_limpa_com_cortada = img_limpa_com[0:M, 0:N] # Cortamos de volta ao tamanho original
    img_limpa_com_norm = cv2.normalize(img_limpa_com_cortada, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    
    # Salvar resultados
    cv2.imwrite(os.path.join(output_path, "3_2_notch_sem_padding.jpg"), img_limpa_sem_norm)
    cv2.imwrite(os.path.join(output_path, "3_2_notch_com_padding.jpg"), img_limpa_com_norm)
    cv2.imwrite(os.path.join(output_path, "3_3_butterworth_detalhes.jpg"), detalhes_norm)
    
    print("Questão 3 processada!")
    
if __name__ == "__main__":
    testar_questao3()