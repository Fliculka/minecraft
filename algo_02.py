    # Stavba domu
'''
Nejdříve musíme definovat nejmenší možný algoritmus stavby zdi. Teď se ho pokusíme identifikovat.
'''
# Import knihoven
'''
Zde importujeme knihovny s příkazy, které nejsou součástí python v Minecraft.
'''
from time import sleep

agent.give

# Definuj funkci postav stěnu
def postav_stenu():
    '''
    Tato funkce staví vertikálně směrem pod agentem.
    '''
	agent.place("down")
	agent.move("forward")

# Definuj funkci otoč se
def otoc_se():
    '''
    Tato funkce otáčí agenta na konci stavby stěny. Je v ní jeden příkaz.
    '''
# Definuj funkci příprava stavby
def set_up():
    agent.teleport()
    agent.move("forward")
    agent.move("up")

# Definuj funkci postav základnu
def base():
    for count in range(4):
        postav_stenu1()

    agent.move("back")
    agent.turn("right")

    for count in range(4):
         postav_stenu()       
TODO: Změnit algoritmus postav_stenu
    agent.turn("right")

    for count in range(4):
        agent.move("forward")
        agent.place("down")

    agent.turn("right")
    agent.move("forward")
    agent.place("down")
    agent.move("forward")
    agent.move("forward")
    agent.place("down")
   
# Main
'''
Zde se nachází spouštění našeho programu. Volám zde jednotlivé funkce.
'''

# Definuj event handler když je v chatu zpráva
def on_player_message(message, sender, receiver, message_type):
    '''
    Tato funkce poslouchá herní chat a spouští programy podle kličových slov, která jsou definovaná níže:
    
    stena - agent staví 1 opakování algoritmu stěny. Pro testování.
    otoc - otočí se 1 krát. Pro testování.
    '''
    slova = message.split()

    # Když je první slovo stěna, proveď stavbu stěny
    if slova[0] == "stena1":
        sleep(1)
        postav_stenu()
    # Když je první slovo otoč, otoč se
    elif slova[0] == "stena2":
        sleep(1)
        postav_stenu2()
