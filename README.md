# 📄➡️🖼️ Conversor PDF para JPG

Sistema em Python para converter arquivos PDF em imagens JPG de forma simples e automática. Ideal para converter grandes volumes de arquivos de uma só vez.

---

## ✨ Funcionalidades

- Converte múltiplos PDFs automaticamente de uma só vez
- Cada página do PDF vira um arquivo JPG separado
- Mostra o progresso em tempo real no terminal
- Exibe relatório final com total convertido, imagens geradas e tempo gasto
- Permite configurar a qualidade e resolução das imagens
- Opção de converter apenas a primeira página de cada PDF

---

## 🖥️ Requisitos

- Python 3.7 ou superior
- Poppler instalado no sistema
- Bibliotecas Python: `pdf2image` e `pillow`

---

## ⚙️ Instalação

### 1. Instalar o Python

Baixe e instale em [python.org](https://www.python.org/downloads/).

> **Windows:** durante a instalação, marque a opção **"Add Python to PATH"**.

---

### 2. Instalar as bibliotecas Python

Abra o terminal e rode:

```bash
pip install pdf2image pillow
```

---

### 3. Instalar o Poppler

O Poppler é uma ferramenta externa obrigatória para a leitura dos PDFs.

**Windows:**
1. Baixe a versão mais recente em: https://github.com/oschwartz10612/poppler-windows/releases
2. Extraia o arquivo ZIP em um local fixo, por exemplo `C:\poppler`
3. Adicione o caminho `C:\poppler\Library\bin` ao PATH do sistema:
   - Pressione `Win + S` e pesquise por **Variáveis de ambiente**
   - Clique em **Editar as variáveis de ambiente do sistema**
   - Clique em **Variáveis de Ambiente...**
   - Em **Variáveis do sistema**, selecione **Path** e clique em **Editar**
   - Clique em **Novo** e cole: `C:\poppler\Library\bin`
   - Clique **OK** em todas as janelas
4. **Feche e abra um novo terminal** para as alterações surtirem efeito

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install poppler-utils
```

**Mac:**
```bash
brew install poppler
```

---

### 4. Verificar se o Poppler foi instalado corretamente

Abra um novo terminal e rode:

```bash
pdftoppm -v
```

Se aparecer um número de versão, está tudo certo. Se aparecer erro, revise o passo 3.

---

## 📁 Organização das pastas

Crie uma estrutura como esta antes de rodar o script:

```
conversao/
├── pdf_para_jpg.py   ← o script principal
├── pdfs/             ← coloque aqui todos os seus PDFs
└── jpgs/             ← os JPGs serão salvos aqui (criada automaticamente)
```

---

## 🚀 Como usar

Abra o terminal na pasta onde está o script e execute:

```bash
# Usando as pastas padrão (./pdfs e ./jpgs)
python pdf_para_jpg.py

# Especificando as pastas manualmente
python pdf_para_jpg.py ./pdfs ./jpgs

# Usando caminhos absolutos (Windows)
python pdf_para_jpg.py C:\conversao\pdfs C:\conversao\jpgs
```

---

## 📊 Exemplo de saída no terminal

```
============================================================
  Conversor PDF → JPG
============================================================
  📂 Entrada  : ./pdfs
  📂 Saída    : ./jpgs
  📄 PDFs     : 100 arquivo(s)
  🖼️  DPI      : 200
  ✨ Qualidade: 90%
  📑 Páginas  : Todas
============================================================

[  1/100] 🔄 relatorio.pdf       ✅  (3 páginas)
[  2/100] 🔄 contrato.pdf        ✅  (1 página)
[  3/100] 🔄 apresentacao.pdf    ✅  (12 páginas)
...
[100/100] 🔄 documento100.pdf    ✅  (2 páginas)

============================================================
  ✅ Convertidos : 100/100 PDFs
  🖼️  Imagens     : 215 JPG(s) gerado(s)
  ⏱️  Tempo total : 87.4s
============================================================

  📁 Imagens salvas em: C:\conversao\jpgs
```

---

## 🔧 Configurações

Abra o arquivo `pdf_para_jpg.py` em qualquer editor de texto e localize a seção de configurações no final do arquivo. Você pode ajustar as seguintes opções:

| Opção | Descrição | Valores disponíveis |
|---|---|---|
| `PASTA_ENTRADA` | Pasta com os PDFs | Qualquer caminho válido |
| `PASTA_SAIDA` | Pasta onde os JPGs serão salvos | Qualquer caminho válido |
| `DPI` | Resolução das imagens geradas | `72` baixa · `150` média · `200` alta · `300` profissional |
| `QUALIDADE` | Nível de compressão do JPG | `70` menor arquivo · `90` padrão · `95` máxima qualidade |
| `APENAS_PRIMEIRA_PAGINA` | Converte só a capa de cada PDF | `True` ou `False` |

---

## 🗂️ Como os arquivos são nomeados

O nome dos JPGs gerados é baseado no nome original do PDF:

| Situação | Nome gerado |
|---|---|
| PDF com 1 página | `relatorio.jpg` |
| PDF com várias páginas | `relatorio_pag001.jpg`, `relatorio_pag002.jpg`, ... |

---

## ❓ Problemas comuns

**`Is poppler installed and in PATH?`**
O Poppler não está instalado ou não foi adicionado ao PATH. Siga o passo 3 da instalação com atenção e abra um novo terminal após configurar.

**`pdftoppm não é reconhecido como comando`**
O PATH não foi configurado corretamente no Windows. Verifique se o caminho adicionado contém a pasta `bin` do Poppler e reinicie o terminal.

**`pip não é reconhecido como comando`**
O Python não foi adicionado ao PATH durante a instalação. Reinstale o Python marcando a opção **"Add Python to PATH"**.

**Imagens com baixa qualidade**
Aumente o valor de `DPI` no script. Para documentos que serão impressos, use `300`.

---

## 📋 Resumo rápido

```bash
# 1. Instalar dependências
pip install pdf2image pillow

# 2. Instalar Poppler (Linux)
sudo apt-get install poppler-utils

# 3. Rodar o script
python pdf_para_jpg.py ./pdfs ./jpgs
```

---

> Desenvolvido com Python • `pdf2image` • `Pillow` • `Poppler`
