# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#innit ====================================================================
define ba = Character("BA Telkom", color ="#b30000")
define chara1 = Character("siapa ya", color = "#ffbf00")
define inc = Character("???")
define narator = character(" ", color = "#00b300")
define kasir = Character("Kasir Jabrig", color ="#b30000")

init python:
    player_max_hp = 100
    player_hp = 100
    player_atk = 15
    player_def = 5
    
    enemy_max_hp = 50
    enemy_hp = 50
    enemy_atk = 8
    enemy_def = 3
    
    #item
    ###############
    
    in_battle = False
    player_defending = False
    
    tutorial_step = 0

# GAME START ====================================================================
label start:
    $ player_hp = player_max_hp
    $ enemy_hp = enemy_max_hp
    $ potions = 2
    $ in_battle = False
    $ player_defending = False
    
    jump opening_cutscene


# OPENING CUTSCENE ====================================================================
label opening_cutscene:

    #scene bg jlrafa at bg_zoom
    #show rafa biasa at zoom_rafa, top

    ba "Halo kawan"
    ba "This game is a work of fiction! Any names, organizations, locations, or events appearing in this game are fictitious. 
        Any resemblance to real names, organizations, locations, events, etc. is purely coincidental." 
    ba "Anak kecil dibawah 15 tahun engga boleh main"

    #scene black with fade

    #scene bg ###############
    #with fade
    
    #show ###############
    #with dissolve

    "(Saya kelaparan)"
    #show ###############stiker ironman kelaparan
    #with fade
    "(Makan dimana ya...)"
    #hide ###############
    #with fade

    inc "Wsg"
    "Hah? siapa itu?"
    #show ###############
    #with dissolve
    inc "Cuy"
    "Oh, halo cuy"
    narator "Ini ##########, dia suka makan mie ayam"
    narator "Katanya kalau mie ayam jadi orang bakal dia kawinin"
    narator "this guy might be retarded"
    chara1 "Lestgo ke jabrig cuy"
    "Jabrig lagi? tadi pagi kan udah"
    chara1 "Dari sumberku katanya ada menu rahasia"
    "fr?"
    chara1 "fr"
    "Yaudah, ayo ke sana"
    #hide ############### 
    #with fade
    
    scene black with fade
    
    jump opening_dialogue


# OPENING DIALOGUE ====================================================================
label opening_dialogue:

    #scene bg ###############
    #with fade
    #show ###############kasir
    #with dissolve
    chara1 "Bang"
    chara1 "Mau menu yang 'itu'"
    kasir "Say less"
    chara1 "Buru kamu juga pesen"

    menu: 
        "Pesen menu yang sama":

            kasir "Type shi"
            kasir "Sebelum pesen kamu harus isi formulir ini dulu"
            "Formulir? buat apa coba?"
            kasir "Rahasia, emang gitu kebijakannya kocak"
            "Kamu juga ngisi formulirnya kah?"
            #hide ###############kasir
            #with fade
            #show ###############chara1
            #with dissolve
            chara1 "Iya"
            chara1 "Emang harus gitu cenah"
            #hide ###############chara1
            #with fade
            #show ###############kasir
            #with dissolve
            kasir "Ayo buruan kocak"
            "Oke gas"
            narator "Kamu mengambil pensil dan mengisi formulir"

            $ you = renpy.input("Enter your name:", length=20, default="Jeruk") #tambah warna kalo mau
            $ you = you.strip()
            if you == "":
                $ you = "Hero"

            you "Beres nih bang"
            kasir "Nice"
            kasir "Saya simpan dulu berkasnya baru saya hidangkan menunya ya"
            #hide ###############kasir
            #with fade

            #jump ############### 
        "Pesen mie ayam biasa aja":
            ###############
            #jump ###############

        "Run like a lil bihh":
            jump no_balls


label no_balls: ############### ini ending 1
    narator "Kamu lari keluar Jabrig dengan cepat"
    kasir "No balls"
    chara1 "No balls"
return




















