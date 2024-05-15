# air courtyard earth courtyard water courtyard fire courtyard learn courtyard basketball court auditorium library play ground amphithatere dhaba/garden area zen garden Tapal, Cafe to go, gym

print("Welcome to Akinator")
print("Choose a place amongst these \n\n - play ground, amphitheatere, dhaba/garden area, zen garden, Tapal, Cafe to go, gym, nestcafe\n\n - pool, auditorium, library- air courtyard, earth courtyard, water courtyard, fire courtyard\n\n - learn courtyard, basketball court\n\n - air courtyard, earth courtyard, water courtyard, fire courtyard")
print()
print("We will try to guess what you are thinking of.")
print("You have to answer the questions in yes/no form.")
print()
question=input("is your place a court/courtyard? " ).lower()

# RECURSIVE FUNCTION: 
def akinator_game():
    if len(courtyard_1)==1:
        print("your character is " + courtyard_1[0]["place"])               
        quit()
    elif len(more_spaces)==1:
        print("your character is"+more_spaces[0]["name"])
        quit()
    else:
       akinator_game(courtyard_1,more_spaces)

# CODE FOR ONLY COURTYARDS:
# SPACES: AIR COURTYARD, WATER COURT,LEARN COURT,FIRE COURT,EARTH COURT, BASKETBALL COURT
if question=="yes":
    courtyard_1=[{"place":"air courtyard","contains water":False,"dsse lab":False , "large scale":False,"painting":False,"glassboard":False, "open space":True, "tables": False, "avatar": True, "connected": True, "prayer area": False, "lower ground": False},
                 
                {"place":"water courtyard","contains water":True,"painting":False,"dsse lab":False,"large scale":False,"glassboard":False, "open space":True, "tables":True, "avatar": False, "connected": True, "prayer area": False, "lower ground": False},

                {"place":"learn courtyard","contains water":False,"dsse lab":False,"large scale":False,"painting":False,"glassboard":True, "open space":True, "tables": True, "avatar": False, "connected": False, "prayer area": True, "lower ground": True},

                {"place":"fire courtyard","contains water":False,"dsse lab":True,"large scale":False,"painting":False,"glassboard":False,"open space":True, "tables": False, "avatar": False, "connected": False, "prayer area": False, "lower ground": False},

                {"place":"earth courtyard","contains water":False,"dsse lab":False,"large scale":False,"painting":True,"glassboard":True, "open space":True, "tables":False, "avatar": False, "connected": True, "prayer area": False, "lower ground": False},

                {"place":"basketball court","contains water":False,"dsse lab":False,"large scale":True,"painting":False,"glassboard":False, "open space":True, "tables": False, "avatar": False, "connected": False, "prayer area": False, "lower ground": True}] 
        # FILTER THE SPACES ACCORDING TO USER INPUT:    
    def check_character(answer,property):
        if answer=="yes":
            ans=True
        else:
            ans=False
        new_lst=[]        
        for i in courtyard_1:
            if i[property]!=ans:
                new_lst.append(i)
        for j in new_lst:
            courtyard_1.remove(j)
        if len(courtyard_1)==1:
            print("your character is " + courtyard_1[0]["place"])               
            quit()

        # MATCHES THE PARAMETERS WITH THE DICTIONARY
    ans=input("Is it an open space? ")
    check_character(ans,"open space")

    ans=input("Is the place connected with other courts?  ")
    check_character(ans,"connected")

    ans=input("Does the place have tables and chairs to study? ")
    check_character(ans,"tables")
    
    ans=input("Does the place have huge painting on migration installed? ")
    check_character(ans,"painting") 

    ans=input("Does the place have glassboards installed? " )
    check_character(ans,"glassboard") 

    ans=input("Does the place have a fountain in it? ")
    check_character(ans,"contains water")   

    ans=input("is the place surrounded by DSSE labs? ")
    check_character(ans,"dsse lab") 

    ans=input("Does the place have space to hold large scale events? ")
    check_character(ans,"large scale") 

    ans=input("is their prayer area near or inside this place? ")
    check_character(ans,"prayer area") 
