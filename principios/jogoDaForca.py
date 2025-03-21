import requests
import random

# URL da API 
url = "https://raw.githubusercontent.com/hexapode/an-array-of-portuguese-words/refs/heads/master/words.json"


def load_words():
    try:
        resposta = requests.get(URL)
        resposta.raise_for_status()  # Garante que não houve erro na requisição
        return resposta.json()  # Retorna a lista de palavras
    except requests.RequestException as e:
        print(f"Erro ao carregar palavra: {e}")
        return[] #pesquisar mais sobre essa lista vazia
    
def  computer(words):
    return random.choice(words).lower()

def game():
    word = load_words()
    
    