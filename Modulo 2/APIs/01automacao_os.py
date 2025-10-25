#Abrir e ler o arquivo
arquivo = open("hello.txt","r", encoding="utf-8") # Abrindo o arquivo
conteudo = arquivo.read() #Lendo o arquivo e armazenando a variavel

print(conteudo) #Apresentando a leitura feita
arquivo.close() #Fechando o arquivo

# Retorna o tamnho do arquivo em bytes
import os 
print(os.path.getsize("hello.txt"),"bytes")

#Listar todos os arquivos e pastas de um diretorio
#nao iremos importar a biblioteca os porqure já fizemos isso nesse script(arquivo)
print(os.listdir(".")) #lista todo o conteudo da pasta atual

#separar diretorios e arquivos 
#nao iremos importar a biblioteca os porqure já fizemos isso nesse script(arquivo)
caminho = "/home/user/documentos/arquivo.txt"
print(os.path.dirname(caminho)) #/home/user/documentos
print(os.path.basename(caminho)) #arquivo.txt