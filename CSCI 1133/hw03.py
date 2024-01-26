import math

def sound(weight) :
    '''
    Purpose:
    Takes in a postive integer "weight" and returns the sound a dog in that inputted "weight class" would most likely make
    Parameter(s):
    weight - a postive integer value represting the weight of the dog that the outputted sound should match
    Return Value:
    A sound of some sort "boof" "ruff" "bork" depending on the specified weight inputted
    '''

    if round(weight) < 13 :
        return 'Yip'
    elif round(weight) <= 30 :
        return 'Ruff'
    elif round(weight) <= 70 :
        return 'Bark'
    elif round(weight) > 70 :
        return 'Boof'


def sound2(weight, is_cat) :
    '''
    Purpose:
    Checks to see, depending on user input, whether the the animal in question is a cat or not, if not a cat then it returns the sound the dog would make at that weight, otherwise, all cats say "meow"
    Parameter(s):
    weight -  a postive integer value represting the weight of the dog or cat that the outputted sound should match 
    is_cat -  a boolean value representing whether or not the animal in question is a cat or not
    Return Value:
    A sound representing what noise the dog or cat in question will make at a given value for its weight
    '''

    chonk = round(weight)

    if is_cat == True :
        return 'Meow'
    else :
        return sound(chonk)

    
def selection(text, optionA, optionB, optionC) :
    '''
    Purpose:
    To output some text and ask 3 questions in response to that text, each of which have their own outcome. Depending on the users input, lead the user down the path their answer to the text takes them
    Parameter(s):
    text- The intial text of which the three questions are a derivative of
    optionA- One response to the question, could be True or False
    optionB- Another response to the question, could be True or False
    optionC- The last response to the output, could be True or False
    Return Value:
    Returns whether or not the users input in response to the question is a valid answer to the question and defaults the answer to A if it is not possible
    '''

    print(text)
    print("")
    print("A. "+optionA)
    print("B. "+optionB)
    print("C. "+optionC)

    answer = str(input('Choose A, B, or C: '))

    if answer == "A" or answer == "B" or answer == "C" :
        return answer
    else :
        print("Invalid option, defaulting to A")
        return 'A'


def adventure() :
   
    case1 = selection("\nYou are in your 3rd lecture period for CSCI 1133 and Prof. Exley is noticeably more annoyed than usual. How will you make it through class without getting in huge trouble?","Remain silent and listen intentively at the lecture Prof. Exley is giving","Ask a question about a topic that he already mentioned because you weren't listening","Stand up and throw your laptop at Prof. Exley with full strength???!!!")
    if case1 == "A" :
        case2 = selection("\nThe class continuous on, where upon Prof. Exley asks you a question about a the possibility of bending space and time...What the hell? This isn't some advanced physics course...","Actually give him a spot on answer because you are a ex-physics major","Yell at him for asking you such a random question","Recite a quote from Star-Trek about the warp drive")
        if case2 == "A" :
            case4 = selection("\nHe accepts your answer and moves on leaving the rest of the class puzzled at how you even answered that question. The whole class is now making fun of you for you being a nerd","Feign saddness to appeal to Prof. Exley's pathos so he will take your side","Flick the class off and proclaim your superior intelligence","Try to internalize all the slander towards yourself and ignore it all")
            if case4 == "A" :
                print("\nFeeling bad for you, Prof. Exley kicks out all the other students who made fun of you, leaving just you and him to have some tea and learn some new things")
                return True
            elif case4 == "B" :
                print("\nThe whole class and prof. Exley are extremely offended at your boasts and mug you. Leaving you a beaten pulp in the middle of the lecture hall")
                return False
            elif case4 == "C" :
                print("\nYou end up peeing yourself from all the stress of being belittled. Not only are you an idiot to the class now, but you are pant-wetter who can't code")
                return False
        elif case2 == "B" :
            print("\nProf. Exley grabs the ruler and smacks your wrist with it full force. It ends up breaking your wrist. He then kicks you out of class because he can ask whatever questions he wants in his classroom")
            return False
        elif case2 == "C" :
            print("\nAll the stress anger previously seen in Prof. Exley's face melts away as you mention a quote from his favorite show. He finishes the end of the quote in unison with you and together you become best friends")
            return True
    elif case1 == "B" :
        case3 = selection("\nProfessor Exley, upon hearing such a annoying question, angerly answers under the condition that you answer a computer science related question afterwards... Turns out the question is giga-hard","Answer the question to the best of your ability, tapping into ancient chakras of knowledge only seen by the coders of old","Answer the question completely wrong but do it with a smug, dumb look on your face","Interactively demonstrate your understanding of the question while teaching the class of the concepts you used in your explanation")
        if case3 == "A" :
            print("\nBeyond impressed at the level of expertise he just witnessed, Prof. Exley awards you with the CSCI 1133 scholar award and names you a legend of the class")
            return True
        elif case3 == "B" :
            case5 = selection("\nHe accepts your answer and moves on leaving the rest of the class puzzled at how you even answered that question. The whole class is now making fun of you for you being a nerd","Feign saddness to appeal to Prof. Exley's pathos so he will take your side","Flick the class off and proclaim your superior intelligence","Try to internalize all the slander towards yourself and ignore it all")
            if case5 == "A" :
                print("\nFeeling bad for you, Prof. Exley kicks out all the other students who made fun of you, leaving just you and him to have some tea and learn some new things")
                return True
            elif case5 == "B" :
                print("\nThe whole class and prof. Exley are extremely offended at your boasts and mug you. Leaving you a beaten pulp in the middle of the lecture hall")
                return False
            elif case5 == "C" :
                print("\nYou end up peeing yourself from all the stress of being belittled. Not only are you an idiot to the class now, but you are pant-wetter who can't code")
                return False
        elif case3 == "C" :
            print("\nProf. Exley's jaw drops as you just taught the class all the material for the day in one explanation. He allows you to teach the rest of the class as he smiles and kicks his feet up while drinking a cup of joe")
            return True
    elif case1 == "C" :
        print("\nHe rages at you for assaulting him and calls the Police. They arrive and charge you with assualt and ban you from all U of MN facilities.  You also get 4 years of jail time LMAOO!!!")
        return False