#Author: Isaac Cyrman (20220289)

"""
[Module] Tic-tac-toe bot utilities.
"""
from random import randint
import requests
from urllib.parse import unquote


API_URL = "http://127.0.0.1:8000"


def is_registry_open() -> bool:
    """
    Checks if registry is available via API.
    """
    try:
        url = "{}/registry".format(API_URL)
        res = requests.get(url)

        if res.text == "true":
            return True
        elif res.text == "false":
            return False

    except:
        return False


def register_user(name: str) -> str:
    """
    Registers user in API game.
    """
    url = "{}/register_player/{}".format(API_URL, name)
    res = requests.post(url)
    player_id = res.text[1]
    return player_id


def is_my_turn(player_id: str) -> bool: 
    """
    Checks if it is our turn via API.
    """
    url = "{}/turn/{}".format(API_URL, player_id)
    res = requests.get(url)
    
    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def read_board() -> list:
    """
    Gets game board via API.
    """
    url = "{}/board".format(API_URL)
    res = requests.get(url)
    board_str = res.text
    board = [
        [board_str[1], board_str[2], board_str[3]], 
        [board_str[4], board_str[5], board_str[6]], 
        [board_str[7], board_str[8], board_str[9]]
    ]

    return board


def decide_move(board: list, player_id: str) -> [int, int]:
    """
    Decides next move to make.
    """
    
    # ---------------------------------------------- | ATACAR: DIAGONALES | ---------------------------------------------- 

    # Iniciamos buscando las diagonales: Esto se hace con la finalidad de analizar los diferentes escenarios que existen para completar una linea de tres y tras anaizarlo, proceder a completar dicha linea.
    
    #Si las posiciones [0,0] y [1,1] ya estan llenados por nuestro player ID y la posición [2,2] esta vacia, entonces, retornar la posición [2,2].
    if board[0][0] == player_id and board[1][1] == player_id and board[2][2] == '-':
        
        return [2, 2]
    
    #Si las posiciones [1,1] y [2,2] ya estan llenados por nuestro player ID y la posición [0,0] esta vacia, entonces, retornar la posición [0,0].
    elif board[1][1] == player_id and board[2][2] == player_id and board[0][0] == '-':
        
        return [0, 0]
    
    #Si las posiciones [2,2] y [0,0] ya estan llenados por nuestro player ID y la posición [1,1] esta vacia, entonces, retornar la posición [1,1].
    elif board[2][2] == player_id and board[0][0] == player_id and board[1][1] == '-':
        
        return [1, 1]

    #Si las posiciones [2,0] y [1,1] ya estan llenados por nuestro player ID y la posición [0,2] esta vacia, entonces, retornar la posición [0,2].
    elif board[2][0] == player_id and board[1][1] == player_id and board[0][2] == '-':
        
        return [0, 2]
    
    #Si las posiciones [1,1] y [0,2] ya estan llenados por nuestro player ID y la posición [2,0] esta vacia, entonces, retornar la posición [2,0].
    elif board[1][1] == player_id and board[0][2] == player_id and board[2][0] == '-':
        
        return [2, 0]
    
    #Si las posiciones [0,2] y [2,0] ya estan llenados por nuestro player ID y la posición [1,1] esta vacia, entonces, retornar la posición [1,1].
    elif board[0][2] == player_id and board[2][0] == player_id and board[1][1] == '-':
        
        return [1, 1]

    # ---------------------------------------------- | ATACAR: HORIZONTALES | ---------------------------------------------- 
    
    # Seguidamente, buscaremos las horizontales: Esto se hace con la finalidad de analizar los diferentes escenarios que existen para completar una linea de tres y tras anaizarlo, proceder a completar dicha linea.
    
    #Si las posiciones [0,0] y [0,1] ya estan llenados por nuestro player ID y la posición [0,2] esta vacia, entonces, retornar la posición [0,2].
    elif board[0][0] == player_id and board[0][1] == player_id and board[0][2] == '-':
        return [0, 2]
    
    #Si las posiciones [0,0] y [0,2] ya estan llenados por nuestro player ID y la posición [0,1] esta vacia, entonces, retornar la posición [0,1].
    elif board[0][0] == player_id and board[0][2] == player_id and board[0][1] == '-':
        return [0, 1]
    
    #Si las posiciones [0,2] y [0,1] ya estan llenados por nuestro player ID y la posición [0,0] esta vacia, entonces, retornar la posición [0,0].
    elif board[0][2] == player_id and board[0][1] == player_id and board[0][0] == '-':
        return [0, 0]

    #Si las posiciones [1,0] y [1,1] ya estan llenados por nuestro player ID y la posición [1,2] esta vacia, entonces, retornar la posición [1,2].
    elif board[1][0] == player_id and board[1][1] == player_id and board[1][2] == '-':
        return [1, 2]
    
    #Si las posiciones [1,1] y [1,2] ya estan llenados por nuestro player ID y la posición [1,0] esta vacia, entonces, retornar la posición [1,0].
    elif board[1][1] == player_id and board[1][2] == player_id and board[1][0] == '-':
        return [1, 0]
    
    #Si las posiciones [1,2] y [1,0] ya estan llenados por nuestro player ID y la posición [1,1] esta vacia, entonces, retornar la posición [1,1].
    elif board[1][2] == player_id and board[1][0] == player_id and board[1][1] == '-':
        return [1, 1]

    #Si las posiciones [2,0] y [2,1] ya estan llenados por nuestro player ID y la posición [2,2] esta vacia, entonces, retornar la posición [2,2].
    elif board[2][0] == player_id and board[2][1] == player_id and board[2][2] == '-':
        return [2, 2]
    
    #Si las posiciones [2,1] y [2,2] ya estan llenados por nuestro player ID y la posición [2,0] esta vacia, entonces, retornar la posición [2,0].
    elif board[2][1] == player_id and board[2][2] == player_id and board[2][0] == '-':
        return [2, 0]
    
    #Si las posiciones [2,0] y [2,2] ya estan llenados por nuestro player ID y la posición [2,1] esta vacia, entonces, retornar la posición [2,1].
    elif board[2][0] == player_id and board[2][2] == player_id and board[2][1] == '-':
        return [2, 1]
    
    # ---------------------------------------------- | ATACAR: VERTICALES | ---------------------------------------------- 
    
    # Seguidamente, buscaremos las verticales: Esto se hace con la finalidad de analizar los diferentes escenarios que existen para completar una linea de tres y tras anaizarlo, proceder a completar dicha linea.
    
    #Si las posiciones [0,0] y [1,0] ya estan llenados por nuestro player ID y la posición [2,0] esta vacia, entonces, retornar la posición [2,0].
    elif board[0][0] == player_id and board[1][0] == player_id and board[2][0] == '-':
        return [2][0]
    
    #Si las posiciones [2,0] y [1,0] ya estan llenados por nuestro player ID y la posición [0,0] esta vacia, entonces, retornar la posición [0,0].
    elif board[2][0] == player_id and board[1][0] == player_id and board[0][0] == '-':
        return [0, 0]
    
    #Si las posiciones [0,0] y [2,0] ya estan llenados por nuestro player ID y la posición [1,0] esta vacia, entonces, retornar la posición [1,0].
    elif board[0][0] == player_id and board[2][0] == player_id and board[1][0] == '-':
        return [1, 0]

    #Si las posiciones [0,1] y [1,1] ya estan llenados por nuestro player ID y la posición [2,1] esta vacia, entonces, retornar la posición [2,1].
    elif board[0][1] == player_id and board[1][1] == player_id and board[2][1] == '-':
        return [2, 1]
    
    #Si las posiciones [1,1] y [2,1] ya estan llenados por nuestro player ID y la posición [0,1] esta vacia, entonces, retornar la posición [0,1].
    elif board[1][1] == player_id and board[2][1] == player_id and board[0][1] == '-':
        return [0, 1]
    
    #Si las posiciones [2,1] y [0,1] ya estan llenados por nuestro player ID y la posición [1,1] esta vacia, entonces, retornar la posición [1,1].
    elif board[2][1] == player_id and board[0][1] == player_id and board[1][1] == '-':
        return [1, 1]

    #Si las posiciones [0,2] y [1,2] ya estan llenados por nuestro player ID y la posición [2,2] esta vacia, entonces, retornar la posición [2,2].
    elif board[0][2] == player_id and board[1][2] == player_id and board[2][2] == '-':
        return [2, 2]
    
    #Si las posiciones [1,2] y [2,2] ya estan llenados por nuestro player ID y la posición [0,2] esta vacia, entonces, retornar la posición [0,2].
    elif board[1][2] == player_id and board[2][2] == player_id and board[0][2] == '-':
        return [0, 2]
    
    #Si las posiciones [0,2] y [2,2] ya estan llenados por nuestro player ID y la posición [1,2] esta vacia, entonces, retornar la posición [1,2].
    elif board[0][2] == player_id and board[2][2] == player_id and board[1][2] == '-':
        return [1, 2]
    
    # ---------------------------------------------- | DEFENDER: DIAGONALES | ---------------------------------------------- 
    
    # Ahora iniciaremos con la estrategia para defender, inicialmente buscaremos las diagonales: Esto se hace con la finalidad de analizar los diferentes escenarios que existen para defender una linea de tres y tras anaizarlo, proceder a bloquear dicha linea.
    
    #Se crea una variable que cuente con los datos: Player ID and "-" con la finalidad de el bot descarte una fila que ya no va a ser de gane/pierde aun que haya una celda vacia.
    campos = [player_id, '-']

    #Si las posiciones [0,0] y [1,1] no estan en campos y la posición [2,2] esta vacia, entonces, retornar la posición [2,2].
    if board[0][0] not in campos and board[1][1] not in campos and board[2][2] == '-':
        return [2, 2]
    
    #Si las posiciones [0,2] y [2,0] no estan en campos y la posición [1,1] esta vacia, entonces, retornar la posición [1,1].
    elif board[0][2] not in campos and board[2][0] not in campos and board[1][1] == '-':
        return [1, 1]
    
    #Si las posiciones [1,1] y [2,2] no estan en campos y la posición [0,0] esta vacia, entonces, retornar la posición [0,0].
    elif board[1][1] not in campos and board[2][2] not in campos and board[0][0] == '-':
        return [0, 0]
    
    #Si las posiciones [2,2] y [0,0] no estan en campos y la posición [1,1] esta vacia, entonces, retornar la posición [1,1].
    elif board[2][2] not in campos and board[0][0] not in campos and board[1][1] == '-':
        return [1, 1]
    
    #Si las posiciones [2,0] y [1,1] no estan en campos y la posición [0,2] esta vacia, entonces, retornar la posición [0,2].
    elif board[2][0] not in campos and board[1][1] not in campos and board[0][2] == '-':
        return [0, 2]
    
    #Si las posiciones [1,1] y [0,2] no estan en campos y la posición [2,0] esta vacia, entonces, retornar la posición [2,0].
    elif board[1][1] not in campos and board[0][2] not in campos and board[2][0] == '-':
        return [2, 0]
    
 # ---------------------------------------------- | DEFENDER: HORIZONTALES | ---------------------------------------------- 
    
 # Ahora iniciaremos con la estrategia para defender, inicialmente buscaremos las horizontales: Esto se hace con la finalidad de analizar los diferentes escenarios que existen para defender una linea de tres y tras anaizarlo, proceder a bloquear dicha linea.
    
    #Si las posiciones [0,0] y [0,1] no estan en campos y la posición [0,2] esta vacia, entonces, retornar la posición [0,2].
    elif board[0][0] not in campos and board[0][1] not in campos and board[0][2] == '-':
        return [0, 2]
    
    #Si las posiciones [0,0] y [0,2] no estan en campos y la posición [0,1] esta vacia, entonces, retornar la posición [0,1].
    elif board[0][0] not in campos and board[0][2] not in campos and board[0][1] == '-':
        return [0, 1]
    
    #Si las posiciones [0,2] y [0,1] no estan en campos y la posición [0,0] esta vacia, entonces, retornar la posición [0,0].
    elif board[0][2] not in campos and board[0][1] not in campos and board[0][0] == '-':
        return [0, 0]

    #Si las posiciones [1,0] y [1,1] no estan en campos y la posición [1,2] esta vacia, entonces, retornar la posición [1,2].
    elif board[1][0] not in campos and board[1][1] not in campos and board[1][2] == '-':
        return [1, 2]
    
    #Si las posiciones [1,1] y [1,2] no estan en campos y la posición [1,0] esta vacia, entonces, retornar la posición [1,0].
    elif board[1][1] not in campos and board[1][2] not in campos and board[1][0] == '-':
        return [1, 0]
    
    #Si las posiciones [1,2] y [1,0] no estan en campos y la posición [1,1] esta vacia, entonces, retornar la posición [1,1].
    elif board[1][2] not in campos and board[1][0] not in campos and board[1][1] == '-':
        return [1, 1]

    #Si las posiciones [2,0] y [2,1] no estan en campos y la posición [2,2] esta vacia, entonces, retornar la posición [2,2].
    elif board[2][0] not in campos and board[2][1] not in campos and board[2][2] == '-':
        return [2, 2]
    
    #Si las posiciones [2,1] y [2,2] no estan en campos y la posición [2,0] esta vacia, entonces, retornar la posición [2,0].
    elif board[2][1] not in campos and board[2][2] not in campos and board[2][0] == '-':
        return [2, 0]
    
    #Si las posiciones [2,0] y [2,2] no estan en campos y la posición [2,1] esta vacia, entonces, retornar la posición [2,1].
    elif board[2][0] not in campos and board[2][2] not in campos and board[2][1] == '-':
        return [2, 1]

