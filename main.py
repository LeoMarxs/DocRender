#!/usr/bin/env python3
"""
Conversor de PDF para JPG
Converte todos os arquivos PDF de uma pasta em imagens JPG.
Cada página do PDF gera um arquivo JPG separado.

Dependências:
    pip install pdf2image pillow
    
    Linux também precisa do poppler:
    sudo apt-get install poppler-utils  
"""

import os
import sys
import time
from pathlib import Path

try:
    from pdf2image import convert_from_path
    from PIL import Image
except ImportError:
    print("❌ Dependências não encontradas. Instale com:")
    print("   pip install pdf2image pillow")
    sys.exit(1)


def converter_pdf_para_jpg(
    pasta_entrada: str,
    pasta_saida: str,
    dpi: int = 200,
    qualidade_jpg: int = 90,
    apenas_primeira_pagina: bool = False
):
    """
    Converte todos os PDFs de uma pasta em arquivos JPG.

    Args:
        pasta_entrada: Pasta com os arquivos PDF
        pasta_saida: Pasta onde os JPGs serão salvos
        dpi: Resolução das imagens (maior = melhor qualidade, maior arquivo)
        qualidade_jpg: Qualidade do JPG de 1-95 (padrão 90)
        apenas_primeira_pagina: Se True, converte apenas a primeira página de cada PDF
    """
    pasta_entrada = Path(pasta_entrada)
    pasta_saida = Path(pasta_saida)

    # Validações
    if not pasta_entrada.exists():
        print(f"❌ Pasta de entrada não encontrada: {pasta_entrada}")
        sys.exit(1)

    # Cria pasta de saída se não existir
    pasta_saida.mkdir(parents=True, exist_ok=True)

    # Lista todos os PDFs
    arquivos_pdf = sorted(pasta_entrada.glob("*.pdf")) + sorted(pasta_entrada.glob("*.PDF"))
    
    if not arquivos_pdf:
        print(f"⚠️  Nenhum arquivo PDF encontrado em: {pasta_entrada}")
        return

    total = len(arquivos_pdf)
    print(f"\n{'='*60}")
    print(f"  Conversor PDF → JPG")
    print(f"{'='*60}")
    print(f"  📂 Entrada  : {pasta_entrada}")
    print(f"  📂 Saída    : {pasta_saida}")
    print(f"  📄 PDFs     : {total} arquivo(s)")
    print(f"  🖼️  DPI      : {dpi}")
    print(f"  ✨ Qualidade: {qualidade_jpg}%")
    print(f"  📑 Páginas  : {'Apenas a 1ª' if apenas_primeira_pagina else 'Todas'}")
    print(f"{'='*60}\n")

    sucessos = 0
    erros = []
    total_imagens = 0
    tempo_inicio = time.time()

    for i, arquivo_pdf in enumerate(arquivos_pdf, 1):
        nome_base = arquivo_pdf.stem
        print(f"[{i:>3}/{total}] 🔄 {arquivo_pdf.name}", end="", flush=True)

        try:
            # Define quais páginas converter
            paginas = 1 if apenas_primeira_pagina else None

            # Converte PDF para lista de imagens
            imagens = convert_from_path(
                str(arquivo_pdf),
                dpi=dpi,
                first_page=1,
                last_page=paginas
            )

            num_paginas = len(imagens)

            # Salva cada página como JPG
            for num_pag, imagem in enumerate(imagens, 1):
                # Define nome do arquivo de saída
                if num_paginas == 1:
                    nome_saida = f"{nome_base}.jpg"
                else:
                    nome_saida = f"{nome_base}_pag{num_pag:03d}.jpg"

                caminho_saida = pasta_saida / nome_saida

                # Converte para RGB (necessário para salvar como JPG)
                if imagem.mode != "RGB":
                    imagem = imagem.convert("RGB")

                # Salva com a qualidade definida
                imagem.save(str(caminho_saida), "JPEG", quality=qualidade_jpg, optimize=True)
                total_imagens += 1

            print(f" ✅  ({num_paginas} página{'s' if num_paginas > 1 else ''})")
            sucessos += 1

        except Exception as e:
            print(f" ❌ ERRO: {e}")
            erros.append((arquivo_pdf.name, str(e)))

    # Relatório final
    tempo_total = time.time() - tempo_inicio
    print(f"\n{'='*60}")
    print(f"  ✅ Convertidos : {sucessos}/{total} PDFs")
    print(f"  🖼️  Imagens     : {total_imagens} JPG(s) gerado(s)")
    print(f"  ⏱️  Tempo total : {tempo_total:.1f}s")
    if erros:
        print(f"  ❌ Erros       : {len(erros)}")
        for nome, erro in erros:
            print(f"     • {nome}: {erro}")
    print(f"{'='*60}\n")

    if sucessos > 0:
        print(f"  📁 Imagens salvas em: {pasta_saida.resolve()}\n")


# ─────────────────────────────────────────────
#  CONFIGURAÇÕES — edite aqui conforme necessário
# ─────────────────────────────────────────────
if __name__ == "__main__":

    # 📂 Pasta onde estão seus arquivos PDF
    PASTA_ENTRADA = "./pdfs"

    # 📂 Pasta onde os JPGs serão salvos
    PASTA_SAIDA = "./jpgs"

    # 🖼️  Resolução (DPI):
    #   72  = baixa qualidade (menor arquivo)
    #   150 = boa qualidade (equilibrado)
    #   200 = alta qualidade (recomendado)
    #   300 = impressão profissional (arquivos grandes)
    DPI = 200

    # ✨ Qualidade do JPG (1-95):
    #   70 = comprimido (menor arquivo)
    #   85 = equilibrado
    #   90 = alta qualidade (recomendado)
    #   95 = máxima qualidade
    QUALIDADE = 90

    # 📑 True  = salva apenas a primeira página de cada PDF
    #    False = salva TODAS as páginas
    APENAS_PRIMEIRA_PAGINA = False

    # Permite passar a pasta como argumento na linha de comando:
    # python pdf_para_jpg.py ./meus_pdfs ./minhas_imagens
    if len(sys.argv) >= 3:
        PASTA_ENTRADA = sys.argv[1]
        PASTA_SAIDA = sys.argv[2]
    elif len(sys.argv) == 2:
        PASTA_ENTRADA = sys.argv[1]

    converter_pdf_para_jpg(
        pasta_entrada=PASTA_ENTRADA,
        pasta_saida=PASTA_SAIDA,
        dpi=DPI,
        qualidade_jpg=QUALIDADE,
        apenas_primeira_pagina=APENAS_PRIMEIRA_PAGINA
    )