import random
import turtle as t


# import colorgram

# using colorgram we have extracted colors from image
# colors = colorgram.extract("images.jpeg",30)
#
# color = []
# for i in range(30):`
#     p_color= colors[i]
#     r = p_color.rgb.r
#     g = p_color.rgb.g
#     b = p_color.rgb.b
#     rgb = (r,g,b)
#     color.append(rgb)
# print(color)


screen = t.Screen()
hist = t.Turtle()
hist.shape("arrow")
hist.speed(0)
t.colormode(255)
rgb_colors = [ (243, 230, 51), (202, 8, 34),
            (237, 228, 2), (191, 70, 25), (220, 153, 81), (35, 208, 91), (204, 11, 6), (35, 92, 176), (238, 43, 128),
            (32, 32, 155), (16, 17, 55), (85, 189, 219), (62, 9, 46), (61, 20, 10), (225, 157, 8), (202, 33, 96),
            (20, 147, 28), (14, 200, 219), (216, 135, 180), (234, 58, 36), (96, 235, 170), (82, 212, 146), (97, 74, 9),
            (236, 160, 201), (6, 36, 30), (82, 83, 210)]
hist.setheading(225)
hist.penup()
hist.forward(300)
hist.pendown()
hist.setheading(0)
stat_pos = hist.position()
for _ in range(10):
    for _ in range(10):
        hist.dot(15,random.choice(rgb_colors))
        hist.penup()
        hist.forward(50)
        p_pos = hist.pos()
    hist.goto(stat_pos[0], p_pos[1]+50)
    hist.pendown()

screen.exitonclick()