# ---------------------------------------------- | DEFENDER: VERTICALES | ---------------------------------------------- 
    
# Ahora iniciaremos con la estrategia para defender, inicialmente buscaremos las verticales: Esto se hace con la finalidad de analizar los diferentes escenarios que existen para defender una linea de tres y tras analizarlo, proceder a bloquear dicha linea.
    
    #Si las posiciones [0,0] y [1,0] no estan en campos y la posición [2,0] esta vacia, entonces, retornar la posición [2,0].
    elif board[0][0] not in campos and board[1][0] not in campos and board[2][0] == '-':
        return [2][0]
    
    #Si las posiciones [2,0] y [1,0] no estan en campos y la posición [0,0] esta vacia, entonces, retornar la posición [0,0].
    elif board[2][0] not in campos and board[1][0] not in campos and board[0][0] == '-':
        return [0, 0]
    
    #Si las posiciones [0,0] y [2,0] no estan en campos y la posición [1,0] esta vacia, entonces, retornar la posición [1,0].
    elif board[0][0] not in campos and board[2][0] not in campos and board[1][0] == '-':
        return [1, 0]

    #Si las posiciones [0,1] y [1,1] no estan en campos y la posición [2,1] esta vacia, entonces, retornar la posición [2,1].
    elif board[0][1] not in campos and board[1][1] not in campos and board[2][1] == '-':
        return [2, 1]
    
    #Si las posiciones [1,1] y [2,1] no estan en campos y la posición [0,1] esta vacia, entonces, retornar la posición [0,1].
    elif board[1][1] not in campos and board[2][1] not in campos and board[0][1] == '-':
        return [0, 1]
    
    #Si las posiciones [2,1] y [0,1] no estan en campos y la posición [1,1] esta vacia, entonces, retornar la posición [1,1].
    elif board[2][1] not in campos and board[0][1] not in campos and board[1][1] == '-':
        return [1, 1]

    #Si las posiciones [0,2] y [1,2] no estan en campos y la posición [2,2] esta vacia, entonces, retornar la posición [2,2].
    elif board[0][2] not in campos and board[1][2] not in campos and board[2][2] == '-':
        return [2, 2]
    
    #Si las posiciones [1,2] y [2,2] no estan en campos y la posición [0,2] esta vacia, entonces, retornar la posición [0,2].
    elif board[1][2] not in campos and board[2][2] not in campos and board[0][2] == '-':
        return [0, 2]
    
    #Si las posiciones [0,2] y [2,2] no estan en campos y la posición [1,2] esta vacia, entonces, retornar la posición [1,2].
    elif board[0][2] not in campos and board[2][2] not in campos and board[1][2] == '-':
        return [1, 2]
    
    # ---------------------------------------------- | FILL BOARD | ---------------------------------------------- 
    
    #En este caso se utilizó un for para que llene alguna posición en el board desde un inicio con una estrategia.
    
    Y = len(board)-1
    
    for i in range(len(board)): #0
        
        for x in range (len(board)):
            
            if player_id == "X" :
   
                #Estrategia de llenado # 1: Busca Posiciones Diagonales.
                
                #Revision / Validación de números iguales para posiciones [0][0] | [1][1] | [2][2]
                
                if board[x][x]== "-":
                    print(x,x)
                    print ("###################################################")
                    return [x,x]
                    

                #Valida todas: [0][0] | [0][1] | [0][2] | [1][0] | [1][1] | [1][2] | [2][0] | [2][1] | [2][2]
                
                if board[i][x]== "-":
                    print(i,x)
                    print ("=====================================================")
                    return [i,x]
                
            
            #Si nuestro player ID es igual a O, entonces hacer o siguiente:
            
            if player_id == "O" :
                
                #Si las posiciones [1,0], [1,2], [2,1] y [1,1] estan vacias, entonces se procedera a validar si esta en alguna esquina.
                
                if board[1][0]=="-" and board[1][2]=="-" and board[2][1]=="-" and board[1][1]=="-": 
                
                    #Si la posición [0,0] es del rival y las posiciones [1,1], [2,2], [2,0], [0,2], [1,0], [1,2] y [2,1] estan vacias, entonces retornar la posición [1,1].
                
                    if board[0][0]!=player_id and board[1][1]=="-" and board[2][2]=="-" and board[2][0]=="-" and board[0][2]=="-" and board[1][0]=="-" and board[1][2]=="-" and board[2][1]=="-":
                        return[1,1]
                    
                    #Si la posición [0,2] es del rival y las posiciones [1,1], [2,2], [2,0], [0,0], [1,0], [1,2] y [2,1] estan vacias, entonces retornar la posición [1,1].
                    
                    elif board[0][2]!=player_id and board[1][1]=="-" and board[2][2]=="-" and board[0][0]=="-" and board[2][0]=="-" and board[1][0]=="-" and board[1][2]=="-" and board[2][1]=="-":
                        return[1,1]
                    
                    #Si la posición [2,2] es del rival y las posiciones [1,1], [0,0], [2,0], [0,2], [1,0], [1,2] y [2,1] estan vacias, entonces retornar la posición [1,1].
                    elif board[2][2]!=player_id and board[1][1]=="-" and board[0][2]=="-" and board[0][0]=="-" and board[2][0]=="-" and board[1][0]=="-" and board[1][2]=="-" and board[2][1]=="-":
                        return[1,1]
                    
                    #Si la posición [2,0] es del rival y las posiciones [1,1], [2,2], [0,0], [0,2], [1,0], [1,2] y [2,1] estan vacias, entonces retornar la posición [1,1].
                    elif board[2][0]!=player_id and board[1][1]=="-" and board[2][2]=="-" and board[0][0]=="-" and board[0][2]=="-"and board[1][0]=="-" and board[1][2]=="-" and board[2][1]=="-":
                        return[1,1]
                
                #Si no se cumple lo anterior, seguir con la estrategia original.
                
                else:
                
                    for i in range(len(board)): #0
        
                        for x in range (len(board)):
                
                            #Estrategia de llenado # 1: Busca Posiciones Diagonales.
                
                            #Revision / Validación de números iguales para posiciones [0][0] | [1][1] | [2][2]
                
                            if board[x][x]== "-":
                                print(x,x)
                                print ("###################################################")
                                return [x,x]
                
                            #Valida todas: [0][0] | [0][1] | [0][2] | [1][0] | [1][1] | [1][2] | [2][0] | [2][1] | [2][2]
                
                            if board[i][x]== "-":
                                print(i,x)
                                print ("=====================================================")
                                return [i,x]    
                

def validate_move(board: list, move: list) -> bool:
    """
    Checks if the desired next move hits an empty position.
    """
    row, col = move[0], move[1]

    if board[row][col] == "-":
        return True

    return False


def send_move(player_id: str, move: list) -> None:
    """
    Sends move to API.
    """
    row, col = move[0], move[1]
    url = "{}/move/{}/{}/{}".format(API_URL, player_id, row, col)
    res = requests.post(url)
    return None


def does_game_continue() -> bool:
    """
    Checks if the current match continues via API.
    """
    url = "{}/continue".format(API_URL)
    res = requests.get(url)

    if res.text == "true":
        return True
    elif res.text == "false":
        return False


def print_board(board: list) -> None:
    '''
    Prints the baord in console to watch the game.
    '''
    print("\nCurrent board: \n")
    print(board[0][0], "|", board[0][1], "|", board[0][2])
    print("----------")
    print(board[1][0], "|", board[1][1], "|", board[1][2])
    print("----------")
    print(board[2][0], "|", board[2][1], "|", board[2][2], "\n")

