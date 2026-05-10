# 🖼️ Image Processing Fundamentals

**Sobre o Projeto**

Este projeto foi desenvolvido para a disciplina de **Processamento Digital de Imagens (PDI) da Universidade de Brasília (UnB)** e tem como objetivo explorar e implementar técnicas clássicas de manipulação de imagens, contrastando operações no **domínio espacial** e no **domínio da frequência**. 

O foco é o entendimento matemático e algorítmico por trás de filtros, redimensionamento matricial e transformadas de Fourier, avaliando o impacto dessas operações na fidelidade visual e na qualidade das imagens.

🚀 **Exemplos de Aplicação**

* *Redimensionamento de imagens (Subamostragem e Superamostragem) operando puramente matrizes, sem uso de bibliotecas de interpolação.*
* *Realce de bordas (Aguçamento) utilizando o Filtro Laplaciano Espacial.*
* *Extração de contornos utilizando Filtros Passa-Altas na Frequência (Ideal e Gaussiano).*
* *Restauração cirúrgica de imagens corrompidas por ruído periódico (Padrão Moire) utilizando Filtro Rejeita-Notch de Butterworth.*

---

## 📁 Estrutura do Projeto

```text
IMAGE-PROCESSING-FUNDAMENTALS/
│
├── .venv/                   # Ambiente virtual Python
├── assets/                  # Imagens originais utilizadas nos testes
│   ├── foto.jpeg            # Imagem base para testes espaciais (Q1)
│   ├── Image1.pgm           # Imagem para aguçamento de bordas (Q2)
│   └── moire.tif            # Imagem com ruído periódico para restauração (Q3)
│
├── output/                  # Resultados gerados pelos scripts
│   ├── q1_results/
│   ├── q2_results/
│   └── q3_results/
│
├── src/                     # Código-fonte principal com as lógicas dos filtros
│   ├── question1.py         # Algoritmos de redução e ampliação matricial
│   ├── question2.py         # Filtros Laplaciano, Ideal e Gaussiano (Alta-Frequência)
│   └── question3.py         # Transformada de Fourier e Filtro Notch
│
├── tests/                   # Scripts de testes unitários para cada questão
│   ├── teste_q1.py
│   ├── teste_q2.py
│   └── teste_q3.py
│
├── notebook.ipynb           # Notebook interativo principal de execução e análise
├── requirements.txt         # Lista de dependências do projeto
├── Análise_Comparat...pdf   # Relatório Técnico Final (Relatório IEEE)
├── trab1ipi.pdf             # Especificações originais do trabalho
└── README.md                # Este arquivo
```
### 📌 Algoritmos e Conceitos Aplicados:

**Domínio Espacial:** Dizimação espacial, Interpolação Linear, Filtro Gaussiano (suavização) e Operador Laplaciano (derivação de 2ª ordem).

**Domínio da Frequência:** Transformada Rápida de Fourier (FFT), Espectro de Magnitude (escala logarítmica).

**Filtros Espectrais:** Passa-Altas Ideal, Passa-Altas Gaussiano, Rejeita-Notch de Butterworth.

**Tratamento de Matrizes:** Técnicas de expansão de borda (Padding) para evitar o fenômeno de wrap-around (convolução circular).

## ⚙️ Como rodar o projeto
Todo o código foi desenhado para ser autoexplicativo e fácil de executar. A forma recomendada de explorar o projeto é através do Jupyter Notebook, onde todos os passos, imagens e filtros estão comentados e visíveis.

#### *1. Requisitos:*

Python 3.10+  
OpenCV (cv2)  
NumPy  
Matplotlib  
Jupyter Notebook

#### *2. Instalação (Usando Ambiente Virtual):*  
Clone o repositório e acesse a pasta do projeto  
Crie e ative o ambiente virtual (venv):
```bash
# No Windows:
python -m venv .venv
.venv\Scripts\activate

# No Linux/Mac:
python3 -m venv .venv
source .venv/bin/activate
```
Instale as dependências:
```bash
pip install -r requirements.txt
```

#### *3. Execução:*

Para rodar todo o projeto e visualizar as imagens passo a passo, inicie o Jupyter Notebook:
```bash
jupyter notebook
```
**Dica:** Abra o arquivo notebook.ipynb na interface do navegador ou na sua IDE. O notebook contém células sequenciais que importam as funções da pasta src/, processam as imagens da pasta assets/ e plotam os comparativos diretamente na tela de forma didática.

*Opcional:* Você também pode rodar os testes individualmente via terminal usando o módulo do python. Exemplo:
```bash
python -m tests.teste_q1
```

## 🛠️ Funcionalidades e Estrutura do Código
As principais funções estão divididas em módulos na pasta src/:

📌 1. `question1.py` (Redimensionamento Nativo)  
- Lida com a amostragem de imagens puramente através de loops matriciais (fatiamento NumPy). Demonstra a perda de alta frequência (aliasing) e o efeito passa-baixas da interpolação.

📌 2. `question2.py` (Detecção de Bordas / Aguçamento)  
- Compara a eficácia da derivada de segunda ordem (Laplaciano com kernels variáveis) contra o corte de baixas frequências na FFT. Demonstra na prática os artefatos de ringing causados por filtros ideais.

📌 3. `question3.py` (Filtro Rejeita-Notch e Moire)  
- Mapeia spikes de alta energia no espectro de Fourier e aplica 4 pares de filtros de Butterworth para apagar interferências senoidais sem destruir os detalhes vitais da fotografia.
