import turtle


def main():
    windows = turtle.Screen()
    kelvin = turtle.Turtle()

    make_square(kelvin)

    turtle.mainloop()


def make_square(kelvin):
    length = int(input('Tamaño del cuadrado: '))

    for i in range(4):
        make_line_and_turn(kelvin, 100)


def make_line_and_turn(kelvin, length):
    kelvin.forward(length)
    kelvin.left(90)


if __name__ == '__main__':
    main()