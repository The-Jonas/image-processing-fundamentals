import os 
import cv2
import numpy as np
from src.question3 import *

def testar_questao3():
    nome_foto = 'assets/moire.tif'
    output_path = "output/q3_results/"
    if not os.path.exists(output_path): os.makedirs(output_path)
    
    img = cv2.imread(nome_foto, 0)
    
    pontos = [
    (38, 30),   # Ponto superior direito
    (-38, -30), # Simétrico (inferior esquerdo)
    (42, -32),  # Ponto inferior direito
    (-42, 32)   # Simétrico (superior esquerdo)
    ]
    
    # Aplicar Notch
    h_notch = filtro_notch_rejeita(img, pontos, D0=10)
    img_limpa = aplicar_filtro_frequencia(img, h_notch)
    img_limpa = cv2.normalize(img_limpa, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    
    # Aplicar Butterworth Passa-Altas para aguçar o que restou
    h_bw = filtro_butterwoth_passa_altas(img_limpa, D0 = 30, n = 2)
    detalhes = aplicar_filtro_frequencia(img_limpa, h_bw)
    detalhes_norm = cv2.normalize(detalhes, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    
    # Salvar
    cv2.imwrite(os.path.join(output_path, "3_1_noth_limpa.jpg"), img_limpa)
    cv2.imwrite(os.path.join(output_path, "3_2_butterworth_detalhes.jpg"), detalhes_norm)
    print("Questão 3 processada!")
    
if __name__ == "__main__":
    testar_questao3()