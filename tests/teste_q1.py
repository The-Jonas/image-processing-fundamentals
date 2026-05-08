import cv2
import os
from src.question1 import * 

#1.7 mostre e comente os resultados usando uma imagem sua (do seu rostro)
#monocromatica no relatório, de usar a funcao 1.3.

def testar_monocromatica():
    # 1. Configura os caminhos
    nome_foto = 'assets/foto.jpeg' # Confirme se sua foto está aqui com este nome
    output_path = "output/q1_results/"
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 2. Lê a imagem forçando escala de cinza (matriz 2D)
    img_cinza = cv2.imread(nome_foto, cv2.IMREAD_GRAYSCALE)

    if img_cinza is None:
        print(f"Erro: Não consegui achar a imagem em '{nome_foto}'.")
        return

    print(f"Original carregada com sucesso! Tamanho: {img_cinza.shape}")

    # 3. Processa passando as matrizes
    img_reduzida = retirar_metade_colunas_e_linhas(img_cinza)
    print(f"Tamanho após redução (1.3): {img_reduzida.shape}")

    img_ampliada = aumentar_imagem(img_reduzida)
    print(f"Tamanho após ampliação (1.6): {img_ampliada.shape}")
    
    # Teste Extra: Ampliando a imagem original diretamente
    img_gigante = aumentar_imagem(img_cinza)
    print(f"Tamanho da imagem original gigante: {img_gigante.shape}")
    
    # 4. Salva os resultados
    cv2.imwrite(os.path.join(output_path, "1_3_reduzida.jpg"), img_reduzida)
    cv2.imwrite(os.path.join(output_path, "1_6_reconstruida.jpg"), img_ampliada)
    cv2.imwrite(os.path.join(output_path, "original_ampliada.jpg"), img_gigante)
    print(f"Imagens salvas na pasta '{output_path}'. Confirme visualmente!")
    
####################### ------------------------------ #######################
#1.8 mostre e comente os resultados para uma imagem colorida (fazendo o processo
#para cada canal separado).
    
def testar_colorida():
    nome_foto = 'assets/foto.jpeg'
    output_path = "output/q1_results/"
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 1. Lê a imagem COLORIDA 
    img_color = cv2.imread(nome_foto)

    if img_color is None:
        print(f"Erro: Não consegui achar a imagem em '{nome_foto}'.")
        return

    print(f"Original Colorida carregada! Tamanho: {img_color.shape}")

    # 2. Separa os três canais (Blue, Green, Red)
    b, g, r = cv2.split(img_color)

    # ==========================================
    # TESTE 1.3: Redução (passando canal por canal)
    # ==========================================
    b_reduzido = retirar_metade_colunas_e_linhas(b)
    g_reduzido = retirar_metade_colunas_e_linhas(g)
    r_reduzido = retirar_metade_colunas_e_linhas(r)
    
    # Junta os canais para formar a imagem reduzida colorida
    img_reduzida_colorida = cv2.merge([b_reduzido, g_reduzido, r_reduzido])
    print(f"Tamanho após redução: {img_reduzida_colorida.shape}")

    # ==========================================
    # TESTE 1.6: Ampliação (passando canal por canal)
    # ==========================================
    b_ampliado = aumentar_imagem(b_reduzido)
    g_ampliado = aumentar_imagem(g_reduzido)
    r_ampliado = aumentar_imagem(r_reduzido)
    
    # Junta os canais novamente
    img_ampliada_colorida = cv2.merge([b_ampliado, g_ampliado, r_ampliado])
    print(f"Tamanho após ampliação: {img_ampliada_colorida.shape}")

    # 3. Salva os resultados
    cv2.imwrite(os.path.join(output_path, "1_8_reduzida_colorida.jpg"), img_reduzida_colorida)
    cv2.imwrite(os.path.join(output_path, "1_8_reconstruida_colorida.jpg"), img_ampliada_colorida)
    print(f"Imagens coloridas salvas na pasta '{output_path}'.")

####################### ------------------------------ #######################    

if __name__ == "__main__":
    # Comente o teste antigo e rode apenas o novo, ou rode os dois!
    #testar_monocromatica()
    testar_colorida()