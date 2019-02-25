import game

def victory():
        game.player_1.points += 1 
def restart():
        game.player_1.points -= 3

def main():
        while True:
                print('1.START', '2.EXIT')
                        
                x = input('ENTER NUMBER:  ')
                if x == '2':
                        exit(0)
                
                if x == '1':
                        print(game.player_1)
                        y = input('hello Mr Hero Man you must make a quest to defeat the most powerful in all the land\n DO YOU EXCEPT 1. yes 2. no: ')
                        if y == '1':
                                print (f'After miles on foot you run into a man /{game.enemy}/ solve the riddle to pass')
                                answer_1 = input('what is at the end of everything: ')
                                if answer_1 == 'g':
                                        victory()
                                        print(game.player_1)
                                        print(f'In a town a old man walks up to you and says hello /{game.friend_1}/')
                                        z = input('hes hungry will you give him food 1.yes 2.no: ')
                                        if z == '1':
                                        
                                                victory()
                                                print('he gives you something that will help you on your journey')
                                                print(game.player_1)
                                                print(f'you are walking through the woods when you encouter a dude\n/{game.enemy_2}/\n solve his problem to pass')
                                                f = input('whats black and white and read all over\n: ')
                                                if f == 'newspaper':
                                                        victory()
                                                        print(game.player_1)
                                                        print('you have reached the bosses lair can you enter?')
                                                        if game.player_1.points == 3:
                                                                print(f'using the strength you aquired in your quest you enter the lair of/{game.boss_1}/. the battle takes place and you use the item th man gave you to defeat him WIN')
                                                                restart()
                                                        else:
                                                                print ('you walk in and die maybenext time help a person in need')
                                                                restart()


                                        elif z == '2':
                                                print(f'you are walking through the woods when you encouter a dude/{game.enemy_2}/ solve his problem to pass')
                                                f = input('whats black and white and read all over: ')
                                                if f == 'newspaper':
                                                        victory()
                                                        print(game.player_1)
                                                        print('you have reached the bosses lair can you enter?')
                                                        if game.player_1.points == 3:
                                                                print(f'using the strength you aquired in your quest you enter the lair of/{game.boss_1}/. the battle takes place and you use the item the hungry man gave you to defeat him WIN')
                                                                restart()
                                                        else:
                                                                print ('you walk in and die maybe next time help a person in need')
                                                                restart()

                                                else:
                                                        print('loser')
                                                        return

                                        else:
                                                print('loser')
                                                return
                                else:
                                        print('loser')
                                        return
                        elif y == '2':
                                return 
                               
                                
                                


# def fight():
#         user_input = input('You encountered a enemy answer riddle to attack\n faliure wil result in damage\n What is the end of evertything?\n: ').lower
#         if user_input == 'g':
#                 game_repo.damage()
#         print(game_repo.enemy_1)
               
main()

        
