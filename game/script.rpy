# Declare characters used by this game.
# The color argument colorizes the name of the character.

#innit ====================================================================
define ba = Character("BA Telkom", color ="#b30000")
define chara1 = Character("siapa ya", color = "#ffbf00")
define inc = Character("???")
define narator = Character(" ", color = "#00b300") # Fixed: Capitalized C to avoid NameError
define kasir = Character("Kasir Jabrig", color ="#b30000")
define pria = Character("Pria misterius")

# Character object for the player
define pc = Character("[you]", color="#0066ff")

init python:
    player_max_hp = 100
    player_hp = 100
    player_atk = 15
    player_def = 5
    
    enemy_max_hp = 50
    enemy_hp = 50
    enemy_atk = 8 # Fixed: Joined split lines
    enemy_def = 3
    
    in_battle = False
    player_defending = False
    tutorial_step = 0

# NEW: Inventory tracking
default inventory = []
default secret_unlocked = False

# GAME START ====================================================================
label start:
    $ player_hp = player_max_hp
    $ enemy_hp = enemy_max_hp
    $ potions = 2
    $ in_battle = False
    $ player_defending = False
    $ guts = 0 # Fixed: Joined split lines
    
    # Initialize variables for exploration
    $ current_floor = 1
    $ you = "Jeruk" 
    $ inventory = []
    $ secret_unlocked = False
    
    jump opening_cutscene

# OPENING CUTSCENE ====================================================================
label opening_cutscene:
    #scene bg jlrafa at bg_zoom
    #show rafa biasa at zoom_rafa, top
    ba "Halo kawan"
    ba "This game is a work of fiction! Any names, organizations, locations, or events appearing in this game are fictitious." 
    ba "Anak kecil dibawah 15 tahun engga boleh main"

    "(Saya kelaparan)"
    "(Makan dimana ya...)"

    inc "Wsg"
    "Hah? siapa itu?"
    inc "Cuy"
    "Oh, halo cuy"
    narator "Ini ##########, dia suka makan mie ayam"
    chara1 "Lestgo ke jabrig cuy"
    "Jabrig lagi? tadi pagi kan udah"
    chara1 "Dari sumberku katanya ada menu rahasia"
    "fr?"
    chara1 "fr"
    "Yaudah, ayo ke sana"
    
    scene black with fade
    jump opening_dialogue

# OPENING DIALOGUE ====================================================================
label opening_dialogue:
    #show ###############kasir
    chara1 "Bang"
    chara1 "Mau menu yang 'itu'"
    kasir "Say less"
    chara1 "Buru kamu juga pesen"

    menu: 
        "Pesen menu yang sama":
            $ guts = guts + 1
            kasir "Sip"
            narator "Kamu merasa tuff as hell"
            narator "Guts bertambah +1"
            pause
            kasir "Sebelum pesen kamu harus isi formulir ini dulu"
            "Formulir? buat apa coba?"
            kasir "Emang gitu kebijakannya kocak"
            chara1 "Iya, emang harus gitu cenah"
            kasir "Ayo buruan kocak"
            "Oke gas"
    
            narator "Kamu mengambil pensil dan mengisi formulir"
            $ you = renpy.input("Enter your name:", length=20, default="Jeruk").strip()
            if not you:
                $ you = "Jeruk"

            pc "Beres nih bang" 
            kasir "Nice"
            kasir "Saya simpan dulu berkasnya baru saya hidangkan menunya ya"
            scene black with fade
            jump section1 

        "Pesen mie ayam biasa aja":
            $ guts = guts - 1
            kasir "Cih. Bitchass."
            "Mie ayam biasa 1"
            kasir "Atas nama siapa?"
            $ you = renpy.input("Enter your name:", length=20, default="Jeruk").strip()
            if not you:
                $ you = "Jeruk"
            kasir "Oke"
            scene black with fade
            jump section1

# ACE ATTORNEY STYLE INVESTIGATION
label section1:
    #scene bg_jabrig_interior 
    chara1 "Sambil nunggu mau ngapain?"
    jump exploration_loop

label exploration_loop:
    menu:
        "LOKASI: LANTAI [current_floor]"
        
        "Examine":
            jump examine_logic
            
        "Talk":
            jump talk_logic
        
        "Move":
            jump move_logic     

# MOVE MENU
label move_logic:
    menu:
        "Ke Lantai 1" if current_floor != 1:
            $ current_floor = 1
            "Kamu kembali ke lantai 1."
            jump exploration_loop
        
        "Ke Lantai 2" if current_floor != 2:
            $ current_floor = 2
            "Kamu naik ke lantai 2. Di sini banyak meja kosong."
            "Kamu melihat seorang pria duduk di pojok."
            jump exploration_loop
            
        "Ke Lantai 3" if current_floor != 3:
            $ current_floor = 3
            "Lantai 3 terlihat seperti tempat latihan..."
            jump exploration_loop
            
        "Back":
            jump exploration_loop

