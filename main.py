if 10 == 10:
    from replit import db
    import time
    from os import system
    import random
    import sys
    from colorama import Style, Fore

    classes = 'mage', 'warrior', 'ranger', 'gunslinger', 'barbarian', 'monk'

    races = 'elf', 'dwarf', 'halfling', 'human'

    race = 'none'

    lvl1_all_spells = "magic missile", "health buff", "attack buff", 'lightning touch', 'speed buff', 'mage armor'
    lvl2_all_spells = "firebolt", "poison shards", 'ice shards', 'drain', 'aerial'

    spd = 0.02

    inv = []

    items = 0

    gp = 20

    max_hp = 10
    hp = 0

    lvl = 1

    expNext = 500

    exp = 0

    gems = 0

    character_class = 'none'

    dex = 2

    character = 'none'

    defense = 10

    weapons = 'none'

    shield = 'none'
    shield_power = 0

    lvl1_spells = 3
    lvl2_spells = 1

    lvl1_available_spells = []
    lvl2_available_spells = []

    commands = []

    wares = []

    bullets = 10
    arrows = 10

    world = 'start'

    location = 'start village'

    villages = [
        "Haling Cove", "White Bridge", "Lockwood", "Daekrahm", "Warlington",
        "Azalea", "Bryxton", "Ark Ville"
    ]

    ruffians = True
    nobles = True
    adventures = True
    workers = True

    logo = f"""{Fore.GREEN}{Style.BRIGHT}
  ___          _              __     _      _             _                
 | _ \\___ __ _| |_ __    ___ / _|   /_\\  __| |_ _____ _ _| |_ _  _ _ _ ___ 
 |   / -_) _` | | '  \\  / _ \\  _|  / _ \\/ _` \\ V / -_) ' \\  _| || | '_/ -_)
 |_|_\\___\\__,_|_|_|_|_| \\___/_|   /_/ \\_\\__,_|\\_/\\___|_||_\\__|\\_,_|_| \\___|
    {Fore.WHITE}
    """

    forest_block = f'{Fore.GREEN}\"\"\"{Style.RESET_ALL}'
    mountain_block = f'{Fore.LIGHTBLACK_EX}^^^{Style.RESET_ALL}'
    water_block = f'{Fore.BLUE}~~~{Style.RESET_ALL}'
    grass_block = f"{Style.RESET_ALL}{Fore.LIGHTGREEN_EX}\'\'\'{Style.RESET_ALL}"
    desert_block = f'{Fore.YELLOW}###{Style.RESET_ALL}'
    swamp_block = f'{Style.DIM}{Fore.GREEN}&&&{Style.RESET_ALL}'
    village_block = [f'VLG{Style.RESET_ALL}', f'|^|{Style.RESET_ALL}']
    dungeon_block = [f'DGN{Style.RESET_ALL}', '{*}']
    dungeon2_block = [f'DGN{Style.RESET_ALL}', '{@}']
    arena_block = [f'ARN{Style.RESET_ALL}', '{!}']


    def map_Start():
        print(
            f'[{water_block}][{mountain_block}][{mountain_block}][{mountain_block}][{mountain_block}][{mountain_block}][{water_block}]')
        print(
            f'[{water_block}][{mountain_block}][{mountain_block}][{mountain_block}][{mountain_block}][{mountain_block}][{water_block}]')
        print(
            f'[{mountain_block}][{grass_block}][{desert_block}][{grass_block}][{forest_block}][{dungeon_block[0]}][{mountain_block}]')
        print(
            f'[{mountain_block}][{grass_block}][{desert_block}][{grass_block}][{forest_block}][{dungeon_block[1]}][{mountain_block}]')
        print(
            f'[{mountain_block}][{desert_block}][{village_block[0]}][{desert_block}][{grass_block}][{mountain_block}][{water_block}]')
        print(
            f'[{mountain_block}][{desert_block}][{village_block[1]}][{desert_block}][{grass_block}][{mountain_block}][{water_block}]')
        print(
            f'[{mountain_block}][{dungeon_block[0]}][{desert_block}][{arena_block[0]}][{mountain_block}][{water_block}][{water_block}]')
        print(
            f'[{mountain_block}][{dungeon_block[1]}][{desert_block}][{arena_block[1]}][{mountain_block}][{water_block}][{water_block}]')
        print(
            f'[{mountain_block}][{dungeon2_block[0]}][{mountain_block}][{mountain_block}][{water_block}][{water_block}][{water_block}]')
        print(
            f'[{mountain_block}][{dungeon2_block[1]}][{mountain_block}][{mountain_block}][{water_block}][{water_block}][{water_block}]')
        print(
            f'[{mountain_block}][{mountain_block}][{water_block}][{water_block}][{water_block}][{water_block}][{water_block}]')
        print(
            f'[{mountain_block}][{mountain_block}][{water_block}][{water_block}][{water_block}][{water_block}][{water_block}]')


    def scrollTxt(text):
        print(text)
        time.sleep(0.5)


    def bar():
        print(f'{Fore.WHITE}')
        print("================================")
        print("")


    def enter():
        scrollTxt('[ENTER] to continue')
        input()


    def print_health():
        scrollTxt(f"HP: {Fore.RED}{hp}{Fore.WHITE}/{Fore.RED}{max_hp}{Fore.WHITE}")


    def print_gp():
        scrollTxt(f"Gold Pieces: {Fore.YELLOW}{gp}{Fore.WHITE}")


    def print_exp():
        scrollTxt(
            f'EXP: {Fore.CYAN}{exp}{Fore.WHITE}/{Fore.CYAN}{expNext}{Fore.WHITE}')


    def addList(commands, other):
        global new_commands
        new_commands = commands
        i = 0
        while i < len(other):
            new_commands.append(other[i])
            i += 1


    def printList(commands, name):
        text = name
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
        i = 0
        while i < len(commands):
            if i + 1 == len(commands):
                text = f"{Fore.BLUE}{commands[i]}{Fore.WHITE}  "
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
            else:
                text = f"{Fore.BLUE}{commands[i]}{Fore.WHITE}, "
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    # replaced
            i += 1


    def printShop(commands, cost, name):
        text = name
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            # replaced
        i = 0
        while i < len(commands):
            if i + 1 == len(commands):
                text = f"{Fore.LIGHTGREEN_EX}{commands[i]}{Fore.WHITE} ~ {Fore.YELLOW}{cost[i]}{Fore.WHITE}  "
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    # replaced
            else:
                text = f"{Fore.LIGHTGREEN_EX}{commands[i]}{Fore.WHITE} ~ {Fore.YELLOW}{cost[i]}{Fore.WHITE},  "
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    # replaced
            i += 1


    def printShopH(commands, cost, name):
        text = name
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            # replaced
        i = 0
        while i < len(commands):
            if i + 1 == len(commands):
                text = f"{Fore.LIGHTGREEN_EX}{commands[i]}{Fore.WHITE} ~ {Fore.LIGHTMAGENTA_EX}{cost[i]}{Fore.WHITE}  "
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    # replaced
            else:
                text = f"{Fore.LIGHTGREEN_EX}{commands[i]}{Fore.WHITE} ~ {Fore.LIGHTMAGENTA_EX}{cost[i]}{Fore.WHITE},  "
                for char in text:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    # replaced
            i += 1


    def inputCommands(commands, extraTxt):
        global answer
        answer = "none"
        while answer == "none":
            answer = input(f"{Fore.GREEN}")
            sys.stdout.write(f"{Fore.WHITE}")
            i = 0
            stop = False
            while i < len(commands):
                if stop is True:
                    i = len(commands)
                else:
                    if answer == f"{extraTxt}{commands[i]}":
                        stop = True
                    else:
                        stop = False
                        i += 1
            if stop is False:
                scrollTxt("That's not a input")
                answer = "none"


    def printInv(inv):

        scrollTxt("~INVENTORY~")
        scrollTxt(f"GP ~ {Fore.YELLOW}{gp}{Fore.WHITE}")
        i = 0
        while i < len(inv):
            scrollTxt(f"{i + 1} ~ {inv[i]}")
            i += 1
        scrollTxt(f'Weapon: {weapons}')


    def inv_interact():
        global gp
        global items

        global items_local

        items_local = items

        inv_done = False

        global hp
        global inv
        global expNext

        global shield_power

        global weapons

        global shield

        global gems

        global character
        global commands
        global answer
        global exp

        global lvl
        global max_hp

        global character_class

        scrollTxt(
            'Commands: \'consume\', \'consume all\', \'remove\', \'equip weapon\', \'enchant weapon\', \'equip shield\', \'done\', \'inv\', \'open crate\''
        )
        while inv_done == False:
            items = len(inv)
            items_local = items

            commands = ['consume', 'consume all', 'remove', 'equip weapon', 'enchant weapon', 'equip shield', 'done',
                        'inv', 'open crate']
            inputCommands(commands, '')
            inv_action = answer
            sys.stdout.write(f"{Fore.WHITE}")
            if inv_action == "done":
                inv_done = True

            if inv_action == "equip weapon":
                if items_local > 0:
                    scrollTxt('What would you like to equip')
                    thing = 'none'
                    while thing == 'none':
                        thing = input(f"{Fore.GREEN}")

                        i = 0
                        equiped = False
                        while i < len(inv):
                            if thing == inv[i]:
                                if equiped is False:
                                    scrollTxt(f'{Fore.WHITE}Weapon equipped')
                                equiped = True
                                weapons = thing
                            i += 1
                        if equiped is False:
                            scrollTxt(f"{Fore.WHITE}That\'s not a weapon")
                            thing = 'none'
                else:
                    scrollTxt('You have nothing to equip')

            if inv_action == "enchant weapon":
                if items_local > 0:
                    if gems > 9:
                        scrollTxt('What would you like to enchant')
                        thing = 'none'
                        while thing == 'none':
                            thing = input(f"{Fore.GREEN}")
                            print(f'{Fore.WHITE}')

                            i = 0
                            equiped = False
                            while i < len(inv):
                                if thing == inv[i]:
                                    if equiped is False:
                                        equiped = True

                                        inv.remove(thing)

                                        if '[common] ' in thing:
                                            listthing = []
                                            for char in thing:
                                                listthing.append(char)
                                            for char in '[common] ':
                                                listthing.remove(char)
                                            i = 0
                                            thing = ''
                                            while i < len(listthing):
                                                thing = f'{thing}{listthing[i]}'
                                                i += 1

                                        if '[rusty] ' in thing:
                                            listthing = []
                                            for char in thing:
                                                listthing.append(char)
                                            for char in '[rusty] ':
                                                listthing.remove(char)
                                            i = 0
                                            thing = ''
                                            while i < len(listthing):
                                                thing = f'{thing}{listthing[i]}'
                                                i += 1

                                        if '[rare] ' in thing:
                                            listthing = []
                                            for char in thing:
                                                listthing.append(char)
                                            for char in '[rare] ':
                                                listthing.remove(char)
                                            i = 0
                                            thing = ''
                                            while i < len(listthing):
                                                thing = f'{thing}{listthing[i]}'
                                                i += 1

                                        if '[epic] ' in thing:
                                            listthing = []
                                            for char in thing:
                                                listthing.append(char)
                                            for char in '[epic] ':
                                                listthing.remove(char)
                                            i = 0
                                            thing = ''
                                            while i < len(listthing):
                                                thing = f'{thing}{listthing[i]}'
                                                i += 1

                                        if '[legendary] ' in thing:
                                            listthing = []
                                            for char in thing:
                                                listthing.append(char)
                                            for char in '[legendary] ':
                                                listthing.remove(char)
                                            i = 0
                                            thing = ''
                                            while i < len(listthing):
                                                thing = f'{thing}{listthing[i]}'
                                                i += 1

                                        scrollTxt('ENCHANTING WEAPON')
                                        i = random.randint(1, 100)
                                        if i > 0 and i < 51:
                                            inv.append(f'[common] {thing}')
                                            scrollTxt(f'[common] {thing}')
                                            thing = f'[common] {thing}'
                                        if i > 50 and i < 71:
                                            inv.append(f'[rusty] {thing}')
                                            scrollTxt(f'[rusty] {thing}')
                                            thing = f'[rusty] {thing}'
                                        if i > 70 and i < 91:
                                            inv.append(f'[rare] {thing}')
                                            scrollTxt(f'[rare] {thing}')
                                            thing = f'[rare] {thing}'
                                        if i > 90 and i < 98:
                                            inv.append(f'[epic] {thing}')
                                            scrollTxt(f'[epic] {thing}')
                                            thing = f'[epic] {thing}'
                                        if i > 97 and i < 101:
                                            inv.append(f'[legendary] {thing}')
                                            scrollTxt(f'[legendary] {thing}')
                                            thing = f'[legendary] {thing}'

                                        scrollTxt(f'-{Fore.LIGHTRED_EX}10{Fore.WHITE} Gems')
                                        gems -= 10
                                        enchanting = True
                                        while enchanting == True:
                                            scrollTxt('re-enchant? yes/no')
                                            answer = input(f'{Fore.GREEN}')
                                            print(f'{Fore.WHITE}')

                                            if answer == 'yes':
                                                if gems > 9:
                                                    inv.remove(thing)

                                                    if '[common] ' in thing:
                                                        listthing = []
                                                        for char in thing:
                                                            listthing.append(char)
                                                        for char in '[common] ':
                                                            listthing.remove(char)
                                                        i = 0
                                                        thing = ''
                                                        while i < len(listthing):
                                                            thing = f'{thing}{listthing[i]}'
                                                            i += 1

                                                    if '[rusty] ' in thing:
                                                        listthing = []
                                                        for char in thing:
                                                            listthing.append(char)
                                                        for char in '[rusty] ':
                                                            listthing.remove(char)
                                                        i = 0
                                                        thing = ''
                                                        while i < len(listthing):
                                                            thing = f'{thing}{listthing[i]}'
                                                            i += 1

                                                    if '[rare] ' in thing:
                                                        listthing = []
                                                        for char in thing:
                                                            listthing.append(char)
                                                        for char in '[rare] ':
                                                            listthing.remove(char)
                                                        i = 0
                                                        thing = ''
                                                        while i < len(listthing):
                                                            thing = f'{thing}{listthing[i]}'
                                                            i += 1

                                                    if '[epic] ' in thing:
                                                        listthing = []
                                                        for char in thing:
                                                            listthing.append(char)
                                                        for char in '[epic] ':
                                                            listthing.remove(char)
                                                        i = 0
                                                        thing = ''
                                                        while i < len(listthing):
                                                            thing = f'{thing}{listthing[i]}'
                                                            i += 1

                                                    if '[legendary] ' in thing:
                                                        listthing = []
                                                        for char in thing:
                                                            listthing.append(char)
                                                        for char in '[legendary] ':
                                                            listthing.remove(char)
                                                        i = 0
                                                        thing = ''
                                                        while i < len(listthing):
                                                            thing = f'{thing}{listthing[i]}'
                                                            i += 1

                                                    scrollTxt('ENCHANTING WEAPON')
                                                    i = random.randint(1, 100)
                                                    if i > 0 and i < 51:
                                                        inv.append(f'[common] {thing}')
                                                        scrollTxt(f'[common] {thing}')
                                                        thing = f'[common] {thing}'
                                                    if i > 50 and i < 71:
                                                        inv.append(f'[rusty] {thing}')
                                                        scrollTxt(f'[rusty] {thing}')
                                                        thing = f'[rusty] {thing}'
                                                    if i > 70 and i < 91:
                                                        inv.append(f'[rare] {thing}')
                                                        scrollTxt(f'[rare] {thing}')
                                                        thing = f'[rare] {thing}'
                                                    if i > 90 and i < 98:
                                                        inv.append(f'[epic] {thing}')
                                                        scrollTxt(f'[epic] {thing}')
                                                        thing = f'[epic] {thing}'
                                                    if i > 97 and i < 101:
                                                        inv.append(f'[legendary] {thing}')
                                                        scrollTxt(f'[legendary] {thing}')
                                                        thing = f'[legendary] {thing}'

                                                    scrollTxt(f'-{Fore.LIGHTRED_EX}10{Fore.WHITE} Gems')
                                                    gems -= 10
                                                else:
                                                    scrollTxt('Not enough gems')
                                                    enchanting = False
                                            else:
                                                enchanting = False
                                i += 1
                            if equiped is False:
                                scrollTxt(f"{Fore.WHITE}That\'s not a weapon")
                                thing = 'none'
                    else:
                        scrollTxt('Not enough gems')
                        scrollTxt(f'Gems: {Fore.LIGHTRED_EX}{gems}{Fore.WHITE}')
                else:
                    scrollTxt('You have nothing to equip')

            if inv_action == "equip shield":
                if items_local > 0:
                    scrollTxt('What would you like to equip')
                    thing = 'none'
                    while thing == 'none':
                        thing = input(f"{Fore.GREEN}")

                        i = 0
                        equiped = False
                        while i < len(inv):
                            if thing == inv[i]:
                                if equiped is False:
                                    scrollTxt(f'{Fore.WHITE}Shield equipped')
                                equiped = True
                                shield = thing
                                if shield == 'iron shield':
                                    shield_power = 6
                                if shield == 'steel shield':
                                    shield_power = 8
                                if shield == 'travelers shield':
                                    shield_power = 4
                                if shield == 'HALLOW SHIELD':
                                    shield_power = 9
                                if shield == 'Ghost Shield':
                                    shield_power = 7
                                if shield == 'legend shield':
                                    shield_power = 12
                                if shield == 'flame shield':
                                    shield_power = 8
                                if shield == 'Pilgrim\'s Hat':
                                    shield_power = 10
                                if shield == 'magma shield':
                                    shield_power = 7
                            i += 1
                        if equiped is False:
                            scrollTxt(f"{Fore.WHITE}That\'s not a shield")
                            thing = 'none'
                else:
                    scrollTxt('You have nothing to equip')

            if inv_action == "remove":
                if items_local > 0:
                    scrollTxt('What would you like to remove')
                    thing = 'none'
                    while thing == 'none':
                        thing = input(f"{Fore.GREEN}")

                        i = 0
                        removed = False
                        while i < len(inv):
                            if thing == inv[i]:
                                scrollTxt(f'{Fore.WHITE}{thing} removed')
                                removed = True
                                items_local -= 1
                                inv.remove(thing)
                            i += 1
                        if removed is False:
                            scrollTxt(f"{Fore.WHITE}That\'s not a item")
                            thing = 'none'
                else:
                    scrollTxt('You have nothing to remove')

            if inv_action == 'consume':
                if items_local > 0:
                    scrollTxt('What would you like to consume?')
                    thing = 'none'
                    while thing == 'none':
                        thing = input(f"{Fore.GREEN}")

                        i = 0
                        removed = False
                        while i < len(inv):
                            if thing == inv[i]:
                                lvl1_hp_bonus = random.randint(1, 3)
                                lvl2_hp_bonus = random.randint(3, 5)
                                lvl3_hp_bonus = random.randint(7, 13)
                                lvl4_hp_bonus = random.randint(20, 30)

                                if 'Titan' in thing or 'Everfire' in thing or 'Evercrystal' in thing or 'Legend' in thing:
                                    hp_bonus = lvl4_hp_bonus
                                elif 'Gourmet' in thing or 'Blessed' in thing or 'Golden' in thing or 'Event' in thing:
                                    hp_bonus = lvl3_hp_bonus
                                elif 'Dwarven' in thing or 'Elven' in thing or 'Hardy' in thing:
                                    hp_bonus = lvl2_hp_bonus
                                else:
                                    hp_bonus = lvl1_hp_bonus

                                hp += hp_bonus

                                scrollTxt(f'{Fore.WHITE}You consumed a {Fore.WHITE}{thing}')
                                scrollTxt(f'+{Fore.RED}{hp_bonus}{Fore.WHITE} health')
                                removed = True
                                items_local -= 1
                                inv.remove(thing)
                                i = len(inv)

                            i += 1
                        if removed is False:
                            scrollTxt(f"{Fore.WHITE}That\'s not a item")
                            thing = 'none'
                else:
                    scrollTxt('You have nothing to consume')

            if inv_action == 'inv':
                bar()
                printInv(inv)
                bar()

            if inv_action == 'consume all':

                if items_local > 0:
                    scrollTxt('What would you like to consume?')
                    thing = 'none'
                    while thing == 'none':
                        thing = input(f"{Fore.GREEN}")

                        i = 0
                        removed = False
                        for i in inv:
                            if thing == i:
                                lvl1_hp_bonus = random.randint(1, 3)
                                lvl2_hp_bonus = random.randint(3, 5)
                                lvl3_hp_bonus = random.randint(7, 13)
                                lvl4_hp_bonus = random.randint(20, 30)

                                if 'Titan' in thing or 'Everfire' in thing or 'Evercrystal' in thing or 'Legend' in thing:
                                    hp_bonus = lvl4_hp_bonus
                                elif 'Gourmet' in thing or 'Blessed' in thing or 'Golden' in thing or 'Event' in thing:
                                    hp_bonus = lvl3_hp_bonus
                                elif 'Dwarven' in thing or 'Elven' in thing or 'Hardy' in thing:
                                    hp_bonus = lvl2_hp_bonus
                                else:
                                    hp_bonus = lvl1_hp_bonus

                                hp += hp_bonus

                                scrollTxt(f'{Fore.WHITE}You consumed a {Fore.WHITE}{thing}')
                                scrollTxt(f'+{Fore.RED}{hp_bonus}{Fore.WHITE} health')
                                removed = True
                                items_local -= 1
                                inv.remove(thing)
                        if removed is False:
                            scrollTxt(f"{Fore.WHITE}That\'s not a item")
                            thing = 'none'
                else:
                    scrollTxt('You have nothing to consume')

            if inv_action == 'open crate':
                scrollTxt('What crate would you like to open?')
                commands = ['common crate', 'rare crate', 'epic crate', 'legendary crate', 'thanksgiving crate']
                inputCommands(commands, '')
                print()
                if answer == 'common crate':
                    inv_text = ''
                    for i in inv:
                        inv_text = f'{inv_text}{i}'
                    if 'common crate' in inv_text:
                        scrollTxt('Opening crate...')
                        inv.remove('common crate')
                        time.sleep(1)
                        gold = random.randint(20, 50)
                        scrollTxt(f'You got {Fore.YELLOW}{gold}{Fore.WHITE} Gold!')
                        gp += gold
                        food_thing = random.randint(1, 3)
                        if food_thing == 1:
                            scrollTxt(f'You got an apple')
                            inv.append('apple')
                        if food_thing == 1:
                            scrollTxt('You got some bread')
                            inv.append('bread')
                            inv.append('bread')
                    else:
                        scrollTxt('You don\'t have that crate')

                if answer == 'rare crate':
                    inv_text = ''
                    for i in inv:
                        inv_text = f'{inv_text}{i}'
                    if answer in inv_text:
                        inv.remove('rare crate')
                        scrollTxt('Opening crate...')
                        time.sleep(1)
                        gold = random.randint(50, 100)
                        scrollTxt(f'You got {Fore.YELLOW}{gold}{Fore.WHITE} Gold!')
                        gp += gold
                        food_thing = random.randint(1, 3)
                        if food_thing == 1:
                            scrollTxt(f'You got an hardy apple')
                            inv.append('Hardy apple')
                        if food_thing == 2:
                            scrollTxt('You got some elven bread')
                            inv.append('elven bread')
                            inv.append('elven bread')

                        weapon_yes = random.randint(1, 5)
                        if weapon_yes == 5:
                            scrollTxt('You got a steel sword!')
                            inv.append('steel sword')
                    else:
                        scrollTxt('You do not have that crate')

                if answer == 'epic crate':
                    inv_text = ''
                    for i in inv:
                        inv_text = f'{inv_text}{i}'
                    if answer in inv_text:
                        inv.remove('epic crate')
                        scrollTxt('Opening crate...')
                        time.sleep(1)
                        gold = random.randint(100, 500)
                        scrollTxt(f'You got {Fore.YELLOW}{gold}{Fore.WHITE} Gold!')
                        gp += gold
                        food_thing = random.randint(1, 3)
                        if food_thing == 1:
                            scrollTxt(f'You got a blessed apple')
                            inv.append('Blessed apple')
                        if food_thing == 2:
                            scrollTxt('You got some golden bread')
                            inv.append('Golden bread')
                            inv.append('Golden bread')

                        weapon_yes = random.randint(1, 5)
                        if weapon_yes == 5:
                            scrollTxt('You got a magic sword!')
                            inv.append('magic sword')
                    else:
                        scrollTxt('You do not have that crate')

                if answer == 'legendary crate':
                    inv_text = ''
                    for i in inv:
                        inv_text = f'{inv_text}{i}'
                    if answer in inv_text:
                        inv.remove('legendary crate')
                        scrollTxt('Opening crate...')
                        time.sleep(1)
                        gold = random.randint(500, 1000)
                        scrollTxt(f'You got {Fore.YELLOW}{gold}{Fore.WHITE} Gold!')
                        gp += gold
                        food_thing = random.randint(1, 3)
                        if food_thing == 1:
                            scrollTxt(f'You got a Everfire apple')
                            inv.append('Everfire apple')
                        if food_thing == 2:
                            scrollTxt('You got some golden bread')
                            inv.append('Golden bread')
                            inv.append('Golden bread')

                        weapon_yes = random.randint(1, 5)
                        if weapon_yes == 5:
                            scrollTxt('You got a [rare] cursed orb!')
                            inv.append('[rare] cursed orb')

                    else:
                        scrollTxt('You do not have that crate')

                if answer == 'thanksgiving crate':
                    inv_text = ''
                    for i in inv:
                        inv_text = f'{inv_text}{i}'
                    if answer in inv_text:
                        inv.remove('thanksgiving crate')
                        scrollTxt('Opening crate...')
                        time.sleep(1)
                        gold = random.randint(100, 200)
                        scrollTxt(f'You got {Fore.YELLOW}{gold}{Fore.WHITE} Gold!')
                        gp += gold

                        xp = random.randint(10, 50)
                        scrollTxt(f'You got {Fore.YELLOW}{xp}{Fore.WHITE} EXP!')
                        exp += xp
                        if exp > expNext:
                            exp -= expNext
                            scrollTxt('You leveled up!')
                            lvl += 1
                            expNext += (expNext / 4)
                            expNext = int(expNext)
                            max_hp += 20

                        food_thing = random.randint(1, 8)
                        if food_thing == 1:
                            scrollTxt(f'You got a event turkey')
                            inv.append('Event Turkey')
                        if food_thing == 2:
                            scrollTxt('You got some Golden pudding')
                            inv.append('Golden pudding')
                            inv.append('Golden pudding')

                        weapon_yes = random.randint(1, 15)

                        if weapon_yes == 5:
                            scrollTxt('You got a Pilgrim\'s Blade!')
                            inv.append('Pilgrim\'s Blade')
                        if weapon_yes == 15:
                            scrollTxt('You got the pilgrim\'s hat!')
                            inv.append('Pilgrim\'s Hat')
                        if weapon_yes == 1:
                            scrollTxt('You got the pilgrim\'s blessing')
                            scrollTxt('Would you like to become a pilgrim? yes/no')
                            answer = input(f'{Fore.GREEN}')
                            print(f'{Fore.WHITE}')
                            if 'y' in answer or 'Y' in answer:
                                scrollTxt('Class: Pilgrim')
                                character_class = 'Pilgrim'

                        inv_text = ''
                        turkey_rage = 0
                        for i in inv:
                            if i == 'Turkey' or i == 'Even Turkey':
                                turkey_rage += 1

                        if turkey_rage > 4:
                            bar()
                            scrollTxt('You have angered the ANCIENT TITAN TURKEY')
                            scrollTxt('(you have too much turkey...)')
                            battle('the ANCIENT TITAN TURKEY',
                                   ['slash', 'stab', 'charge', 'acid blast', 'fire blast', 'reaping blow', 'fly',
                                    'claw',
                                    'smash',
                                    'rest', 'wild slash', 'fangs'],
                                   random.randint(30, 70) * lvl, 1 * lvl, 10, 1.5 * lvl, 600, 500)
                            if ran is True:
                                scrollTxt('You can\'t escape impending doom')
                                quit()
                            else:
                                if lose is True:
                                    scrollTxt('You died to the ANCIENT TITAN TURKEY')
                                    quit()
                                else:
                                    scrollTxt('You defeated the ANCIENT TITAN TURKEY!')
                                    scrollTxt(f'+ {Fore.LIGHTRED_EX}20{Fore.WHITE} GEMS')
                                    how_many_t = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]
                                    for i in how_many_t:
                                        scrollTxt('+ Turkey')
                                        inv.append('Turkey')
                                    gems += 20
                                    db.get(character)[18] = gems

                    else:
                        scrollTxt('You do not have that crate')

                print()
        answer = character
        db.get(answer)[18] = gems


    def inputShop(commands, extraTxt, cost):
        global new_wares
        new_wares = wares
        global nothing
        nothing = False
        global answer
        answer = "none"
        global gp
        global items_local
        items_local = items
        while answer == "none":
            answer = input(f"{Fore.GREEN}")
            sys.stdout.write(f"{Fore.WHITE}")
            i = 0
            stop = False
            while i < len(commands):
                costTxt = False
                if stop is True:
                    i = len(commands)
                else:
                    if answer == 'nothing':
                        nothing = True
                        stop = True
                        costTxt = True
                        i = len(commands)

                    elif answer == f"{extraTxt}{commands[i]}":
                        stop = True
                        if gp < cost[i - 1]:
                            scrollTxt("You can't afford that")
                            print_gp()
                            stop = True
                            costTxt = True
                            i = len(commands)

                        else:
                            inv.append(commands[i])
                            gp -= cost[i - 1]
                            items_local -= 1
                            scrollTxt(f'+{commands[i]}')
                            scrollTxt(f'-{Fore.YELLOW}{cost[i - 1]}{Fore.WHITE}')

                    else:
                        stop = False
                        i += 1
            if stop is False:
                if costTxt is False:
                    scrollTxt("That's not an item")
                answer = "none"


    def inputShopH(commands, extraTxt, cost):
        global new_wares
        new_wares = wares
        global nothing
        nothing = False
        global answer
        answer = "none"
        global candy
        global items_local
        global character_class
        global lvl
        global max_hp

        items_local = items
        while answer == "none":
            answer = input(f"{Fore.GREEN}")
            sys.stdout.write(f"{Fore.WHITE}")
            i = 0
            stop = False
            while i < len(commands):
                costTxt = False
                if stop is True:
                    i = len(commands)
                else:
                    if answer == 'nothing':
                        nothing = True
                        stop = True
                        costTxt = True
                        i = len(commands)

                    elif answer == f"{extraTxt}{commands[i]}":
                        stop = True
                        if candy < cost[i - 1]:
                            scrollTxt("You can't afford that")
                            scrollTxt(f'Candy: {Fore.LIGHTMAGENTA_EX}{candy}{Fore.WHITE}')
                            stop = True
                            costTxt = True
                            i = len(commands)

                        else:
                            if commands[i] == 'Hallow Soldier':
                                scrollTxt('Class: Hallow Soldier')
                                character_class = 'Hallow Solider'
                                lvl += 1
                                max_hp += 10
                                candy -= cost[i - 1]
                                scrollTxt(f'-{Fore.LIGHTMAGENTA_EX}{cost[i - 1]}{Fore.WHITE}')
                                scrollTxt('+1 lvl')
                            else:
                                inv.append(commands[i])
                                candy -= cost[i - 1]
                                items_local -= 1
                                scrollTxt(f'+{commands[i]}')
                                scrollTxt(f'-{Fore.LIGHTMAGENTA_EX}{cost[i - 1]}{Fore.WHITE}')

                    else:
                        stop = False
                        i += 1
            if stop is False:
                if costTxt is False:
                    scrollTxt("That's not an item")
                answer = "none"


    def battle(monster_name, monster_moves, monster_hp, monster_dex, monster_def,
               monster_power, monster_drop, monster_exp):
        system('clear')
        bar()

        global exp
        global expNext
        global lvl

        global gp

        global ran
        ran = False

        global max_hp

        global shield_power

        global attack_buff

        global lose
        lose = False

        lvl1_spells_left = lvl1_spells
        if len(lvl1_available_spells) > 0:
            lvl1_spell_choice = random.choice(lvl1_available_spells)
        else:
            lvl1_spell_choice = 'none'

        lvl2_spells_left = lvl2_spells
        if len(lvl2_available_spells) > 0:
            lvl2_spell_choice = random.choice(lvl2_available_spells)
        else:
            lvl2_spell_choice = 'none'

        turn = 'player'
        battle_over = False

        attack_buff = lvl

        attack_buff += int(lvl / 3)

        monster_hp += (lvl - 1) * 10

        monster_exp += (lvl - 1) * 10

        global hp

        poison = False
        global character
        poison_turns = 0

        global bullets
        global arrows

        global inv

        global answer

        global gems

        global max_hp
        new_hp = hp

        if new_hp < max_hp:
            new_hp = max_hp

        global items

        dropped = False

        monster_attack_buff = monster_power

        monster_attack_buff += ((monster_power + int(lvl / 3)) / 5) * 4

        burn = False
        burn_turns = 0

        freeze = False
        freeze_turns = 0

        global weapons

        global candy

        speed_buff = lvl - 1
        defense_buff = lvl - 1

        monster_burn = False
        monster_burn_turns = 0

        monster_poison = False
        monster_poison_turns = 0

        global inv

        run = False
        go_again = False

        monster_dodge = False

        lvl1_local_spells = []
        addList(lvl1_local_spells, lvl1_available_spells)

        lvl2_local_spells = []
        addList(lvl2_local_spells, lvl2_available_spells)

        poisoned = False
        burned = False
        frozen = False

        monster_boss_check = monster_name
        if 'the ' in monster_boss_check:
            monster_boss_check_list = []
            for char in monster_boss_check:
                monster_boss_check_list.append(char)
            for char in 'the ':
                monster_boss_check_list.remove(char)
            i = 0
            monster_boss_check = ''
            while i < len(monster_boss_check_list):
                monster_boss_check = f'{monster_boss_check}{monster_boss_check_list[i]}'
                i += 1

        if monster_boss_check.isupper():
            monster_boss_check = f'{Style.DIM}{Fore.RED}{monster_boss_check}{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}'
            monster_name = f'the {monster_boss_check}'
            scrollTxt(f'~{Style.DIM}{Fore.RED}BOSS FIGHT{Fore.WHITE}{Style.RESET_ALL}{Style.BRIGHT}~')
            boss = True
        else:
            boss = False

        if turn == "player":
            scrollTxt("You go first")
            scrollTxt(f"Your weapon is {weapons}")
            scrollTxt(f"You know {lvl1_local_spells} ~ lvl 1 spells")
            scrollTxt(f"You know {lvl2_local_spells} ~ lvl 2 spells")
            scrollTxt(f"You have {lvl1_spells} spell slots ~ lvl 1 spells")
            scrollTxt(f"You have {lvl2_spells} spell slots ~ lvl 2 spells")
            bar()
            scrollTxt(f'You are battling {monster_name}')
            scrollTxt(
                f'{monster_name} has {Fore.RED}{monster_hp}{Fore.WHITE} health')
        else:
            scrollTxt(f"{monster_name} goes first")
            scrollTxt(f"Your weapon is {weapons}")
            scrollTxt(f"You know {lvl1_available_spells} ~ lvl 1 spells")
            scrollTxt(f"You know {lvl2_available_spells} ~ lvl 2 spells")
            scrollTxt(f"You have {lvl1_spells} spell slots ~ lvl 1 spells")
            scrollTxt(f"You have {lvl2_spells} spell slots ~ lvl 2 spells")
            bar()
            scrollTxt(f'You are battling {monster_name}')
            scrollTxt(
                f'{monster_name} has {Fore.RED}{monster_hp}{Fore.WHITE} health')

        bar()
        answer = ''
        scrollTxt('How would you like to attack?')
        scrollTxt('rage, steady, rapid')
        commands = ['rage', 'steady', 'rapid']
        inputCommands(commands, '')

        print()
        if answer == 'rage':
            scrollTxt('Rage fills you as you get ready for battle')
            attack_buff = int(attack_buff * 1.5)
            speed_buff -= int(2 * (lvl / 5))

        if answer == 'steady':
            scrollTxt('You steady yourself and take a deep breath')
            speed_buff += int(1 * (lvl / 5))
            defense_buff += int(5 * (lvl / 5))

        if answer == 'rapid':
            scrollTxt('You are stuck with lightning and filled with speed')
            speed_buff += int(6 * (lvl / 5))
            defense_buff -= int(1 * (lvl / 5))

        while battle_over is False:
            if turn == 'player':
                bar()
                poisoned = False
                burned = False
                frozen = False

                if monster_poison:
                    hp -= int(1 * monster_attack_buff)
                    monster_poison_turns -= 1
                    if monster_poison_turns < 1:
                        monster_poison = False
                    scrollTxt(f"You took {Fore.GREEN}{int(1 * monster_attack_buff)}{Fore.WHITE} damage from poison")

                if monster_burn:
                    hp -= int(2 * monster_attack_buff)
                    monster_burn_turns -= 1
                    if monster_burn_turns < 1:
                        monster_burn = False
                    scrollTxt(f"You took {Fore.GREEN}{int(2 * monster_attack_buff)}{Fore.WHITE} damage from burning")

                if hp < 1:
                    scrollTxt(f"You died, {monster_name} killed you")
                    lose = True
                    scrollTxt('[ENTER] to continue')
                    input()
                    battle_over = True

                    system('clear')
                elif run is True:
                    scrollTxt("You ran away")
                    ran = True
                    scrollTxt('[ENTER] to continue')
                    input()
                    battle_over = True
                    system('clear')
                    break
                else:
                    scrollTxt("It's your turn to attack...")
                    if weapons != 'fists':
                        scrollTxt(
                            f"Commands: \"1 or magic\", \"2 or {weapons}\", \"3 or heal\", \"4 or dodge\", \"5 or run\", \"6 or throw {weapons}\""
                        )
                    else:
                        scrollTxt(
                            f"Commands: \"1 or magic\", \"2 or {weapons}\", \"3 or heal\", \"4 or dodge\", \"5 or run\"")

                    attack = "none"

                    while attack == "none":
                        if weapons != 'fists':
                            attack = input(f"{Fore.GREEN}")
                            if attack != "magic" and attack != weapons and attack != "heal" and attack != 'run' and attack != 'dodge' and attack != f'throw {weapons}' and attack != '1' and attack != '2' and attack != '3' and attack != '4' and attack != '5' and attack != '6':
                                attack = "none"
                            if attack == "none":
                                scrollTxt(f"{Fore.WHITE}That's not an attack")
                        else:
                            attack = input(f"{Fore.GREEN}")
                            if attack != "magic" and attack != weapons and attack != "heal" and attack != 'run' and attack != 'dodge' and attack != f'throw {weapons}' and attack != '1' and attack != '2' and attack != '3' and attack != '4' and attack != '5':
                                attack = "none"
                            if attack == "none":
                                scrollTxt(f"{Fore.WHITE}That's not an attack")

                    speed = False

                    print("")
                    if attack == "magic" or attack == '1':
                        scrollTxt(f"{Fore.WHITE}~Spells~")
                        scrollTxt(">lvl 1<")
                        if lvl1_spells_left > 0 or lvl2_spells_left > 0:
                            i = lvl1_spells_left
                            lvl1_spell_write = []

                            while i > 0:
                                lvl1_spell_write.append(lvl1_spell_choice)
                                i -= 1
                                if len(lvl1_available_spells) > 0:
                                    lvl1_spell_choice = random.choice(lvl1_available_spells)
                                else:
                                    lvl1_spell_choice = 'none'
                            i = 0
                            while i < lvl1_spells_left:
                                scrollTxt(lvl1_spell_write[i])
                                i += 1
                            print("")

                            scrollTxt(">lvl 2<")
                            i = lvl2_spells_left
                            lvl2_spell_write = []
                            while i > 0:
                                lvl2_spell_write.append(lvl2_spell_choice)
                                i -= 1
                                if len(lvl2_available_spells) > 0:
                                    lvl2_spell_choice = random.choice(lvl2_available_spells)
                                else:
                                    lvl2_spell_choice = 'none'
                            i = 0
                            while i < lvl2_spells_left:
                                scrollTxt(lvl2_spell_write[i])
                                i += 1

                            magic = "none"
                            no = True
                            while magic == "none":
                                no = True
                                magic = input(f"{Fore.GREEN}")

                                lvl1_allspells_text = ''
                                for i in lvl1_available_spells:
                                    lvl1_allspells_text = f'{lvl1_allspells_text}{i}'

                                lvl2_allspells_text = ''
                                for i in lvl2_available_spells:
                                    lvl2_allspells_text = f'{lvl2_allspells_text}{i}'

                                if magic not in lvl2_allspells_text and magic not in lvl1_allspells_text:
                                    no = False

                                if no is False:
                                    scrollTxt(f"{Fore.WHITE}That's not a spell")
                                    magic = "none"

                            lvl1 = False
                            if lvl1_spells_left > 0:
                                i = len(lvl1_available_spells)
                                while i > 0 and lvl1 is False:
                                    if str(magic) == str(lvl1_available_spells[i - 1]):
                                        lvl1 = True
                                    else:
                                        lvl1 = False
                                    i -= 1

                                if lvl1 is True:
                                    lvl1_spells_left -= 2
                                    lvl1_spells_left += 1

                            lvl2 = False
                            if lvl2_spells_left > 0:
                                i2 = len(lvl2_available_spells)
                                while i2 > 0 and lvl2 is False:
                                    if str(magic) == str(lvl2_available_spells[i2 - 1]):
                                        lvl2 = True
                                    else:
                                        lvl2 = False
                                    i2 -= 1
                                if lvl2 == True:
                                    lvl2_spells_left -= 2
                                    lvl2_spells_left += 1

                            hit = 0
                            buff = False
                            health = False
                            dodge = False
                            run = False
                            speed = False

                            if magic == "magic missile":
                                damage = int(((random.randint(1, 2)) + (random.randint(1, 2)) + (
                                    random.randint(1, 2))) * attack_buff)

                                text = f"{Fore.WHITE}You hit {monster_name} with 3 magic missiles dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                                hit = random.randint(1, 20) + dex * 2

                            elif magic == "poison shards":
                                poison = True
                                poison_turns += random.randint(3, 6)
                                damage = 0
                                text = f"{Fore.WHITE}You hit {monster_name} with a dose of poison dealing damage for {Fore.GREEN}{poison_turns}{Fore.WHITE} turns\n{monster_name} is now poisoned"
                                hit = 11000
                                poisoned = True

                            elif magic == "health buff":
                                hit = 0
                                health = True
                                damage = 0
                                heal = random.randint(2, 5) * lvl
                                text = f"{Fore.WHITE}You used health buff and healed your self"

                            elif magic == "attack buff":
                                hit = 0
                                buff = True
                                attack_buff += 0.5
                                damage = 0
                                text = f"{Fore.WHITE}You used attack buff and made your self stronger"

                            elif magic == "speed buff":
                                hit = 0
                                buff = True
                                damage = 0
                                speed_buff += 2
                                text = f"{Fore.WHITE}You used speed buff and made your self faster"

                            elif magic == "mage armor":
                                hit = 0
                                buff = True
                                damage = 0
                                defense_buff += 2
                                text = f"{Fore.WHITE}You used mage armor and made your self tougher"

                            elif magic == "firebolt":
                                damage = int((random.randint(2, 4) + (random.randint(2, 4))) *
                                             attack_buff)
                                burn = True
                                burn_turns += random.randint(1, 2)
                                text = f"{Fore.WHITE}You hit {monster_name} with a firebolt dealing {Fore.GREEN}{damage}{Fore.WHITE} damage and causing {monster_name} to burn for {Fore.GREEN}{burn_turns}{Fore.WHITE} turns"
                                hit = random.randint(1, 20) + dex
                                burned = True

                            elif magic == "lightning touch":
                                damage = int((random.randint(1, 2) + (random.randint(1, 2))) *
                                             attack_buff)
                                burn = True
                                burn_turns += 1
                                text = f"{Fore.WHITE}You hit {monster_name} with your fists of lightning dealing {Fore.GREEN}{damage}{Fore.WHITE} damage and causing {monster_name} to burn for {Fore.GREEN}{burn_turns}{Fore.WHITE} turns"
                                hit = random.randint(1, 20) + dex - 3
                                burned = True

                            elif magic == "ice shards":
                                damage = int((random.randint(1, 3) + (random.randint(1, 3))) *
                                             attack_buff)
                                freeze = True
                                freeze_turns += 1
                                text = f"{Fore.WHITE}You hit {monster_name} with a hundred ice shards, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage and causing {monster_name} to freeze for {Fore.GREEN}{freeze_turns}{Fore.WHITE} turns"
                                hit = random.randint(1, 20) + dex
                                frozen = True

                            elif magic == "drain":
                                damage_dealing = int(
                                    (random.randint(1, 2) +
                                     (random.randint(1, 2)) + 1) * attack_buff)
                                damage = damage_dealing

                                text = f"{Fore.WHITE}You drained {monster_name}\'s life force, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage" \
                                       f"\nYou healed {Fore.RED}{damage_dealing}{Fore.WHITE} health"
                                hp += damage_dealing
                                hit = random.randint(1, 20) + dex * 2

                            elif magic == 'aerial slash':
                                damage = int((random.randint(1, 2) + (random.randint(1, 2)) +
                                              (random.randint(1, 4))) * attack_buff)

                                text = f"{Fore.WHITE}You fly into the air, slicing {monster_name} with an airborne slash dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n[AIRBORNE] You go again"
                                hit = random.randint(1, 20) + dex * 3
                                go_again = True

                        else:
                            hit = 1100
                            damage = 0
                            text = "you have no spells"

                    if attack == f"{weapons}" or attack == f'throw {weapons}' or attack == '2' or attack == '6':
                        health = False
                        buff = False
                        dodge = False
                        run = False

                        common = False
                        rare = False
                        epic = False
                        rusty = False
                        legendary = False
                        if 1 == 1:
                            thing = weapons
                            if '[common] ' in thing:
                                common = True
                                listthing = []
                                for char in thing:
                                    listthing.append(char)
                                for char in '[common] ':
                                    listthing.remove(char)
                                i = 0
                                thing = ''
                                while i < len(listthing):
                                    thing = f'{thing}{listthing[i]}'
                                    i += 1

                            if '[rusty] ' in thing:
                                rusty = True
                                listthing = []
                                for char in thing:
                                    listthing.append(char)
                                for char in '[rusty] ':
                                    listthing.remove(char)
                                i = 0
                                thing = ''
                                while i < len(listthing):
                                    thing = f'{thing}{listthing[i]}'
                                    i += 1

                            if '[rare] ' in thing:
                                rare = True
                                listthing = []
                                for char in thing:
                                    listthing.append(char)
                                for char in '[rare] ':
                                    listthing.remove(char)
                                i = 0
                                thing = ''
                                while i < len(listthing):
                                    thing = f'{thing}{listthing[i]}'
                                    i += 1

                            if '[epic] ' in thing:
                                epic = True
                                listthing = []
                                for char in thing:
                                    listthing.append(char)
                                for char in '[epic] ':
                                    listthing.remove(char)
                                i = 0
                                thing = ''
                                while i < len(listthing):
                                    thing = f'{thing}{listthing[i]}'
                                    i += 1

                            if '[legendary] ' in thing:
                                legendary = True
                                listthing = []
                                for char in thing:
                                    listthing.append(char)
                                for char in '[legendary] ':
                                    listthing.remove(char)
                                i = 0
                                thing = ''
                                while i < len(listthing):
                                    thing = f'{thing}{listthing[i]}'
                                    i += 1
                        weapons = thing

                        if weapons == "bow":
                            if arrows > 0:
                                hit = random.randint(1, 20) + dex
                                damage = int(random.randint(1, 7) * attack_buff)
                                if hit > monster_def:
                                    arrows -= 1
                                text = f"{Fore.WHITE}You stabbed {monster_name} with an arrows, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n-1 arrows\n{arrows} arrowss left"
                            else:
                                hit = 11000
                                damage = 0
                                text = f"{Fore.WHITE}You have no arrows"

                        elif weapons == "fire bow":
                            if arrows > 0:
                                hit = random.randint(1, 20) + dex
                                damage = int(random.randint(1, 7) * attack_buff)
                                burn = True
                                burn_turns += 1
                                if hit > monster_def:
                                    arrows -= 1
                                text = f"{Fore.WHITE}You stabbed {monster_name} with a flame lit arrow, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage" \
                                       f"\nCausing {monster_name} to burn for {burn_turns} turns" \
                                       f"\n-1 arrow" \
                                       f"\n{arrows} arrows left"
                                burned = False
                            else:
                                hit = 11000
                                damage = 0
                                text = f"{Fore.WHITE}You have no arrows"

                        elif weapons == "dwarven bow":
                            if arrows > 0:
                                hit = random.randint(1, 20) + dex
                                damage = int(random.randint(1, 12) * attack_buff)
                                if hit > monster_def:
                                    arrows -= 1
                                text = f"{Fore.WHITE}You stabbed {monster_name} with an dwarven arrow, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n-1 arrow\n{arrows} arrows left"

                            else:
                                hit = 11000
                                damage = 0
                                text = f"{Fore.WHITE}You have no arrows"

                        elif weapons == "staff":
                            damage = int(random.randint(1, 6) * attack_buff)
                            text = f"{Fore.WHITE}You smacked {monster_name} with your staff, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            hit = random.randint(1, 20) + (dex * 2)

                        elif weapons == "sword":
                            damage = int(random.randint(1, 6) * attack_buff)
                            text = f"{Fore.WHITE}You slashed {monster_name} with your sword, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            hit = random.randint(1, 20) + dex

                        elif weapons == "Pilgrim\'s Blade":
                            damage = int(random.randint(1, 10) * attack_buff)
                            text = f"{Fore.WHITE}You slashed {monster_name} with your Pilgrim\'s Blade, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n[THANKSGIVING?] + Turkey"
                            hit = random.randint(1, 20) + dex
                            inv.append('Turkey')

                        elif weapons == "frost blade":
                            damage = int(random.randint(1, 12) * attack_buff)
                            freeze = True
                            freeze_turns += random.randint(1, 3)
                            text = f"{Fore.WHITE}You slashed {monster_name} with your frost blade, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n" \
                                   f"Causing {monster_name} to freeze for {freeze_turns} turns"
                            hit = random.randint(1, 20) + dex
                            frozen = True

                        elif weapons == "scimitar":
                            damage = int(random.randint(1, 5) * attack_buff)
                            hit = random.randint(1, 20) + (dex * 2)
                            i = random.randint(1, 6)
                            if i != 1:
                                text = f"{Fore.WHITE}You slashed {monster_name} with your scimitar, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            else:
                                text = f"{Fore.WHITE}You slashed {monster_name} with your scimitar, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n" \
                                       f"[BLADE MASTER] You go again"
                                go_again = True

                        elif weapons == "rapier":
                            damage = int(random.randint(1, 4) * attack_buff)
                            hit = random.randint(1, 20) + (dex * 2)
                            i = random.randint(1, 3)
                            if i != 1:
                                text = f"{Fore.WHITE}You stabbed {monster_name} with your rapier, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            else:
                                text = f"{Fore.WHITE}You stabbed {monster_name} with your rapier, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n" \
                                       f"[BLADE MASTER] You go again"
                                go_again = True

                        elif weapons == "Skeleton-bone spear":
                            damage = int(random.randint(1, 6) * attack_buff)
                            hit = random.randint(1, 20) + (dex * 2)
                            i = random.randint(1, 2)
                            if i != 1:
                                text = f"{Fore.WHITE}You stabbed {monster_name} with your Skeleton-bone spear, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            else:
                                text = f"{Fore.WHITE}You stabbed {monster_name} with your Skeleton-bone spear, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n" \
                                       f"[HALLOW POWER] You go again"
                                go_again = True


                        elif weapons == "axe":
                            damage = int(random.randint(1, 12) * attack_buff)
                            text = f"{Fore.WHITE}You slashed {monster_name} with your axe, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            hit = random.randint(1, 20) + dex - 4

                        elif weapons == "dagger":
                            damage = int(random.randint(1, 4) * attack_buff)
                            text = f"{Fore.WHITE}You stabbed {monster_name} with your dagger, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            hit = random.randint(1, 20) + dex

                        elif weapons == "pike":
                            damage = int(random.randint(1, 6) * attack_buff)
                            text = f"{Fore.WHITE}You stabbed {monster_name} with your pike, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            hit = random.randint(1, 20) + dex

                        elif weapons == "spear":
                            damage = int(random.randint(1, 6) * attack_buff)
                            text = f"{Fore.WHITE}You stabbed {monster_name} with your spear, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            hit = random.randint(1, 20) + dex

                        elif weapons == "mace":
                            damage = int(random.randint(1, 7) * attack_buff)
                            text = f"{Fore.WHITE}You smacked {monster_name} with your mace, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            hit = random.randint(1, 20) + dex

                        elif weapons == "morningstar":
                            damage = int(random.randint(1, 10) * attack_buff)
                            text = f"{Fore.WHITE}You smacked {monster_name} with your morningstar, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            hit = random.randint(1, 20) + dex

                        elif weapons == "crossbow":
                            if arrows > 0:
                                hit = random.randint(1, 20) + dex
                                damage = int(random.randint(2, 10) * attack_buff)
                                if hit > monster_def:
                                    arrows -= 1
                                text = f"{Fore.WHITE}You stabbed {monster_name} with an arrow, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n-1 arrow\n{arrows} arrows left"
                            else:
                                hit = 11000
                                damage = 0
                                text = f"{Fore.WHITE}You have no arrows"

                        elif weapons == "pistol":
                            if bullets > 0:
                                hit = random.randint(1, 20) + dex
                                if hit > monster_def:
                                    bullets -= 1
                                damage = int(random.randint(1, 3) * attack_buff)
                                i = random.randint(1, 4)
                                if i != 1:
                                    text = f"{Fore.WHITE}You shot {monster_name} with your pistol, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n-1 bullet\n{bullets} bullets left"
                                else:
                                    text = f"{Fore.WHITE}You shot {monster_name} with your pistol, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n-1 bullet\n{bullets} bullets left\n[GUN-SLINGING] You go again"
                                    go_again = True
                            else:
                                hit = 11000
                                damage = 0
                                text = f"{Fore.WHITE}You have no bullets"

                        elif weapons == "poison pistol":
                            if bullets > 0:
                                poison = True
                                poison_turns += random.randint(1, 2)
                                hit = random.randint(1, 20) + dex
                                if hit > monster_def:
                                    bullets -= 1
                                damage = int(random.randint(1, 3) * attack_buff)
                                i = random.randint(1, 4)
                                if i != 1:
                                    text = f"{Fore.WHITE}You shot {monster_name} with your poison pistol, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\nInflicting poison on {monster_name} for {poison_turns} turn \n-1 bullet\n{bullets} bullets left"
                                else:
                                    text = f"{Fore.WHITE}You shot {monster_name} with your poison pistol, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n-1 bullet\n{bullets} bullets left\n[GUN-SLINGING] You go again"
                                    go_again = True
                                poisoned = True
                            else:
                                hit = 11000
                                damage = 0
                                text = f"{Fore.WHITE}You have no bullets"

                        elif weapons == "sniper":
                            if bullets > 0:
                                hit = random.randint(1, 20) + dex
                                if hit > monster_def:
                                    bullets -= 1
                                damage = int(random.randint(2, 10) * attack_buff)
                                text = f"{Fore.WHITE}You shot {monster_name} with your sniper, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n-1 bullet\n{bullets} bullets left"
                            else:
                                hit = 11000
                                damage = 0
                                text = f"{Fore.WHITE}You have no bullets"

                        elif weapons == 'steel sword':
                            damage = int(random.randint(1, 10) * attack_buff)
                            text = f"{Fore.WHITE}You slashed {monster_name} with your steel sword, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            hit = random.randint(1, 20) + dex

                        elif weapons == 'King Jack\'s Blade':
                            damage = int(random.randint(1, 10) * attack_buff)
                            text = f"{Fore.WHITE}You slashed {monster_name} with your steel sword, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            hit = random.randint(10, 20) + dex
                            i = random.randint(1, 5)

                            if i == 5:
                                text = f'{text}\n+{Fore.LIGHTMAGENTA_EX}1{Fore.WHITE} Candy'
                                candy += 1

                        elif weapons == 'magic sword':
                            damage = int(random.randint(1, 10) * attack_buff)
                            i = random.randint(1, 5)
                            if i != 1:
                                text = f"{Fore.WHITE}You slashed {monster_name} with your magic sword, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage" \
                                       f"\nThe sword shimmers and heals you\n+{Fore.RED}{1 * lvl}{Fore.WHITE} Health"
                            else:
                                text = f"{Fore.WHITE}You slashed {monster_name} with your magic sword, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage" \
                                       f"\nThe sword shimmers and heals you\n+{Fore.RED}{1 * lvl}{Fore.WHITE} Health" \
                                       f"\n[MYSTIC BLADE] You go again"
                                go_again = True
                            hit = random.randint(1, 20) + dex + 2
                            hp += 1 * lvl

                        elif weapons == 'cursed War Hammer':
                            damage = int(random.randint(1, 14) * attack_buff)
                            text = f"{Fore.WHITE}You smashed {monster_name} with your cursed War Hammer, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n-{Fore.RED}{1 + lvl / 2}{Fore.WHITE} Health"
                            hit = random.randint(1, 20) + dex - 2
                            hp -= 1 + lvl / 2

                        elif weapons == 'HALLOW SWORD':
                            damage = int(random.randint(1, 20) * attack_buff)
                            text = f"{Fore.WHITE}You slashed {monster_name} with your HALLOW SWORD, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n-{Fore.RED}{1 + lvl}{Fore.WHITE} Health"
                            hit = random.randint(1, 20) + dex
                            hp -= 1 + lvl

                        elif weapons == 'cursed orb':
                            damage = int(random.randint(1, 40) * attack_buff)
                            text = f"{Fore.WHITE}You blasted {monster_name} with your cursed orb, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n-{Fore.RED}{1 + int(lvl * 1.5)}{Fore.WHITE} Health"
                            hit = random.randint(1, 20) + dex
                            hp -= 1 + int(lvl * 1.5)

                        elif weapons == 'Flame Blade':
                            damage = int(random.randint(1, 18) * attack_buff)
                            burn = True
                            burn_turns += 3
                            text = f"{Fore.WHITE}You slashed {monster_name} with your Flame Blade, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\nBurning {monster_name} for {burn_turns} turns"
                            hit = random.randint(1, 20) + dex

                        elif weapons == 'Everfire Blade':
                            damage = int(random.randint(1, 12) * attack_buff)
                            burn = True
                            burn_turns += 7
                            text = f"{Fore.WHITE}You slashed {monster_name} with your Everfire Blade, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage\n+{Fore.RED}{1 + lvl / 2}{Fore.WHITE} Health\nBurning {monster_name} for {burn_turns} turns"
                            i = random.randint(1, 4)
                            if i == 1:
                                text = f'{text}\n[ANCIENT POWER] You go again'
                                go_again = True

                            hit = random.randint(1, 20) + (dex * 2)
                            hp += 1 + lvl / 2

                        else:
                            damage = int(random.randint(1, 3) * attack_buff)
                            text = f"{Fore.WHITE}You hit {monster_name} with your {weapons}, dealing {Fore.GREEN}{damage}{Fore.WHITE} damage"
                            hit = random.randint(1, 20) + dex

                        if go_again is False:
                            i = 12 - dex
                            if i < 2:
                                i = 2
                            i = random.randint(1, i)
                            if i == 1:
                                text = f'{text}\n[SPEED MASTER] You go again'
                                go_again = True

                        scrollTxt(f'{Fore.WHITE}>ATTACK<')
                        scrollTxt(
                            f'Heavy Attack ~ {Fore.GREEN}+dam{Fore.WHITE}, {Fore.RED}-hit{Fore.WHITE}'
                        )
                        scrollTxt('Normal Attack ~ dam, hit')
                        scrollTxt(
                            f'Focused Attack ~ {Fore.RED}-dam{Fore.WHITE}, {Fore.GREEN}+hit{Fore.WHITE}'
                        )

                        answer = 'none'

                        while answer == 'none':
                            answer = input(f'{Fore.GREEN}')
                            if answer != 'Heavy Attack' and answer != 'Normal Attack' and answer != 'Focused Attack':
                                answer = 'none'
                                scrollTxt(f'{Fore.WHITE}That\'s not an attack')

                        if answer == 'Heavy Attack':
                            scrollTxt(f'{Fore.WHITE}You used charge attack')
                            damage = damage * 2
                            hit = hit / 2
                            text = f'{text}\n+{Fore.GREEN}{damage / 2}{Fore.WHITE} [CHARGED]'
                        if answer == 'Normal Attack':
                            scrollTxt(f'{Fore.WHITE}You used normal attack')
                        if answer == 'Focused Attack':
                            scrollTxt(f'{Fore.WHITE}You used focused attack')
                            text = f'{text}\n-{Fore.GREEN}{damage / 2}{Fore.WHITE} [FOCUSED]'
                            damage = damage / 2
                            hit = hit * 2

                        if rusty is True:
                            damage = damage / 2
                            text = f'{text}\n-{Fore.GREEN}{damage}{Fore.WHITE} [RUSTY]\nTotal: {Fore.GREEN}{damage}{Fore.WHITE}'
                            weapons = f'[rusty] {weapons}'

                        if common is True:
                            damage = damage
                            text = f'{text}\n+{Fore.GREEN}{0}{Fore.WHITE} [COMMON]\nTotal: {Fore.GREEN}{damage}{Fore.WHITE}'
                        if rare is True:
                            damage = damage * 1.5
                            text = f'{text}\n+{Fore.GREEN}{damage / 3}{Fore.WHITE} [RARE]\nTotal: {Fore.GREEN}{damage}{Fore.WHITE}'
                            weapons = f'[rare] {weapons}'

                        if epic is True:
                            damage = damage * 2
                            text = f'{text}\n+{Fore.GREEN}{damage / 2}{Fore.WHITE} [EPIC]\nTotal: {Fore.GREEN}{damage}{Fore.WHITE}'
                            weapons = f'[epic] {weapons}'

                        if legendary is True:
                            damage = damage * 3
                            text = f'{text}\n+{Fore.GREEN}{(damage / 3) * 2}{Fore.WHITE} [LEGENDARY]\nTotal: {Fore.GREEN}{damage}{Fore.WHITE}'

                            weapons = f'[legendary] {weapons}'

                        print()

                    if attack == "heal" or attack == '3':
                        buff = False
                        health = True
                        hit = 0
                        text = f"{Fore.WHITE}You heal some of your wounds"
                        heal = random.randint(2, 4)
                        dodge = False
                        run = False

                    if attack == 'dodge' or attack == '4':
                        buff = False
                        health = False
                        hit = 100000
                        text = f'{Fore.WHITE}You get ready to dodge'
                        dodge = True
                        run = False
                        damage = 0

                    if attack == 'run' or attack == '5':
                        buff = False
                        health = False
                        hit = 100000
                        text = f'{Fore.WHITE}You start running'
                        dodge = False
                        run = True
                        damage = 0

                    if monster_dodge:
                        hit -= (5 * monster_power)

                    hit += speed_buff
                    if hp > new_hp:
                        hp = new_hp

                    if hit >= monster_def:
                        if attack != f'throw {weapons}' and attack != '6' or attack == 'fists':
                            monster_hp -= damage
                            monster_health = monster_hp
                            scrollTxt(text)
                            scrollTxt(
                                f"{monster_name} has {Fore.RED}{monster_health}{Fore.WHITE} health left"
                            )
                        else:
                            monster_hp -= (damage * 2)
                            monster_health = monster_hp
                            scrollTxt(f'{Fore.WHITE}You threw your {weapons}')
                            scrollTxt(
                                f'Your {weapons} sails threw the air finding its mark, piercing {monster_name}, '
                                f'dealing {Fore.GREEN}{damage * 2}{Fore.WHITE}')
                            scrollTxt(f'-{weapons}')

                            weapons = 'fists'
                            dropped = True

                            scrollTxt(
                                f"{monster_name} has {Fore.RED}{monster_health}{Fore.WHITE} health left"
                            )

                    elif health is True:
                        scrollTxt(text)
                        scrollTxt(f"You healed {Fore.GREEN}{heal}{Fore.WHITE} health")
                        hp += heal
                        if hp > new_hp:
                            hp = new_hp
                        scrollTxt(f"You have {Fore.RED}{hp}{Fore.WHITE} health left")
                    elif buff is True:
                        scrollTxt(text)
                        scrollTxt(
                            f"Your attack power is now {Fore.GREEN}{attack_buff}{Fore.WHITE}"
                        )
                        scrollTxt(
                            f'Your defense is now {Fore.GREEN}{defense_buff}{Fore.WHITE}')
                        scrollTxt(
                            f'Your speed is now {Fore.GREEN}{speed_buff}{Fore.WHITE}')
                    else:
                        if attack != f'throw {weapons}' and attack != '6' or attack == 'fists':
                            scrollTxt(f"{Fore.WHITE}{monster_name} blocked your attack")
                            if poisoned is True:
                                scrollTxt(
                                    f'Even though you got blocked by {monster_name} still got poisoned for {poison_turns} turns'
                                )
                            if burned is True:
                                scrollTxt(
                                    f'Even though you got blocked by {monster_name} still got burned for {burn_turns} turns'
                                )
                            if frozen is True:
                                scrollTxt(
                                    f'Even though you got blocked by {monster_name} still got freezed for {freeze_turns} turns'
                                )
                        else:
                            scrollTxt(f'{Fore.WHITE}You threw your {weapons}')
                            scrollTxt(f"{Fore.WHITE}{monster_name} blocked your attack")
                            if poisoned is True:
                                scrollTxt(
                                    f'Even though you got blocked by {monster_name} still got poisoned for {poison_turns} turns'
                                )
                            if burned is True:
                                scrollTxt(
                                    f'Even though you got blocked by {monster_name} still got burned for {burn_turns} turns'
                                )
                            if frozen is True:
                                scrollTxt(
                                    f'Even though you got blocked by {monster_name} still got freezed for {freeze_turns} turns'
                                )
                            scrollTxt(f'-{weapons}')
                            weapons = 'fists'
                            dropped = True

                    if go_again is True:
                        turn = 'player'
                        go_again = False
                    else:
                        turn = "enemy"

            if turn == 'enemy':
                if hp > 0:
                    bar()
                    if poison:
                        monster_hp -= 1 * lvl
                        poison_turns -= 1
                        if poison_turns < 1:
                            poison = False
                        scrollTxt(
                            f"{monster_name} took {Fore.GREEN}{1 * lvl}{Fore.WHITE} damage from poison"
                        )

                    if burn:
                        monster_hp -= 2 * lvl
                        burn_turns -= 1
                        if burn_turns < 1:
                            burn = False
                        scrollTxt(
                            f"{monster_name} took {Fore.GREEN}{2 * lvl}{Fore.WHITE} damage from burning"
                        )

                    if freeze:
                        monster_hp -= 1
                        freeze_turns -= 1
                        if freeze_turns < 1:
                            freeze = False
                        scrollTxt(
                            f"{monster_name} took {Fore.GREEN}{1 * lvl}{Fore.WHITE} damage from freezing"
                        )

                    if monster_hp <= 0:
                        scrollTxt(f"You defeated {monster_name}")
                        scrollTxt(
                            f"{monster_name} dropped {Fore.YELLOW}{monster_drop}{Fore.WHITE} gold pieces"
                        )
                        scrollTxt(
                            f"{monster_name} dropped {Fore.CYAN}{monster_exp}{Fore.WHITE} experience"
                        )
                        scrollTxt('You got a thanksgiving crate!')
                        inv.append('thanksgiving crate')
                        crate_chance = random.randint(1, 3)
                        if crate_chance == 1:
                            scrollTxt('You got a common crate')
                            inv.append('common crate')

                        crate_chance = random.randint(1, 9)
                        if crate_chance == 1:
                            scrollTxt('You got a rare crate')
                            inv.append('rare crate')

                        crate_chance = random.randint(1, 18)
                        if crate_chance == 1:
                            scrollTxt('You got a epic crate')
                            inv.append('epic crate')

                        crate_chance = random.randint(1, 35)
                        if crate_chance == 1:
                            scrollTxt('You got a legendary crate')
                            inv.append('legendary crate')
                        if boss is True:
                            scrollTxt(f'{monster_name} dropped {Fore.LIGHTRED_EX}{10}{Fore.WHITE} GEMS')
                            gems += 10
                            db.get(character)[18] = gems
                            crate_chance = random.randint(1, 1)
                            if crate_chance == 1:
                                scrollTxt('You got a legendary crate')
                                inv.append('legendary crate')
                        if weapons == 'fists' and dropped is True:
                            scrollTxt('You picked up your weapon')
                            scrollTxt('It\'s in your inventory')
                            items += 1
                        exp += monster_exp
                        if exp > expNext:
                            exp -= expNext
                            scrollTxt('You leveled up!')
                            lvl += 1
                            expNext += (expNext / 4)
                            expNext = int(expNext)
                            max_hp += 20

                        lose = False
                        scrollTxt('[ENTER] to continue')
                        input()
                        gp += monster_drop
                        battle_over = True

                        system('clear')
                    else:
                        monster_attack_info = True
                        monster_attack = random.choice(monster_moves)
                        scrollTxt(f"{monster_name} attacks...")
                        scrollTxt(f"{monster_name} uses {monster_attack}")

                        monster_health = False
                        monster_buff = False
                        monster_attack_info = True

                        if monster_attack == "slash":
                            hit = random.randint(1, 20) + monster_dex
                            damage = int((1 * (random.randint(2, 5))) * monster_attack_buff)

                        if monster_attack == "stab":
                            hit = random.randint(1, 20) + (monster_dex * 2)
                            damage = int((1 * (random.randint(3, 3))) * monster_attack_buff)

                        if monster_attack == "claw":
                            hit = random.randint(1, 20) + (monster_dex * 2)
                            damage = int((1 * (random.randint(2, 3))) * monster_attack_buff)

                        if monster_attack == "wild slash":
                            hit = random.randint(1, 20) + (monster_dex / 2)
                            damage = int((1 * (random.randint(1, 10))) * monster_attack_buff)

                        if monster_attack == "smash":
                            hit = random.randint(1, 20) + (monster_dex / 1)
                            damage = int((1 * (random.randint(1, 10))) * monster_attack_buff)

                        if monster_attack == "punch":
                            hit = random.randint(1, 20) + (monster_dex * 2)
                            damage = int(2 * monster_attack_buff)

                        if monster_attack == "uppercut":
                            hit = random.randint(1, 20) + (monster_dex * 2)
                            damage = int(4 * monster_attack_buff)

                        if monster_attack == "wind blast":
                            hit = random.randint(1, 20) + (monster_dex * 2)
                            damage = int(4 * monster_attack_buff)

                        if monster_attack == "fangs":
                            hit = random.randint(1, 20) + (monster_dex)
                            damage = int(3 * monster_attack_buff)

                        if monster_attack == "charge":
                            hit = random.randint(1, 20) + int(monster_dex / 1)
                            damage = int((1 * (random.randint(1, 7))) * monster_attack_buff)

                        if monster_attack == 'reaping blow':
                            hit = random.randint(1, 20) + int(monster_dex / 1)
                            damage = int((1 * (random.randint(1, 20))) * monster_attack_buff)

                        if monster_attack == 'rest':
                            hit = 0
                            monster_health = True
                            heal = random.randint(1, 3) * monster_attack_buff

                        if monster_attack == "chant":
                            hit = 0
                            monster_buff = True
                            monster_attack_buff += 0.5

                        if monster_attack == "acid blast":
                            hit = 200
                            monster_poison = True
                            monster_poison_turns = random.randint(1, 2)
                            monster_burn = True
                            monster_burn_turns = random.randint(1, 2)
                            monster_attack_info = False

                        if monster_attack == "poison jab":
                            hit = 200
                            monster_poison = True
                            monster_poison_turns = random.randint(1, 4)

                        if monster_attack == "fire blast":
                            hit = 200
                            monster_burn = True
                            monster_burn_turns = random.randint(4, 7)
                            damage = random.randint(3, 5)

                        if monster_attack == 'dodge':
                            hit = 0
                            monster_dodge = True

                        if monster_attack == 'fly':
                            hit = 0
                            monster_dodge = True

                        if dodge is True:
                            i = random.randint(1, 2)
                        else:
                            i = 1
                        if i == 1:
                            if hit - defense_buff - shield_power >= defense:
                                if monster_poison is True and monster_attack_info is False:
                                    scrollTxt(f"{monster_name} has now poisoned you")
                                    scrollTxt(
                                        f"You are now poisoned for {Fore.GREEN}{monster_poison_turns}{Fore.WHITE}"
                                    )
                                if monster_burn is True and monster_attack_info is False:
                                    scrollTxt(f"{monster_name} has now burned you")
                                    scrollTxt(
                                        f"You are now burned for {Fore.GREEN}{monster_burn_turns}{Fore.WHITE}"
                                    )

                                if monster_attack_info is True:
                                    scrollTxt(
                                        f"{monster_name}'s attack deals {Fore.GREEN}{damage}{Fore.WHITE} damage"
                                    )
                                    hp -= damage
                                    scrollTxt(f"You have {Fore.RED}{hp}{Fore.WHITE} health left")
                            elif monster_health:
                                scrollTxt(
                                    f"{monster_name} healed {Fore.GREEN}{heal}{Fore.WHITE} health"
                                )
                                monster_hp += heal
                                scrollTxt(
                                    f"{monster_name} has {Fore.RED}{monster_hp}{Fore.WHITE} health left"
                                )

                            elif monster_buff:
                                scrollTxt(
                                    f"{monster_name}'s attack power is {Fore.GREEN}{monster_attack_buff}{Fore.WHITE}"
                                )

                            elif monster_dodge:
                                scrollTxt(f'{monster_name} gets ready to dodge')

                            else:
                                scrollTxt("You blocked their attack")
                                scrollTxt(f'+{Fore.RED}{1 * lvl}{Fore.WHITE} Health')
                                hp += 1 * lvl
                        else:
                            scrollTxt("You blocked their attack")
                            scrollTxt(f'+{Fore.RED}1{Fore.WHITE} Health')
                            hp += 1
                        turn = "player"


                else:
                    scrollTxt('You died')
                    quit()


    def black_dragon(other):
        system('clear')
        bar()
        global gp
        global tie

        scrollTxt('~BLACK DRAGON~')
        scrollTxt(f'{character} vs {other}')

        scrollTxt("insert betting amount")
        amount = 'none'
        while amount == 'none':
            amount = input(f'{Fore.GREEN}')
            if not amount.isdigit():
                amount = 'none'
                scrollTxt(f'{Fore.WHITE}that\'s not an amount')
            else:
                amount = int(amount)
                if amount > gp:
                    scrollTxt(f'{Fore.WHITE}You don\'t have that much money')
                    scrollTxt(f'Gold Pieces: {Fore.YELLOW}{gp}{Fore.WHITE}')
                    amount = 'none'

        bar()

        scrollTxt('Do you want to know the rules?')
        scrollTxt("y/n")

        y_or_n = 'none'
        while y_or_n == "none":
            y_or_n = input(f"{Fore.GREEN}")
            if y_or_n != "y" and y_or_n != "n":
                y_or_n = 'none'
                scrollTxt(f"{Fore.WHITE}That's not yes or no")

        if y_or_n == "y":
            scrollTxt(f"{Fore.WHITE}In Black Dragon the goal is to get 26 points")
            scrollTxt("You do this by drawing cards from a deck")
            scrollTxt("meanwhile your opponent is doing the same thing")
            scrollTxt(
                "You can choose to hit (get another card) or stand (stop getting cards)"
            )
            scrollTxt('You can only hit up to 4 times')

        bar()
        scrollTxt("Drawing cards...")
        time.sleep(1)
        points = random.randint(1, 13)
        points += random.randint(1, 13)
        scrollTxt(f"Your points are: {points}")

        lost = False

        scrollTxt("hit or stand")
        hit_or_stand = "none"
        while hit_or_stand == "none":
            hit_or_stand = input(f"{Fore.GREEN}")
            if hit_or_stand != "hit" and hit_or_stand != "stand":
                hit_or_stand = "none"
                scrollTxt(f"{Fore.WHITE}that\'s not a command")
        if hit_or_stand == "hit":
            points += random.randint(1, 13)
            scrollTxt(f"{Fore.WHITE}Your points are: {points}")
        if hit_or_stand == "hit":
            scrollTxt("hit or stand")
            hit_or_stand = "none"
            while hit_or_stand == "none":
                hit_or_stand = input(f"{Fore.GREEN}")
                if hit_or_stand != "hit" and hit_or_stand != "stand":
                    hit_or_stand = "none"
                    scrollTxt(f"{Fore.WHITE}that\'s not a command")
            if hit_or_stand == "hit":
                points += random.randint(1, 13)
                scrollTxt(f"{Fore.WHITE}Your points are: {points}")
            if hit_or_stand == "hit":
                scrollTxt("hit or stand")
                hit_or_stand = "none"
                while hit_or_stand == "none":
                    hit_or_stand = input(f"{Fore.GREEN}")
                    if hit_or_stand != "hit" and hit_or_stand != "stand":
                        hit_or_stand = "none"
                        scrollTxt(f"{Fore.WHITE}that\'s not a command")
                if hit_or_stand == "hit":
                    points += random.randint(1, 13)
                    scrollTxt(f"{Fore.WHITE}Your points are: {points}")
                if hit_or_stand == "hit":
                    scrollTxt("hit or stand")
                hit_or_stand = "none"
                while hit_or_stand == "none":
                    hit_or_stand = input(f"{Fore.GREEN}")
                    if hit_or_stand != "hit" and hit_or_stand != "stand":
                        hit_or_stand = "none"
                        scrollTxt(f"{Fore.WHITE}that\'s not a command")
                if hit_or_stand == "hit":
                    points += random.randint(1, 13)
                    scrollTxt(f"{Fore.WHITE}Your points are: {points}")
                if hit_or_stand == "hit":
                    scrollTxt(f"{Fore.WHITE}You lost because you drew to many cards")
                    scrollTxt(f"-{Fore.YELLOW}{amount}{Fore.WHITE} gold pieces")
                    gp -= amount
                    tie = False
                    lost = True

        bar()

        if lost is False:
            tie = False
            other_points = random.randint(2, 26)
            if other_points < 16:
                other_points += random.randint(1, 13)
                scrollTxt(f"{other} has {points} points")

            if other_points > 26 and points > 26:
                lost = False
                tie = True
                scrollTxt("You both busted")
            elif other_points > 26:
                lost = False
                scrollTxt(f"{other} busted")
            elif points > 26:
                lost = True
                scrollTxt("You busted")
            elif points > other_points:
                lost = False
                scrollTxt("You got closer to 26 points")
            elif points < other_points:
                lost = True
                scrollTxt(f"{other} got closer to 26 points")
            else:
                lost = False
                tie = True
                scrollTxt("You both had the same points")
            bar()

        if tie is True:
            scrollTxt("~TIE GAME~")
        elif lost == False:
            scrollTxt(f"~{character} WINS~")
            scrollTxt(f"+{Fore.YELLOW}{amount}{Fore.WHITE} gold pieces")
            gp += amount
        else:
            scrollTxt(f"~{other} WINS~")
            scrollTxt(f"-{Fore.YELLOW}{amount}{Fore.WHITE} gold pieces")
            gp -= amount


    def dice_and_cards(other):
        system('clear')
        bar()
        global gp
        global tie

        tie = False

        scrollTxt('~DICE & CARDS~')
        scrollTxt(f'{character} vs {other}')

        scrollTxt("insert betting amount")
        amount = 'none'
        while amount == 'none':
            amount = input(f'{Fore.GREEN}')
            if not amount.isdigit():
                amount = 'none'
                scrollTxt(f'{Fore.WHITE}that\'s not an amount')
            else:
                amount = int(amount)
                if amount > gp:
                    scrollTxt(f'{Fore.WHITE}You don\'t have that much money')
                    scrollTxt(f'Gold Pieces: {Fore.YELLOW}{gp}{Fore.WHITE}')
                    amount = 'none'

        bar()

        scrollTxt('Do you want to know the rules?')
        scrollTxt("y/n")

        y_or_n = 'none'
        while y_or_n == "none":
            y_or_n = input(f"{Fore.GREEN}")
            if y_or_n != "y" and y_or_n != "n":
                y_or_n = 'none'
                scrollTxt(f"{Fore.WHITE}That's not yes or no")

        if y_or_n == "y":
            scrollTxt(
                f"{Fore.WHITE}Your goal in this game is to get the most points")
            scrollTxt("You start by drawing a card from a deck")
            scrollTxt(
                "You can draw as many cards as you want but if the total points of the cards is greater than 15 you lose"
            )
            scrollTxt(
                "Then the total points of the cards is how many dices you can roll")

        bar()

        scrollTxt("How many cards would you like to draw")
        cards = 'none'
        while cards == 'none':
            cards = input(f'{Fore.GREEN}')
            if not cards.isdigit():
                cards = 'none'
                scrollTxt(f'{Fore.WHITE}that\'s not an amount')
            else:
                cards = int(cards)

        print(f"{Fore.WHITE}")
        scrollTxt("Drawing cards...")
        time.sleep(1)
        print("")
        points = 0
        while cards > 0:
            points += random.randint(1, 13)
            cards -= 1

        scrollTxt(f"Your card total is {points}")
        lost = False

        if points > 15:
            scrollTxt(f"You busted")
            lost = True

        if lost is False:
            cards = points
            points = 0

            time.sleep(0.5)
            print("")

            scrollTxt("Rolling dice...")
            while cards > 0:
                points += random.randint(1, 6)
                cards -= 1
            scrollTxt(f"Your total points are: {points}")

            other_cards = random.randint(1, 13)
            other_points = 0
            while other_cards > 0:
                other_points += random.randint(1, 6)
                other_cards -= 1
            scrollTxt(f"{other} total points are: {other_points}")

            lost = False
            tie = False
            bar()

            if other_points == points:
                tie = True
                scrollTxt("You both got the same amount of points")
            elif other_points > points:
                lost = True
                scrollTxt("You got less points")
            else:
                lost = False
                scrollTxt("You got more points")

        if tie is True:
            scrollTxt("~TIE GAME~")
        else:
            if lost is False:
                scrollTxt(f"~{character} WINS~")
                scrollTxt(f"+{Fore.YELLOW}{amount}{Fore.WHITE} gold pieces")
                gp += amount

            else:
                scrollTxt(f"~{other} WINS~")
                scrollTxt(f"-{Fore.YELLOW}{amount}{Fore.WHITE} Gold pieces")
                gp -= amount


    def dice_towers(other):
        system('clear')
        bar()
        global gp
        global tie

        scrollTxt('~DICE TOWERS~')
        scrollTxt(f'{character} vs {other}')

        scrollTxt("insert betting amount")
        amount = 'none'
        while amount == 'none':
            amount = input(f'{Fore.GREEN}')
            if not amount.isdigit():
                amount = 'none'
                scrollTxt(f'{Fore.WHITE}that\'s not an amount')
            else:
                amount = int(amount)
                if amount > gp:
                    scrollTxt(f'{Fore.WHITE}You don\'t have that much money')
                    scrollTxt(f'Gold Pieces: {Fore.YELLOW}{gp}{Fore.WHITE}')
                    amount = 'none'

        bar()

        scrollTxt('Do you want to know the rules?')
        scrollTxt("y/n")

        y_or_n = 'none'
        while y_or_n == "none":
            y_or_n = input(f"{Fore.GREEN}")
            if y_or_n != "y" and y_or_n != "n":
                y_or_n = 'none'
                scrollTxt(f"{Fore.WHITE}That's not yes or no")

        if y_or_n == "y":
            scrollTxt(
                f"{Fore.WHITE}Your goal in this game is to get the most dice stacked")
            scrollTxt("You start by rolling dice")
            scrollTxt(
                "You can roll as many dice as you want but the more dice you roll the more unstable your tower will be"
            )
            scrollTxt(
                "The total number of points on the dice is the amount of dice you get to use to build"
            )
            scrollTxt(
                "The amount of dice in you tower is you score but with each dice placed the chance of the tower falling increases."
            )
            scrollTxt("""
                        1st point ~ 1% chance of falling
                        2nd point ~ 2% chance of falling
                        3rd point ~ 3% chance of falling
                        ect
            """)

        bar()

        scrollTxt("How many dice would you like to roll")
        dice = 'none'
        while dice == 'none':
            dice = input(f'{Fore.GREEN}')
            if not dice.isdigit():
                dice = 'none'
                scrollTxt(f'{Fore.WHITE}that\'s not an amount')
            else:
                dice = int(dice)

        print(f"{Fore.WHITE}")
        scrollTxt("Rolling dice...")
        time.sleep(1)
        print("")
        points = 0
        while dice > 0:
            points += random.randint(1, 6)
            dice -= 1

        scrollTxt(f"Your dice total is {points}")

        dice = 0
        percent_fall = 0
        while points > 0:
            dice += 1
            percent_fall += 1
            points -= 1
        percent_fall = min(percent_fall, 100)
        scrollTxt(f"Your chance of building your tower is {100 - percent_fall}%")
        print("")
        scrollTxt("building tower...")
        time.sleep(1)

        rand = random.randint(int(percent_fall / 10), 10)

        lost = False
        tie = False
        if rand == 10:
            scrollTxt("Your tower fell")
            lost = True
        else:
            scrollTxt("Your tower was made!")

        bar()
        if lost is False:
            other_dice = random.randint(5, 15)
            other_points = 0
            while other_dice > 0:
                other_points += random.randint(1, 6)
                other_dice -= 1

            scrollTxt(f"{other} dice total is {other_points}")

            other_dice = 0
            other_percent_fall = 0
            while other_points > 0:
                other_dice += 1
                other_percent_fall += 1
                other_points -= 1
            other_percent_fall = min(other_percent_fall, 100)
            scrollTxt(
                f"{other} chance of building their tower is {100 - other_percent_fall}%"
            )
            print("")
            scrollTxt("building tower...")
            time.sleep(1)

            rand = random.randint(int(other_percent_fall / 10), 10)

            if rand == 10:
                scrollTxt(f"{other}\'s tower fell")
                lost = False
                bar()
            else:
                scrollTxt("Their tower was made!")

                bar()
                if other_dice == dice:
                    tie = True
                    scrollTxt("You both got the same amount of points")
                elif other_dice > dice:
                    lost = True
                    scrollTxt("You got less points")
                else:
                    lost = False
                    scrollTxt("You got more points")

        if tie is True:
            scrollTxt("~TIE GAME~")
        else:
            if lost is False:
                scrollTxt(f"~{character} WINS~")
                scrollTxt(f"+{Fore.YELLOW}{amount}{Fore.WHITE} gold pieces")
                gp += amount

            else:
                scrollTxt(f"~{other} WINS~")
                scrollTxt(f"-{Fore.YELLOW}{amount}{Fore.WHITE} gold pieces")
                gp -= amount


    def NPCtalk(startTxt, commands, answerTxt1, answerTxt2, answerTxt3):
        scrollTxt(startTxt)

        printList(commands, 'Commands: ')

        global answer
        answer = 'none'
        while answer == 'none':
            answer = input(f"{Fore.GREEN}")
            if answer != '1' and answer != "2" and answer != "3":
                answer = "none"
                scrollTxt(f"{Fore.WHITE} That\'s not a answer")
        print(f"{Fore.WHITE}")

        global happen
        if answer == f"1":
            scrollTxt(answerTxt1)
            happen = 1
        if answer == f"2":
            scrollTxt(answerTxt2)
            happen = 2
        if answer == f"3":
            scrollTxt(answerTxt3)
            happen = 3
        print("")


    def mysteriousCave():
        global hp
        global gp
        global max_hp
        global exp
        global expNext
        global inv
        global dex
        global items
        global race

        global answer
        answer = 'none'

        scrollTxt('What difficulty would you like to play at? 1-4')
        commands = ['1', '2', '3', '4']
        printList(commands, 'Difficulty: ')
        inputCommands(commands, '')
        difficulty = int(answer)

        print()
        scrollTxt('LOADING CAVE')
        time.sleep(.5)
        bar()

        scrollTxt('You travel down the dark damp cave...')
        scrollTxt('You can see many mushrooms and moss decorading the cave walls')
        scrollTxt('After walking for awhile you deicde to talk a break')

        scrollTxt('You feel disturbed like your being watched')
        commands = ['rest', 'search around']
        printList(commands, 'Choose one: ')
        inputCommands(commands, '')

        print()

        if answer == 'rest':
            scrollTxt('You rest...')
            time.sleep(.5)
            hp = max_hp
            print_health()

            bar()

            scrollTxt(
                'As you get up to leave a great spider jumps down and attacks you')
            scrollTxt('You are unprepared')
            enter()

            battle('the Giant Spider',
                   ['poison jab', 'fangs', 'acid blast', 'dodge'],
                   difficulty * (random.randint(7, 13)), difficulty * 3,
                   difficulty * 2, 2 * (difficulty / 2), 0, 20 * difficulty)
        else:
            scrollTxt('You search around looking for traps')
            scrollTxt('You found a Giant Spider')
            enter()

            battle('the Giant Spider',
                   ['poison jab', 'fangs', 'acid blast', 'dodge'],
                   difficulty * (random.randint(5, 10)), difficulty * 3,
                   difficulty * 2, 1 * (difficulty / 2), 0, 20 * difficulty)

        if ran is True:
            scrollTxt('You run from the Giant Spider')
            scrollTxt(f'You escaped the Giant Spider')
        else:
            if lose is True:
                scrollTxt('You died game over...')
                scrollTxt(f'the Giant Spider killed you')
                quit()
            if lose is False:
                scrollTxt(f'You stand victorious over the Giant Spider')
                print()

        bar()

        scrollTxt(
            'After another hour of walking through the cave you see a great stone staute of a dragon'
        )
        scrollTxt(
            'The cave shakes as the dragon speaks, '
            '\'To pass you must choose either to fight a Infected mutant mushroom or to answer this riddle\''
        )
        commands = ['fight', 'riddle']
        printList(commands, 'Commands: ')
        inputCommands(commands, '')
        print()

        if answer == 'fight':
            scrollTxt(
                'With a wave of the great dragon\'s claw a mutant mushroom appears')
            enter()
            battle('the mutant mushroom', ['poison jab', 'claw', 'punch', 'dodge'],
                   difficulty * (random.randint(7, 13)), difficulty * 1,
                   difficulty * 3, 1 * (difficulty / 2) + .5, 0, 20 * difficulty)

            if ran is True:
                scrollTxt('You run from the mutant mushroom')
                scrollTxt(
                    f'The dragon shakes its head and says, \'YOU COWARD FOR THIS YOU SHALL DIE\''
                )
                scrollTxt('THe last thing you remember is being engulfed in flames')
                quit()
            else:
                if lose is True:
                    scrollTxt('You died game over...')
                    scrollTxt(f'the mutant mushroom killed you')
                    quit()
                if lose is False:
                    scrollTxt(f'You stand victorious over the mutant mushroom')
                    print()
        if answer == 'riddle':
            scrollTxt(
                '\'Answer this: What is always in front of you but can’t be seen?\', the dragon growls'
            )
            scrollTxt('Answer in lower-case')
            answer = input()

            if answer == 'the future' or answer == 'future' or answer == 'your future':
                scrollTxt('The dragon breaths, \'Correct\'')
                print()
                scrollTxt(
                    '\'What can you keep after giving to someone?\', asks the dragon')
                scrollTxt('Answer in lower-case')
                answer = input()

                if answer == 'your word' or answer == 'a promise' or answer == 'promise':
                    scrollTxt('\'You have passed\', nods the dragon')
                    print()
                else:
                    scrollTxt('\'No, the answer was your word\', hisses the dragon')
                    scrollTxt('Then they crush you under their tail')
                    quit()
            else:
                scrollTxt('\'No, the answer was your future\', the dragon growls')
                scrollTxt('They then crush you under their claws')
                quit()

        scrollTxt('The dragon allows you to pass...')
        bar()

        scrollTxt(
            'Finally you reach a vast cavern, full of treasures; swords, crowns, shields, jewerly'
        )
        scrollTxt(
            'As you get closer you are startled after seeing a great stone statue of a goblin holding a huge gem'
            'the gem shines bright and sparkles.'
            '')
        scrollTxt(
            'You hear it calling your name, temptation washes over you as you draw closer'
        )
        commands = ['take the gem', 'take other treasures', 'leave']
        printList(commands, ' Commands: ')
        inputCommands(commands, '')
        print()

        if answer == 'take the gem':
            scrollTxt('You can resist the temptation and take the gem')
            scrollTxt('As the gem enters your hand, you gasp then scream')
            scrollTxt(
                f'To this day a mysterious statue of a {race} can be seen holding a great gem'
            )
            quit()
        if answer == 'take other treasures':
            scrollTxt('You greedily fill your pockets will gems and gold')
            gp += 20 * difficulty
            scrollTxt(f'+{Fore.YELLOW}{20 * difficulty}{Fore.WHITE} GP')
            scrollTxt('As you turn to leave you see the statue of a goblin stirring')
            scrollTxt('A moment later it charges at you')
            enter()

            battle(
                'the stone goblin',
                ['stab', 'claw', 'punch', 'smash', 'charge', 'wild slash', 'dodge'],
                difficulty * (random.randint(10, 13)), difficulty * 1, difficulty * 4,
                1 * (difficulty / 2) + .5, 20, 30 * difficulty)
            if ran is True:
                scrollTxt('You run from the stone goblin')
                scrollTxt('As you do you lose some of your gold')
                gp -= (20 * difficulty) / 10
                scrollTxt(f'-{Fore.YELLOW}70{Fore.WHITE} GP')
            else:
                if lose is True:
                    scrollTxt('You died game over...')
                    scrollTxt(f'the stone goblin killed you')
                    quit()
                if lose is False:
                    scrollTxt(f'You stand victorious over the stone goblin')
                    print()

                    scrollTxt('You then leave the cave')
                    enter()
        if answer == 'leave':
            scrollTxt('You leave the cave...')
            enter()


    def forestTemple():
        global hp
        global gp
        global max_hp
        global exp
        global expNext
        global inv
        global dex
        global items
        global race

        global answer
        answer = 'none'

        scrollTxt('What difficulty would you like to play at? 1-4')
        commands = ['1', '2', '3', '4']
        printList(commands, 'Difficulty: ')
        inputCommands(commands, '')
        difficulty = int(answer)

        print()
        scrollTxt('LOADING TEMPLE')
        time.sleep(.5)
        bar()

        scrollTxt('You travel into the mossy temple...')
        scrollTxt('The great stone doors shut behind you...')
        scrollTxt(
            'You can see many crumbling remains of what might have been a great alter'
        )
        scrollTxt('After walking for awhile you find a dark long hall')
        scrollTxt('Huge axes swing side to side along the hall')
        scrollTxt('What do you do?')

        actions = [
            '1 ~ run and try to dodge the axes', '2 ~ look more closely',
            '3 ~ Do nothing'
        ]
        commands = ['1', '2', '3']
        printList(actions, 'Choose one: ')
        inputCommands(commands, '')

        print()

        if answer == '1':
            scrollTxt('You run and try to dodge the axes')
            if dex > 1:
                i = random.randint(1 + dex, 10)
                if i == 10:
                    scrollTxt('You dodge and weave through the axes and reach the end')
                else:
                    scrollTxt(
                        'You fail and become one of the many bloody bodies on the floor')
                    quit()
            else:
                scrollTxt(
                    'You fail and become one of the many bloody bodies on the floor')
                quit()
        if answer == '2':
            scrollTxt('You can see there is 2 lever, one must control the axes')
            scrollTxt('There is only one stone in your hand')

            commands = ['left', 'right']
            printList(commands, 'Choose one: ')
            inputCommands(commands, '')

            if answer == 'left':
                scrollTxt(
                    'The stone sails through the air, knocking the lever back...')
                time.sleep(.5)
                scrollTxt('The axes stop and you safely cross through')
            else:
                scrollTxt(
                    'The stone sails through the air, knocking the lever back...')
                time.sleep(.5)
                scrollTxt('Nothing happens...')

                scrollTxt('You now have to just run through and hope to make it.')
                scrollTxt('You run and try to dodge the axes')
                if dex > 1:
                    i = random.randint(1 + dex, 10)
                    if i == 10:
                        scrollTxt('You dodge and weave through the axes and reach the end')
                    else:
                        scrollTxt(
                            'You fail and become one of the many bloody bodies on the floor')
                        quit()
                else:
                    scrollTxt(
                        'You fail and become one of the many bloody bodies on the floor')
                    quit()

        if answer == '3':
            scrollTxt('You do nothing...')
            time.sleep(1)
            scrollTxt('Nothing happens')
            scrollTxt('You decide to wait another million years...')
            time.sleep(2)
            scrollTxt(
                'The axes eventually stop moving and you safely cross the hall')
        bar()

        scrollTxt(
            'After another hour of walking through the temple you see a chopped up body on the floor'
        )
        scrollTxt('You try to muffle you scream.')
        scrollTxt(
            'As you turn to leave the bodies starts to shake violently and convulses'
        )
        scrollTxt('With sharp movements it rises and charges at you!')
        enter()

        battle('the chopped up body', [
            'wild slash', 'claw', 'punch', 'chant', 'charge', 'acid blast', 'dodge'
        ], difficulty * (random.randint(5, 10)), difficulty * 1, difficulty * 2,
               1 * (difficulty / 2) + .5, 0, 20 * difficulty)
        if ran is True:
            scrollTxt('You run from the chopped up body')
            scrollTxt('You escape!')

        else:
            if lose is True:
                scrollTxt('You died game over...')
                scrollTxt(f'the chopped up body killed you')
                quit()
            if lose is False:
                scrollTxt(f'You stand victorious over the chopped up body')

        bar()

        scrollTxt('Finally you reach a vast room...')
        scrollTxt('In the center of the room sits a person frail and old')
        scrollTxt('All around them are skulls...')

        commands = ['try to leave', 'attack the person', 'speak to the person']
        printList(commands, ' Commands: ')
        inputCommands(commands, '')
        print()

        if answer == 'try to leave':
            scrollTxt(
                'You try to leave as you turn around the frail monk charges towards you!'
            )
            enter()
            battle(
                'the DARK MONK',
                ['stab', 'slash', 'punch', 'chant', 'charge', 'acid blast', 'dodge'],
                difficulty * (random.randint(10, 11)), difficulty * 3, difficulty * 4,
                1 * (difficulty / 2) + 1, 30, 30 * difficulty)
        if answer == 'attack the person':
            scrollTxt('As you charge at them they rise, ready to fight')
            enter()
            battle(
                'the DARK MONK',
                ['stab', 'slash', 'punch', 'chant', 'charge', 'acid blast', 'dodge'],
                difficulty * (random.randint(10, 11)), difficulty * 3, difficulty * 4,
                1 * (difficulty / 2) + 1, 30, 30 * difficulty)
        if answer == 'speak to the person':
            scrollTxt('You try to speak to them, but to no avail')
            scrollTxt('You walk up to tap them on the shoulder')
            scrollTxt(
                'The moment you touch them the grab your hand they grab your hand and throw you on the floor!'
            )
            enter()
            battle(
                'the DARK MONK',
                ['stab', 'slash', 'punch', 'chant', 'charge', 'acid blast', 'dodge'],
                difficulty * (random.randint(10, 11)), difficulty * 3, difficulty * 4,
                1 * (difficulty / 2) + 1, 30, 30 * difficulty)
            if ran is True:
                scrollTxt('You run from the monk')
                scrollTxt('They start chanting and as you run')
                scrollTxt('You are engualfed in dark flames')
                quit()

            else:
                if lose is True:
                    scrollTxt('You died game over...')
                    scrollTxt(f'the dark monk killed you')
                    quit()
                if lose is False:
                    scrollTxt(f'You stand victorious over the dark monk')
                    scrollTxt('You walk over the dead monk out of the temple')


    def arena():
        global hp
        global gp
        global max_hp
        global exp
        global expNext
        global inv
        global dex
        global items
        global race
        global character

        scrollTxt('The crowd screams as you enter the arena')
        scrollTxt('They cheer for blood to be spilled')
        time.sleep(.5)
        print()
        scrollTxt('~TEIR1~')
        scrollTxt(f'{character} vs deranged goblin')
        enter()

        battle('the deranged goblin', ['slash', 'stab', 'charge', 'wild slash'],
               random.randint(5, 7), 6, 5, 1.5, 0, 20)

        if ran is True:
            scrollTxt('You run from goblin')
            scrollTxt(f'You escaped the goblin')
            scrollTxt('The crowd jeers as you leave the arena')
            bar()
        else:
            if lose is True:
                scrollTxt('You died game over...')
                scrollTxt(f'the goblin killed you')
                quit()
            if lose is False:
                scrollTxt(f'You stand victorious over the goblin')
                bar()

                commands = ['stop', 'continue']
                printList(commands, 'Commands: ')
                inputCommands(commands, '')

                if answer == 'continue':
                    bar()
                    scrollTxt('~TEIR2~')
                    scrollTxt(f'{character} vs mutant bugbear')

                    battle('the mutant bugbear', [
                        'acid blast', 'stab', 'charge', 'chant', 'wild slash', 'claw',
                        'smash'
                    ], random.randint(10, 13), 5, 8, 2, random.randint(0, 0), 40)

                    if ran is True:
                        scrollTxt('You run from the bugbear')
                        scrollTxt(f'You escaped the bugbear')
                        scrollTxt('The crowd jeers as you leave the arena')
                        bar()
                    else:
                        if lose is True:
                            scrollTxt('You died game over...')
                            scrollTxt(f'the bugbear killed you')
                            quit()
                        if lose is False:
                            scrollTxt(f'You stand victorious over the bugbear')
                            bar()

                            commands = ['stop', 'continue']
                            printList(commands, 'Commands: ')
                            inputCommands(commands, '')

                            if answer == 'continue':
                                bar()
                                scrollTxt('TIER3')
                                scrollTxt(f'{character} vs dragonic earthbound')

                                battle('the dragonic earthbound', [
                                    'acid blast', 'poison jab', 'charge', 'chant', 'wild slash',
                                    'claw', 'smash', 'punch'
                                ], random.randint(13, 15), 2, 10, 2.5, random.randint(0, 0),
                                       60)
                                if ran is True:
                                    scrollTxt('You run from the dragonic earthbound')
                                    scrollTxt(f'You escaped the dragonic earthbound')
                                    scrollTxt('The crowd jeers as you leave the arena')
                                    bar()
                                else:
                                    if lose is True:
                                        scrollTxt('You died game over...')
                                        scrollTxt(f'the dragonic earthbound killed you')
                                        quit()
                                    if lose is False:
                                        scrollTxt(
                                            f'You stand victorious over the dragonic earthbound')
                                        print()
                                        commands = ['stop', 'continue']
                                        printList(commands, 'Commands: ')
                                        inputCommands(commands, '')

                                        if answer == 'continue':
                                            bar()
                                            scrollTxt('~TEIR4~')
                                            scrollTxt(f'{character} vs demond of death')

                                            battle(
                                                'demond of death',
                                                ['acid blast', 'poison jab', 'chant', 'reaping blow'],
                                                random.randint(15,
                                                               20), 6, 10, 3, random.randint(0, 0), 80)

                                            if ran is True:
                                                scrollTxt('You run from the demond of death')
                                                scrollTxt(f'You escaped don\'t escape')
                                                scrollTxt(
                                                    'The last thing you know is the scythe coming down')
                                                quit()
                                            else:
                                                if lose is True:
                                                    scrollTxt('You died game over...')
                                                    scrollTxt(f'the demond of death killed you')
                                                    quit()

                                                if lose is False:
                                                    scrollTxt(
                                                        f'You stand victorious over the demond of death')
                                                    print()

                                                    scrollTxt('YOU WON!')
                                                    gp += 200
                                                    scrollTxt(f'+{Fore.YELLOW}200{Fore.WHITE}')

                                        else:
                                            scrollTxt('You take a bow and leave the arena')
                                            gp += 90
                                            scrollTxt(f'+{Fore.YELLOW}90{Fore.WHITE}')

                            else:
                                scrollTxt('You take a bow and leave the arena')
                                gp += 60
                                scrollTxt(f'+{Fore.YELLOW}60{Fore.WHITE}')

                else:
                    scrollTxt('You take a bow and leave the arena')
                    gp += 30
                    scrollTxt(f'+{Fore.YELLOW}30{Fore.WHITE}')


    def darkestDungeon():
        global hp
        global gp
        global max_hp
        global exp
        global expNext
        global inv
        global dex
        global items
        global race
        global gems
        global character

        global answer
        answer = 'none'

        scrollTxt('What difficulty would you like to play at? 1-4')
        commands = ['1', '2', '3', '4']
        printList(commands, 'Difficulty: ')
        inputCommands(commands, '')
        difficulty = int(answer)

        print()
        scrollTxt('LOADING DUNGEON')
        time.sleep(.5)
        bar()

        scrollTxt('You travel into the dark dungeon...')
        scrollTxt('The great metal doors shut behind you...')
        scrollTxt(
            'You can see many a hobbled over man...'
        )
        scrollTxt('They greet you saying that their name is \'rebbor\'')
        scrollTxt('They ask for some food...')
        actions = [
            '1 ~ give them food', '2 ~ leave',
            '3 ~ say you don\'t have any'
        ]
        commands = ['1', '2', '3']
        printList(actions, 'Choose one: ')
        inputCommands(commands, '')

        print()

        if answer == '1':
            scrollTxt('They thank you, by thrusting a dagger into!')
            hp = 1
            print_health()
            enter()

            battle('the robber', ['stab', 'punch', 'slash'], random.randint(10, 20), 7, 10, difficulty, 60, 20)
            if ran is True:
                scrollTxt('You run from the robber')
                scrollTxt('You escape!')
            else:
                if lose is True:
                    scrollTxt('You died game over...')
                    scrollTxt(f'the robber killed you')
                    quit()
                if lose is False:
                    scrollTxt(f'You stand victorious over the robber')
        if answer == '2':
            scrollTxt('They sigh and look sad...')
            scrollTxt(
                f'You roll your eyes and leave only to find that you have {Fore.YELLOW}200{Fore.WHITE} less gold!')
            gp -= 200
            if gp < 0:
                gp = 0

        if answer == '3':
            scrollTxt('You say you don\'t have anything...')
            time.sleep(1)
            scrollTxt('They frown...')
            scrollTxt('Then charge at you!')
            enter()

            battle('the robber', ['stab', 'punch', 'slash'], random.randint(10, 20), 7, 10, difficulty, 60, 20)
            if ran is True:
                scrollTxt('You run from the robber')
                scrollTxt('You escape!')
            else:
                if lose is True:
                    scrollTxt('You died game over...')
                    scrollTxt(f'the rober killed you')
                    quit()
                if lose is False:
                    scrollTxt(f'You stand victorious over the robber')
        bar()

        scrollTxt(
            'After some more walking you see a glob of ooze covering the floor'
        )
        actions = [
            '1 ~ take another path', '2 ~ touch the glob',
            '3 ~ investigate'
        ]
        commands = ['1', '2', '3']
        printList(actions, 'Choose one: ')
        inputCommands(commands, '')

        immunity = False

        if answer == '1':
            scrollTxt('You decide to take another path...')
            scrollTxt('You encounter a iron golem')
            scrollTxt('They charge at you!')
            enter()

            battle(
                'the iron golem',
                ['stab', 'slash', 'punch', 'dodge', 'charge', 'acid blast', 'poison jab'],
                difficulty * (random.randint(10, 11)), difficulty * 3, difficulty * 4,
                1 * (difficulty / 2) + 1, 30, 30 * difficulty)

        if answer == '2':
            scrollTxt('You touch the glob...')
            scrollTxt(f'-{Fore.RED}{5 * difficulty}{Fore.WHITE} HP')
            hp -= 5 * difficulty
            if hp < 1:
                scrollTxt('You died...')
                quit()
            scrollTxt('After touching it you decide you touch it again...')
            scrollTxt('This time you take no damage!')
            immunity = True
        if answer == '3':
            scrollTxt('You decide to investigate...')
            scrollTxt('You find a gem!')
            scrollTxt(f'+{Fore.LIGHTRED_EX}1{Fore.WHITE}')
            gems += 1
            db.get(character)[18] = gems
            scrollTxt('After even more investigating you find a shield that you allows you to cross')
            scrollTxt('You cross safely')
        bar()

        scrollTxt('Finally you reach a pile of immense gold...')
        scrollTxt('In the ceter of the pile lies a dark dragon')
        scrollTxt('All around them are human bones...')

        commands = ['try to leave', 'fight']
        printList(commands, ' Commands: ')
        inputCommands(commands, '')
        print()

        if answer == 'try to leave':
            scrollTxt(
                'You try to leave as you turn around the dragon charges at you!'
            )
            enter()
            battle('the DARK DRAGON',
                   ['slash', 'stab', 'charge', 'acid blast', 'fire blast', 'reaping blow', 'fly', 'claw', 'smash',
                    'rest', 'wild slash', 'fangs'],
                   random.randint(30, 40) * lvl, 4 * lvl, 10, 1 * (lvl / 2) + difficulty + 1, 100 * lvl, 200 * lvl)
        if answer == 'fight':
            scrollTxt('As you charge at them they rise, ready to fight')
            enter()
            battle('the DARK DRAGON',
                   ['slash', 'stab', 'charge', 'acid blast', 'fire blast', 'reaping blow', 'fly', 'claw', 'smash',
                    'rest', 'wild slash', 'fangs'],
                   random.randint(30, 40) * lvl, 4 * lvl, 10, 1 * (lvl / 2) + difficulty + 1, 30 * lvl, 50 * lvl)

        if ran is True:
            scrollTxt('You run from the dragon')
            scrollTxt('You they kill you!')
            quit()
        else:
            if lose is True:
                scrollTxt('You died game over...')
                scrollTxt(f'the dragon killed you')
                quit()
            if lose is False:
                scrollTxt(f'You stand victorious over the DARK DRAGON')
                scrollTxt('You escape the dungeon')


    def bossRaid():
        global hp
        global gp
        global max_hp
        global exp
        global expNext
        global inv
        global dex
        global items
        global race
        global character

        bar()

        scrollTxt(f'{Style.DIM}GET READY FOR THE BOSS RAID')
        scrollTxt('blood will be be spilled')
        time.sleep(.5)
        print()
        scrollTxt('~BOSS 1~')
        scrollTxt(f'{character} vs DARK SUN KING')
        enter()

        battle('the DARK SUN KING', ['slash', 'stab', 'charge', 'wild slash'],
               random.randint(100, 170), 10, 7, 5, 300, 200)

        if ran is True:
            scrollTxt('You run from the DARK SUN KING')
            scrollTxt(f'You escaped the the DARK SUN KING')
            scrollTxt('The crowd jeers as you leave the arena')
            bar()
        else:
            if lose is True:
                scrollTxt('You died game over...')
                scrollTxt(f'the DARK SUN KING killed you')
                quit()
            if lose is False:
                scrollTxt(f'You stand victorious over the DARK SUN KING')
                bar()

                commands = ['stop', 'continue']
                printList(commands, 'Commands: ')
                inputCommands(commands, '')

                if answer == 'continue':
                    bar()
                    scrollTxt('~BOSS2~')
                    scrollTxt(f'{character} vs MUTANT SAND TITAN')

                    battle('the MUTANT SAND TITAN', [
                        'wind blast', 'stab', 'charge', 'chant', 'wild slash', 'claw',
                        'smash'
                    ], random.randint(200, 300), 5, 10, 6, random.randint(0, 0), 400)

                    if ran is True:
                        scrollTxt('You run from the MUTANT SAND TITAN')
                        scrollTxt(f'You escaped the MUTANT SAND TITAN')
                        scrollTxt('The crowd jeers as you leave the arena')
                        bar()
                    else:
                        if lose is True:
                            scrollTxt('You died game over...')
                            scrollTxt(f'the MUTANT SAND TITAN killed you')
                            quit()
                        if lose is False:
                            scrollTxt(f'You stand victorious over the MUTANT SAND TITAN')
                            bar()

                            commands = ['stop', 'continue']
                            printList(commands, 'Commands: ')
                            inputCommands(commands, '')

                            if answer == 'continue':
                                bar()
                                scrollTxt('BOSS4')
                                scrollTxt(f'{character} vs DRAGONIC DESERT MUMMY KING')

                                battle('the DRAGONIC DESERT MUMMY KING', [
                                    'acid blast', 'poison jab', 'charge', 'chant', 'wild slash',
                                    'claw', 'smash', 'punch', 'reaping blow'
                                ], random.randint(300, 400), 12, 10, 7, random.randint(500, 600),
                                       600)
                                if ran is True:
                                    scrollTxt('You run from the DRAGONIC DESERT MUMMY KING')
                                    scrollTxt(f'You escaped the DRAGONIC DESERT MUMMY KING')
                                    scrollTxt('The crowd jeers as you leave the arena')
                                    bar()
                                else:
                                    if lose is True:
                                        scrollTxt('You died game over...')
                                        scrollTxt(f'the DRAGONIC DESERT MUMMY KING killed you')
                                        quit()
                                    if lose is False:
                                        scrollTxt(
                                            f'You stand victorious over the DRAGONIC DESERT MUMMY KING')
                                        print()
                                        commands = ['stop', 'continue']
                                        printList(commands, 'Commands: ')
                                        inputCommands(commands, '')

                                        if answer == 'continue':
                                            bar()
                                            scrollTxt('~BOSS5~')
                                            scrollTxt(f'{character} vs DEATH MAGMA TITAN')

                                            battle(
                                                'DEATH MAGMA TITAN',
                                                ['fire blast', 'smash', 'chant', 'reaping blow'],
                                                random.randint(500,
                                                               600), 3, 12, 8, random.randint(0, 0), 800)

                                            if ran is True:
                                                scrollTxt('You run from the DEATH MAGMA TITAN')
                                                scrollTxt(f'You don\'t escape')
                                                scrollTxt(
                                                    'The last thing you know is burning to death')
                                                quit()
                                            else:
                                                if lose is True:
                                                    scrollTxt('You died game over...')
                                                    scrollTxt(f'the DEATH MAGMA TITAN killed you')
                                                    quit()

                                                if lose is False:
                                                    scrollTxt(
                                                        f'You stand victorious over the DEATH MAGMA TITAN')
                                                    print()

                                                    scrollTxt('YOU WON!')
                                                    gp += 2000
                                                    scrollTxt(f'+{Fore.YELLOW}2000{Fore.WHITE}')

                                        else:
                                            scrollTxt('You take a bow and leave the arena')
                                            gp += 900
                                            scrollTxt(f'+{Fore.YELLOW}900{Fore.WHITE}')

                            else:
                                scrollTxt('You take a bow and leave the arena')
                                gp += 600
                                scrollTxt(f'+{Fore.YELLOW}600{Fore.WHITE}')

                else:
                    scrollTxt('You take a bow and leave the arena')
                    gp += 300
                    scrollTxt(f'+{Fore.YELLOW}300{Fore.WHITE}')


    def passMountains():
        global hp
        global gp
        global max_hp
        global exp
        global expNext
        global inv
        global dex
        global items
        global race
        global character

        bar()

        scrollTxt('You enter the great mountain')
        scrollTxt('You notice that you were not the first person to be here')
        scrollTxt('Dead bodied litter the floor...')
        bar()
        scrollTxt('Eventually you reach a great cavern room')
        scrollTxt('You can faintly hear great machines moving')
        scrollTxt(
            'The moment you enter the room a great stone rock rises to reveil that it is a ANCIENT TITAN STONE GOLEM!')
        scrollTxt('It charages at you!')
        battle(
            'ANCIENT TITAN STONE GOLEM',
            ['smash', 'chant', 'reaping blow'],
            random.randint(1000,
                           3000), 3, 13, 14, random.randint(0, 0), 1000)


    scrollTxt('/DISCLAIMER\\')
    scrollTxt('there is violence and mild gore')
    system('clear')
    scrollTxt(f'{Style.BRIGHT}Overdrive Games Presents...')
    time.sleep(.5)
    system('clear ')

    print(logo)
    scrollTxt("Enter to start...")
    answer = input("")

    system("clear")
    print(logo)
    bar()

    scrollTxt('Do you have a save? yes/no')
    scrollTxt('If you made an account before 11/1/2022 type \'transfer\'')
    save = input()

    if save == 'yes':
        scrollTxt('What save do you want to load?')
        answer = 'none'
        while answer == 'none':
            answer = input()
            if answer not in db.keys():
                scrollTxt(f'No account found with the name {answer}')
                answer = 'none'

        scrollTxt('What is the password?')
        answer2 = 'none'
        while answer2 == 'none':
            answer2 = input()
            if answer2 != db.get(answer)[21]:
                scrollTxt(f'INCORRECT')
                answer2 = 'none'

        scrollTxt('LOADING SAVE...')
        character = db.get(answer)[0]
        character_class = db.get(answer)[1]
        race = db.get(answer)[2]
        max_hp = db.get(answer)[3]
        hp = db.get(answer)[4]
        gp = db.get(answer)[5]
        dex = db.get(answer)[6]
        defense = db.get(answer)[7]
        lvl1_available_spells = db.get(answer)[8]
        lvl2_available_spells = db.get(answer)[9]
        lvl1_spells = db.get(answer)[10]
        lvl2_spells = db.get(answer)[11]
        location = db.get(answer)[12]
        inv = db.get(answer)[13]

        weapons = db.get(answer)[14]
        exp = db.get(answer)[15]
        expNext = db.get(answer)[16]
        lvl = db.get(answer)[17]
        gems = db.get(answer)[18]
        world = db.get(answer)[19]
        candy = db.get(answer)[20]
        items = len(inv)
        scrollTxt('You get a gem for logging in!')
        gems += 1
        db.get(answer)[18] = gems
        scrollTxt(f'+{Fore.LIGHTRED_EX}1{Fore.WHITE} gem')
        scrollTxt(f'GEMS: {Fore.LIGHTRED_EX}{gems}{Fore.WHITE}')
        bar()

        scrollTxt(f'~{Fore.BLUE}Lobby{Fore.WHITE}~')
        lobby = True
        while lobby == True:
            commands = ['1 ~ check out other players', '2 ~ play', '3 ~ convert', '4 ~ library', '5 ~ go to village',
                        '6 ~ fight world boss', '7 ~ train', '8 ~ map']
            actions = ['1', '2', '3', '4', '5', '6', '7', '8']

            printList(commands, 'Commands: ')
            inputCommands(actions, '')

            if answer == '1':
                scrollTxt('Who would you like to look at?')
                scrollTxt('Type \'none\' to exit')
                player = 'noone'
                while player == 'noone':
                    player = input()

                    if player not in db.keys() and player != 'none':
                        scrollTxt('That\'s not a player')
                        player = 'noone'

                if player != 'none':
                    answer = player
                    spells1 = []
                    spells2 = []
                    i = []
                    addList(spells1, db.get(answer)[8])
                    addList(spells2, db.get(answer)[9])
                    addList(i, db.get(answer)[13])
                    print()
                    scrollTxt(f'Character: {db.get(answer)[0]}')
                    scrollTxt(f'Level: {db.get(answer)[17]}')
                    print()
                    scrollTxt(f'Class: {db.get(answer)[1]}')
                    scrollTxt(f'Race: {db.get(answer)[2]}')
                    scrollTxt(f'HP: {db.get(answer)[4]}/{db.get(answer)[3]}')
                    scrollTxt(f'Gold: {db.get(answer)[5]}')
                    scrollTxt(f'EXP: {db.get(answer)[15]}/{db.get(answer)[16]}')
                    print()
                    scrollTxt(f'DEX: {db.get(answer)[6]}')
                    scrollTxt(f'DEF: {db.get(answer)[7]}')
                    scrollTxt(f'LVL1 SPELLS: {spells1}')
                    scrollTxt(f'LVL2 SPELLS: {spells2}')
                    print()
                    scrollTxt(f'Weapon: {db.get(answer)[14]}')
                    scrollTxt(f'Inventory: {i}')
                    print()

            if answer == '2':
                scrollTxt('LOADING WORLD')
                if location == 'halloween':
                    location = 'start village'
                time.sleep(.5)
                lobby = False
                enter()

            if answer == '3':
                scrollTxt('What would you like to get? gems/coins')
                commands = ['gems', 'coins']
                printList(commands, 'Commands: ')
                inputCommands(commands, '')

                if answer == 'gems':
                    scrollTxt("insert convert amount")

                    amount = 'none'
                    while amount == 'none':
                        amount = input(f'{Fore.GREEN}')
                        if not amount.isdigit():
                            amount = 'none'
                            scrollTxt(f'{Fore.WHITE}that\'s not an amount')
                        else:
                            amount = int(amount)
                            if amount > gp:
                                scrollTxt(f'{Fore.WHITE}You don\'t have that much money')
                                scrollTxt(f'Gold Pieces: {Fore.YELLOW}{gp}{Fore.WHITE}')
                                amount = 'none'

                    gems += int(amount / 20)
                    db.get(character)[18] = gems

                    gp -= amount

                    scrollTxt(f'{Fore.WHITE}+{Fore.LIGHTRED_EX}{int(amount / 20)}{Fore.WHITE} gems')
                    scrollTxt(f'-{Fore.YELLOW}{amount}{Fore.WHITE} gold')

                if answer == 'coins':
                    amount = 'none'
                    while amount == 'none':
                        amount = input(f'{Fore.GREEN}')
                        if not amount.isdigit():
                            amount = 'none'
                            scrollTxt(f'{Fore.WHITE}that\'s not an amount')
                        else:
                            amount = int(amount)
                            if amount > gems:
                                scrollTxt(f'{Fore.WHITE}You don\'t have that much gems')
                                scrollTxt(f'Gems: {Fore.LIGHTRED_EX}{gems}{Fore.WHITE}')
                                amount = 'none'

                    gp += int(amount * 20)
                    db.get(character)[5] = gp

                    gems -= amount

                    scrollTxt(f'{Fore.WHITE}+{Fore.YELLOW}{int(amount * 20)}{Fore.WHITE} GP')
                    scrollTxt(f'-{Fore.LIGHTRED_EX}{amount}{Fore.WHITE} Gems')

                bar()

            if answer == '4':
                scrollTxt('What lore would you like to read?')
                commands = ['Start lore', 'Inferno lore']
                printList(commands, '')
                inputCommands(commands, '')

                if answer == 'Start lore':
                    bar()
                    scrollTxt(
                        'There once was a peaceful magical world full of humans, creatures, and monsters and all of them lived in harmony. But then everything changed when the monsters attacked the humans. A prophecy says that a traveler that\'s trying to find the wonders of the world will one day stumble upon the small town of Lockwood. There they will save the town from the ancient magic or fail horribly from the dark dragon that is trying to make it surrender. ')

                if answer == 'Inferno lore':
                    bar()
                    scrollTxt(
                        'If the brave traveler defeats the dragon, a mysterious portal will open. The traveler curiously hops through the portal and ends up at the city of fire, Veras. At the time when the traveler arrives, the city will be in a severe drought. All the people that live in Veras can survive 50 days without water due to the circumstances of birth. But with the heat increases, that water supply has been decreasing, without this water, the civilians of Veras won’t survive. There have been rumors that there is a paradise with lots of water behind the great mountains but people who have tried never came back. But somehow this traveler will somehow lead the city of Veras to this paradise.')
                bar()

            if answer == '5':
                scrollTxt('LOADING VILLAGE')
                enter()
                location = 'start village'
                world = 'start'
                lobby = False

            if answer == '6':
                print()
                scrollTxt('SUMMONING WORlD BOSS')
                enter()

                if world == 'start':
                    battle('the DARK DRAGON (WORLD BOSS)',
                           ['slash', 'stab', 'charge', 'acid blast', 'fire blast', 'reaping blow', 'fly', 'claw',
                            'smash',
                            'rest', 'wild slash', 'fangs'],
                           random.randint(500, 1000), 10, 8, 10, 600,
                           500)
                    if ran is True:
                        scrollTxt('You can\'t escape impending doom')
                        quit()
                    else:
                        if lose is True:
                            scrollTxt('You died to the DARK DRAGON (WORLD BOSS)')
                            quit()
                        else:
                            scrollTxt('You defeated the world boss!')
                            scrollTxt(f'+ {Fore.LIGHTRED_EX}20{Fore.WHITE} GEMS')
                            gems += 20
                            db.get(character)[18] = gems

                if world == 'inferno':
                    battle(
                        'DEATH MAGMA TITAN (WORLD BOSS)',
                        ['fire blast', 'smash', 'chant', 'reaping blow'],
                        random.randint(1000,
                                       2000), 3, 12, 15, random.randint(0, 0), 1000)

                    if ran is True:
                        scrollTxt('You can\'t escape impending doom')
                        quit()
                    else:
                        if lose is True:
                            scrollTxt('You died to the DEATH MAGMA TITAN (WORLD BOSS)')
                            quit()
                        else:
                            scrollTxt('You defeated the world boss!')
                            scrollTxt(f'+ {Fore.LIGHTRED_EX}30{Fore.WHITE} GEMS')
                            gems += 30
                            db.get(character)[18] = gems

                print()

            if answer == '7':
                scrollTxt(f'Would you like to train? cost {Fore.YELLOW}50{Fore.WHITE} GP')
                commands = ['yes', 'no']
                printList(commands, '')
                inputCommands(commands, '')
                print()

                if answer == 'yes':
                    if gp >= 50:
                        scrollTxt('TRAINING...')
                        time.sleep(1)
                        print()
                        scrollTxt(f'+{Fore.CYAN}100{Fore.WHITE} EXP')

                        print(f'-{Fore.YELLOW}50{Fore.WHITE} GP')
                        gp -= 50
                        exp += 100
                        print_exp()
                        if exp > expNext:
                            exp -= expNext
                            scrollTxt('You leveled up!')
                            lvl += 1
                            expNext += (expNext / 4)
                            expNext = int(expNext)
                            max_hp += 20
                    else:
                        scrollTxt('You don\'t have enough gold')
                        print_gp()
                bar()

            if answer == '8':
                map_Start()
                print()
        print()
    elif save == 'transfer':
        scrollTxt('TRANSFERING DATA')
        character = db['character']
        character_class = db['character_class']
        race = db['race']
        max_hp = db['max_hp']
        hp = db['hp']
        gp = db['gp']
        dex = db['dex']
        defense = db['defense']
        lvl1_available_spells = db['lvl1_available_spells']
        lvl2_available_spells = db['lvl2_available_spells']
        lvl1_spells = db['lvl1_spells']
        lvl2_spells = db['lvl2_spells']
        location = db['location']
        inv = db['inv']
        weapons = db['weapons']
        exp = db['exp']
        expNext = db['expNext']
        lvl = db['lvl']
        gems = db['gems']
        candy = db['candy']

        scrollTxt('What is your password?')
        password = input()
        db[
            character] = character, character_class, race, max_hp, hp, gp, dex, defense, lvl1_available_spells, lvl2_available_spells, lvl1_spells, lvl2_spells, location, inv, weapons, exp, expNext, lvl, gems, world, candy, password
    else:

        world = 'start'
        candy = 0

        print()
        print()
        scrollTxt("~CHARACTER~")
        print("")
        scrollTxt("What is your character's name?")
        character = 'none'
        while character == 'none':
            character = input(f"{Fore.GREEN}")

            if character in db.keys():
                character = 'none'
                scrollTxt('Username taken')

        print(f"{Fore.WHITE}")

        scrollTxt('What is your password?')
        password = input()
        print()

        scrollTxt(f'{Fore.WHITE}what race would you like to be?')
        commands = []
        addList(commands, races)
        printList(commands, 'Races: ')
        inputCommands(commands, "")
        race = answer
        scrollTxt(f'You are now a {race}')
        print()

        scrollTxt(f"{Fore.WHITE}what class would you like to be?")
        commands = []
        addList(commands, classes)
        printList(commands, 'Classes: ')
        addList(commands, ['Overdrive', 'Troy', 'Lucas', 'Jayden', 'Brandon', 'Hansel', 'Pig'])
        inputCommands(commands, "")
        character_class = answer
        scrollTxt(f'You are now a {character_class}')
        print()

        scrollTxt(f"{Fore.WHITE}Rolling stats...")
        print()
        time.sleep(1)

        scrollTxt(f'LVL: {lvl}')
        print_exp()
        if character_class == classes[0]:
            max_hp = random.randint(8, 9)
            hp = max_hp
            print_health()

            gp = random.randint(40, 60)
            print_gp()

            dex = random.randint(2, 3)
            scrollTxt(f"DEX: {dex}")

            defense = random.randint(7, 13)
            scrollTxt(f"DEF: {defense}")

            i = 0
            while i < 4:
                lvl1_available_spells.append(lvl1_all_spells[i])
                i += 1

            i = 0
            while i < 2:
                lvl2_available_spells.append(lvl2_all_spells[i])
                i += 1

            scrollTxt(f"Your known lvl 1 spells are: {str(lvl1_available_spells)}")
            scrollTxt(f"Your known lvl 2 spells are: {str(lvl2_available_spells)}")

            lvl1_spells = 3
            lvl2_spells = 1

            weapons = 'dagger'
            scrollTxt(f"Your weapon is {weapons}")
        if character_class == classes[1]:
            max_hp = random.randint(10, 12)
            hp = max_hp
            print_health()

            gp = random.randint(50, 70)
            print_gp()

            dex = random.randint(1, 2)
            scrollTxt(f"DEX: {dex}")

            defense = random.randint(10, 13)
            scrollTxt(f"DEF: {defense}")

            lvl1_available_spells.append(lvl1_all_spells[2])

            scrollTxt(f"Your known lvl 1 spells are: {str(lvl1_available_spells)}")
            scrollTxt(f"Your known lvl 2 spells are: {str(lvl2_available_spells)}")

            lvl1_spells = 1
            lvl2_spells = 0

            weapons = "sword"
            scrollTxt(f"Your weapon is {weapons}")
        if character_class == classes[2]:
            max_hp = random.randint(8, 10)
            hp = max_hp
            print_health()

            gp = random.randint(20, 40)
            print_gp()

            dex = random.randint(3, 5)
            scrollTxt(f"DEX: {dex}")

            defense = random.randint(5, 7)
            scrollTxt(f"DEF: {defense}")

            lvl1_available_spells.append(lvl1_all_spells[1])

            scrollTxt(f"Your known lvl 1 spells are: {str(lvl1_available_spells)}")
            scrollTxt(f"Your known lvl 2 spells are: {str(lvl2_available_spells)}")

            lvl1_spells = 1
            lvl2_spells = 0

            weapons = "bow"
            scrollTxt(f"Your weapon is {weapons}")
        if character_class == classes[3]:
            max_hp = random.randint(8, 9)
            hp = max_hp
            print_health()

            gp = random.randint(40, 70)
            print_gp()

            dex = random.randint(5, 7)
            scrollTxt(f"DEX: {dex}")

            defense = random.randint(3, 7)
            scrollTxt(f"DEF: {defense}")

            lvl1_available_spells.append(lvl1_all_spells[2])

            scrollTxt(f"Your known lvl 1 spells are: {str(lvl1_available_spells)}")
            scrollTxt(f"Your known lvl 2 spells are: {str(lvl2_available_spells)}")

            lvl1_spells = 1
            lvl2_spells = 0

            weapons = "pistol"
            scrollTxt(f"Your weapon is {weapons}")
        if character_class == classes[4]:
            max_hp = random.randint(10, 15)
            hp = max_hp
            print_health()

            gp = random.randint(15, 30)
            print_gp()

            dex = random.randint(-3, 2)
            scrollTxt(f"DEX: {dex}")

            defense = random.randint(12, 13)
            scrollTxt(f"DEF: {defense}")

            lvl1_available_spells.append('speed buff')

            scrollTxt(f"Your known lvl 1 spells are: {str(lvl1_available_spells)}")
            scrollTxt(f"Your known lvl 2 spells are: {str(lvl2_available_spells)}")

            lvl1_spells = 1
            lvl2_spells = 0

            weapons = "axe"
            scrollTxt(f"Your weapon is {weapons}")
        if character_class == classes[5]:
            max_hp = random.randint(9, 11)
            hp = max_hp
            print_health()

            gp = random.randint(10, 20)
            print_gp()

            dex = random.randint(3, 5)
            scrollTxt(f"DEX: {dex}")

            defense = random.randint(10, 14)
            scrollTxt(f"DEF: {defense}")

            lvl1_available_spells.append(lvl1_all_spells[3])
            lvl2_available_spells.append(lvl2_all_spells[1])

            scrollTxt(f"Your known lvl 1 spells are: {str(lvl1_available_spells)}")
            scrollTxt(f"Your known lvl 2 spells are: {str(lvl2_available_spells)}")

            lvl1_spells = 1
            lvl2_spells = 1

            weapons = "staff"
            scrollTxt(f"Your weapon is {weapons}")
        if character_class == 'Overdrive':
            max_hp = random.randint(10, 20)
            hp = max_hp
            print_health()

            gp = random.randint(400, 600)
            print_gp()

            dex = random.randint(7, 10)
            scrollTxt(f"DEX: {dex}")

            defense = random.randint(10, 13)
            scrollTxt(f"DEF: {defense}")

            i = 0
            while i < 6:
                lvl1_available_spells.append(lvl1_all_spells[i])
                i += 1

            i = 0
            while i < 4:
                lvl2_available_spells.append(lvl2_all_spells[i])
                i += 1

            scrollTxt(f"Your known lvl 1 spells are: {str(lvl1_available_spells)}")
            scrollTxt(f"Your known lvl 2 spells are: {str(lvl2_available_spells)}")

            lvl1_spells = 3
            lvl2_spells = 1

            weapons = 'frost blade'
            scrollTxt(f"Your weapon is {weapons}")
        if character_class == 'Troy':
            max_hp = random.randint(20, 30)
            hp = max_hp
            print_health()

            gp = random.randint(500, 700)
            print_gp()

            dex = random.randint(3, 5)
            scrollTxt(f"DEX: {dex}")

            defense = random.randint(13, 16)
            scrollTxt(f"DEF: {defense}")

            lvl1_available_spells.append(lvl1_all_spells[2])

            scrollTxt(f"Your known lvl 1 spells are: {str(lvl1_available_spells)}")
            scrollTxt(f"Your known lvl 2 spells are: {str(lvl2_available_spells)}")

            lvl1_spells = 1
            lvl2_spells = 0

            weapons = "Flame Blade"
            scrollTxt(f"Your weapon is {weapons}")

        inv.append(f'{weapons}')

        location = 'start village'

        candy = 0

        db[
            character] = character, character_class, race, max_hp, hp, gp, dex, defense, lvl1_available_spells, lvl2_available_spells, lvl1_spells, lvl2_spells, location, inv, weapons, exp, expNext, lvl, gems, world, candy, password

        bar()

        scrollTxt("Get ready for a test encounter")
        scrollTxt('If you throw your weapon you no longer have it')
        scrollTxt('{ENTER} to continue')
        answer = input()
        if answer != 'skip':
            system('clear')
            time.sleep(.5)

            battle("the goblin", ["slash", "stab", "charge", "rest"],
                   random.randint(5, 10), 2, 3, 1, 4, 20)

            hp = max_hp

            if ran is True:
                scrollTxt('There\'s no shame in running away')
                scrollTxt('You escaped the goblin')
            else:
                if lose is True:
                    scrollTxt('Don\'t worry you didn\'t really die')
                if lose is False:
                    scrollTxt('Good job you killed the goblin')

            scrollTxt('Now that your used to your class ready for your adventure?')
            enter()

    system('clear')
    print(logo)
    bar()

    while 1 == 1:
        while world == 'start':
            if location == 'start village' or location == 'small village':

                # START VILLAGE
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                db.get(answer)[20] = candy
                db.get(answer)[19] = world
                start_village = f"{Fore.LIGHTBLUE_EX}Lockwood{Fore.WHITE}"

                village_activites = [
                    'inn', 'merchants', 'converse', 'inventory', 'assess', 'settings',
                    'save', 'leave village'
                ]

                print(f'~{start_village}~')
                scrollTxt(f'You wake up in the bustling hamlet of {start_village}')
                scrollTxt('The shouts of merchants and the scents animals reaches you')
                startvill = False

                village_done = False

                while village_done is False:
                    if startvill == True:
                        print(f'~{start_village}~')
                    else:
                        startvill = True

                    commands = []
                    addList(commands, village_activites)
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    bar()

                    if answer == 'inn':
                        inn_done = False

                        print(f'~{Fore.LIGHTBLUE_EX}Inn{Fore.WHITE}~')
                        scrollTxt('You reach the inn after a short walk')
                        scrollTxt(
                            'The sound of music fills your ears and the aroma of food permeates'
                        )

                        while inn_done is False:

                            inn_activites = [
                                'merchant', 'musicians', 'rooms', 'gamble', 'leave'
                            ]

                            print()

                            commands = []
                            addList(commands, inn_activites)
                            printList(commands, 'Commands: ')
                            commands.append('murder')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'merchant':
                                scrollTxt('You walk over to the merchant')
                                scrollTxt(
                                    '\'Would you like to look at my wares?\' asks the merchant')

                                wares = ['nothing']
                                cost = []

                                lvl3_wares = ['Magic bread', 'Golden Apple', 'Blessed Water']
                                lvl3_cost = [40, 35, 30]

                                lvl2_wares = ['Hardy Pineapple', 'Dwarven Cake', 'Hardy Durian']
                                lvl2_cost = [10, 15, 5]

                                lvl1_wares = ['Apple', "Bread", "Potato"]
                                lvl1_cost = [1, 2, 3]

                                addList(wares, lvl1_wares)
                                addList(wares, lvl2_wares)
                                addList(wares, lvl3_wares)

                                addList(cost, lvl1_cost)
                                addList(cost, lvl2_cost)
                                addList(cost, lvl3_cost)

                                commands = []
                                addList(commands, ['y', 'n'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'y':
                                    bar()
                                    scrollTxt("~WARES~")
                                    addList(commands, lvl1_wares)
                                    commands = new_commands
                                    printShop(commands, lvl1_cost, "Tier 1 Wares - ")
                                    commands = []
                                    print()

                                    addList(commands, lvl2_wares)
                                    commands = new_commands
                                    printShop(commands, lvl2_cost, "Tier 2 Wares - ")
                                    commands = []
                                    print()

                                    addList(commands, lvl3_wares)
                                    commands = new_commands
                                    printShop(commands, lvl3_cost, "Tier 3 Wares - ")
                                    commands = []
                                    print()

                                    scrollTxt("What would you like to buy (type nothing to exit)")
                                    addList(commands, wares)
                                    commands = new_commands
                                    inputShop(wares, "", cost)
                                    items = len(inv)
                                    wares = new_wares
                                    gp = gp
                                    commands = []

                                    if nothing is True:
                                        done = True
                                    else:
                                        done = False
                                    while done is False:
                                        scrollTxt("Is that all?")
                                        commands.append("yes")
                                        commands.append("no")
                                        printList(commands, "Commands: ")
                                        inputCommands(commands, "")
                                        commands = []
                                        print()

                                        if answer == 'no':
                                            scrollTxt(
                                                "What would you like to buy (type nothing to exit)")
                                            addList(commands, wares)
                                            commands = new_commands
                                            inputShop(wares, "", cost)
                                            items = len(inv)
                                            wares = new_wares
                                            gp = gp
                                            commands = []
                                        else:
                                            done = True

                            if answer == 'musicians':
                                scrollTxt('You walk up to the musicians')
                                scrollTxt('As you draw closer, the melody intensifies')
                                scrollTxt(
                                    f'Would you like to tip? ({Fore.YELLOW}1{Fore.WHITE} GP)')

                                commands = []
                                addList(commands, ['yes', 'no'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'yes':
                                    scrollTxt('You tip them')
                                    scrollTxt('The lead musician smiles and thanks you')
                                    scrollTxt(f'-{Fore.YELLOW}1{Fore.WHITE} GP')

                                    gp -= 1
                                    print()

                            if answer == 'rooms':
                                scrollTxt(
                                    'You walk up to the front and ask the person there if you can buy a room'
                                )
                                scrollTxt(
                                    f'\'Sure rooms cost {Fore.YELLOW}3{Fore.WHITE} GP a night\', they say'
                                )
                                commands = []
                                addList(commands, ['yes', 'no'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'yes':
                                    print()
                                    scrollTxt('You buy a room')
                                    scrollTxt('In the morning you are completely healed')

                                    print_health()
                                    hp = max_hp

                                print()

                            if answer == 'gamble':
                                scrollTxt("You look around searching for a gambling table")
                                scrollTxt(
                                    'After finding one you sit your self down and ask to join in')
                                scrollTxt('The dealer nods and ask what you would like to play')
                                commands = ['black dragon', 'dice & cards', 'dice & towers']
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'black dragon':
                                    black_dragon('dealer')
                                    gp = gp

                                if answer == 'dice & cards':
                                    dice_and_cards('dealer')
                                    gp = gp

                                if answer == 'dice & towers':
                                    dice_towers('dealer')
                                    gp = gp

                                print()

                            if answer == 'leave':
                                scrollTxt('You leave the inn')
                                inn_done = True
                                print()

                            if answer == 'murder':
                                scrollTxt(
                                    'Driven by craze for gold you decide it best to murder someone...'
                                )
                                scrollTxt(
                                    f'As you raise your {weapons} to strike down a innocient civilian, someone notices and screams!'
                                )
                                scrollTxt('Then the police start rushing in...')
                                scrollTxt('You try to run but they catch you')
                                battle('The Police', ['punch', 'charge', 'shoot'], random.randint(10, 20), 3, 8, 2, 30,
                                       40)
                                if ran is True:
                                    scrollTxt('There\'s no escape from the law...')
                                    scrollTxt('jk you escaped')
                                else:
                                    if lose is True:
                                        scrollTxt('You died a criminal')
                                    if lose is False:
                                        scrollTxt('You murder the police')

                    if answer == 'merchants':
                        merchant_done = False

                        print(f'~{Fore.LIGHTBLUE_EX}Merchants{Fore.WHITE}~')
                        scrollTxt('You walk over to the many vendors west of the gate')
                        scrollTxt(
                            'The vendor to the left is a stoud dwarf who appears to be selling weapons\n'
                            'To the right is a kenku (bird-like humanoid) selling an assortment of roasted meats'
                        )

                        while merchant_done is False:

                            commands = []
                            addList(commands, ['left', 'right', 'leave'])
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            print()

                            if answer == 'left':
                                scrollTxt(
                                    f"\"Welcome to {Fore.LIGHTBLUE_EX}Makud Greatbrew\'s{Fore.WHITE} weapon shop\", booms the dwarf"
                                )
                                scrollTxt("\"Would you like to look at my wares?\", they ask")

                                wares = ['nothing']
                                cost = []

                                lvl3_wares = ['magic sword', 'steel shield', 'cursed War Hammer']
                                lvl3_cost = [350, 100, 120]

                                lvl2_wares = ['steel sword', 'dwarven bow', 'iron shield']
                                lvl2_cost = [70, 50, 40]

                                lvl1_wares = ['rusty sword', "axe", "travelers shield"]
                                lvl1_cost = [10, 30, 20]

                                addList(wares, lvl1_wares)
                                addList(wares, lvl2_wares)
                                addList(wares, lvl3_wares)

                                addList(cost, lvl1_cost)
                                addList(cost, lvl2_cost)
                                addList(cost, lvl3_cost)

                                commands = []
                                addList(commands, ['y', 'n'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'y':
                                    bar()
                                    scrollTxt("~WARES~")
                                    addList(commands, lvl1_wares)
                                    commands = new_commands
                                    printShop(commands, lvl1_cost, "Tier 1 Wares - ")
                                    commands = []
                                    print()

                                    addList(commands, lvl2_wares)
                                    commands = new_commands
                                    printShop(commands, lvl2_cost, "Tier 2 Wares - ")
                                    commands = []
                                    print()

                                    addList(commands, lvl3_wares)
                                    commands = new_commands
                                    printShop(commands, lvl3_cost, "Tier 3 Wares - ")
                                    commands = []
                                    print()

                                    scrollTxt("What would you like to buy (type nothing to exit)")
                                    addList(commands, wares)
                                    commands = new_commands
                                    inputShop(wares, "", cost)
                                    items = len(inv)
                                    wares = new_wares
                                    gp = gp
                                    commands = []

                                    if nothing is True:
                                        done = True
                                    else:
                                        done = False
                                    while done == False:
                                        scrollTxt("Is that all?")
                                        commands.append("yes")
                                        commands.append("no")
                                        printList(commands, "Commands: ")
                                        inputCommands(commands, "")
                                        commands = []
                                        print()

                                        if answer == 'no':
                                            scrollTxt(
                                                "What would you like to buy (type nothing to exit)")
                                            addList(commands, wares)
                                            commands = new_commands
                                            inputShop(wares, "", cost)
                                            items = len(inv)
                                            wares = new_wares
                                            gp = gp
                                            commands = []
                                        else:
                                            done = True
                                print()

                            if answer == 'right':
                                scrollTxt('You walk over to the kenku')
                                scrollTxt(
                                    '\'Would you like to look at my wares?\' asks the kenu')

                                wares = ['nothing']
                                cost = []

                                lvl3_wares = [
                                    'Golden Meat Kebab', 'Golden Steak', 'Gourmet Boar Meat'
                                ]
                                lvl3_cost = [50, 40, 45]

                                lvl2_wares = [
                                    'Hardy Chicken', 'Dwarven Feast Turkey', 'Elven Jerky'
                                ]
                                lvl2_cost = [10, 30, 20]

                                lvl1_wares = ['Stake', 'Chicken', "Orc bone marrow"]
                                lvl1_cost = [5, 2, 3]

                                addList(wares, lvl1_wares)
                                addList(wares, lvl2_wares)
                                addList(wares, lvl3_wares)

                                addList(cost, lvl1_cost)
                                addList(cost, lvl2_cost)
                                addList(cost, lvl3_cost)

                                commands = []
                                addList(commands, ['y', 'n'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'y':
                                    bar()
                                    scrollTxt("~WARES~")
                                    addList(commands, lvl1_wares)
                                    commands = new_commands
                                    printShop(commands, lvl1_cost, "Tier 1 Wares - ")
                                    commands = []
                                    print()

                                    addList(commands, lvl2_wares)
                                    commands = new_commands
                                    printShop(commands, lvl2_cost, "Tier 2 Wares - ")
                                    commands = []
                                    print()

                                    addList(commands, lvl3_wares)
                                    commands = new_commands
                                    printShop(commands, lvl3_cost, "Tier 3 Wares - ")
                                    commands = []
                                    print()

                                    scrollTxt("What would you like to buy (type nothing to exit)")
                                    addList(commands, wares)
                                    commands = new_commands
                                    inputShop(wares, "", cost)
                                    items = len(inv)
                                    wares = new_wares
                                    gp = gp
                                    commands = []

                                    if nothing is True:
                                        done = True
                                    else:
                                        done = False
                                    while done == False:
                                        scrollTxt("Is that all?")
                                        commands.append("yes")
                                        commands.append("no")
                                        printList(commands, "Commands: ")
                                        inputCommands(commands, "")
                                        commands = []
                                        print()

                                        if answer == 'no':
                                            scrollTxt(
                                                "What would you like to buy (type nothing to exit)")
                                            addList(commands, wares)
                                            commands = new_commands
                                            inputShop(wares, "", cost)
                                            items = len(inv)
                                            wares = new_wares
                                            gp = gp
                                            commands = []
                                        else:
                                            done = True
                                print()

                            if answer == 'leave':
                                scrollTxt('You leave the merchants')
                                merchant_done = True
                                print()

                    if answer == 'converse':
                        converse_done = False
                        print(f'~{Fore.LIGHTBLUE_EX}Market{Fore.WHITE}~')
                        scrollTxt(
                            'You walk over to the many people bustling around the market center'
                        )
                        if ruffians is True:
                            scrollTxt('You see a group of rowdy ruffians in one corner')
                        if nobles is True:
                            scrollTxt(
                                'In the other corner you see a group of gossiping nobles')
                        scrollTxt('Who would you like to talk to?')

                        while converse_done is False:

                            commands = ['leave']
                            if ruffians is True:
                                commands.append('rowdy ruffians')
                            if nobles is True:
                                commands.append('gossiping nobles')
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'rowdy ruffians':
                                print()
                                ruffians = False
                                mob_boss = f'{Fore.LIGHTBLUE_EX}Glarb the fearsome{Fore.WHITE}'
                                NPCtalk(
                                    'The ruffians look at you as you strut up, \'Who are you\'', [
                                        '1 ~ No one that concerns you', '2 ~ just a stranger',
                                        '3 ~ I don\'t know'
                                    ],
                                    f'\'No one talks to {mob_boss} that way\' growls the leader',
                                    '\'Well then stranger, get lost\' growls the leader',
                                    '\'Then get lost!\' yells the leader')
                                print()

                                if happen == 1:
                                    scrollTxt(f'{mob_boss} charges at you!')
                                    scrollTxt('Get ready to fight')
                                    enter()

                                    battle(f"{mob_boss}", ["slash", "stab", "charge", "punch"],
                                           random.randint(7, 10), 3, 5, 1, 7, 40)
                                    print()
                                    hp = hp
                                    gp = gp
                                    bullets = bullets
                                    arrows = arrows

                                    if ran is True:
                                        scrollTxt('You run from the the rowdy ruffians')
                                        scrollTxt(f'You escaped the {mob_boss}')
                                    else:
                                        if lose is True:
                                            scrollTxt('You died game over...')
                                            scrollTxt(f'{mob_boss} killed you')
                                            quit()
                                        if lose is False:
                                            scrollTxt(f'You stand victorious over {mob_boss}')
                                            scrollTxt('The other ruffians run away')
                                    print()

                                if happen == 2 or happen == 3:
                                    scrollTxt('What do you do?')
                                    commands = []
                                    addList(commands, ['1 ~ leave', '2 ~ stand your ground'])
                                    printList(commands, 'Commands: ')
                                    commands = ['1', '2']
                                    inputCommands(commands, "")

                                    if answer == 'stand your ground':
                                        scrollTxt(f'{mob_boss} charges at you!')
                                        scrollTxt('Get ready to fight')
                                        enter()

                                        battle(f"{mob_boss}", ["slash", "stab", "charge", "punch"],
                                               random.randint(7, 10), 3, 5, 1, 7, 40)
                                        hp = hp
                                        gp = gp
                                        bullets = bullets
                                        arrows = arrows
                                        print()

                                        if ran is True:
                                            scrollTxt('You run from the the rowdy ruffians')
                                            scrollTxt(f'You escaped the {mob_boss}')
                                        else:
                                            if lose is True:
                                                scrollTxt('You died game over...')
                                                scrollTxt(f'{mob_boss} killed you')
                                                quit()
                                            if lose is False:
                                                scrollTxt(f'You stand victorious over {mob_boss}')
                                                scrollTxt('The other ruffians run away')
                                        print()

                                    if answer == 'leave':
                                        scrollTxt('You leave the rowdy ruffians')
                                        print()

                            if answer == 'gossiping nobles':
                                print()
                                nobles = False
                                noble_leader = f'{Fore.LIGHTBLUE_EX}Zander noble of {start_village}{Fore.WHITE}'
                                NPCtalk(
                                    'You walk over to the nobles, as you get closer you can hear them talking about a'
                                    ' huge bugbear(hairy goblinoids) near the cave north of the village\nThey speak about the great reward'
                                    ' that is offered to anyone who can slay the beast\nWhat do you do?',
                                    [
                                        '1 ~ say \'I can defeat the beast\'', '2 ~ leave',
                                        '3 ~ stay silent'
                                    ],
                                    'the nobles all laugh at you and say that there is no way you can defeat the bugbear',
                                    'You leave the nobles',
                                    'After awhile one of the nobles notices you and tells you to get lost\nYou leave'
                                )
                                print()

                                if happen == 1:
                                    scrollTxt('What do you do?')
                                    commands = []
                                    addList(commands,
                                            ['1 ~ leave', '2 ~ retort back at the lead noble'])
                                    printList(commands, 'Commands: ')
                                    commands = ['1', '2']
                                    inputCommands(commands, "")

                                    if answer == '1':
                                        scrollTxt(
                                            'Ashamed you leave the nobles as they laugh and laugh at you'
                                        )

                                        print()
                                    if answer == '2':
                                        scrollTxt(
                                            'You retort back at the lead noble, dishonoring them, shaming them'
                                        )
                                        scrollTxt(
                                            '\'How dare you question my honor!\' screams the lead noble'
                                        )
                                        scrollTxt('Then they charge at you')
                                        scrollTxt('Get ready for a fight')
                                        enter()

                                        battle(f"the lead noble",
                                               ["slash", "stab", "charge", "dodge"],
                                               random.randint(5, 7), 4, 5, 1.5, 23, 10)
                                        print()
                                        hp = hp
                                        gp = gp
                                        bullets = bullets
                                        arrows = arrows

                                        if ran is True:
                                            scrollTxt('You run away from the lead noble')
                                            scrollTxt('You escaped the lead noble')
                                        else:
                                            if lose is True:
                                                scrollTxt('You died game over...')
                                                scrollTxt(f'the lead noble killed you')
                                                quit()
                                            if lose is False:
                                                scrollTxt(f'You stand victorious over the lead noble')
                                                scrollTxt('The other nobles run away')
                                        print()

                            if answer == 'leave':
                                scrollTxt('You leave the market')
                                converse_done = True
                                print()

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        answer = character
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        db.get(answer)[19] = world
                        print()

                    if answer == 'leave village':
                        scrollTxt('You leave the village...')
                        scrollTxt(
                            'You are now right outside the village in the open plains...')
                        location = 'open plains'
                        village_done = True
                        print()

            if location == 'open plains':
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                db.get(answer)[19] = world
                start = True
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Open Plains{Fore.WHITE}~')
                scrollTxt(
                    'You are in the open plains to the north are great mountains, to the south the small village, to the east and west are grasslands'
                )

                while location == 'open plains':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Open Plains{Fore.WHITE}~')
                    else:
                        start = False

                    commands = []
                    addList(commands, [
                        'encounter', 'explore', 'inventory', 'assess', 'settings', 'save',
                        'travel south', 'travel east', 'travel west'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'encounter':
                        scrollTxt('You search for monster or beasts to fight...')
                        time.sleep(1)
                        monster = random.choice(
                            ['lion', 'goblin', 'mutant snake', 'bugbear'])
                        scrollTxt(f'Finally you see a {monster}')
                        enter()

                        if monster == 'lion':
                            battle('the lion', ['wild slash', 'claw', 'charge'],
                                   random.randint(5, 10), 6, 4, 1, 0, 20)

                            if ran is True:
                                scrollTxt('You run from lion')
                                scrollTxt(f'You escaped the lion')
                            else:
                                if lose is True:
                                    scrollTxt('You died game over...')
                                    scrollTxt(f'the lion killed you')
                                    quit()
                                if lose is False:
                                    scrollTxt(f'You stand victorious over the lion')
                                    print()

                        if monster == 'goblin':
                            battle('the goblin', ['slash', 'stab', 'charge', 'punch'],
                                   random.randint(5, 10), 3, 8, 1, 10, 20)

                            if ran is True:
                                scrollTxt('You run from goblin')
                                scrollTxt(f'You escaped the goblin')
                            else:
                                if lose is True:
                                    scrollTxt('You died game over...')
                                    scrollTxt(f'the goblin killed you')
                                    quit()
                                if lose is False:
                                    scrollTxt(f'You stand victorious over the goblin')
                                    print()

                        if monster == 'mutant snake':
                            battle('the mutant snake',
                                   ['rest', 'acid blast', 'charge', 'chant'],
                                   random.randint(4, 7), 7, 3, 1.5, 0, 20)

                            if ran is True:
                                scrollTxt('You run from the mutant snake')
                                scrollTxt(f'You escaped the mutant snake')
                            else:
                                if lose is True:
                                    scrollTxt('You died game over...')
                                    scrollTxt(f'the mutant snake killed you')
                                    quit()
                                if lose is False:
                                    scrollTxt(f'You stand victorious over the muntant snake')
                                    print()

                        if monster == 'bugbear':
                            battle('the bugbear', [
                                'rest', 'stab', 'charge', 'chant', 'wild slash', 'claw', 'punch'
                            ], random.randint(7, 13), 3, 10, 1.5, random.randint(5, 15), 40)

                            if ran is True:
                                scrollTxt('You run from the bugbear')
                                scrollTxt(f'You escaped the bugbear')
                            else:
                                if lose is True:
                                    scrollTxt('You died game over...')
                                    scrollTxt(f'the bugbear killed you')
                                    quit()
                                if lose is False:
                                    scrollTxt(f'You stand victorious over the bugbear')
                                    print()

                        print()

                    if answer == 'explore':
                        scrollTxt('You spend the whole day exploring...')
                        time.sleep(2)
                        i = random.randint(1, 3)
                        if i == 3:
                            scrollTxt('You found some wheat')
                            inv.append('wheat')
                            inv.append('wheat')
                        elif i == 2:
                            scrollTxt('You found some grain')
                            inv.append('grain')
                            inv.append('grain')
                        else:
                            scrollTxt('You found nothing')
                        print()

                    if answer == 'travel south':
                        bar()
                        scrollTxt(
                            'You travel for many days before coming upon a small village')
                        location = 'start village'
                        print()

                    if answer == 'travel east':
                        bar()
                        scrollTxt(
                            'You travel for an hour before the plains turn lush and green')
                        location = 'grassland shop'
                        print()

                    if answer == 'travel west':
                        bar()
                        scrollTxt(
                            'You travel for an hour before the plains turn lush and green')
                        location = 'grassland encounter'
                        print()

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[19] = world
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()

            if location == 'grassland shop':
                start = True
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                db.get(answer)[19] = world
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Grassland{Fore.WHITE}~')
                scrollTxt(
                    'You are in the grasslands ,to the north are great mountains, to the south wheat plains, to the east is the start of a forest and to the west are more plains'
                )
                scrollTxt('You can also see a merchant in the distance')

                while location == 'grassland shop':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Grassland{Fore.WHITE}~')
                    else:
                        start = False
                    commands = []
                    addList(commands, [
                        'encounter', 'explore', 'inventory', 'assess', 'settings',
                        'merchant', 'save', 'travel south', 'travel east', 'travel west'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'encounter':
                        scrollTxt('You search for monster or beasts to fight...')
                        time.sleep(1)
                        monster = random.choice(
                            ['rabid rabbit', 'goblin', 'mutant snake', 'bugbear'])
                        scrollTxt(f'Finally you see a {monster}')
                        enter()

                        if monster == 'rabid rabbit':
                            battle('rabid rabbit', ['wild slash', 'claw', 'charge'],
                                   random.randint(3, 7), 7, 2, 1.5, 0, 15)

                        if monster == 'goblin':
                            battle('the goblin', ['slash', 'stab', 'charge', 'punch'],
                                   random.randint(5, 10), 3, 8, 1, 10, 20)

                        if monster == 'mutant snake':
                            battle('the mutant snake',
                                   ['rest', 'acid blast', 'charge', 'chant'],
                                   random.randint(4, 7), 7, 3, 1.5, 0, 20)

                        if monster == 'bugbear':
                            battle('the bugbear', [
                                'rest', 'stab', 'charge', 'chant', 'wild slash', 'claw', 'punch'
                            ], random.randint(7, 13), 3, 10, 1.5, random.randint(5, 15), 40)

                        if ran is True:
                            scrollTxt(f'You run from the {monster}')
                            scrollTxt(f'You escaped the {monster}')
                        else:
                            if lose is True:
                                scrollTxt('You died game over...')
                                scrollTxt(f'the {monster} killed you')
                                quit()
                            if lose is False:
                                scrollTxt(f'You stand victorious over the {monster}')
                        print()

                    if answer == 'explore':
                        scrollTxt('You spend the whole day exploring...')
                        time.sleep(4)
                        i = random.randint(1, 3)
                        if i == 3:
                            scrollTxt('You found some apples')
                            inv.append('apple')
                            inv.append('apple')
                        elif i == 2:
                            scrollTxt('You found some grass')
                            inv.append('grass')
                            inv.append('grass')
                        else:
                            scrollTxt('You found nothing')
                        print()

                    if answer == 'merchant':
                        scrollTxt('You walk over to the merchant')
                        scrollTxt(
                            '\'Would you like to look at my wares?\' asks the merchant')

                        wares = ['nothing']
                        cost = []

                        lvl3_wares = ['poison pistol', 'fire bow']
                        lvl3_cost = [70, 75]

                        lvl2_wares = ['morningstar', 'scimitar', 'rapier']
                        lvl2_cost = [30, 20, 17]

                        lvl1_wares = ['Eggs', "Sorghum bread", "spear"]
                        lvl1_cost = [4, 2, 10]

                        addList(wares, lvl1_wares)
                        addList(wares, lvl2_wares)
                        addList(wares, lvl3_wares)

                        addList(cost, lvl1_cost)
                        addList(cost, lvl2_cost)
                        addList(cost, lvl3_cost)

                        commands = []
                        addList(commands, ['y', 'n'])
                        printList(commands, 'Commands: ')
                        inputCommands(commands, "")
                        commands = []

                        if answer == 'y':
                            bar()
                            scrollTxt("~WARES~")
                            addList(commands, lvl1_wares)
                            commands = new_commands
                            printShop(commands, lvl1_cost, "Tier 1 Wares - ")
                            commands = []
                            print()

                            addList(commands, lvl2_wares)
                            commands = new_commands
                            printShop(commands, lvl2_cost, "Tier 2 Wares - ")
                            commands = []
                            print()

                            addList(commands, lvl3_wares)
                            commands = new_commands
                            printShop(commands, lvl3_cost, "Tier 3 Wares - ")
                            commands = []
                            print()

                            scrollTxt("What would you like to buy (type nothing to exit)")
                            addList(commands, wares)
                            commands = new_commands
                            inputShop(wares, "", cost)
                            items = len(inv)
                            wares = new_wares
                            gp = gp
                            commands = []

                            if nothing is True:
                                done = True
                            else:
                                done = False
                            while done is False:
                                scrollTxt("Is that all?")
                                commands.append("yes")
                                commands.append("no")
                                printList(commands, "Commands: ")
                                inputCommands(commands, "")
                                commands = []
                                print()

                                if answer == 'no':
                                    scrollTxt("What would you like to buy (type nothing to exit)")
                                    addList(commands, wares)
                                    commands = new_commands
                                    inputShop(wares, "", cost)
                                    items = len(inv)
                                    wares = new_wares
                                    gp = gp
                                    commands = []
                                else:
                                    done = True

                    if answer == 'travel west':
                        bar()
                        scrollTxt('You travel for 6 hours before the grass becomes dryer')
                        scrollTxt('You are now in the plains')
                        location = 'open plains'

                    if answer == 'travel south':
                        bar()
                        scrollTxt('You travel for 6 hours before the grass becomes dryer')
                        scrollTxt('You are now in the plains')
                        location = 'open plains encounter'

                    if answer == 'travel east':
                        bar()
                        scrollTxt('You travel for 6 hours before the grass turns into trees')
                        scrollTxt('You are now in the forest')
                        location = 'forest'
                        bar()

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[19] = world
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()

            if location == 'grassland encounter':
                start = True
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[19] = world
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Grassland{Fore.WHITE}~')
                scrollTxt('You are in the grasslands,'
                          ' to the north and west are great mountains,'
                          ' to the south wheat plains,'
                          ' and to the east are more plains')
                time.sleep(1)
                scrollTxt('A huge ogre is charging at you!')
                enter()
                battle('the huge ogre', [
                    'rest', 'stab', 'charge', 'chant', 'wild slash', 'claw', 'punch',
                    'smash'
                ], random.randint(10, 15), 3, 7, 2, random.randint(10, 20), 65)

                if ran is True:
                    scrollTxt('You run from the huge ogre')
                    scrollTxt(f'You escaped the huge ogre')
                else:
                    if lose is True:
                        scrollTxt('You died game over...')
                        scrollTxt(f'the ogre killed you')
                        quit()
                    if lose is False:
                        scrollTxt(f'You stand victorious over the ogre')
                        scrollTxt('After a quick examination you find some ogre teeth')
                        scrollTxt('+2 ogre tooth')
                        inv.append('ogre tooth')
                        inv.append('ogre tooth')
                print()

                while location == 'grassland encounter':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Grassland{Fore.WHITE}~')
                    else:
                        start = False
                    commands = []
                    addList(commands, [
                        'encounter', 'rest', 'inventory', 'assess', 'settings', 'save',
                        'travel south', 'travel east'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'encounter':
                        scrollTxt('You search for monster or beasts to fight...')
                        time.sleep(1)
                        monster = random.choice(
                            ['rabid rabbit', 'goblin', 'gnoll', 'bugbear'])
                        scrollTxt(f'Finally you see a {monster}')
                        enter()

                        if monster == 'rabid rabbit':
                            battle('rabid rabbit', ['wild slash', 'claw', 'charge'],
                                   random.randint(3, 7), 7, 2, 1.5, 0, 15)

                        if monster == 'goblin':
                            battle('the goblin', ['slash', 'stab', 'charge', 'punch'],
                                   random.randint(5, 10), 3, 8, 1, 10, 20)

                        if monster == 'gnoll':
                            battle('the gnoll', ['rest', 'stab', 'claw', 'chant'],
                                   random.randint(7, 11), 5, 4, 1, random.randint(1, 5), 30)

                        if monster == 'bugbear':
                            battle('the bugbear', [
                                'rest', 'stab', 'charge', 'chant', 'wild slash', 'claw', 'punch'
                            ], random.randint(7, 13), 3, 10, 1.5, random.randint(5, 15), 40)

                        if ran is True:
                            scrollTxt(f'You run from the {monster}')
                            scrollTxt(f'You escaped the {monster}')
                        else:
                            if lose is True:
                                scrollTxt('You died game over...')
                                scrollTxt(f'the {monster} killed you')
                                quit()
                            if lose is False:
                                scrollTxt(f'You stand victorious over the {monster}')
                        print()

                    if answer == 'rest':
                        scrollTxt('You rest for 4 hours')
                        time.sleep(2)
                        scrollTxt(f'You healed {Fore.RED}1{Fore.WHITE} health')
                        hp += 1
                        print()

                    if answer == 'travel east':
                        bar()
                        scrollTxt('You travel for 6 hours before the grass becomes dryer')
                        scrollTxt('You are now in the plains')
                        location = 'open plains'

                    if answer == 'travel south':
                        bar()
                        scrollTxt(
                            'You travel for 2 hours before the grass drys out and becomes wheat'
                        )
                        print()
                        location = 'open plains shop'
                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[19] = world
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()

            if location == 'open plains shop':
                start = True
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[19] = world
                db.get(answer)[17] = lvl
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Open Plains{Fore.WHITE}~')
                scrollTxt(
                    'You are in the open plains to the north are grasslands, to the south the a mysterious cave, to the east a small village and to the west are grasslands'
                )
                scrollTxt('You can see a merchant in the distance')

                while location == 'open plains shop':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Open Plains{Fore.WHITE}~')
                    else:
                        start = False

                    commands = []
                    addList(commands, [
                        'encounter', 'explore', 'inventory', 'assess', 'merchant',
                        'settings', 'save', 'travel south', 'travel east', 'travel west'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'encounter':
                        scrollTxt('You search for monster or beasts to fight...')
                        time.sleep(1)
                        monster = random.choice(
                            ['lion', 'goblin', 'wheat monster', 'bugbear'])
                        scrollTxt(f'Finally you see a {monster}')
                        enter()

                        if monster == 'lion':
                            battle('the lion', ['wild slash', 'claw', 'charge'],
                                   random.randint(5, 10), 6, 4, 1, 0, 20)

                            if ran is True:
                                scrollTxt('You run from lion')
                                scrollTxt(f'You escaped the lion')
                            else:
                                if lose is True:
                                    scrollTxt('You died game over...')
                                    scrollTxt(f'the lion killed you')
                                    quit()
                                if lose is False:
                                    scrollTxt(f'You stand victorious over the lion')
                            print()

                        if monster == 'goblin':
                            battle('the goblin', ['slash', 'stab', 'charge', 'punch'],
                                   random.randint(5, 10), 3, 8, 1, 10, 20)

                            if ran is True:
                                scrollTxt('You run from goblin')
                                scrollTxt(f'You escaped the goblin')
                            else:
                                if lose is True:
                                    scrollTxt('You died game over...')
                                    scrollTxt(f'the goblin killed you')
                                    quit()
                                if lose is False:
                                    scrollTxt(f'You stand victorious over the goblin')
                            print()

                        if monster == 'wheat monster':
                            battle('the wheat monster', ['rest', 'punch', 'charge', 'smash'],
                                   random.randint(10, 23), 1, 4, 1.5, 0, 40)

                            if ran is True:
                                scrollTxt('You run from the wheat monster')
                                scrollTxt(f'You escaped the wheat monster')
                            else:
                                if lose is True:
                                    scrollTxt('You died game over...')
                                    scrollTxt(f'the wheat monster killed you')
                                    quit()
                                if lose is False:
                                    scrollTxt(f'You stand victorious over the wheat monster')
                            print()

                        if monster == 'bugbear':
                            battle('the bugbear', [
                                'rest', 'stab', 'charge', 'chant', 'wild slash', 'claw', 'punch'
                            ], random.randint(7, 13), 3, 10, 1.5, random.randint(5, 15), 40)

                            if ran is True:
                                scrollTxt('You run from the bugbear')
                                scrollTxt(f'You escaped the bugbear')
                            else:
                                if lose is True:
                                    scrollTxt('You died game over...')
                                    scrollTxt(f'the bugbear killed you')
                                    quit()
                                if lose is False:
                                    scrollTxt(f'You stand victorious over the bugbear')
                            print()

                        print()

                    if answer == 'explore':
                        scrollTxt('You spend the whole day exploring...')
                        time.sleep(2)
                        i = random.randint(1, 3)
                        if i == 3:
                            scrollTxt('You found some wheat')
                            inv.append('wheat')
                            inv.append('wheat')
                        elif i == 2:
                            scrollTxt('You found some grain')
                            inv.append('grain')
                            inv.append('grain')
                        else:
                            scrollTxt('You found nothing')
                        print()

                    if answer == 'merchant':
                        scrollTxt('You walk over to the merchant')
                        scrollTxt(
                            '\'Would you like to look at my wares?\' asks the merchant')

                        wares = ['nothing']
                        cost = []

                        lvl3_wares = ['Golden wheat', 'Blessed wheat']
                        lvl3_cost = [15, 13]

                        lvl2_wares = ['Hardy wheat', 'Elven wheat', 'Dwarven wheat']
                        lvl2_cost = [10, 12, 8]

                        lvl1_wares = ['pike', "wheat", "wheat"]
                        lvl1_cost = [12, 2, 10]

                        addList(wares, lvl1_wares)
                        addList(wares, lvl2_wares)
                        addList(wares, lvl3_wares)

                        addList(cost, lvl1_cost)
                        addList(cost, lvl2_cost)
                        addList(cost, lvl3_cost)

                        commands = []
                        addList(commands, ['y', 'n'])
                        printList(commands, 'Commands: ')
                        inputCommands(commands, "")
                        commands = []

                        if answer == 'y':
                            bar()
                            scrollTxt("~WARES~")
                            addList(commands, lvl1_wares)
                            commands = new_commands
                            printShop(commands, lvl1_cost, "Tier 1 Wares - ")
                            commands = []
                            print()

                            addList(commands, lvl2_wares)
                            commands = new_commands
                            printShop(commands, lvl2_cost, "Tier 2 Wares - ")
                            commands = []
                            print()

                            addList(commands, lvl3_wares)
                            commands = new_commands
                            printShop(commands, lvl3_cost, "Tier 3 Wares - ")
                            commands = []
                            print()

                            scrollTxt("What would you like to buy (type nothing to exit)")
                            addList(commands, wares)
                            commands = new_commands
                            inputShop(wares, "", cost)
                            items = len(inv)
                            wares = new_wares
                            gp = gp
                            commands = []

                            if nothing is True:
                                done = True
                            else:
                                done = False
                            while done is False:
                                scrollTxt("Is that all?")
                                commands.append("yes")
                                commands.append("no")
                                printList(commands, "Commands: ")
                                inputCommands(commands, "")
                                commands = []
                                print()

                                if answer == 'no':
                                    scrollTxt("What would you like to buy (type nothing to exit)")
                                    addList(commands, wares)
                                    commands = new_commands
                                    inputShop(wares, "", cost)
                                    items = len(inv)
                                    wares = new_wares
                                    gp = gp
                                    commands = []
                                else:
                                    done = True

                    if answer == 'travel north':
                        bar()
                        scrollTxt(
                            'You travel for an hour before the plains turn lush and green')
                        location = 'grassland encounter'
                        print()

                    if answer == 'travel east':
                        bar()
                        scrollTxt('You travel for many days before comming upon a village')
                        location = 'start village'
                        print()

                    if answer == 'travel south':
                        bar()
                        scrollTxt('You travel for many days before comming upon a cave')
                        location = 'mysterious cave'
                        print()

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[19] = world
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()

            if location == 'open plains encounter':
                start = True
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[19] = world
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Open Plains{Fore.WHITE}~')
                scrollTxt(
                    'You are in the open plains to the north,to the east are grasslands, to the south an arena, to the west a small village'
                )
                scrollTxt('Suddently a wizard appears in front of you')
                scrollTxt('They ask if you would like to learn \'DRAIN\'')
                scrollTxt(f'It cost {Fore.YELLOW}30{Fore.WHITE}GP')
                commands = ['yes', 'no']
                printList(commands, '')
                inputCommands(commands, '')
                if answer == 'yes':
                    if gp > 30:
                        gp -= 30
                        scrollTxt(f'-{Fore.YELLOW}30{Fore.WHITE}GP')
                        scrollTxt('+DRAIN spell')
                        lvl2_spells += 1
                        lvl2_available_spells.append('drain')
                    else:
                        scrollTxt('You don\'t have enough money')
                print()
                commands = []

                scrollTxt('They ask if you would like to learn \'ICE SHARDS\'')
                scrollTxt(f'It cost {Fore.YELLOW}30{Fore.WHITE}GP')
                commands = ['yes', 'no']
                printList(commands, '')
                inputCommands(commands, '')
                if answer == 'yes':
                    if gp > 30:
                        gp -= 30
                        scrollTxt(f'-{Fore.YELLOW}30{Fore.WHITE}GP')
                        scrollTxt('+ICE SHARDS spell')
                        lvl2_spells += 1
                        lvl2_available_spells.append('ice shards')
                    else:
                        scrollTxt('You don\'t have enough money')
                print()
                commands = []

                scrollTxt('They then ask if you would like more spell slots')
                scrollTxt(f'It cost {Fore.YELLOW}20{Fore.WHITE}GP')
                commands = ['yes', 'no']
                inputCommands(commands, '')
                if answer == 'yes':
                    if gp > 20:
                        scrollTxt('+2 spell slots')
                        scrollTxt(f'-{Fore.YELLOW}20{Fore.WHITE} GP')
                        lvl1_spells += 1
                        lvl2_spells += 1
                        gp -= 20
                    else:
                        scrollTxt('You don\'t have enough money')

                while location == 'open plains encounter':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Open Plains{Fore.WHITE}~')
                    else:
                        start = False

                    commands = []
                    addList(commands, [
                        'explore', 'inventory', 'assess', 'settings', 'save', 'travel south',
                        'travel east', 'travel west', 'travel north'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'explore':
                        scrollTxt('You spend the whole day exploring...')
                        time.sleep(2)
                        i = random.randint(1, 3)
                        if i == 3:
                            scrollTxt('You found some wheat')
                            inv.append('wheat')
                            inv.append('wheat')
                        elif i == 2:
                            scrollTxt('You found some grain')
                            inv.append('grain')
                            inv.append('grain')
                        else:
                            scrollTxt('You found nothing')
                        print()

                    if answer == 'travel north':
                        bar()
                        scrollTxt(
                            'You travel for an hour before the plains turn lush and green')
                        location = 'grassland shop'
                        print()

                    if answer == 'travel south':
                        bar()
                        scrollTxt(
                            'You travel for an hour before coming upon the great arena')
                        location = 'arena'
                        print()

                    if answer == 'travel west':
                        bar()
                        scrollTxt(
                            'You travel for many days before coming upon a small village')
                        location = 'start village'
                        print()

                    if answer == 'travel east':
                        bar()
                        scrollTxt(
                            'You travel for an hour before the plains turn lush and green')
                        location = 'grassland'
                        print()

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[19] = world
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()
                        lvl2_spells += 1

            if location == 'mysterious cave':
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[19] = world
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                start = True
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Mysterious Cave{Fore.WHITE}~')
                scrollTxt('You can see a great cave looming above you...')
                scrollTxt(
                    'To the north and east are plains, to the south is a great dungeon, and to the west are grasslands.'
                )

                while location == 'mysterious cave':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Open Plains{Fore.WHITE}~')
                    else:
                        start = False

                    commands = []
                    addList(commands, [
                        'explore', 'inventory', 'assess', 'settings', 'travel north', 'save',
                        'go in the cave', 'travel east', 'travel south'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'go in the cave':
                        scrollTxt('You enter the cave...')
                        enter()
                        system('clear')
                        bar()
                        mysteriousCave()

                    if answer == 'travel north':
                        scrollTxt('You travel for many days before reaching the open plains')
                        location = 'open plains shop'
                        bar()

                    if answer == 'travel south':
                        scrollTxt('You travel for many days before reaching the dungeon')
                        location = 'darkest dungeon'
                        bar()

                    if answer == 'travel east':
                        scrollTxt(
                            'You travel for many hours before reaching the open plains')
                        location = 'open plains spells'
                        bar()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'explore':
                        scrollTxt('You spend the whole day exploring...')
                        time.sleep(2)
                        i = random.randint(1, 3)
                        if i == 3:
                            scrollTxt('You found some mushrooms')
                            inv.append('mushroom')
                            inv.append('mushroom')
                        elif i == 2:
                            scrollTxt('You found some dead bodies')
                        else:
                            scrollTxt('You found nothing')
                        print()

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[19] = world
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()

            if location == 'arena':
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[19] = world
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                start = True
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Arena of White Bridge{Fore.WHITE}~')
                scrollTxt('You enter the arena...')
                enter()
                arena()
                scrollTxt('You leave the arena')

                commands = []
                addList(commands, ['travel north', 'travel west'])
                printList(commands, 'Commands: ')
                inputCommands(commands, "")

                if answer == 'travel north':
                    scrollTxt('You travel north for a day')
                    scrollTxt('The arena is far behind you when you reach the open plains')
                    bar()
                    location = 'open plains encounter'

                if answer == 'travel west':
                    scrollTxt('You travel west for a day')
                    scrollTxt('The arena is far behind you when you reach the open plains')
                    bar()
                    location = 'open plains spells'

            if location == 'forest':
                start = True
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[19] = world
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Forest{Fore.WHITE}~')
                scrollTxt('You are in the forest,'
                          ' to the north is the great mountians,'
                          ' to the south and west more grasslands,'
                          ' and to the east are is a mysterious temple')
                time.sleep(.5)
                print()
                scrollTxt(
                    'As you look more closly at the forest you can see the tree\'s bark and leave look darker than what\'s'
                    ' healthy. You also not the lack of animals')

                while location == 'forest':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Forest{Fore.WHITE}~')
                    else:
                        start = False
                    commands = []
                    addList(commands, [
                        'inventory', 'assess', 'settings', 'save', 'investigate',
                        'encounter', 'travel west', 'travel south', 'travel east'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'encounter':
                        scrollTxt('You search for monster or beasts to fight...')
                        time.sleep(1)
                        scrollTxt('You don\'t find anything')

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[19] = world
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()

                    if answer == 'travel west':
                        scrollTxt('You travel many days west')
                        scrollTxt('Eventually the trees thin out')
                        bar()
                        location = 'grassland shop'

                    if answer == 'travel south':
                        scrollTxt('You travel many days south')
                        scrollTxt('Eventually the trees thin out')
                        bar()
                        location = 'grassland'

                    if answer == 'travel east':
                        scrollTxt('You travel many days east')
                        scrollTxt('Eventually you reach the great temple')
                        bar()
                        location = 'mysterious temple'

                    if answer == 'investigate':
                        print()
                        scrollTxt('You decide to invenstigate...')
                        scrollTxt(
                            'You walk around the forest concluding that the trees nearest to the temple are the '
                            'most unhealty')
                        scrollTxt('Also there is complete no living things')

            if location == 'grassland':
                start = True
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[19] = world
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Grassland{Fore.WHITE}~')
                scrollTxt('You are in the grasslands,'
                          ' to the north, south, and east are forests,'
                          ' to the west are plains')

                while location == 'grassland':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Grassland{Fore.WHITE}~')
                    else:
                        start = False
                    commands = []
                    addList(commands, [
                        'encounter', 'rest', 'inventory', 'assess', 'settings', 'save',
                        'travel north', 'travel west'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'encounter':
                        scrollTxt('You search for monster or beasts to fight...')
                        time.sleep(1)
                        monster = random.choice(
                            ['muck monster', 'goblin', 'gnoll', 'bugbear'])
                        scrollTxt(f'Finally you see a {monster}')
                        enter()

                        if monster == 'muck monster':
                            battle('the muck monster', ['acid blast', 'poison jab', 'charge'],
                                   random.randint(7, 13), 2, 8, 1.5, 0, 20)

                        if monster == 'goblin':
                            battle('the goblin warrior',
                                   ['slash', 'stab', 'charge', 'punch', 'chant', 'poison jab'],
                                   random.randint(7, 12), 3, 8, 2, 20, 30)

                        if monster == 'gnoll':
                            battle('the gnoll', ['rest', 'stab', 'claw', 'chant'],
                                   random.randint(7, 11), 5, 4, 1.5, random.randint(1, 5), 30)

                        if monster == 'bugbear':
                            battle('the bugbear', [
                                'rest', 'stab', 'charge', 'chant', 'wild slash', 'claw', 'punch'
                            ], random.randint(7, 13), 3, 10, 1.5, random.randint(5, 15), 40)

                        if ran is True:
                            scrollTxt(f'You run from the {monster}')
                            scrollTxt(f'You escaped the {monster}')
                        else:
                            if lose is True:
                                scrollTxt('You died game over...')
                                scrollTxt(f'the {monster} killed you')
                                quit()
                            if lose is False:
                                scrollTxt(f'You stand victorious over the {monster}')
                        print()

                    if answer == 'travel north':
                        scrollTxt('You travel northward...')
                        scrollTxt('The grass turns into trees as you reach the forest.')
                        bar()
                        location = 'forest'

                    if answer == 'travel west':
                        scrollTxt('You travel westward...')
                        scrollTxt('The grass drys as you reach the open plains.')
                        bar()
                        location = 'open plains encounter'

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[19] = world
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()

            if location == 'open plains spells':
                start = True
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[19] = world
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Open Plains{Fore.WHITE}~')
                scrollTxt(
                    'You are in the open plains to the north a small village, to the east is a great arena, to the south great mountains,  and to the west are is a mysterious cave'
                )
                scrollTxt('Suddently a warlock appears in front of you')
                scrollTxt('They ask if you would like to learn \'LIGHTNING TOUCH\'')
                scrollTxt(f'It cost {Fore.YELLOW}30{Fore.WHITE}GP')
                commands = ['yes', 'no']
                printList(commands, '')
                inputCommands(commands, '')
                if answer == 'yes':
                    if gp > 20:
                        gp -= 20
                        scrollTxt(f'-{Fore.YELLOW}20{Fore.WHITE}GP')
                        scrollTxt('+LIGHTNING TOUCH spell')
                        lvl1_spells += 1
                        lvl1_available_spells.append('lightning touch')
                    else:
                        scrollTxt('You don\'t have enough money')
                print()
                commands = []

                scrollTxt('They ask if you would like to learn \'MAGE ARMOR\'')
                scrollTxt(f'It cost {Fore.YELLOW}20{Fore.WHITE}GP')
                commands = ['yes', 'no']
                printList(commands, '')
                inputCommands(commands, '')
                if answer == 'yes':
                    if gp > 20:
                        gp -= 20
                        scrollTxt(f'-{Fore.YELLOW}20{Fore.WHITE}GP')
                        scrollTxt('+MAGE ARMOR spell')
                        lvl2_spells += 1
                        lvl2_available_spells.append('mage armor')
                    else:
                        scrollTxt('You don\'t have enough money')
                print()
                commands = []

                scrollTxt('They then ask if you would like more spell slots')
                scrollTxt(f'It cost {Fore.YELLOW}20{Fore.WHITE}GP')
                commands = ['yes', 'no']
                inputCommands(commands, '')
                if answer == 'yes':
                    if gp > 20:
                        scrollTxt('+2 spell slots')
                        scrollTxt(f'-{Fore.YELLOW}20{Fore.WHITE} GP')
                        lvl1_spells += 1
                        lvl2_spells += 1
                        gp -= 20
                    else:
                        scrollTxt('You don\'t have enough money')

                while location == 'open plains spells':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Open Plains{Fore.WHITE}~')
                    else:
                        start = False

                    commands = []
                    addList(commands, [
                        'explore', 'inventory', 'assess', 'settings', 'save', 'travel east',
                        'travel west', 'travel north'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'explore':
                        scrollTxt('You spend the whole day exploring...')
                        time.sleep(2)
                        i = random.randint(1, 3)
                        if i == 3:
                            scrollTxt('You found some wheat')
                            inv.append('wheat')
                            inv.append('wheat')
                        elif i == 2:
                            scrollTxt('You found some grain')
                            inv.append('grain')
                            inv.append('grain')
                        else:
                            scrollTxt('You found nothing')
                        print()

                    if answer == 'travel north':
                        scrollTxt('You travel north many days...')
                        scrollTxt('You finally come upon a small village')
                        bar()
                        location = 'start village'

                    if answer == 'travel east':
                        scrollTxt('You travel east many days...')
                        scrollTxt('You finally come upon a great arena')
                        bar()
                        location = 'arena'

                    if answer == 'travel west':
                        scrollTxt('You travel west many days...')
                        scrollTxt('You finally come upon a mysterious cave')
                        bar()
                        location = 'mysterious cave'
                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[19] = world
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()
                        lvl2_spells += 1

            if location == 'mysterious temple':
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[19] = world
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                start = True
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Mysterious Temple{Fore.WHITE}~')
                scrollTxt('You can see a great temple looming over you...')
                scrollTxt('All around you are great mountains.')
                scrollTxt('Except to the west there are forest')

                while location == 'mysterious temple':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Mysterious Temple{Fore.WHITE}~')
                    else:
                        start = False

                    commands = []
                    addList(commands, [
                        'explore', 'inventory', 'assess', 'settings', 'save',
                        'go in the temple', 'travel west'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'go in the temple':
                        scrollTxt('You enter the temple...')
                        enter()
                        system('clear')
                        bar()
                        forestTemple()

                    if answer == 'travel west':
                        scrollTxt('You travel for many hours before reaching the forest')
                        location = 'forest'
                        bar()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'explore':
                        scrollTxt('You spend the whole day exploring...')
                        time.sleep(2)
                        i = random.randint(1, 3)
                        if i == 3:
                            scrollTxt('You found some mushrooms')
                            inv.append('mushroom')
                            inv.append('mushroom')
                        elif i == 2:
                            scrollTxt('You found some dead bodies')
                        else:
                            scrollTxt('You found nothing')
                        print()

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[19] = world
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()

            if location == 'halloween':
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                db.get(answer)[20] = candy
                db.get(answer)[19] = world
                start = True
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}HALLOWEEN LAND 🎃{Fore.WHITE}~')
                scrollTxt(
                    'You are halloween land!'
                )

                while location == 'halloween':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}HALLOWEEN LAND 🎃{Fore.WHITE}~')
                    else:
                        start = False

                    commands = []
                    addList(commands, [
                        'encounter', 'inventory', 'assess', 'settings', 'save',
                        'leave', 'candy', 'shop', 'boss'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'candy':
                        scrollTxt(f'Candy: {Fore.LIGHTMAGENTA_EX}{candy}{Fore.WHITE}')
                        print()
                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'encounter':
                        scrollTxt('You search for monster or beasts to fight...')
                        time.sleep(1)
                        monster = random.choice(
                            ['skeleton', 'King Jack', 'ghost', 'vampire'])
                        scrollTxt(f'Finally you see a {monster}')
                        enter()

                        if monster == 'skeleton':
                            battle('the skeleton', ['wild slash', 'claw', 'charge'],
                                   random.randint(5, 10), 6, 4, 1, 0, 20)

                            if ran is True:
                                scrollTxt('You run from the skeleton')
                                scrollTxt(f'You escaped the skeleton')
                            else:
                                if lose is True:
                                    scrollTxt('You died game over...')
                                    scrollTxt(f'the skeleton killed you')
                                    quit()
                                if lose is False:
                                    scrollTxt(f'You stand victorious over the skeleton')
                                    scrollTxt(f'+{Fore.LIGHTMAGENTA_EX}1{Fore.WHITE} candy')
                                    candy += 1
                                    print()

                        if monster == 'King Jack':
                            battle('King Jack', ['slash', 'stab', 'charge', 'punch'],
                                   random.randint(10, 13), 3, 8, 2, 10, 20)

                            if ran is True:
                                scrollTxt('You run from King Jack')
                                scrollTxt(f'You escaped King Jack')
                            else:
                                if lose is True:
                                    scrollTxt('You died game over...')
                                    scrollTxt(f'King Jack killed you')
                                    quit()
                                if lose is False:
                                    scrollTxt(f'You stand victorious over King Jack')
                                    scrollTxt(f'+{Fore.LIGHTMAGENTA_EX}2{Fore.WHITE} candy')
                                    candy += 2
                                    print()

                        if monster == 'ghost':
                            battle('the ghost',
                                   ['rest', 'acid blast', 'charge', 'chant'],
                                   random.randint(4, 7), 7, 3, 1.5, 0, 20)

                            if ran is True:
                                scrollTxt('You run from the the ghost')
                                scrollTxt(f'You escaped the ghost')
                            else:
                                if lose is True:
                                    scrollTxt('You died game over...')
                                    scrollTxt(f'the ghost killed you')
                                    quit()
                                if lose is False:
                                    scrollTxt(f'You stand victorious over the ghost')
                                    scrollTxt(f'+{Fore.LIGHTMAGENTA_EX}1{Fore.WHITE} candy')
                                    candy += 1
                                    print()

                        if monster == 'vampire':
                            battle('the vampire', [
                                'rest', 'stab', 'charge', 'chant', 'wild slash', 'claw', 'punch'
                            ], random.randint(7, 13), 3, 10, 1.5, random.randint(5, 15), 40)

                            if ran is True:
                                scrollTxt('You run from the vampire')
                                scrollTxt(f'You escaped the vampire')
                            else:
                                if lose is True:
                                    scrollTxt('You died game over...')
                                    scrollTxt(f'the vampire killed you')
                                    quit()
                                if lose is False:
                                    scrollTxt(f'You stand victorious over the vampire')
                                    scrollTxt(f'+{Fore.LIGHTMAGENTA_EX}1{Fore.WHITE} candy')
                                    candy += 1
                                    print()

                        print()

                    if answer == 'leave':
                        bar()
                        scrollTxt('You leave halloween land...')
                        bar()
                        location = 'start village'

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[20] = candy
                        db.get(answer)[17] = lvl
                        print()

                    if answer == 'shop':
                        scrollTxt('You walk over to the shop')
                        scrollTxt(
                            '\'Would you like to look at my wares?\' asks the merchant')

                        wares = ['nothing']
                        cost = []

                        lvl3_wares = ['HALLOW SWORD', 'HALLOW SHIELD', 'Hallow Soldier']
                        lvl3_cost = [20, 15, 50]

                        lvl2_wares = ['King Jack\'s Blade', 'Ghost Shield', 'Skeleton-bone spear']
                        lvl2_cost = [11, 9, 10]

                        lvl1_wares = ['Golden snikers', "Gourmet choloate", "Blessed hi-chew"]
                        lvl1_cost = [3, 2, 2]

                        addList(wares, lvl1_wares)
                        addList(wares, lvl2_wares)
                        addList(wares, lvl3_wares)

                        addList(cost, lvl1_cost)
                        addList(cost, lvl2_cost)
                        addList(cost, lvl3_cost)

                        commands = []
                        addList(commands, ['y', 'n'])
                        printList(commands, 'Commands: ')
                        inputCommands(commands, "")
                        commands = []

                        if answer == 'y':
                            bar()
                            scrollTxt("~WARES~")
                            addList(commands, lvl1_wares)
                            commands = new_commands
                            printShopH(commands, lvl1_cost, "Tier 1 Wares - ")
                            commands = []
                            print()

                            addList(commands, lvl2_wares)
                            commands = new_commands
                            printShopH(commands, lvl2_cost, "Tier 2 Wares - ")
                            commands = []
                            print()

                            addList(commands, lvl3_wares)
                            commands = new_commands
                            printShopH(commands, lvl3_cost, "Tier 3 Wares - ")
                            commands = []
                            print()

                            scrollTxt("What would you like to buy (type nothing to exit)")
                            addList(commands, wares)
                            commands = new_commands
                            inputShopH(wares, "", cost)
                            items = len(inv)
                            wares = new_wares
                            gp = gp
                            commands = []

                            if nothing is True:
                                done = True
                            else:
                                done = False
                            while done is False:
                                scrollTxt("Is that all?")
                                commands.append("yes")
                                commands.append("no")
                                printList(commands, "Commands: ")
                                inputCommands(commands, "")
                                commands = []
                                print()

                                if answer == 'no':
                                    scrollTxt("What would you like to buy (type nothing to exit)")
                                    addList(commands, wares)
                                    commands = new_commands
                                    inputShopH(wares, "", cost)
                                    items = len(inv)
                                    wares = new_wares
                                    gp = gp
                                    commands = []
                                else:
                                    done = True

                    if answer == 'boss':
                        scrollTxt('You summon the HALLOW KING')
                        enter()
                        battle('the HALLOW KING', ['slash', 'stab', 'charge', 'punch', 'acid blast', 'reaping blow'],
                               random.randint(25, 30) * lvl, 3 * lvl, 8, 2 * (lvl / 2), 10 * lvl, 40 * lvl)
                        if ran is True:
                            scrollTxt('You run from the THE HALLOW KING')
                            scrollTxt(f'They obliterate you...')
                            quit()
                        else:
                            if lose is True:
                                scrollTxt('You died game over...')
                                scrollTxt(f'THE HALLOW KING killed you')
                                quit()
                            if lose is False:
                                scrollTxt(f'You stand victorious over THE HALLOW KING')
                                scrollTxt(f'+{Fore.LIGHTMAGENTA_EX}{10 + lvl}{Fore.WHITE} candy')
                                candy += 10 + lvl
                                print()

            if location == 'darkest dungeon':
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[19] = world
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                start = True
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Darkest Dungeon{Fore.WHITE}~')
                enter()
                darkestDungeon()

                while location == 'darkest dungeon':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Out of Dungeon{Fore.WHITE}~')
                    else:
                        start = False

                    scrollTxt('In front of you lies a great flaming portal')

                    commands = []
                    addList(commands, [
                        'travel north', 'portal'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'travel north':
                        scrollTxt('You travel for many hours before reaching a cave')
                        location = 'mysterious cave'
                        bar()

                    if answer == 'portal':
                        scrollTxt('You enter the portal')
                        scrollTxt('Heat rushes over you as your a transported to another world')
                        enter()

                        system('clear')
                        scrollTxt(f'Welcome to the burning world of {Fore.LIGHTBLUE_EX}INFERNO{Fore.WHITE}')
                        world = 'inferno'
                        location = 'start city'

        while world == 'inferno':

            if location == 'start city':
                # START VILLAGE
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                db.get(answer)[19] = world
                start_village = f"{Fore.LIGHTBLUE_EX}Veras{Fore.WHITE}"

                village_activites = [
                    'tavern', 'merchants', 'fight', 'inventory', 'assess', 'settings',
                    'save', 'leave north', 'leave east', 'leave south', 'leave world'
                ]

                print(f'~{start_village}~')
                scrollTxt(f'You wake up in the inferno city of {start_village}')
                scrollTxt('The shouts of Magmanites and the scents of smoke reaches you')
                startvill = False

                village_done = False

                while village_done is False:
                    if startvill == True:
                        print(f'~{start_village}~')
                    else:
                        startvill = True

                    commands = []
                    addList(commands, village_activites)
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    bar()

                    if answer == 'tavern':
                        inn_done = False

                        print(f'~{Fore.LIGHTBLUE_EX}Tavern{Fore.WHITE}~')
                        scrollTxt('You reach the arena after a short walk')
                        scrollTxt(
                            'The sound of swords clashing fills your ears and the aroma of blood permeates'
                        )

                        while inn_done is False:

                            inn_activites = [
                                'fight', 'converse', 'gamble', 'leave', 'merchant'
                            ]

                            print()

                            commands = []
                            addList(commands, inn_activites)
                            printList(commands, 'Commands: ')
                            commands.append('sing')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'merchant':
                                scrollTxt('You walk over to the merchant')
                                scrollTxt(
                                    '\'Would you like to look at my wares?\' asks the merchant')

                                wares = ['nothing']
                                cost = []

                                lvl3_wares = ['Legend magma cream', 'Titan rock', 'Everfire apple']
                                lvl3_cost = [100, 80, 120]

                                lvl2_wares = ['Golden Flamepapya', 'Magic Inferno cracker', 'Blessed rock']
                                lvl2_cost = [45, 35, 30]

                                lvl1_wares = ['Hardy magma rock', "Elven Flameapple", "Dwarven Firepotato"]
                                lvl1_cost = [10, 12, 13]

                                addList(wares, lvl1_wares)
                                addList(wares, lvl2_wares)
                                addList(wares, lvl3_wares)

                                addList(cost, lvl1_cost)
                                addList(cost, lvl2_cost)
                                addList(cost, lvl3_cost)

                                commands = []
                                addList(commands, ['y', 'n'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'y':
                                    bar()
                                    scrollTxt("~WARES~")
                                    addList(commands, lvl1_wares)
                                    commands = new_commands
                                    printShop(commands, lvl1_cost, "Tier 2 Wares - ")
                                    commands = []
                                    print()

                                    addList(commands, lvl2_wares)
                                    commands = new_commands
                                    printShop(commands, lvl2_cost, "Tier 3 Wares - ")
                                    commands = []
                                    print()

                                    addList(commands, lvl3_wares)
                                    commands = new_commands
                                    printShop(commands, lvl3_cost, "Tier 4 Wares - ")
                                    commands = []
                                    print()

                                    scrollTxt("What would you like to buy (type nothing to exit)")
                                    addList(commands, wares)
                                    commands = new_commands
                                    inputShop(wares, "", cost)
                                    items = len(inv)
                                    wares = new_wares
                                    gp = gp
                                    commands = []

                                    if nothing is True:
                                        done = True
                                    else:
                                        done = False
                                    while done is False:
                                        scrollTxt("Is that all?")
                                        commands.append("yes")
                                        commands.append("no")
                                        printList(commands, "Commands: ")
                                        inputCommands(commands, "")
                                        commands = []
                                        print()

                                        if answer == 'no':
                                            scrollTxt(
                                                "What would you like to buy (type nothing to exit)")
                                            addList(commands, wares)
                                            commands = new_commands
                                            inputShop(wares, "", cost)
                                            items = len(inv)
                                            wares = new_wares
                                            gp = gp
                                            commands = []
                                        else:
                                            done = True

                            if answer == 'fight':
                                scrollTxt('You walk up to the ring')
                                scrollTxt('As you draw closer, you can hear punches and bones breaking')
                                scrollTxt(
                                    'Would you like to play?')

                                commands = []
                                addList(commands, ['yes', 'no'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'yes':
                                    scrollTxt('You hop in the ring')
                                    scrollTxt('The lead fighter smiles and cracks their knuckles')
                                    scrollTxt(f'-{Fore.YELLOW}{weapons}{Fore.WHITE} GP')
                                    scrollTxt('Select a difficulty (1 = lvl 1)')
                                    difficulty = 'none'
                                    while difficulty == 'none':
                                        difficulty = input(f'{Fore.GREEN}')
                                        sys.stdout.write(f'{Fore.WHITE}')
                                        print()
                                        if not difficulty.isdigit():
                                            difficulty = 'none'
                                            scrollTxt('That\'s not a number')
                                        else:
                                            difficulty = int(difficulty)
                                    pre_weapon = weapons
                                    weapons = 'fists'
                                    enter()

                                    battle('lead fighter', ['punch', 'charge', 'smash'],
                                           random.randint(difficulty * 10, difficulty * 20), difficulty, difficulty * 3,
                                           difficulty, difficulty * 50, difficulty * 10)

                                    if ran is True:
                                        scrollTxt('You tried to run away')
                                        scrollTxt('There\'s no escape from the ring')
                                        quit()
                                    else:
                                        if lose is True:
                                            scrollTxt('You died a to the lead fighter')
                                            quit()
                                        if lose is False:
                                            scrollTxt('You stand in victory over the lead fighter')

                                if answer == 'no':
                                    scrollTxt('You leave the ring')
                                bar()

                            if answer == 'converse':
                                scrollTxt(
                                    'You walk up to decide to try to talk to people...'
                                )
                                scrollTxt('Choose a group to talk to')
                                commands = ['1', '2', '3']
                                if adventures == False:
                                    commands.remove('1')
                                if workers == False:
                                    commands.remove('2')
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == '1':
                                    print()
                                    adventures = False
                                    scrollTxt('You walk up to a group of friendly looking adventures...')
                                    scrollTxt('They welcome you as you draw closer')
                                    scrollTxt(
                                        'They are talking about a myth that says there is paradise behind a huge mountain')
                                    scrollTxt('\'What do you think about the myth?\', inquires the lead adventure')
                                    answer = input(f'{Fore.GREEN}')
                                    print(f'{Fore.WHITE}')

                                    scrollTxt('The look at you with distain and leave...')
                                    bar()

                                if answer == '2':
                                    print()
                                    workers = False
                                    scrollTxt('You decide to try your luck with a group of sturdy magmanites')
                                    scrollTxt('The look suspicously at you as you approach them')
                                    scrollTxt('After one of them snorts the resume talking about how there jobs suck')
                                    scrollTxt('Eventually one of them ask what your problem is...')
                                    input(f'{Fore.GREEN}')
                                    print(f'{Fore.WHITE}')

                                    scrollTxt('The growl and tell you to get lost')
                                    commands = ['leave', 'stay']
                                    printList(commands, 'Commands: ')
                                    inputCommands(commands, '')
                                    commands = []

                                    if answer == 'leave':
                                        scrollTxt('You leave...')
                                        bar()
                                    if answer == 'stay':
                                        scrollTxt('You stand your ground...')
                                        scrollTxt('One of the magmanites grunts and charges at you')
                                        enter()

                                        battle('the magmanite', ['punch', 'charge', 'smash', 'chant'],
                                               random.randint(40, 60), 3, 10, 2, 40, 70)

                                        if ran is True:
                                            scrollTxt('You run from the magmanite')
                                            scrollTxt('You escape')

                                        else:
                                            if lose is True:
                                                scrollTxt('You died a to the magmanite')
                                                quit()
                                            if lose is False:
                                                scrollTxt('You stand in victory over the magmanite')

                                        bar()

                                if answer == '3':
                                    scrollTxt('You decide to talk a crazy old human...')

                                    if race == 'elf':
                                        scrollTxt('As you approach them they scream with delight')
                                        scrollTxt('\'A elf, and elf!\', cries the human')
                                        scrollTxt('After that there words become gibberish')
                                    if race == 'dwarf':
                                        scrollTxt('As you walk up to them the look at you, then walk away')
                                    if race == 'halfling':
                                        scrollTxt('As you approach the old human they scream, \'Shorty!, Shorty!\'')
                                        scrollTxt('You sigh and leave')
                                    if race == 'human':
                                        scrollTxt(
                                            'You walk up the them and they wisper in your ear that, \'MOUNTAIN BEAST BEWARE\'')
                                        scrollTxt('After that there words become gibberish')

                                    bar()
                            if answer == 'gamble':
                                scrollTxt("You look around searching for a gambling table")
                                scrollTxt(
                                    'After finding one you sit your self down and ask to join in')
                                scrollTxt('The dealer nods and ask what you would like to play')
                                commands = ['black dragon', 'dice & cards', 'dice & towers']
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'black dragon':
                                    black_dragon('dealer')
                                    gp = gp

                                if answer == 'dice & cards':
                                    dice_and_cards('dealer')
                                    gp = gp

                                if answer == 'dice & towers':
                                    dice_towers('dealer')
                                    gp = gp

                                print()

                            if answer == 'leave':
                                scrollTxt('You leave the tavern')
                                inn_done = True
                                print()

                    if answer == 'merchants':
                        merchant_done = False

                        print(f'~{Fore.LIGHTBLUE_EX}Merchants{Fore.WHITE}~')
                        scrollTxt('You walk over to the many vendors south of the gate')
                        scrollTxt(
                            'The vendor to the left is a stout magmanite who appears to be selling weapons\n'
                            'To the right is a sly halfling selling an assortment of metal'
                        )

                        while merchant_done is False:

                            commands = []
                            addList(commands, ['left', 'right', 'leave'])
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            print()

                            if answer == 'left':
                                scrollTxt(
                                    f"\"Welcome to {Fore.LIGHTBLUE_EX}Dranfire\'s Family Forge'{Fore.WHITE}\", booms the magmanite"
                                )
                                scrollTxt("\"Would you like to look at my wares?\", they ask")

                                wares = ['nothing']
                                cost = []

                                lvl3_wares = ['Everfire Blade', 'legend shield', 'cursed orb']
                                lvl3_cost = [1000, 500, 750]

                                lvl2_wares = ['Flame Blade', 'sniper', 'flame shield']
                                lvl2_cost = [300, 120, 90]

                                lvl1_wares = ['steel sword', "magma shield"]
                                lvl1_cost = [70, 50]

                                addList(wares, lvl1_wares)
                                addList(wares, lvl2_wares)
                                addList(wares, lvl3_wares)

                                addList(cost, lvl1_cost)
                                addList(cost, lvl2_cost)
                                addList(cost, lvl3_cost)

                                commands = []
                                addList(commands, ['y', 'n'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'y':
                                    bar()
                                    scrollTxt("~WARES~")
                                    addList(commands, lvl1_wares)
                                    commands = new_commands
                                    printShop(commands, lvl1_cost, "Tier 2 Wares - ")
                                    commands = []
                                    print()

                                    addList(commands, lvl2_wares)
                                    commands = new_commands
                                    printShop(commands, lvl2_cost, "Tier 3 Wares - ")
                                    commands = []
                                    print()

                                    addList(commands, lvl3_wares)
                                    commands = new_commands
                                    printShop(commands, lvl3_cost, "Tier 4 Wares - ")
                                    commands = []
                                    print()

                                    scrollTxt("What would you like to buy (type nothing to exit)")
                                    addList(commands, wares)
                                    commands = new_commands
                                    inputShop(wares, "", cost)
                                    items = len(inv)
                                    wares = new_wares
                                    gp = gp
                                    commands = []

                                    if nothing is True:
                                        done = True
                                    else:
                                        done = False
                                    while done == False:
                                        scrollTxt("Is that all?")
                                        commands.append("yes")
                                        commands.append("no")
                                        printList(commands, "Commands: ")
                                        inputCommands(commands, "")
                                        commands = []
                                        print()

                                        if answer == 'no':
                                            scrollTxt(
                                                "What would you like to buy (type nothing to exit)")
                                            addList(commands, wares)
                                            commands = new_commands
                                            inputShop(wares, "", cost)
                                            items = len(inv)
                                            wares = new_wares
                                            gp = gp
                                            commands = []
                                        else:
                                            done = True
                                print()

                            if answer == 'right':
                                scrollTxt('You walk over to the hafling')
                                scrollTxt(
                                    '\'Would you like to look at my wares?\' asks the kenu')

                                wares = ['nothing']
                                cost = []

                                lvl3_wares = [
                                    'LEGEND MEDALLION OF COURAGE'
                                ]
                                lvl3_cost = [5000]

                                lvl2_wares = [
                                    'TITAN MEDALLION OF POWER'
                                ]
                                lvl2_cost = [2000]

                                lvl1_wares = ['GOLDEN MEDALLION OF WISDOM']
                                lvl1_cost = [1000]

                                addList(wares, lvl1_wares)
                                addList(wares, lvl2_wares)
                                addList(wares, lvl3_wares)

                                addList(cost, lvl1_cost)
                                addList(cost, lvl2_cost)
                                addList(cost, lvl3_cost)

                                commands = []
                                addList(commands, ['y', 'n'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'y':
                                    bar()
                                    scrollTxt("~WARES~")
                                    addList(commands, lvl1_wares)
                                    commands = new_commands
                                    printShop(commands, lvl1_cost, "Tier 1 Wares - ")
                                    commands = []
                                    print()

                                    addList(commands, lvl2_wares)
                                    commands = new_commands
                                    printShop(commands, lvl2_cost, "Tier 2 Wares - ")
                                    commands = []
                                    print()

                                    addList(commands, lvl3_wares)
                                    commands = new_commands
                                    printShop(commands, lvl3_cost, "Tier 3 Wares - ")
                                    commands = []
                                    print()

                                    scrollTxt("What would you like to buy (type nothing to exit)")
                                    addList(commands, wares)
                                    commands = new_commands
                                    inputShop(wares, "", cost)
                                    items = len(inv)
                                    wares = new_wares
                                    gp = gp
                                    commands = []

                                    if nothing is True:
                                        done = True
                                    else:
                                        done = False
                                    while done == False:
                                        scrollTxt("Is that all?")
                                        commands.append("yes")
                                        commands.append("no")
                                        printList(commands, "Commands: ")
                                        inputCommands(commands, "")
                                        commands = []
                                        print()

                                        if answer == 'no':
                                            scrollTxt(
                                                "What would you like to buy (type nothing to exit)")
                                            addList(commands, wares)
                                            commands = new_commands
                                            inputShop(wares, "", cost)
                                            items = len(inv)
                                            wares = new_wares
                                            gp = gp
                                            commands = []
                                        else:
                                            done = True
                                print()

                            if answer == 'leave':
                                scrollTxt('You leave the merchants')
                                merchant_done = True
                                print()

                    if answer == 'fight':
                        print(f'~{Fore.LIGHTBLUE_EX}City Square{Fore.WHITE}~')
                        scrollTxt(
                            'You walk over to the many people bustling around the city square'
                        )
                        scrollTxt('You come just in time to see a burly magmanite beating up a human warrior')
                        scrollTxt('After the human dies the burly magmanite challenges anyone to a fight...')
                        scrollTxt(f'They offer {Fore.YELLOW}500{Fore.WHITE} gp if someone can beat them')

                        commands = ['fight', 'leave']
                        printList(commands, 'Commands: ')
                        inputCommands(commands, '')

                        if answer == 'fight':
                            scrollTxt('You execpt their challenge...')
                            enter()

                            battle('the titan magmanite',
                                   ['punch', 'charge', 'smash', 'chant', 'slash', 'wild slash', 'uppercut'],
                                   random.randint(200, 300), 7, 13, 3 + (lvl / 2), 100, 250)

                            if ran is True:
                                scrollTxt('You run from the magmanite')
                                scrollTxt('You escape')

                            else:
                                if lose is True:
                                    scrollTxt('You died a to the magmanite')
                                    quit()
                                if lose is False:
                                    scrollTxt('You stand in victory over the magmanite')
                                    scrollTxt(f'+{Fore.YELLOW}500{Fore.WHITE} GP')
                                    gp += 500

                            bar()

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        db.get(answer)[19] = world
                        print()

                    if answer == 'leave north':
                        scrollTxt('You leave the city heading north...')
                        location = 'outlands encounter'
                        village_done = True
                        print()

                    if answer == 'leave south':
                        scrollTxt('You leave the city heading south...')
                        location = 'desert'
                        village_done = True
                        print()

                    if answer == 'leave east':
                        scrollTxt('You leave the city heading east...')
                        location = 'outlands spells'
                        village_done = True
                        print()

                    if answer == 'leave world':
                        scrollTxt('You leave inferno through the portal...')
                        location = 'mystious cave'
                        village_done = True
                        world = 'start'

            if location == 'outlands encounter':
                start = True
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[19] = world
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Outlands{Fore.WHITE}~')
                scrollTxt('You are in the outlands,'
                          ' all around you is great mountains, '
                          'except to the south which is a large city')
                time.sleep(.5)
                scrollTxt('As you gaze at your new suroundings you see a bundled up human approaching you...')
                scrollTxt('Upon closer examination you find they are a bandit!')
                enter()
                battle('the bandit', [
                    'rest', 'stab', 'charge', 'slash', 'wild slash', 'punch',
                    'smash'
                ], random.randint(10, 15), 6, 8, 2, random.randint(10, 20), 55)
                monster = 'the bandit'
                if ran is True:
                    scrollTxt(f'You run from {monster}')
                    scrollTxt(f'You escaped {monster}')
                else:
                    if lose is True:
                        scrollTxt('You died game over...')
                        scrollTxt(f'{monster} killed you')
                        quit()
                    if lose is False:
                        scrollTxt(f'You stand victorious over {monster}')
                        scrollTxt('After a quick examination you find a dagger')
                        scrollTxt('+dagger')
                        inv.append('dagger')

                print()

                while location == 'outlands encounter':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Outlands{Fore.WHITE}~')
                    else:
                        start = False
                    commands = []
                    addList(commands, [
                        'encounter', 'inventory', 'assess', 'settings', 'save',
                        'travel south'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'encounter':
                        scrollTxt('You search for monster or beasts to fight...')
                        time.sleep(1)
                        monster = random.choice(
                            ['bandit', 'goblin', 'bandit lord', 'sand monster'])
                        scrollTxt(f'Finally you see a {monster}')
                        enter()

                        if monster == 'bandit':
                            battle('the bandit', [
                                'rest', 'stab', 'charge', 'slash', 'wild slash', 'punch',
                                'smash'
                            ], random.randint(10, 15), 6, 8, 1.5, random.randint(10, 20), 55)

                        if monster == 'goblin':
                            battle('the goblin', ['slash', 'stab', 'charge', 'punch'],
                                   random.randint(5, 10), 3, 8, 1.5, 10, 20)

                        if monster == 'bandit lord':
                            battle('the bandit lord', [
                                'rest', 'stab', 'charge', 'slash', 'wild slash', 'punch',
                                'smash', 'chant', 'uppercut'
                            ], random.randint(10, 15), 7, 10, 3, random.randint(50, 100), 105)

                        if monster == 'sand monster':
                            battle('the sand monster', [
                                'charge', 'uppercut', 'smash', 'chant', 'wild slash', 'acid blast', 'punch'
                            ], random.randint(10, 20), 1, 10, 2, random.randint(0, 0), 50)

                        if ran is True:
                            scrollTxt(f'You run from the {monster}')
                            scrollTxt(f'You escaped the {monster}')
                        else:
                            if lose is True:
                                scrollTxt('You died game over...')
                                scrollTxt(f'the {monster} killed you')
                                quit()
                            if lose is False:
                                scrollTxt(f'You stand victorious over the {monster}')
                        print()

                    if answer == 'rest':
                        scrollTxt('You rest for 4 hours')
                        time.sleep(2)
                        scrollTxt(f'You healed {Fore.RED}1{Fore.WHITE} health')
                        hp += 1
                        print()

                    if answer == 'travel south':
                        bar()
                        scrollTxt('You travel for 6 hours before reaching a great city')
                        scrollTxt('You are now in the city')
                        location = 'start city'

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[19] = world
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()

            if location == 'outlands spells':
                start = True
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[19] = world
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Outlands{Fore.WHITE}~')
                scrollTxt(
                    'You are in the outlands to the north and east are great mountains, '
                    'to the west is a large city and to the south rocky ruins'
                )
                scrollTxt('As you survey the area you see an old bundled up human')
                scrollTxt(
                    f'When you approach the they say they are called {Fore.LIGHTBLUE_EX}\'Jessie the red handed\'{Fore.WHITE}')
                scrollTxt(
                    f'\'I\'ve been the leader of the {Fore.BLUE}sand claws{Fore.WHITE} (bandit group) for 50 years'
                    f'\', Jessie explains')
                scrollTxt('They then ask if you would like to learn \'AERIAL SLASH\'')
                scrollTxt(f'It cost {Fore.YELLOW}70{Fore.WHITE}GP')
                commands = ['yes', 'no']
                printList(commands, '')
                inputCommands(commands, '')
                if answer == 'yes':
                    if gp > 70:
                        gp -= 70
                        scrollTxt(f'-{Fore.YELLOW}70{Fore.WHITE}GP')
                        scrollTxt('+AERIAL SLASH spell')
                        lvl2_spells += 1
                        lvl2_available_spells.append('aerial slash')
                    else:
                        scrollTxt('You don\'t have enough money')
                print()
                commands = []

                while location == 'outlands spells':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Outlands{Fore.WHITE}~')
                    else:
                        start = False

                    commands = []
                    addList(commands, [
                        'explore', 'inventory', 'assess', 'settings', 'save',
                        'travel west', 'encounter'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'explore':
                        scrollTxt('You spend the whole day exploring...')
                        time.sleep(2)
                        i = random.randint(1, 3)
                        if i == 3:
                            scrollTxt('You found some rocks')
                            inv.append('rocks')
                            inv.append('rocks')
                        elif i == 2:
                            scrollTxt('You found some grain')
                            inv.append('grain')
                            inv.append('grain')
                        else:
                            scrollTxt('You found nothing')
                        print()

                    if answer == 'encounter':
                        scrollTxt('You search for monster or beasts to fight...')
                        time.sleep(1)
                        monster = random.choice(
                            ['bandit', 'magma giga rock (animate)', 'bandit lord', 'Sun cultist'])
                        scrollTxt(f'Finally you see a {monster}')
                        enter()

                        if monster == 'bandit':
                            battle('the bandit', [
                                'rest', 'stab', 'charge', 'slash', 'wild slash', 'punch',
                                'smash'
                            ], random.randint(10, 15), 6, 8, 1.5, random.randint(10, 20), 55)

                        if monster == 'magma giga rock (animate)':
                            battle('the magma giga rock', ['smash', 'fire blast', 'charge', 'punch', 'rest'],
                                   random.randint(100, 150), -1, 12, 3, 100, 200)

                        if monster == 'bandit lord':
                            battle('the bandit lord', [
                                'rest', 'stab', 'charge', 'slash', 'wild slash', 'punch',
                                'smash', 'chant', 'uppercut'
                            ], random.randint(10, 15), 7, 10, 3, random.randint(50, 100), 105)

                        if monster == 'Sun cultist':
                            battle('the Sun cultist', [
                                'charge', 'reaping blow', 'chant', 'wild slash', 'dodge'
                            ], random.randint(7, 10), 10, 3, 2, random.randint(100, 200), 100)

                        if ran is True:
                            scrollTxt(f'You run from the {monster}')
                            scrollTxt(f'You escaped the {monster}')
                        else:
                            if lose is True:
                                scrollTxt('You died game over...')
                                scrollTxt(f'the {monster} killed you')
                                quit()
                            if lose is False:
                                scrollTxt(f'You stand victorious over the {monster}')
                        print()

                    if answer == 'travel west':
                        scrollTxt('You travel north many days...')
                        scrollTxt('You finally come upon a great city')
                        bar()
                        location = 'start city'

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[19] = world
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()
                        lvl2_spells += 1

            if location == 'desert':
                start = True
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[19] = world
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Desert{Fore.WHITE}~')
                scrollTxt('You are in the desert,'
                          ' to the north is a great city, to the south are large mountains, and to the west a desert temple.'
                          ' Also to the east is rocky ruins')

                while location == 'desert':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Desert{Fore.WHITE}~')
                    else:
                        start = False
                    commands = []
                    addList(commands, [
                        'encounter', 'rest', 'inventory', 'assess', 'settings', 'save',
                        'travel north', 'summon boss', 'travel west'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'encounter':
                        scrollTxt('You search for monster or beasts to fight...')
                        time.sleep(1)
                        monster = random.choice(
                            ['sun snake', 'sand rock monster', 'bandit lord', 'Sun cultist'])
                        scrollTxt(f'Finally you see a {monster}')
                        enter()

                        if monster == 'sun snake':
                            battle('the sun snake', [
                                'rest', 'stab', 'charge', 'fangs', 'fire blast', 'poison jab',
                                'acid blast'
                            ], random.randint(7, 15), 6, 5, 2, random.randint(0, 0), 55)

                        if monster == 'sand rock monster':
                            battle('the sand rock monster', ['smash', 'acid blast', 'charge', 'punch', 'rest'],
                                   random.randint(100, 150), 3, 8, 3, 100, 200)

                        if monster == 'bandit lord':
                            battle('the bandit lord', [
                                'rest', 'stab', 'charge', 'slash', 'wild slash', 'punch',
                                'smash', 'chant', 'uppercut'
                            ], random.randint(10, 15), 7, 10, 3, random.randint(50, 100), 105)

                        if monster == 'Sun cultist':
                            battle('the Sun cultist', [
                                'charge', 'reaping blow', 'chant', 'wild slash', 'dodge'
                            ], random.randint(7, 10), 10, 3, 2, random.randint(100, 200), 100)

                        if ran is True:
                            scrollTxt(f'You run from the {monster}')
                            scrollTxt(f'You escaped the {monster}')
                        else:
                            if lose is True:
                                scrollTxt('You died game over...')
                                scrollTxt(f'the {monster} killed you')
                                quit()
                            if lose is False:
                                scrollTxt(f'You stand victorious over the {monster}')
                        print()

                    if answer == 'travel north':
                        scrollTxt('You travel northward...')
                        scrollTxt('The you reach a great city')
                        bar()
                        location = 'start city'

                    if answer == 'travel west':
                        scrollTxt('You travel westward...')
                        scrollTxt('Then you reach a desert temple')
                        bar()
                        location = 'desert temple'

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[19] = world
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()

                    if answer == 'summon boss':
                        scrollTxt('You summon the DESERT SOULKING')
                        enter()
                        battle('the DESERT SOULKING',
                               ['slash', 'stab', 'charge', 'punch', 'acid blast', 'reaping blow'],
                               random.randint(200, 300), 7, 10, 5, 100, 400)
                        if ran is True:
                            scrollTxt('You run from the THE DESERT SOULKING')
                            scrollTxt(f'They obliterate you...')
                            quit()
                        else:
                            if lose is True:
                                scrollTxt('You died game over...')
                                scrollTxt(f'THE DESERT SOULKING killed you')
                                quit()
                            if lose is False:
                                scrollTxt(f'You stand victorious over THE DESERT SOULKING')
                                print()

            if location == 'abandoned village':
                start = True
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[19] = world
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Village Ruins{Fore.WHITE}~')
                scrollTxt('You are what seems to be an abandoned village,'
                          ' to the north and east are outlands, and to the west a desert.'
                          ' Also to the south, great mountains')

                while location == 'abandoned village':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Village Ruins{Fore.WHITE}~')
                    else:
                        start = False
                    commands = []
                    addList(commands, [
                        'encounter', 'rest', 'inventory', 'assess', 'settings', 'save',
                        'travel north', 'investigate'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'encounter':
                        scrollTxt('You search for monster or beasts to fight...')
                        time.sleep(1)
                        monster = random.choice(
                            ['zombie (villager)', 'zombie (warrior)', 'zombie (lord)', 'Iron Golem'])
                        scrollTxt(f'Finally you see a {monster}')
                        enter()

                        if monster == 'zombie (villager)':
                            battle('the zombie (villager)', [
                                'rest', 'stab', 'charge', 'fangs', 'claw', 'poison jab',
                                'wild slash'
                            ], random.randint(10, 15), 6, 5, 2, random.randint(50, 100), 55)

                        if monster == 'zombie (warrior)':
                            battle('the zombie (warrior)', [
                                'rest', 'stab', 'charge', 'uppercut', 'slash', 'poison jab',
                                'wild slash', 'acid blast'
                            ], random.randint(15, 20), 6, 8, 3, random.randint(50, 100), 75)

                        if monster == 'zombie (lord)':
                            battle('the zombie (villager)', [
                                'rest', 'stab', 'charge', 'slash', 'fire blast', 'poison jab',
                                'wild slash', 'dodge'
                            ], random.randint(10, 15), 10, 10, 2, random.randint(100, 150), 75)

                        if monster == 'Iron Golem':
                            battle('the Iron Golem', ['smash', 'acid blast', 'charge', 'punch', 'rest'],
                                   random.randint(100, 150), -1, 12, 3.5, 200, 250)

                        if ran is True:
                            scrollTxt(f'You run from the {monster}')
                            scrollTxt(f'You escaped the {monster}')
                        else:
                            if lose is True:
                                scrollTxt('You died game over...')
                                scrollTxt(f'the {monster} killed you')
                                quit()
                            if lose is False:
                                scrollTxt(f'You stand victorious over the {monster}')
                        print()

                    if answer == 'travel west':
                        scrollTxt('You travel east...')
                        scrollTxt('You reach the desert')
                        bar()
                        location = 'desert'

                    if answer == 'travel north':
                        scrollTxt('You travel north...')
                        scrollTxt('You reach the outlands')
                        bar()
                        location = 'outlands spells'

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[19] = world
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()

                    if answer == 'investigate':
                        bar()
                        scrollTxt('You decide to investigate the village...')
                        time.sleep(1)
                        scrollTxt('You find out the the village has been taken over by zombies...')
                        inv_text = ''
                        for i in inv:
                            inv_text = f'{inv_text}{i}'

                        if 'climbing gear' not in inv_text:
                            inv.append('climbing gear')
                            scrollTxt('You found some climbing geaer')

            if location == 'outlands':
                start = True
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[19] = world
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Outlands{Fore.WHITE}~')
                scrollTxt(
                    'You are in the outlands to the north, east and south are great mountains, '
                    'to the west is rocky ruins'
                )

                while location == 'outlands':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Outlands{Fore.WHITE}~')
                    else:
                        start = False

                    commands = []
                    addList(commands, [
                        'explore', 'inventory', 'assess', 'settings', 'save',
                        'travel west', 'encounter'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'explore':
                        scrollTxt('You spend the whole day exploring...')
                        time.sleep(2)
                        i = random.randint(1, 3)
                        if i == 3:
                            scrollTxt('You found some rocks')
                            inv.append('rocks')
                            inv.append('rocks')
                        elif i == 2:
                            scrollTxt('You found some grain')
                            inv.append('grain')
                            inv.append('grain')
                        else:
                            scrollTxt('You found nothing')
                        print()

                    if answer == 'encounter':
                        scrollTxt('You search for monster or beasts to fight...')
                        time.sleep(1)
                        monster = random.choice(
                            ['air elemental', 'Giant Scorpion', 'Dark Sun Lord', 'Sun cultist'])
                        scrollTxt(f'Finally you see a {monster}')
                        enter()

                        if monster == 'air elemental':
                            battle('the air elemental', [
                                'rest', 'charge', 'slash', 'wild slash', 'wind blast'
                            ], random.randint(20, 50), 10, 12, 1.5, random.randint(10, 20), 100)

                        if monster == 'Giant Scorpion':
                            battle('the Giant Scorpion', ['smash', 'fire blast', 'charge', 'stab', 'rest'],
                                   random.randint(50, 70), 1, 10, 2, 50, 100)

                        if monster == 'Dark Sun Lord':
                            battle('the Dark Sun Lord', [
                                'rest', 'stab', 'charge', 'slash', 'wild slash', 'punch',
                                'smash', 'chant', 'uppercut', 'reaping blow'
                            ], random.randint(20, 50), 7, 10, 3.5, random.randint(50, 100), 140)

                        if monster == 'Sun cultist':
                            battle('the Sun cultist', [
                                'charge', 'reaping blow', 'chant', 'wild slash', 'dodge'
                            ], random.randint(7, 10), 10, 3, 2, random.randint(100, 200), 100)

                        if ran is True:
                            scrollTxt(f'You run from the {monster}')
                            scrollTxt(f'You escaped the {monster}')
                        else:
                            if lose is True:
                                scrollTxt('You died game over...')
                                scrollTxt(f'the {monster} killed you')
                                quit()
                            if lose is False:
                                scrollTxt(f'You stand victorious over the {monster}')
                        print()

                    if answer == 'travel west':
                        scrollTxt('You travel north many days...')
                        scrollTxt('You finally come upon a great ruins')
                        bar()
                        location = 'abandoned village'

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[19] = world
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()
                        lvl2_spells += 1

            if location == 'desert temple':
                answer = character
                db.get(answer)[0] = character
                db.get(answer)[1] = character_class
                db.get(answer)[2] = race
                db.get(answer)[3] = max_hp
                db.get(answer)[4] = hp
                db.get(answer)[5] = gp
                db.get(answer)[6] = dex
                db.get(answer)[7] = defense
                db.get(answer)[8] = lvl1_available_spells
                db.get(answer)[9] = lvl2_available_spells
                db.get(answer)[10] = lvl1_spells
                db.get(answer)[11] = lvl2_spells
                db.get(answer)[12] = location
                db.get(answer)[13] = inv
                db.get(answer)[19] = world
                db.get(answer)[14] = weapons
                db.get(answer)[15] = exp
                db.get(answer)[16] = expNext
                db.get(answer)[17] = lvl
                start = True
                scrollTxt(f'~{Fore.LIGHTBLUE_EX}Desert Temple{Fore.WHITE}~')
                scrollTxt('You can see a great temple looming above you...')
                scrollTxt(
                    'To the south and west are great mountains, to the north is a small mountain, and to the west is a desert.'
                )

                while location == 'desert temple':
                    if start is False:
                        scrollTxt(f'~{Fore.LIGHTBLUE_EX}Desert Temple{Fore.WHITE}~')
                    else:
                        start = False

                    commands = []
                    addList(commands, [
                        'explore', 'inventory', 'assess', 'settings', 'save',
                        'enter temple', 'travel east'
                    ])
                    printList(commands, 'Commands: ')
                    inputCommands(commands, "")

                    if answer == 'inventory':
                        printInv(inv)
                        inv_interact()
                        items = len(inv)
                        print()

                    if answer == 'enter temple':
                        scrollTxt('You enter the temple...')
                        enter()
                        system('clear')
                        bar()
                        bossRaid()
                        bar()

                    if answer == 'travel east':
                        scrollTxt(
                            'You travel for many hours before reaching the desert')
                        location = 'desert'
                        bar()

                    if answer == 'assess':
                        scrollTxt(f'{character} {race}, LVL{lvl} {character_class}')
                        print_exp()
                        print_health()
                        print_gp()
                        print()

                    if answer == 'settings':
                        settings_done = False
                        while settings_done is False:
                            settings = ['font', 'scroll speed', 'done']
                            commands = []
                            addList(commands, settings)
                            printList(commands, 'Commands: ')
                            inputCommands(commands, "")
                            commands = []

                            if answer == 'font':
                                addList(commands, ['Bright', 'Dim', 'Normal'])
                                printList(commands, 'Commands: ')
                                inputCommands(commands, "")
                                commands = []

                                if answer == 'Bright':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.BRIGHT}Font: Bright')

                                if answer == 'Dim':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.DIM}Font: Dim')

                                if answer == 'Normal':
                                    scrollTxt(f'{Style.RESET_ALL}{Style.NORMAL}Font: Normal')
                            if answer == 'scroll speed':
                                scrollTxt("insert scroll speed (closer to 0 means faster)")
                                amount = 'none'
                                while amount == 'none':
                                    amount = input(f'{Fore.GREEN}')
                                    if not amount.isdigit():
                                        amount = 'none'
                                        scrollTxt(f'{Fore.WHITE}that\'s not a number')
                                    else:
                                        spd = (int(amount) / 100)
                                        amount = 'done'
                            if answer == 'done':
                                print()
                                settings_done = True

                    if answer == 'explore':
                        scrollTxt('You spend the whole day exploring...')
                        time.sleep(2)
                        i = random.randint(1, 3)
                        if i == 3:
                            scrollTxt('You found some mushrooms')
                            inv.append('mushroom')
                            inv.append('mushroom')
                        elif i == 2:
                            scrollTxt('You found some dead bodies')
                        else:
                            scrollTxt('You found nothing')
                        print()

                    if answer == 'save':
                        answer = character
                        time.sleep(.5)
                        db.get(answer)[0] = character
                        db.get(answer)[1] = character_class
                        db.get(answer)[2] = race
                        db.get(answer)[3] = max_hp
                        db.get(answer)[4] = hp
                        db.get(answer)[19] = world
                        db.get(answer)[5] = gp
                        db.get(answer)[6] = dex
                        db.get(answer)[7] = defense
                        db.get(answer)[8] = lvl1_available_spells
                        db.get(answer)[9] = lvl2_available_spells
                        db.get(answer)[10] = lvl1_spells
                        db.get(answer)[11] = lvl2_spells
                        db.get(answer)[12] = location
                        db.get(answer)[13] = inv
                        db.get(answer)[14] = weapons
                        db.get(answer)[15] = exp
                        db.get(answer)[16] = expNext
                        db.get(answer)[17] = lvl
                        print()
