# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define maya = Character("Maya")
define dan = Character("Dan")

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

    dan "Maya! where are you? do you want to skip class with me?"

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
    show maya frustrated at left with easeinleft
    with dissolve
    
    jump scene2


label stay_class:

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

    show dan neutral at right with easeinright
    show maya neutral at left with easeinleft

    dan "Maya show me your phone messages"
    show maya scared at left
    menu:

        "What should Maya do?"

        "Allow dan to read her messages":
            maya "Ok.. here you have it.."
            show dan phone at right 
            with fade
            show maya frustrated at left
            
        "Refuse to show Dan her phone":
            show maya angry
            with fade
            maya "No Dan! im not giving you my phone"
            show dan scared
            with fade
            dan "Ok.. "
    return
