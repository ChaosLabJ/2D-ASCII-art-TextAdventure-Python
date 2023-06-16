# Game by ChaosLabJ
coords={}
player={}
won=False

def intro():
    print("You are a duck.\nAnd I hate you.")
    tutorial()
    
def tutorial():
    tutorialspace = " ".join(loadTutorial())
    print(tutorialspace)
    print("This here is the space you will move about.")
    if(str(input())=="y"):
        coords["y"][2][2]="$"
        lastX=2
        lastY=2
        moves=0
        print(" ".join(renderSpace()))
        print("This $ is you. Try moving your character by typing w,a,s or d. Take some time to get used to these controls.")
        while moves<5:
            moveUser=str(input())   ##Chatgpt found the missing 2 () that follows the input-function and pointed out that I was calling input() twice...
            if(moveUser.isalpha()): 
                if(moveUser=="w"):
                    coords["y"][lastY][lastX]="-"
                    lastY-=1
                    coords["y"][lastY][lastX]="$"
                    print(" ".join(renderSpace()))
                    print(lastY,lastX)
                    moves+=1
                elif(moveUser=="a"):
                    coords["y"][lastY][lastX]="-"
                    lastX-=1
                    coords["y"][lastY][lastX]="$"
                    print(" ".join(renderSpace()))
                    print(lastY,lastX)
                    moves+=1
                elif(moveUser=="d"):
                    coords["y"][lastY][lastX]="-"
                    lastX+=1
                    coords["y"][lastY][lastX]="$"
                    print(" ".join(renderSpace()))
                    print(lastY,lastX)
                    moves+=1
                elif(moveUser=="s"):
                    coords["y"][lastY][lastX]="-"
                    lastY+=1
                    coords["y"][lastY][lastX]="$"
                    print(" ".join(renderSpace()))
                    print(lastY,lastX)
                    moves+=1
                elif(moveUser.isalpha()):
                    print("Use W,A,S or D to move about.")
        print("Great! Now that we got that sorted we can start the game :) ")
        game()

    

def loadTutorial():
    coords["y"]={}
    space = [""]
    size=4
    x={}
    for i in range(size+1): 
        coords["y"][i]=x
        for l in range(int(size*1.5)):
            x = {l:[]}
            #print(i,l)
            symbol = "-"
            space.append(symbol)
            coords["y"][i][l]=symbol
        space.append("\n")
        l=0
    #print(coords)
    return space

def loadMap(height, building):
    spacePreset=[""]
    coords["z"]=height
    if(building=="home"):
        if(height==0):
            spacePreset="@ # # # * # # # # # @,= = = : + + + + + @ @,= = = : + + + + + @ @,= = = : + + + + + @ @,= = = : + + + + + @ @,+ + + : + + + + + @ @,+ x · · · · · * + @ @,+ x · · · · · ~ + @ @,+ > > · · ~ & ~ + @ @,# # # # # # # # # @ @"
        elif(height==1):
            spacePreset="@ # # # : # # # # # @,= = = : + + + + + @ @,= = = : + + + + + @ @,= = = : + + + + + @ @,= = = : + + + + + @ @,+ + + + + + + + + @ @,+ ~ · x x · · x + @ @,+ ~ · · · · [ ] + @ @,+ < < · · · [ ] + @ @,# # # # # # # # # @ @"
        elif(height==2):
            spacePreset="@ # # # : # # # # # @,= = = : + + + + + @ @,= = = : + + + + + @ @,= = = : + + + + + @ @,= = = : + + + + + @ @,+ + + + + + + + + @ @,+ + + + + + + + + @ @,+ + + + + + + + + @ @,+ + + + + + + + + @ @,# # # # # # # # # @ @"
        elif(height==-1):
            spacePreset="@ # # # : # # # # # @,= = = : + + + + + @ @,= = = : + + + + + @ @,= = = : + + + + + @ @,= = = : + + + + + @ @,+ + + + + + + + + @ @,+ + + + + + + + + @ @,+ + + + + + + + + @ @,+ + + + + + + + + @ @,# # # # # # # # # @ @"
    coords["y"]={}
    space = [""]
    size=10
    x={}
    for i in range(size): 
        coords["y"][i]=x
        spacePresetX=spacePreset.split(",")
        for l in range(len(spacePresetX)+1):
            x = {l:[]}
            symbol=str(spacePresetX[i].split()[l])
            space.append(symbol)
            coords["y"][i][l]=symbol
        space.append("\n")
        l=0
    #print(coords)
    return space

def renderSpace():
    space=[""]
    for i in coords["y"]:
        for l in coords["y"][i]:
            space.append(coords["y"][i][l])
        space.append("\n")
    #print(coords["y"])
    return space

