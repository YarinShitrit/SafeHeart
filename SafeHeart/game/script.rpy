# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define maya = Character("Maya")
define dan = Character("Dan", what_xalign=0.7)
define rachel = Character("Rachel", what_xalign=0.7)

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

    "Dan: Maya! where are you? do you want to skip class with me?"

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
    show maya surprised at left with easeinleft
    with dissolve

    maya "We should have went to class.."
    
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
    scene bg lunch
    with fade

    show dan happy at right with easeinright
    show maya happy at left with easeinleft
    maya "Hey Dan!"

    show maya scared at left
    dan "Maya show me your phone messages"

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

    jump scene3

label refuse_to_read_messages:
    show maya angry
    with fade
    maya "No Dan! im not giving you my phone"
    show dan shrug
    with fade
    dan "Ok.. Maya don't overreact please"


label scene3:
    scene bg school_hall
    with fade

    show dan angry at right with easeinright
    show maya anxious at left with easeinleft

    dan "Maya are you talking to other boys?!"

    menu:

        "What should Maya do?"

        "Apologize to Dan":
            jump apologize

        "Tell Dan he is overracting":
            jump overreacting

label apologize:
    show maya scared
    with dissolve    
    maya "I'm sorry Dan"
    show dan shrug

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
    maya "Oh Dan sent me a message"

    "Dan: Maya i'm sorry about yesterday.. please give me another chance"

    menu:
        "What should Maya do?"

        "Give Dan a second chance":

            jump second_chance

        "Tell Dan she wants to break up":
            jump breakup
        
    
label second_chance:
    scene bg school
    with fade
    show maya scared
    with dissolve

    maya "I guess I should give him another chance"
    maya "He said he will change"

    scene bg weeklater
    with fade

    "The abusive cycle starts again"
    jump start


label breakup:
    scene bg school
    with fade

    show rachel happy at right with easeinright
    show maya sad at left with easeinleft
    rachel "Hi Maya, How have you been since the break up?"
    maya "On one hand I'm sad, but I'm also feeling relief"
    rachel "I know it's hard, but it was the right decision"
    rachel "You deserve a loving and healthy relationship"
    show maya happy
    maya "Thanks rachel, I appreciate your support"
    jump scene5


label scene5:

    scene bg final
    with fade
    pause 2.0
    scene bg final2
    with dissolve
    pause 2.0
    return