# TALK & TRADING MENU
label talk_logic:
    if current_floor == 1:
        menu:
            "Tanya soal menu rahasia":
                chara1 "Sabar, lagi dibikin sama Bang Jabrig."
                jump exploration_loop
            
            "Bicara dengan Chara1" if "Discount Voucher" not in inventory and "Sambal Setan" not in inventory:
                chara1 "Eh, tadi aku nemu ini di jalan. Mau?"
                menu:
                    "Terima":
                        "Kamu mendapatkan Discount Voucher!"
                        $ inventory.append("Discount Voucher")
                        jump exploration_loop
                    "Tolak":
                        jump exploration_loop

            "Bicara dengan Kasir" if "Discount Voucher" in inventory:
                kasir "Wah, itu voucher punyaku yang hilang! Mau tukar sama sambal spesial?"
                menu:
                    "Tukar":
                        $ inventory.remove("Discount Voucher")
                        $ inventory.append("Sambal Setan")
                        "Kamu mendapatkan Sambal Setan!"
                        jump exploration_loop
                    "Jangan":
                        jump exploration_loop

    elif current_floor == 2:
        menu:
            "Ajak Bicara Pria Misterius":
                if "Sambal Setan" in inventory:
                    pria "Bau itu... Sambal Setan! Berikan padaku, dan aku akan memberimu harta karun."
                    menu:
                        "Tukar":
                            $ inventory.remove("Sambal Setan")
                            $ inventory.append("Ancient Coin")
                            "Pria itu memberikanmu Koin Kuno (Ancient Coin)."
                            jump exploration_loop
                        "Tolak":
                            jump exploration_loop
                else:
                    pc "Halo bang!"
                    pria ". . ."
                    pria "Jangan ganggu aku kalau tidak bawa makanan pedas."
                    jump exploration_loop
            "Back":
                jump exploration_loop

    elif current_floor == 3:
        "Tidak ada orang di sini untuk diajak bicara."
        jump exploration_loop
    return

# EXAMINE MENU
label examine_logic:
    if current_floor == 1:
        "Meja kasir terlihat sangat berminyak."
        jump exploration_loop
    elif current_floor == 3:
        "Ada dummy latihan di pojok ruangan."
        if "Ancient Coin" in inventory:
            "Koin di sakumu mulai bersinar..."
            menu:
                "Gunakan Koin pada Dummy":
                    "Dummy itu berubah menjadi Secret Boss!"
                    $ secret_unlocked = True
                    jump battle_tutorial_setup 
                "Abaikan":
                    jump exploration_loop
        else:
            menu:
                "Pukul dummy-nya":
                    "Sepertinya ini saat yang tepat untuk pemanasan."
                    jump battle_tutorial_setup 
                "Jangan disentuh":
                    jump exploration_loop
    else:
        "Hening. Hanya ada meja dan kursi kayu biasa."
        jump exploration_loop

# BATTLE SETUP
label battle_tutorial_setup:
    if secret_unlocked:
        "SECRET BOSS: THE GOLDEN DUMMY APPEARS!"
        $ enemy_hp = 200
        $ enemy_atk = 20
    else:
        "Here we go. The training dummy is already set up."
        $ enemy_hp = 50
        $ enemy_atk = 8

    $ in_battle = True
    $ tutorial_step = 0
    jump battle_tutorial

# BATTLE SYSTEM
label battle_tutorial:
    if tutorial_step == 0:
        "The combat interface shows my status and the enemy's."
        "[player_hp]/[player_max_hp] HP | Potions: [potions]"
        "Enemy: [enemy_hp] HP"
        $ tutorial_step = 1
    
    if enemy_hp <= 0:
        jump victory_screen
    
    if player_hp <= 0:
        "Kalah..."
        return # Game Over

    menu:
        "Attack":
            $ damage = max(1, player_atk - enemy_def)
            $ enemy_hp -= damage
            "Hit for [damage] damage!"
        
        "Defend":
            $ player_defending = True
            "Defense up!"
        
        "Use Item" if potions > 0:
            $ player_hp = min(player_max_hp, player_hp + 30)
            $ potions -= 1
            "Used potion!"

    # Enemy Turn
    if enemy_hp > 0:
        if player_defending:
            $ damage = max(1, (enemy_atk - player_def) // 2)
            $ player_defending = False
        else:
            $ damage = max(1, enemy_atk - player_def)
        $ player_hp -= damage
        "Took [damage] damage!"
    
    jump battle_tutorial

label victory_screen:
    "The dummy falls apart!"
    if secret_unlocked:
        "You obtained the LEGENDARY MIE AYAM!"
    "Training complete!"
    jump endgame

label endgame:
    "Tutorial Complete!"
    return
