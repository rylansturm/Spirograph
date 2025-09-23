import turtle
import math

"""
Simulation Parameters
"""
RESOLUTION = 80  # Higher number gives a higher resolution, but runs slower
SIM_STEPS = 20000  # How many total steps to run
RADS_PER_STEP = (2 * math.pi) / RESOLUTION  # Don't change
DO_COLORS = True


""" 
Spirograph Parameters
    In reality, p < r < R
    In this simulation, feel free to play
    with values that don't conform to that!
"""
R = 600  # Radius of outer ring
r = 407  # Radius of inner cog
p = 256  # Distance between pen hole and center of inner cog


def main():
    turtle.width(3)
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

        if DO_COLORS:
            # Play around with these!
            red = (1 + math.sin(x / 100)) * 0.5
            green = (1 + math.cos(y / 100)) * 0.5
            blue = (1 + math.sin((x + y) / 100)) * 0.5
            color = (red, green, blue)
            turtle.pencolor(color)
        turtle.goto((x, y))

    input("Press enter to exit")


if __name__ == "__main__":
    try:
        main()
    except (turtle.Terminator, KeyboardInterrupt):
        print("Goodbye!\n")
