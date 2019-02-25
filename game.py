

class Character:
    def __init__(self, name, type_, ):
        self.name = name
        self.type_ = type_
        
    def __repr__(self):
        return f'{self.name}/{self.type_}'

class Player:
    def __init__(self, name, type_, points):
        self.name = name
        self.type_ = type_
        self.points = points
    def __repr__(self):
        return f'{self.name}/{self.type_}/{self.points}'
    
    
# class Enemy_1(Character):

#     def __init__(self, name, hp):
#         super().__init__(name,hp)
#     # def attack(self, player):
#     #     player.hp -= 1
    
player_1 = Player('Mr Hero Man','player_1', 0)
enemy = Character('Mr Bad Man', 'ENEMY')
enemy_2 = Character('Mr Even worse man','ENEMY')
friend_1 = Character('Mr Friendly Man', 'FREIND') 
boss_1 = Character('Mr Boss man', 'BOSS')  


    



# player_1 = Player('Mr Hero Man', 4 )
# enemy_1 = Enemy_1('Bad guy', 3)
# player_1.player_attack (enemy_1)
# print (enemy_1.hp)
# print (enemy_1.name)
            
