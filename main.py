import sys

def search(string, type, path):
    if type == 'arquivo':
        search_file(path)

    elif type == 'pasta':
        search_folder(path)

    else:
        sys.exit('Tipo de busca não informado. Utilize "arquivo" ou "pasta" como tipos de busca.')

def search_file(file_path):
    pass

def search_folder(folder_path):
    pass

args = len(sys.argv)

if args > 3:
    search_string = sys.argv[1]
    search_type = sys.argv[2]
    path = sys.argv[3]
else:
    sys.exit('Requer argumentos: string_de_busca tipo_de_busca(arquivo/pasta) caminho.')

