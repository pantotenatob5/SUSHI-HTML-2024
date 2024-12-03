from random import choice

players = ["Messi", "Cristiano", "Romário", "Bebeto", "Douglas"]

teamA = []
teamB = []

while len(players) > 0:
    playerA = choice(players)
    players.remove(playerA)
    teamA.append(playerA)

    if len(players) > 0:
        playerB = choice(players)
        players.remove(playerB)
        teamB.append(playerB)

print(f'JogadorA: {playerA}')
print(f'TimeA: {teamA}')
print(f'JogadorB: {playerB}')
print(f'TimeB: {teamB}')
print(f'Lista Original: {players}')
