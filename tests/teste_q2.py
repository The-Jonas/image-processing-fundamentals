import os
import cv2
from src.question2 import * 

def testar_questao2_parteA():
    nome_foto = 'assets/Image1.pgm' 
    output_path = "output/q2_results/"
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 1. Lê a imagem
    img = cv2.imread(nome_foto, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Erro: Não consegui achar a imagem em '{nome_foto}'.")
        return

    print("Processando Parte A (Domínio Espacial)...")

    # --- 2.1 Laplaciano Direto (Sem suavização) ---
    agucada_direto, bordas_direto = agucar_laplaciano(img, sigma=None)
    
    # --- 2.2 Laplaciano com Gaussiano (Sigma = 0.5) ---
    agucada_g05, _ = agucar_laplaciano(img, sigma=0.5)

    # --- 2.3 Laplaciano com Gaussiano (Sigma = 1.0) ---
    agucada_g10, _ = agucar_laplaciano(img, sigma=1.0)

    # 3. Salvar Resultados
    cv2.imwrite(os.path.join(output_path, "2_1_agucada_direto.jpg"), agucada_direto)
    cv2.imwrite(os.path.join(output_path, "2_2_agucada_sigma05.jpg"), agucada_g05)
    cv2.imwrite(os.path.join(output_path, "2_3_agucada_sigma10.jpg"), agucada_g10)
    
    # Bônus: Salvar as bordas puras para ilustrar no relatório
    cv2.imwrite(os.path.join(output_path, "extra_somente_bordas_laplaciano.jpg"), bordas_direto)

    print(f"Imagens salvas na pasta '{output_path}'.")
    
def testar_questao2_parteB():
    nome_foto = 'assets/Image1.pgm'
    output_path = "output/q2_results/"
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
         
    # Leitura da imagem
    img = cv2.imread(nome_foto, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print(f"Erro: Não consegui achar a imagem em '{nome_foto}'.")
        return

    print("Processando Parte B (Domínio da Frequência)...")
    
    # --- Aplica o Laplaciano via FFT ---
    agucada_freq, bordas_freq = laplaciano_frequencia(img)

    # Salvar Resultados
    cv2.imwrite(os.path.join(output_path, "2_B_agucada_frequencia.jpg"), agucada_freq)
    cv2.imwrite(os.path.join(output_path, "extra_bordas_frequencia.jpg"), bordas_freq)

    print(f"Imagens da Parte B salvas na pasta '{output_path}'.")

if __name__ == "__main__":
    testar_questao2_parteA()
    testar_questao2_parteB()