import turtle
import math

'''
Simulation Parameters
'''
RESOLUTION = 50  # Higher number gives a higher resolution, but runs slower
SIM_STEPS = 20000  # How many total steps to run
RADS_PER_STEP = (2 * math.pi) / RESOLUTION  # Don't change


''' 
Spirograph Parameters
    In reality, p < r < R
    In this simulation, feel free to play
    with values that don't conform to that!
'''
R = 400  # Radius of outer ring
r = 205  # Radius of inner cog
p = 50  # Distance between pen hole and center of inner cog


def main():
    turtle.speed(0)
    turtle.up()
    turtle.goto((R - r + p, 0.0))
    turtle.down()

    T = 0
    t = 0
    for _ in range(SIM_STEPS):
        T += RADS_PER_STEP
        t = -((R - r) / r) * T
        x_c = (R - r) * math.cos(T)
        y_c = (R - r) * math.sin(T)
        x = p * math.cos(t)
        y = p * math.sin(t)
        x = x_c + x
        y = y_c + y

        turtle.goto((x, y))

    input("Press enter to exit")


if __name__ == "__main__":
    main()
