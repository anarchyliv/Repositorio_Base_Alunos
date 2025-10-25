import requests
from bs4 import BeautifulSoup

# URL do site de notícias (exemplo com G1)
URL = "https://g1.globo.com/"

def coletar_manchetes(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança erro para status diferentes de 200
    except requests.RequestException as erro:
        print(f"Erro ao acessar a página: {erro}")
        return []

    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # Seleciona as manchetes — tag e classe específicas do G1
    manchetes = soup.find_all('a', class_='feed-post-link')

    lista_manchetes = [manchete.get_text(strip=True) for manchete in manchetes]
    return lista_manchetes

def exibir_manchetes(manchetes):
    print("Manchetes do G1:")
    for i, titulo in enumerate(manchetes, 1):
        print(f"{i}. {titulo}")

if __name__ == "__main__":
    manchetes = coletar_manchetes(URL)
    if manchetes:
        exibir_manchetes(manchetes)
    else:
        print("Nenhuma manchete encontrada.")
