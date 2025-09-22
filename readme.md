# Spirograph

I wanted to emulate a spirograph with turtle graphics.
I used the equations from [the Wikipedia page](https://en.wikipedia.org/wiki/Spirograph)
to get the function for the path.

### How to manipulate

Mainly you will want to manipulate the values `R`, `r`, and `p` which
are in the "Spirograph Parameters" section near the top of [main.py](./main.py).
They correspond to the radius of the outer ring, the radius of the
inner cog, and the distance from the pen hole to the center of the
inner cog. See what you can make!

You can also change the `RESOLUTION` parameter. This can have some
interesting effects. I don't notice much of any difference in quality
with any value above 50, but I do notice a dramatic increase in draw
time. Where things get interesting is when you decrease the resolution.
Play with it and see!