import sys
import io

def search(string, type, path):
    if type == 'arquivo':
        search_file(string, path)

    elif type == 'pasta':
        search_folder(string, path)

    else:
        sys.exit('Tipo de busca não informado. Utilize "arquivo" ou "pasta" como tipos de busca.')

def search_file(string, file_path):
    with io.open(file_path) as file:
        if string in file.readlines():
            print(f'Texto ENCONTRADO no arquivo: {file_path}')

def search_folder(folder_path):
    pass

args = len(sys.argv)

if args > 3:
    search_string = sys.argv[1]
    search_type = sys.argv[2]
    path = sys.argv[3]

    search(search_string, search_type, path)
    
else:
    sys.exit('Requer argumentos: string_de_busca tipo_de_busca(arquivo/pasta) caminho.')

