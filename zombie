#Story
start = '''
It's July 20th, 2017. You are walking home from Girls Who Code when
you hear a bewildering groan coming from the Moody's entrance.
Thinking nothing of it, you continue walking to the subway entrance until
hoards of people flood out of the Path, screaming in fear. They rush past,
nearly knocking you over. Once they've cleared, you see three grotesque
human-like creatures follow behind.

You lock eyes with them and immediately run into the nearest alleyway.
There you see a lead pipe on the ground and a ladder leading up to the roof.
'''
leadpipeStory = '''
You decide to pick up the lead pipe and fight. You bash each of their heads
and make your escape. When you exit the alley, you see an entrance to the
subway station.
'''
leadpipeStoryShelter = '''
You decide to look for shelter. You turn left to see a hoard of zombies.
You turn to your right and see even more. They have you surrounded.
You fight as many as you can before one of them latches onto your arm.
'''
leadpipeStorySubway = '''
You decide to go down to the subway. None of the trains are running and
there is no one in sight. You reach into your backpack and pull out a
flashlight. You jump onto the tracks and start walking. You come to a
fork in the road.

Type 'left' to go left or 'right' to go right.
'''
leadpipeLeft = '''
You decide to turn left. As you venture further down, moans echo in the
distance. You turn around and see zombies. You find that you are surrounded
and outnumbered.
'''
leadpipeRight = '''
You decide to turn right. As you venture further down, you see a group
of people hudled together. You approach the group and they tell you they
are going to work together to find a cure. A man and a woman, both wearing
bloody lab coats, rapidly explain their plan for a cure. Confused, you ask
them where they will go and how they know what to do. The two sheepishly
glance at each other before admitting that they accidently created the
virus that caused the apocalypse. They ask if you want to join them.
'''
leadpipeJoin = '''
They welcome with you with open arms and you travel with them. With your
combined knowledge, you and the group discover a cure and save humanity.
WIN STORY
'''
leadpipeLeave = '''
They look dejected. The man walks up to you and hugs you. He says good
luck and begins to walk away. Suddenly, he turns back around and punches
you, knocking you out instantly. You wake up to the sound of disoriented
groans. Panicked, you reach for your backpack to see it is gone.
The group robbed you of your supplies and left you to deal with the
incoming hoard.
'''

ladderStory = '''
You escape to the rooftops, but are surprised to see zombies there too.
Do you want to jump off or try to fight them off?
'''

jumpStory = '''
You land in the Hudson river. Zombies are waiting for you on the docks
and you can't swim. You eventually drown.
GAME OVER
'''

fightStory = '''
You look through your bag. You have a pocket knife and a book.
Which one do you choose as your weapon?
'''

pocketknifeStory = '''
While fighting the zombies, you lose your knife. Zombies eat your brains.
GAME OVER
'''

bookStory = '''
You fight off all the zombies, bashing them in the head with the book.
It's getting late... You can either decide to stick to yourself and find shelter
or look for other survivors.
'''

shelterStory = '''
You find an empty Target. You spend the night there and plan a way to defeat
the zombies in the morning.
WIN GAME
'''

survivorsStory = '''
You walk around the neighborhood and can't find a single person. The zombies
eat you up as a midnight snack. GAME OVER
'''


#Code
print(start)


