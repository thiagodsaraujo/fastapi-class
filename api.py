from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


# Create FastAPI instance
app = FastAPI()

# Pydantic Model - Definição do modelo de dados
# Explicação: https://fastapi.tiangolo.com/tutorial/body/
class Jogador(BaseModel):
    nome: str
    idade: int
    time: str

# Precisa de um BaseModel para funcionar a atualização e criação de jogadores
class JogadorUpdate(BaseModel):
    # Pode ser que queiramos atualizar apenas um campo, por isso todos são opcionais
    nome: Optional[str] = None
    idade: Optional[int] = None
    time: Optional[str] = None

jogadores = {
    1: {
        'nome' : 'Fulano',
        'idade' : 25,
        'time' : 'Time A'
    },
    2: {
        'nome': 'Ciclano',
        'idade': 30,
        'time': 'Time B'
    },
    3: {
        'nome': 'Beltrano',
        'idade': 22,
        'time': 'Time C'
    }
}

# Define a root endpoint, rota principal
@app.get("/")
def inicio():
    return jogadores

@app.get("/jogadores")
def retorno_jogadores():
    print("rota executada")
    return jogadores


@app.get("/jogador/{id_jogador}")
def retorno_jogador(id_jogador: int):
    return jogadores[id_jogador]

# Via query - recuperar jogador pelo time
@app.get("/jogador/")
def retorno_jogador_time(time: str):
    for jogador_id in jogadores:
        if jogadores[jogador_id]["time"] == time:
            return jogadores[jogador_id]
    return {"mensagem": "Nenhum jogador encontrado para o time especificado."}

@app.post("/cadastro/jogador/{jogador_id}")
def criar_jogador(jogador_id: int, jogador: Jogador):
    if jogador_id in jogadores:
        return {"mensagem": "Jogador já existe."}
    # Lista de Jogadores já existe acima
    jogadores[jogador_id] = jogador
    # Retorna o jogador criado na posição jogador_id
    return jogadores[jogador_id]

@app.put("/atualizar/jogador/{jogador_id}")
def atualizar_jogador(jogador_id: int, jogador: JogadorUpdate):
    """
    Atualiza os dados de um jogador existente.

    Parâmetros:
    jogador_id (int): ID do jogador a ser atualizado (passado na URL).
    jogador (JogadorUpdate): Dados do jogador a serem atualizados (passados no corpo da requisição).

    Retorna:
    dict: Dados atualizados do jogador ou mensagem de erro caso o jogador não seja encontrado.
    """
    # Verifica se o jogador existe no dicionário
    if jogador_id not in jogadores:
        return {"Erro" : "Jogador não encontrado."}
    # Atualiza o nome se fornecido
    if jogador.nome != None:
        jogadores[jogador_id]['nome'] = jogador.nome
    # Atualiza a idade se fornecida
    if jogador.idade != None:
        jogadores[jogador_id]['idade'] = jogador.idade
    # Atualiza o time se fornecido
    if jogador.time != None:
        jogadores[jogador_id]['time'] = jogador.time
    # Retorna os dados atualizados do jogador
    return jogadores[jogador_id]


@app.delete("/deletar/jogador/{jogador_id}")
def deletar_jogador(jogador_id: int):
    if jogador_id not in jogadores:
        return {"Erro": "Jogador não encontrado."}
    del jogadores[jogador_id]
    return {"Success": "Jogador deletado com sucesso."}




# Path Parameters - Explicação: https://fastapi.tiangolo.com/tutorial/path-params/
# Query Parameters - Explicação: https://fastapi.tiangolo.com/tutorial/query-params/
# Request Body - Explicação: https://fastapi.tiangolo.com/tutorial/body/
# Extração de dados do corpo da requisição
# Usando Pydantic - Explicação: https://fastapi.tiangolo.com/tutorial/body/
# Usando dataclasses - Explicação: https://fastapi.tiangolo.com/tutorial/body/dataclasses/
# Usando listas - Explicação: https://fastapi.tiangolo.com/tutorial/body/multiple-models/
# Usando listas de modelos - Explicação: https://fastapi.tiangolo.com/tutorial/body/multiple-models/
# Usando listas de modelos - Explicação: https://fastapi.tiangolo.com/tutorial/body/nested-model
