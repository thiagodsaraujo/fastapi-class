from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

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
    print("rota executada")
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


# Path Parameters - Explicação: https://fastapi.tiangolo.com/tutorial/path-params/
# Query Parameters - Explicação: https://fastapi.tiangolo.com/tutorial/query-params/
# Request Body - Explicação: https://fastapi.tiangolo.com/tutorial/body/
# Extração de dados do corpo da requisição
# Usando Pydantic - Explicação: https://fastapi.tiangolo.com/tutorial/body/
# Usando dataclasses - Explicação: https://fastapi.tiangolo.com/tutorial/body/dataclasses/
# Usando listas - Explicação: https://fastapi.tiangolo.com/tutorial/body/multiple-models/
# Usando listas de modelos - Explicação: https://fastapi.tiangolo.com/tutorial/body/multiple-models/
# Usando listas de modelos - Explicação: https://fastapi.tiangolo.com/tutorial/body/nested-model
