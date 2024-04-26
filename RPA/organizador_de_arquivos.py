import os
import shutil

# Retorna o diretório atual
path = os.getcwd()

# Lista todos arquivos no diretório
files = os.listdir(path)

# Define as extensões e suas respectivas pastas
extensions = {
    "pdf": "PDF",
    "doc": "Word",
    "docx": "Word",
    "exe": "Programas",
    "msi": "Programas",
    "xls": "Excel",
    "xlsx": "Excel",
    "csv": "Excel",
    "ppt": "PowerPoint",
    "pptx": "PowerPoint",
    "jpg": "Imagens",
    "jpeg": "Imagens",
    "png": "Imagens",
    "txt": "Word",
    "zip": "Compactados",
    "iso": "Compactados",
    "rar": "Compactados"
}

# Criando as pastas
for folder in extensions.values():
    if not os.path.exists(path + "/" + folder):
        os.makedirs(path + "/" + folder)

# Movendo os arquivos
for file in files:
    name, ext = os.path.splitext(file)
    ext = ext[1:] # remove o ponto (.)
    if ext in extensions:
        shutil.move(path + "/" + file, path + "/" + extensions[ext] + "/" + file)
