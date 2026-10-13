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

    enter = input("Choose (I don't ask poitely)")
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
            print("You")
    elif enter == "2":
        print("You missed the last [yellow]99[/yellow] and now need to take the [green]R4[/green], and as you do the floor breaks beneath you and now you're stuck in the bored tunnels for the M line expansion")
elif walk == "2":
    print("You get on the [yellow]99[/yellow] to Joyce")
    print("The bus goes [blue]slow[/blue], and the bus is [green]empty[/green]")
    print("You get to Production way university, and get on the 145")
    print("It catches fire from going uphill and you [red]die[/red]")
    print("The end")