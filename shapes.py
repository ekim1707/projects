def shape(call):
    if call == 'c':
        import turtlecircle.py
    elif call == 's':
        import turtlesquare.py
    elif call == 'p':
        import turtlepentagon.py
    elif call == 'st':
        import turtlestar.py

answer = input('Would you like a circle ("c"), square ("s"), pentagon ("p"), or star("st")? ')
newanswer = str(answer).lower()
shape(newanswer)