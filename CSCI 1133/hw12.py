import random

class Character:
    '''
    Purpose:
    Creates a base class for all possible characters that exist in "Among Us" game.  Represents what the basis of a character within this game represents
    Instance Variables:
    name, color, alive, role - specifies the name, color, status, as well as role of the character at hand
    task_list - a list of tasks from possible_tasks of length num_tasks
    Methods:
    __repr__ overrides the repr method to output the variables of the class in an organized manner
    get_identity - returns the identity of the specific character, which is just "Character" in this case
    __init__ initializes all instance variables of the class and creates a task_list
    '''
    def __init__(self,name,color,num_tasks):
        possible_tasks = ['Stabilize drill', 'Calibrate distributor',
        'Map course', 'Clear out O2 filter', 'Download files',
        'Redirect power', 'Empty garbage', 'Repair wiring',
        'Fill engines tanks', 'Inspect laboratory', 'Record temperature',
        'Sign in with ID', 'Enable manifolds', 'Upload files']
        self.name = name
        self.color = color
        self.alive = True
        self.role = 'Good'

        self.task_list = []
        while len(self.task_list) < num_tasks:
            temptask = random.choice(possible_tasks)
            if temptask not in self.task_list:
                self.task_list.append(temptask)

    def __repr__(self):
        if self.alive == True:
            status = "Alive"
        else:
            status = "Ghost"

        return f"{self.name}: {self.color} - Health Status: {status}"

    def get_identity(self):
        return 'Character'


class Crewperson(Character):
    '''
    Purpose:
    An object of the crewperson class derives from character and alters one main thing. It changes the identity to crewperson from character.  It represents the crewperson in among us who is good and does tasks
    Instance Variables:
    Has the same instance variables as a character would since it derives from character
    Methods:
    get_identity - returns 'crewperson' instead of character.  In this case, crewperson overwrites the get_identity method from character
    complete_task - prints out which character completed which task and then removes that task from the list of tasks that crewperson needs to complete
    '''

    def get_identity(self):
        return 'Crewperson'

    def complete_task(self):
        if self.task_list == []:
            print(f"{self.name} has completed all their tasks.")
        else:
            task = self.task_list.pop(0)
            print(f"{self.name} has completed task: {task}.")


class Pretender(Character):
    '''
    Purpose:
    The pretender class represents another derivative of character that derives from character except it alters the role to Evil
    Instance Variables:
    The instance variables of pretender are the exact same as character, except the role is altered to return "Evil" instead of "Good"
    Methods:
    get_identity - overrides the get_identity method of the character class by returning pretender instead of character
    eliminate - takes in a target character object and set that target's status (alive) to False and prints who killed who
    '''
    def __init__(self,name,color,num_tasks):
        Character.__init__(self,name,color,num_tasks)

        self.role = 'Evil'

    def get_identity(self):
        return 'Pretender'

    def eliminate(self, target):
        target.alive = False
        print(f"{self.name} eliminated {target.name}.")


class Sheriff(Crewperson):
    '''
    Purpose:
    Instance Variables:
    Methods:
    '''
    def get_identity(self):
        return 'Sheriff'

    def encounter(self,target):
        if target.get_identity() == 'Pretender':
            target.alive = False
            print(f"{self.name} eliminated {target.name}.")


class Game:
    '''
    Purpose:
    Instance Variables:
    Methods:
    '''
    def __init__(self,player_list):
        self.player_list = player_list

    def check_winner(self):
        totaltasks = 0
        allgood = 0
        allevil = 0
        for players in self.player_list:
            if players.role == 'Good':
                totaltasks += len(players.task_list)
                if players.alive == True:
                    allgood += 1
            elif players.role == 'Evil':
                if players.alive == True:
                    allevil += 1
        if totaltasks == 0 or allevil == 0:
            print("Crewpersons win!")
            return 'C'
        if allevil >= allgood:
            print("Pretenders win!")
            return 'P'
        else:
            return '-'

    def meeting(self):
        aliveplayers = []
        for players in self.player_list:
            if players.alive == True:
                aliveplayers.append(players)
        target = random.choice(aliveplayers)
        for players in self.player_list:
            print(f"{players.name} voted for {target.name}.")
        print(f"{target.name} was voted out and eliminated.")
        target.alive = False
        return None

    def play_game(self):
        tasks = [1,2,3]
        while self.check_winner() == '-':
            aliveplayers = []
            for players in self.player_list:
                if players.role == 'Good':
                    for i in range(random.choice(tasks)):
                        players.complete_task()
                if players.role == 'Evil' and players.alive == True:
                    target = random.choice(self.player_list)
                    if target.role == 'Good' and target.alive == True:
                        players.eliminate(target)
                for players in self.player_list:
                    if players.alive == True:
                        aliveplayers.append(players)
                if players.get_identity() == 'Sheriff' and players.alive == True:
                    target = random.choice(aliveplayers)
                    players.encounter(target)
            if self.check_winner == 'P' or self.check_winner == 'C':
                break
            self.meeting()
        if self.check_winner == 'P':
            return 'P'
        elif self.check_winner == 'C':
            return 'C'