print("Type 'lead pipe' to fight or 'ladder' to escape.")
user_input = input()
if user_input == "lead pipe":
    print(leadpipeStory) # finished the story by writing what happens
    print("Type 'shelter' to look for shelter or 'subway' to go underground.")
    user_input = input()
    if user_input == "shelter":
        print(leadpipeStoryShelter)
        print("GAME OVER")
    elif user_input == "subway":
        print(leadpipeStorySubway)
        user_input = input()
        if user_input == "left":
            print(leadpipeLeft)
            print("GAME OVER")
        elif user_input == "right":
            print(leadpipeRight)
            user_input = input()
            if user_input == "join":
                print(leadpipeJoin)
            elif user_input == "leave":
                print(leadpipeLeave)
            else:
                print("Incorrect input! Try again. Type 'join' to go with the survivors or 'leave' to abandon the survivors.")
                while True:
                    user_input = input()
                    if user_input == "join":
                        print(leadpipeJoin)
                    elif user_input == "leave":
                        print(leadpipeLeave)
                        print("GAME OVER")
        else:
            print("Incorrect input! Try again. Type 'right' to go right and 'left' to go left.")
            while True:
                user_input = input()
                if user_input == "left":
                    print(leadpipeLeft)
                elif user_input == "right":
                    print(leadpipeRight)
                    user_inout = input()
                    if user_input == "join":
                        print(leadpipeJoin)
                    elif user_input == "leave":
                        print(leadpipeLeave)
                    else:
                        print("Incorrect input! Try again. Type 'join' to go with the survivors or 'leave' to abandon the survivors.")
                        while True:
                            user_input = input()
                            if user_input == "join":
                                print(leadpipeJoin)
                            elif user_input == "leave":
                                print(leadpipeLeave)
                                print("GAME OVER")
                else:
                    print("Incorrect input! Try again. Type 'left' to go left and 'right' to go right. ")
                    if user_input == "left":
                        print(leadpipeLeft)
                        print("GAME OVER")
                    elif user_input == "right":
                        print(leadpipeRight)
                        user_input = input()
                        if user_input == "join":
                            print(leadpipeJoin)
                        elif user_input == "leave":
                            print(leadpipeLeave)
                        else:
                            print("Incorrect input! Try again. Type 'join' to go with the survivors or 'leave' to abandon the survivors.")
                            while True:
                                user_input = input()
                                if user_input == "join":
                                    print(leadpipeJoin)
                                elif user_input == "leave":
                                    print(leadpipeLeave)
                                    print("GAME OVER")
    else:
        print("Incorrect input! Try again. Type 'shelter' to look for shelter or 'subway' to go underground.")
        while True:
            user_input = input()
            if user_input == "left":
                print(leadpipeLeft)
                print("GAME OVER")
            elif user_input == "right":
                print(leadpipeRight)
                user_input = input()
                if user_input == "join":
                    print(leadpipeJoin)
                elif user_input == "leave":
                    print(leadpipeLeave)
                else:
                    print("Incorrect input! Try again. Type 'join' to go with the survivors or 'leave' to abandon the survivors.")
                    while True:
                        user_input = input()
                        if user_input == "join":
                            print(leadpipeJoin)
                        elif user_input == "leave":
                            print(leadpipeLeave)
                            print("GAME OVER")
            else:
                print("Incorrect input! Try again. Type 'left' to go left and 'right' to go right. ")
                if user_input == "left":
                    print(leadpipeLeft)
                    print("GAME OVER")
                elif user_input == "right":
                    print(leadpipeRight)
                    user_input = input()
                    if user_input == "join":
                        print(leadpipeJoin)
                    elif user_input == "leave":
                        print(leadpipeLeave)
                    else:
                        print("Incorrect input! Try again. Type 'join' to go with the survivors or 'leave' to abandon the survivors.")
                        while True:
                            user_input = input()
                            if user_input == "join":
                                print(leadpipeJoin)
                            elif user_input == "leave":
                                print(leadpipeLeave)
                                print("GAME OVER")
elif user_input == "ladder":
    print(ladderStory) # finished the story writing what happens
    print("Type 'jump' to jump off the roof or 'fight' to attempt to fight off the zombies.")
    user_input = input()
    if user_input == "jump":
        print(jumpStory)
    elif user_input == "fight":
        print(fightStory)
        print("Type 'pocket knife' to pull out a pocket knife as your weapon or 'book' to use a book as your weapon")
        user_input = input()
        if user_input == "pocket knife":
            print(pocketknifeStory)
        elif user_input == "book":
            print(bookStory)
            print("Type 'shelter' to look for shelter by yourself or 'survivors'to look for other survivors")
            user_input = input()
            if user_input == "shelter":
                print(shelterStory)
            elif user_input == "survivors":
                print(survivorsStory)
            else:
                print("Incorrect input! Try again. Type 'shelter' to look for shelter by yourself or 'survivors'to look for other survivors")
                while True:
                    user_input = input()
                    if user_input == "shelter":
                        print(shelterStory)
                    elif user_input == "survivors":
                        print(survivorsStory)
                    else:
                        print("Incorrect input! Try again. Type 'shelter' to look for shelter by yourself or 'survivors'to look for other survivors")
        else:
            print("Incorrect Input! Try again. Type 'pocket knife' to pull out a pocket knife as your weapon or 'book' to use a book as your weapon")
            while True:
                user_input = input()
                if user_input == "pocket knife":
                    print(pocketknifeStory)
                elif user_input == "book":
                    print(bookStory)
                else:
                    print("Incorrect Input! Try again. Type 'pocket knife' to pull out a pocket knife as your weapon or 'book' to use a book as your weapon")
    else:
        print("Incorrect Input! Try again. Type 'jump' to jump off the roof or 'fight' to attempt to fight off the zombies.")
        while True:
            user_input = input()
            if user_input == "jump":
                print(jumpStory)
            elif user_input == "fight":
                print(fightStory)
            else:
                print("Incorrect Input! Try again. Type 'jump' to jump off the roof or 'fight' to attempt to fight off the zombies.")
else:
    print("Incorrect Input! Try again. Type 'lead pipe' to fight or 'ladder' to escape.")
    while True:
        user_input = input()
        if user_input == "lead pipe":
            print(leadpipeStory) # finished the story by writing what happens
        elif user_input == "ladder":
            print(ladderStory) # finished the story writing what happens
        else:
            print("Incorrect Input! Try again. Type 'lead pipe' to fight or 'ladder' to escape.")