#########################################################################################################
#########################################################################################################
# BATTLE SETUP ====================================================================
label battle_tutorial_setup:
    scene bg_arena  # PLACEHOLDER: Training arena background
    with fade
    
    show protagonist_battle at left  # PLACEHOLDER: Battle stance sprite
    with dissolve
    
    "Here we go. The training dummy is already set up."
    
    show enemy_dummy at right  # PLACEHOLDER: Training dummy enemy sprite
    with dissolve
    
    play music "bgm_battle.ogg" fadein 1.0  # PLACEHOLDER: Battle music
    
    "Let's see what I remember..."
    
    $ in_battle = True
    $ tutorial_step = 0
    
    jump battle_tutorial

# BATTLE SYSTEM ====================================================================
label battle_tutorial:
    # Display battle status
    if tutorial_step == 0:
        "The combat interface shows my status and the enemy's."
        "[player_hp]/[player_max_hp] HP | Potions: [potions]"
        "Training Dummy: [enemy_hp]/[enemy_max_hp] HP"
        $ tutorial_step = 1
    
    # Check victory condition
    if enemy_hp <= 0:
        jump victory_screen
    
    # Check defeat (shouldn't happen in tutorial, but just in case)
    if player_hp <= 0:
        "Wait, this is just training... Let me try that again."
        $ player_hp = player_max_hp
        $ enemy_hp = enemy_max_hp
        $ potions = 2
        jump battle_tutorial
    
    # PLAYER TURN ====================================================================
    "My turn!"
    
    menu:
        "What should I do?"
        
        "Attack":
            "I swing my sword at the dummy!"
            play sound "sfx_attack.ogg"  # PLACEHOLDER: Attack sound
            
            $ damage = max(1, player_atk - enemy_def)
            $ enemy_hp -= damage
            
            "Hit for [damage] damage!"
            "Training Dummy: [enemy_hp]/[enemy_max_hp] HP"
            
            if enemy_hp <= 0:
                jump victory_screen
        
        "Defend":
            "I raise my guard and prepare for the counter-attack."
            $ player_defending = True
            "Defense up for this turn!"
        
        "Use Item" if potions > 0:
            menu:
                "Which item?"
                
                "Potion ([potions] left)" if potions > 0:
                    play sound "sfx_heal.ogg"  # PLACEHOLDER: Healing sound
                    $ heal_amount = 30
                    $ player_hp = min(player_max_hp, player_hp + heal_amount)
                    $ potions -= 1
                    
                    "Used a potion and recovered [heal_amount] HP!"
                    "[player_hp]/[player_max_hp] HP | Potions: [potions]"
                
                "Never mind":
                    jump battle_tutorial
        
        "Use Item" if potions == 0:
            "I'm out of potions!"
            jump battle_tutorial
    
    # ENEMY TURN ====================================================================
    if enemy_hp > 0:
        "The training dummy strikes back!"
        play sound "sfx_enemy_attack.ogg"  # PLACEHOLDER: Enemy attack sound
        
        if player_defending:
            $ damage = max(1, (enemy_atk - player_def) // 2)
            $ player_defending = False
            "My defense reduced the damage!"
        else:
            $ damage = max(1, enemy_atk - player_def)
        
        $ player_hp -= damage
        
        "Took [damage] damage!"
        "[player_hp]/[player_max_hp] HP"
    
    jump battle_tutorial

# VICTORY SEQUENCE ====================================================================
label victory_screen:
    stop music fadeout 1.0
    play sound "sfx_victory.ogg"  # PLACEHOLDER: Victory fanfare
    
    hide enemy_dummy with dissolve
    
    "The training dummy falls apart!"
    
    play music "bgm_victory.ogg"  # PLACEHOLDER: Victory theme
    
    scene bg_arena
    show protagonist_battle at center
    with dissolve
    
    "Training complete!"
    "Not bad. I think I've got the basics down."
    
    $ in_battle = False
    
    jump endgame

# END SCREEN ====================================================================
label endgame:
    scene black with fade
    stop music fadeout 2.0
    
    centered "{size=+20}Tutorial Complete!{/size}"
    
    "You've mastered the basics of combat."
    "You're ready for whatever comes next."
    
    centered "Thanks for playing!"
    
    menu:
        "What would you like to do?"
        
        "Return to Main Menu":
            return
        
        "Quit Game":
            $ renpy.quit()
    
    return