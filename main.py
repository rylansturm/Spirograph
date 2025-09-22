import turtle
import math

STEPS_PER_2PI = 100
RADS_PER_STEP = (2 * math.pi) / STEPS_PER_2PI
SIM_STEPS = 20000

R = 400
r = 205
p = 50


def main():
    turtle.speed(0)
    turtle.up()
    turtle.goto((R - r + p, 0.0))
    turtle.down()

    T = 0
    t = 0
    for _ in range(SIM_STEPS):
        T = T + RADS_PER_STEP
        t = -((R - r) / r) * T
        x_c = (R - r) * math.cos(T)
        y_c = (R - r) * math.sin(T)
        x = p * math.cos(t)
        y = p * math.sin(t)
        x = x_c + x
        y = y_c + y

        turtle.goto((x, y))

    input()


if __name__ == "__main__":
    main()
