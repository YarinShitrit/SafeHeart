# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define maya = Character("Maya")
define dan = Character("Dan", what_xalign=0.7)
define rachel = Character("Rachel, The School Counselor", what_xalign=0.7)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg school
    with fade

    show maya happy
    with dissolve

    # These display lines of dialogue.

    maya "Oh, a message from Dan"

    show maya phone

    "Dan: Maya! Skip class with me I need your help with something urgent"

    menu:
        
        "What should Maya do?"

        "Skip class with Dan":

            jump skip_class

        "Tell Dan she doesn't want to miss the class":

            jump stay_class


label skip_class:
    
    scene bg school
    with fade

    show dan happy at right with easeinright
    show maya anxious at left with easeinleft
    with dissolve

    maya "Is everything okay Dan? What do you need help with?"
    dan "Nothing, I just didn't feel like going to class"
    show maya surprised at left 
    maya "I thought you needed help! We skipped class for no reason!"
    dan "Why are you always so stressed?"
    show dan shrug at right with easeinright
    dan "Besides, it was your choice to do it, blame yourself for skipping class"
    maya "You can't be serious..."
    
    jump scene2


label stay_class:
    scene bg school
    show dan angry
    
    dan "What a nerd Maya is.."

    scene bg in_class
    with fade

    show maya sad 

    maya "I hope Dan is not mad at me.."

    jump scene2


    
label scene2:
    scene bg nextday
    with fade
    pause 2.0
    scene bg lunch
    with fade

    show dan happy at right with easeinright
    show maya happy at left with easeinleft
    maya "Hey Dan!"

    
    dan "Hi Maya, let me look your phone messages"
    show maya scared at left
    maya "But that's private, it's my phone..."
    show dan angry
    dan "Are you hiding something? Are you cheating on me?"
    maya "No.."
    dan "Then show me your messages"

    menu:

        "What should Maya do?"

        "Allow Dan to read her messages":
            jump read_messages
            
        "Refuse to show Dan her phone":
            jump refuse_to_read_messages



label read_messages:
    show dan phone at right 
    with fade
    show maya scared at left
    maya "Ok.. here you have it.."
    scene bg readmessage
    with fade
    pause 4.0
    jump scene3

label refuse_to_read_messages:
    show maya angry
    with fade
    maya "No Dan! im not giving you my phone"
    show dan shrug
    with fade
    dan "Ok.. Maya don't overreact please"


label scene3:
    scene bg weeklater
    with fade
    pause 2.0
    scene bg school_hall
    with fade

    show dan angry at right with easeinright
    show maya anxious at left with easeinleft

    dan "Maya why were you talking to that guy?!"
    maya "Dan please don't yell infront of everyone here..."
    maya "He just asked me something about class"
    dan "I won't stop yelling, I'm trying to protect you"

    menu:

        "What should Maya do?"

        "Apologize to Dan":
            jump apologize

        "Tell Dan he is overracting":
            jump overreacting

label apologize:
    show maya scared
    with dissolve    
    maya "Okay okay sorry, just please stop"
    show dan happy
    with dissolve
    dan "You don't get it, I'm taking care of you"
    maya "Yelling at me like that of everyone is not protecting..."
    show dan shrug
    pause 1.0

    scene bg yellatschool
    pause 4.0
    jump scene4

label overreacting:
    show maya anxious
    with dissolve
    maya "No Dan, i'm not talking to anyone else.."

    show dan shrug
    dan "You know what I'm talking about.. Don't do it again"

    jump scene4

label scene4:
    scene bg school
    with dissolve

    show maya scared
    maya "what should I do with Dan.."

    scene bg school
    show dan phone
    with fade
    dan "*Texting Maya*"

    scene bg school
    show maya phone
    with fade
    maya "Dan sent me a message..."

    "Dan: Maya I'm sorry about yesterday.. please give me another chance, I'll be better"
    
    show maya scared at left with dissolve
    pause 1.0
    show rachel happy at right with easeinright
    rachel "Hi Maya, I heard about yesterday with Dan"
    maya "Yeah... but he told me that he's sorry and that he'll change"
    rachel "Maya, Dan's behavior is a form of dating violence"
    rachel "He's being manipulative and controlling, it might never change..."
    rachel "You deserve a healthy relationship. And I'm here if you need my help"
    show maya happy
    maya "Thanks rachel, I appreciate it"

    menu:
        "What should Maya do?"

        "Tell Dan she wants to break up":
            jump breakup

        "Give Dan a second chance":
            jump second_chance
        
    
label second_chance:
    scene bg school
    with dissolve
    show maya scared
    with dissolve

    maya "I guess I should give him another chance"
    maya "He said he will change"

    scene bg weeklater
    with fade

    "The abusive cycle starts again"
    jump start


label breakup:
    scene bg brokeup
    pause 3.0
    scene bg school
    with fade

    show rachel happy at right with easeinright
    show maya sad at left with easeinleft
    rachel "Hi Maya, How have you been since the break up?"
    maya "Part of me is sad, but I'm also relieved"
    rachel "I know it's hard, but it was the right decision"
    rachel "You can always come to me or to your friends for support"
    show maya happy
    maya "Thanks rachel, that means a lot"
    jump scene5


label scene5:

    scene bg final
    with fade
    pause 2.0
    scene bg final2
    with dissolve
    pause 2.0
    return
