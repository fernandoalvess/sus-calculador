### **Instruções para Uso do Código SUS Score Calculator**
  A System Usability Scale (SUS) é uma escala de usabilidade composta por 10 afirmações, cada uma avaliada em uma escala de 1 (discordo totalmente) a 5 (concordo totalmente). Aqui está um script em Python para calcular a pontuação SUS com base nas respostas de múltiplos participantes. O código recebe as respostas, ajusta os valores conforme a regra da SUS, calcula a pontuação individual e gera a média para todos os participantes.

#### **Requisitos para Executar o Projeto**
- Python **3.7+**  
- **pip** instalado  

#### **Instalação das Dependências**
Para instalar as dependências do projeto, execute o seguinte comando no terminal na raiz do projeto:  

```bash
pip install numpy
```

Caso esteja usando um ambiente virtual, ative-o antes da instalação:  

```bash
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate      # Para Windows
pip install numpy
```

#### **Executando o Projeto**
Para calcular as pontuações SUS, execute o seguinte comando no terminal:  

```bash
python sus_calculo.py
```

#### **Testando com Novos Dados**
Para testar com novos participantes, edite a variável `respostas_exemplo` no arquivo `sus_calculo.py`, inserindo as respostas dos usuários no formato de lista.  