# CODE FOR SPACES OTHER THAN COURTYARDS:
# SPACES: AMPHI,POOL,ZEN GARDEN,CAFE2 GO, DHABA, AUDI,PLAY GROUND,LIB,TAPAL,NESTCAFE,GYM
elif  question=="no":
        more_spaces=[{"name":"Amphitheatre", "food":False, "money":False, "hu dukaan":True, "open space":True, "used for health and wellbeing":False, "plays":True, "natural shade with dense plantation":False, "pakistani street snacks":False, "bamboo stick roof":False, "italian & continental":False, "academic purposes":False, "events":True, "has rooms":False, "large windows":False, "tea":False, "lose calories": False, "shower": False, "collaboration": False, "computers": False, "piano": False},
                     
                    {"name":"Pool", "food":False,"plays":False, "money":True, "hu dukaan":False, "open space":True, "used for health and wellbeing":True, "natural shade with dense plantation":False,"pakistani street snacks":False,"bamboo stick roof":True, "italian & continental":False, "academic purposes":False,"events":False,"has rooms":False,"large windows":False, "tea":False, "lose calories": True, "shower": False, "collaboration": False, "computers": False, "piano": False},

                    {"name":"Zen Garden", "food":False, "plays":False, "money":False, "hu dukaan":False, "open space":True, "used for health and wellbeing":True, "benches/chairs":True, "natural shade with dense plantation":True,"pakistani street snacks":False,"bamboo stick roof":False, "italian & continental":False, "academic purposes":False,"events":False,"has rooms":False,"large windows":False, "tea":False, "lose calories": False, "shower": False, "collaboration": False, "computers": False, "piano": False},
                    
                    {"name":"cafe2go","food":True, "plays":False, "money":True, "hu dukaan":False, "open space":True, "used for health and wellbeing":False, "benches/chairs":True, "natural shade with dense plantation":False,"pakistani street snacks":False,"bamboo stick roof":False, "italian & continental":True,"academic purposes":False,"events":False,"has rooms":False,"large windows":False, "tea":False, "lose calories": False, "shower": False, "collaboration": False, "computers": False, "piano": False},

                    {"name":"Dhaba/Garden Area", "food":True, "plays":False, "money":True, "hu dukaan":True, "open space":True, "used for health and wellbeing":False, "benches/chairs":True, "natural shade with dense plantation":False, "pakistani street snacks":True, "bamboo stick roof":False, "italian & continental":False, "academic purposes":False, "events":False, "has rooms":False, "large windows":False, "tea":False, "lose calories": False, "shower": False, "collaboration": False,"computers": False, "piano": False},
                    
                    {"name":"auditorium", "academic purposes":True,"events":True, "has rooms":False,"large windows":False, "tea":False, "lose calories": False, "food":False, "money":False, "hu dukaan":False, "open space":False, "used for health and wellbeing":False, "plays":False, "natural shade with dense plantation":False,"pakistani street snacks":False,"bamboo stick roof":False, "italian & continental":False, "shower": False, "collaboration": False, "computers": False, "piano": True}, 
                     
                    {"name":"playground", "academic purposes":True,"events":False, "has rooms":True,"large windows":False, "tea":False, "lose calories": False, "food":False, "money":False, "hu dukaan":False, "open space":False, "used for health and wellbeing":False, "plays":False, "natural shade with dense plantation":False,"pakistani street snacks":False,"bamboo stick roof":False, "italian & continental":False, "shower": False, "collaboration": True, "computers": False, "piano": False},

                    {"name":"library", "academic purposes":True,"events":False,"has rooms":True,"large windows":False, "tea":False, "lose calories": False, "food":False, "money":False, "hu dukaan":False, "open space":False, "used for health and wellbeing":False, "plays":False, "natural shade with dense plantation":False,"pakistani street snacks":False,"bamboo stick roof":False, "italian & continental":False, "shower": False, "collaboration": True, "computers": True, "piano": False},

                    {"name":"tapal", "academic purposes":False,"events":False,"has rooms":False,"large windows":False, "tea":True, "lose calories": False, "food":True, "money":True, "hu dukaan":True, "open space":False, "used for health and wellbeing":False, "plays":False, "natural shade with dense plantation":False,"pakistani street snacks":False,"bamboo stick roof":False, "italian & continental":False, "shower": False, "collaboration": False, "computers": False, "piano": False},

                    {"name":"nestcafe", "academic purposes":False,"events":False,"has rooms":False,"large windows":True, "tea":False, "lose calories": False, "food":True, "money":True, "hu dukaan":False, "open space":False, "used for health and wellbeing":False, "plays":False, "natural shade with dense plantation":False,"pakistani street snacks":False,"bamboo stick roof":False, "italian & continental":False, "shower": False, "collaboration": False, "computers": False, "piano": False},

                    {"name":"gym", "academic purposes":False,"events":False,"has rooms":False,"large windows":False, "tea":False, "lose calories": True, "food":False, "money":True, "hu dukaan":True, "open space":False, "used for health and wellbeing":True, "plays":True, "natural shade with dense plantation":False,"pakistani street snacks":False,"bamboo stick roof":False, "italian & continental":False, "shower": True, "collaboration": False, "computers": False, "piano": False}]
                # FILTER THE SPACES ACCORDING TO USER INPUT: 
        def extra_spaces(space_a,space_b):
            if space_a=='yes':
                ans=True
            else:                  
                ans=False
            new3_lst=[]
            for x in more_spaces: 
                if x[space_b]!=ans:
                    new3_lst.append(x)
            for y in new3_lst:
                more_spaces.remove(y)
            if len(more_spaces)==1:
                print("your place is " + more_spaces[0]["name"])
                quit ()

            # MATCHES THE PARAMETERS WITH THE DICTIONARY
        ans=input("is your place an open space? ")
        extra_spaces(ans,"open space")   

        ans=input("Do you need to pay to avail service(s) at this place? ")
        extra_spaces(ans,"money")      

        ans=input("Is the place related to food and dining? ")
        extra_spaces(ans,"food")      

        ans=input("Does the place have small pods/rooms inside it? ")
        extra_spaces(ans,"has rooms")

        ans=input("Is the place for betterment mental and physical health and wellbeing? ")
        extra_spaces(ans,"used for health and wellbeing")

        ans=input("Is the place near HU Dukaan? ")
        extra_spaces(ans,"hu dukaan")

        ans=input("Is the place used for academic purposes? ")
        extra_spaces(ans,"academic purposes")

        ans=input("Is the place used to conduct lareg scale events? ")
        extra_spaces(ans,"events")

        ans=input("Do activities at this place help you lose calories? ")
        extra_spaces(ans,"lose calories")

        ans=input("Is the place famous for plays and performances conducted there? ")
        extra_spaces(ans,"plays")

        ans=input("Does the place have natural shade and dense plantation? ")
        extra_spaces(ans,"natural shade with dense plantation") 
        
        ans=input("Does the place has a roof made of bamboo sticks? ")
        extra_spaces(ans,"bamboo stick roof") 

        ans=input("Can you find Italian and Continental cuisine in this place? ")
        extra_spaces(ans,"italian & continental") 
        
        ans=input("Can you find Pakistani street snack in this place? ")
        extra_spaces(ans,"pakistani street snacks")

        ans=input("Does the place have large windows instead of AC for ventilation? ")
        extra_spaces(ans,"large windows")

        ans=input("Is the place named after a tea brand? ")
        extra_spaces(ans,"tea")

        ans=input("Does the place offer shower facility? ")
        extra_spaces(ans,"shower")

        ans=input("Is the place ideal for collaborative work? ")
        extra_spaces(ans,"collaboration")

        ans=input("Does the place have lots and lots of computers? ")
        extra_spaces(ans,"computers")

        ans=input("Is there a around in or around the place? ")
        extra_spaces(ans,"piano")