def passable(Symbol):
    if(Symbol=="="):
        return True
    elif(Symbol==":"):
        return True
    elif(Symbol=="·"):
        return True
    elif(Symbol=="<"or Symbol==">"):
        return True
    else:
        return False

def interActable(Symbol):
    if(Symbol=="*"):
        return True
    elif(Symbol=="["or Symbol=="]"):
        return True
    elif(Symbol=="~"):
        return True
    elif(Symbol=="?"):
        return True
    elif(Symbol=="&"):
        return True
    elif(Symbol=="x"):
        return True
    else:
        return False

def items(container,posY,posX):
    if(container=="freezer"):
        if(posY==6 and posX==7):
            return ""
    return "nothing"

def event(Symbol,posY,posX):
    if(Symbol=="*"):
        container="fridge"
        if(posY==6 and posX==7):
            print("It's your fridge and contains the following items:")
            itemList=(items(container,posY,posX))
            if(itemList!="nothing"):
                print("")
        elif(posY==3 and posX==7):
            print("This fridge contains the following items:")
            print(items(container,posY,posX))
    elif(Symbol=="["or Symbol=="]"):
        if(posY==7 and posX==6 or posX==7 or posY==8 and posX==6 or posX==7):
            if(input("This is your bed. Do you want to rest now?\n")=="y"):
                rest()
        if(posY==2 and posX==1 or posX==2):
            if(input("It's an empty bed. Do you want to rest now?\n")=="y"):
                rest()
    elif(Symbol=="~"):
        container="surface"
        if(posY==6 and posX==7):
            print(items(container,posY,posX))
    elif(Symbol=="?"):
        print("SPECIAL")
    elif(Symbol=="&"):
        print("WATER")
    elif(Symbol=="x"):
        print("CHEST")

def rest():
    print("You're rested now.")

def movement(startY,startX):
    oldSymbol=coords["y"][startY][startX]
    coords["y"][startY][startX]="$"
    transitionCoords="8/1,4/3,0/4"
    lastY=startY
    lastX=startX
    print(" ".join(renderSpace()))
    while(won!=True):
        moveUser=str(input())   
        if(moveUser.isalpha()): 
            if(moveUser=="w"):
                if(passable(coords["y"][lastY-1][lastX])):
                    coords["y"][lastY][lastX]=oldSymbol
                    lastY-=1
                    oldSymbol=coords["y"][lastY][lastX]
                    coords["y"][lastY][lastX]="$"
                elif(interActable(coords["y"][lastY-1][lastX])):
                    event(coords["y"][lastY-1][lastX],lastY,lastX)
            elif(moveUser=="a"):
                if(passable(coords["y"][lastY][lastX-1])):
                    coords["y"][lastY][lastX]=oldSymbol
                    lastX-=1
                    oldSymbol=coords["y"][lastY][lastX]
                    coords["y"][lastY][lastX]="$"
                elif(interActable(coords["y"][lastY][lastX-1])):
                    event(coords["y"][lastY-1][lastX],lastY,lastX)
            elif(moveUser=="d"):
                if(passable(coords["y"][lastY][lastX+1])):
                    coords["y"][lastY][lastX]=oldSymbol
                    lastX+=1
                    oldSymbol=coords["y"][lastY][lastX]
                    coords["y"][lastY][lastX]="$"
                elif(interActable(coords["y"][lastY][lastX+1])):
                    event(coords["y"][lastY-1][lastX],lastY,lastX)
            elif(moveUser=="s"):
                if(passable(coords["y"][lastY+1][lastX])):
                    coords["y"][lastY][lastX]=oldSymbol
                    lastY+=1
                    oldSymbol=coords["y"][lastY][lastX]
                    coords["y"][lastY][lastX]="$"
                elif(interActable(coords["y"][lastY+1][lastX])):
                    event(coords["y"][lastY-1][lastX],lastY,lastX)
            lastCoords=str(lastY)+"/"+str(lastX)
            if(lastCoords in transitionCoords.split(",")):
                if(lastCoords=="8/1" and coords["z"]==0):
                    loadMap(1,"home")
                elif(lastCoords=="8/1" and coords["z"]==1):
                    loadMap(0,"home")
                elif(lastCoords=="4/3" and coords["z"]==0):
                    loadMap(2,"home")
                elif(lastCoords=="4/3" and coords["z"]==2):
                    loadMap(0,"home")
                elif(lastCoords=="0/4" and coords["z"]==2):
                    loadMap(2,"house1")
            print(" ".join(renderSpace()))

def game():
    loadMap(0,"home")
    print(" ".join(renderSpace()))
    print("This here is your house.")
    movement(7,3)

def test():
    print("--TEST--")
    print("--TEST--")

test()
intro()