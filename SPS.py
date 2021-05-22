import random
import sys
print("---------------------------")
print("Game: Scissor Paper Stone")
print("---------------------------")
name = input("Enter your name: ")



win = 0
lose = 0
draw = 0
game = 0

while game < 3:
	print('\n')
	print("Win:", win, "Lose:", lose, "Draw:", draw)
	player = input("Enter s, p or r: ")
	player = player.lower()
	player = player.replace(" ", "")
	if player == 's':
		print(name, ":Scissor")
	elif player == 'p':
		print(name, ":Paper")
	elif player == 'r':
		print(name, ":Stone")
	else:
		print(name, "Invalid entry")

	rand = random.randint(1, 3)
	if rand == 1:
		computer = 's'
		print("Computer: Scissor")
	elif rand == 2:
		computer = 'p'
		print("Computer: Paper")
	elif rand == 3:
		computer = 'r'
		print("Computer: Stone")

	if player == computer:
		print("We Draw")
		draw += 1

	elif player == 'r' and computer == 's':
		print("You Win")
		win += 1
	elif player == 'r' and computer == 'p':
		print("I Win. You Lose")
		lose += 1

	elif player == 'p' and computer == 'r':
		print("You Win")
		win += 1
	elif player == 'p' and computer == 's':
		print("I Win. You Lose")
		lose += 1

	elif player == 's' and computer == 'p':
		print("You Win")
		win += 1
	elif player == 's' and computer == 'r':
		print("I Win. You Lose")
		lose += 1

	game += 1

print('\n')
print("Final Score:")
print("Win:", win, "Lose:", lose, "Draw:", draw)
if win < 2:
	print('\n')
	print(name, "You did not win. Better luck next time")
	print("Bye Bye")
else:
	print(name, "Congratulations. You won. I will remember you.")
print('\n')

exitgame = input("Enter any key to exit the game.")