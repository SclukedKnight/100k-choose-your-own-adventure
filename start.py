from os import system
from rich import print

system("clear||cls")

print("[purple on white]Welcome to your first day of living in Vancouver[/purple on white]")

print("Today you will start your journey as a [bold cyan underline]crimminal[/bold cyan underline] or, as a [bold red underline]upstanding citizen[/bold red underline]")
print("")
print("What do you want to do next?")
print("1. Look around [yellow]West Broadway[/yellow]")
print("2. Go to school at [red]SFU[/red]")

walk = input("Make a choice!:")
system("clear||cls")
if walk == "1":
    print("You see a building with a small poster saying '[magenta]GTA VI stealing, people wanted[/magenta]' do you go in?")
    print("1. Enter the building")
    print("2. Decide to reform and go to [red]SFU[/red] like an upstanding citizen")

    enter = input("Choose (I don't ask poitely): ")
    system("clear||cls")
    if enter == "1":
        print("you enter the building")
        print("They usher you into a room where they do a [cyan]presentation[/cyan] on how they're going to break in using the broadway extenions tunnels")
        print("They start asking each person if they want to keep going. You're next")
        print("What do you do?")
        print("1. Say yes")
        print("2. Say no")
        print("3. Book it, and attack people that stop you")
        print("")
        booking = input("Choose, times ticking")
        system("clear||cls")
        if booking == "1":
            print("You get shuffled into a van and are now inside the unfinished tunnels with the [blue]crew[/blue]")
        elif booking == "2":
            print("You get [purple]trapped[/purple] in the building and the day ends, you hear people come back and mention how they got GTA VI through the door to the room you're locked in.")
            print("the day ends, the end")
    elif enter == "2":
        print("You missed the last [yellow]99[/yellow] and now need to take the [green]R4[/green], and as you do the floor breaks beneath you and now you're stuck in the bored tunnels for the M line expansion")
        print("You we're walking on the false roadway and it collpased beneath you")
elif walk == "2":
    print("You get on the [yellow]99[/yellow] to Joyce")
    print("The bus goes [blue]slow[/blue], and the bus is [green]empty[/green]")
    print("You get to Production way university, and get on the 145")
    print("It catches fire from going uphill and you [red]die[/red]")
    print("The end")

if booking == "1" or enter == "2":
    print("You see another, unframiliar group of people and they ask what you're doing there")
    print("They're asking [yellow]YOU[/yellow] specifically, what do you say:")
    print("1: Was kidnapped, and need help")
    print("2: nonya buissness")
    print("3: (start running at them)")

    attack = input("Choose, times ticking: ")
    system("clear||cls")
    if attack == "1":
        print("No, I don't belive you get off the tracks though, we have a [white]test train[/white] running through right now")
        print("As he says that you freeze, is it glee or fear, the glee of seeing a [white]train[/white] from GTA VI?")
        print("You're being dilusional and are hit by the [white]train[/white], and die the end")
    elif attack == "2":
        print("You start running away while a group of people follow you, you run straight into the path of a [white]train[/white] and [red]die[/red]")
        print("The end")
    elif attack == "3":
        print("as you start running, he backs up as you trip on the tracks, and get shocked by the [red]650V DC[/red] third rail for [blue]expo[/blue] and [yellow]m[/yellow] line trains, and die")
    print("What if the real GTAVI is the friends we made along the way?")
    print("it's not, the friends are as real as GTA VI, and you wasted a valuable day where you could've gone to school")