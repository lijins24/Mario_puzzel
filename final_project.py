"""
    CS 5001
    Fall 2022
    Final Project
    Puzzle Game
    Jinsheng Li
"""
import datetime
import math
import turtle
import random
import time

# length of each image
tile_length = []
# empty list to store images' file names
images, images2, images3 = [], [], []
# coordinates
coordinates2 = []

loadbutton = "Resources/loadbutton.gif"
quitbutton = "Resources/quitbutton.gif"
resetbutton = "Resources/resetbutton.gif"

screen = turtle.Screen()
screen.title("CS5001 Sliding Puzzle Game")

default_puz = ["mario.puz"]

# empty list to store function starter's output
tem_infor = []
file_names = []
pieces_count = []
thumbnail = []
title = []


def starter():
    """
        By reading the .puz file,
        retrieve all information as needed
        and store them in the empty list above
    """
    images.clear()
    images2.clear()
    images3.clear()
    tem_infor.clear()
    file_names.clear()
    pieces_count.clear()
    thumbnail.clear()
    title.clear()
    with open(default_puz[-1], mode="r") as infile:
        for i in infile:
            tem_infor.append(i)
    # get the name
    for l in range(len(tem_infor[0])):
        if tem_infor[0][l] == ' ':
            title.append(tem_infor[0][l + 1:-1])
    # get the thumbnail file name
    for q in range(len(tem_infor[3])):
        if tem_infor[3][q] == ' ':
            thumbnail.append(tem_infor[3][q + 1:-1])
    # get the tile length
    for z in range(len(tem_infor[2])):
        if tem_infor[2][z] == ' ':
            tile_length.append(tem_infor[2][z + 1:-1])
    # get how many pieces of puzzle is needed
    for p in range(len(tem_infor[1])):
        if tem_infor[1][p] == ' ':
            pieces_count.append(tem_infor[1][p + 1:-1])
    # get each puzzle pieces' file names
    for j in tem_infor[4:]:
        # remove all '\n'
        j = j.strip('\n')
        for k in range(len(j)):
            if j[k] == ' ':
                file_names.append(j[k + 1:])
    # add each puzzle pieces' file names into three empty list
    for i in range(len(file_names)):
        each_file = file_names[i]
        images.append(str(each_file))
        images2.append(str(each_file))
        images3.append(str(each_file))

    for k in images:
        print(k)

    return default_puz


def splash_screen():
    """
        display the beginning splash screen
    """
    turtle.bgpic("Resources/splash_screen.gif")
    turtle.setup(850, 900)
    time.sleep(3)
    turtle.clearscreen()


def user_data():
    """
        display the text input box to store the usernames and moves
    """
    name = turtle.textinput("CS5001 Puzzle Slide", "Your name:")
    moves = turtle.textinput("5001 Puzzle Slide - Movers",
                             "Enter the number of moves (chances) you want (5-200)?")
    moves = int(moves)
    if 5 <= moves <= 200:
        # store the data inside a txt file
        with open("leaderboard.txt", mode="a") as file:
            file.write(f"{moves}: {name}\n")
    else:
        # if the value is outside the allowed range, raise ValueError
        raise ValueError


def gaming_arena():
    """
        draw the gaming area
    """
    draw = turtle.Turtle()
    draw.speed(10)
    draw.penup()
    draw.goto(-400, 380)
    draw.pendown()
    draw.pencolor("black")
    draw.pensize(10)
    draw.forward(500)
    draw.right(90)
    draw.forward(600)
    draw.right(90)
    draw.forward(500)
    draw.right(90)
    draw.forward(600)
    draw.right(90)
    draw.hideturtle()


def scoreboard():
    """
        draw scoreboard area
    """
    draw = turtle.Turtle()
    draw.speed(10)
    draw.penup()
    draw.goto(130, 380)
    draw.pendown()
    draw.pencolor("blue")
    draw.pensize(10)
    draw.forward(270)
    draw.right(90)
    draw.forward(600)
    draw.right(90)
    draw.forward(270)
    draw.right(90)
    draw.forward(600)
    draw.right(90)
    draw.hideturtle()


def status_area():
    """
        draw the status area
    """
    draw = turtle.Turtle()
    draw.speed(10)
    draw.penup()
    draw.goto(-400, -250)
    draw.pendown()
    draw.pencolor("black")
    draw.pensize(10)
    draw.forward(800)
    draw.right(90)
    draw.forward(130)
    draw.right(90)
    draw.forward(800)
    draw.right(90)
    draw.forward(130)
    draw.right(90)
    draw.hideturtle()


def quitbutton_gif(filename):
    """
        display quitbutton image
    """
    new_pen = turtle.Turtle()
    new_pen.speed(10)
    new_pen.penup()
    new_pen.goto(330, -310)
    new_pen.pendown()
    screen.register_shape(filename)
    screen.addshape(filename)
    new_pen.shape(filename)


def loadbutton_gif(filename):
    """
        display loadbutton image
    """
    new_pen = turtle.Turtle()
    new_pen.speed(10)
    new_pen.penup()
    new_pen.goto(230, -310)
    new_pen.pendown()
    screen.register_shape(filename)
    screen.addshape(filename)
    new_pen.shape(filename)


def resetbutton_gif(filename):
    """
        display resetbutton image
    """
    new_pen = turtle.Turtle()
    new_pen.speed(10)
    new_pen.penup()
    new_pen.goto(130, -310)
    new_pen.pendown()
    screen.register_shape(filename)
    screen.addshape(filename)
    new_pen.shape(filename)


def thumbnail_gif(filename):
    """
        display thumbnail image
    """
    new_pen = turtle.Turtle()
    new_pen.speed(10)
    new_pen.penup()
    new_pen.goto(340, 350)
    new_pen.pendown()
    screen.register_shape(filename)
    screen.addshape(filename)
    new_pen.shape(filename)


def leaderboard():
    """
        Write the leaderboard title
    """
    new_pen = turtle.Turtle()
    new_pen.speed(10)
    new_pen.penup()
    new_pen.goto(210, 330)
    new_pen.color("blue")
    new_pen.pendown()
    new_pen.write("Leaders:", align="center",
                  font=("Arial", 24, "bold"))
    new_pen.hideturtle()


def username():
    """
        Write the player's names on leaderboard
    """
    new_pen = turtle.Turtle()
    new_pen.speed(10)
    # read the txt file that stores the user data
    with open("leaderboard.txt", mode="r") as infile:
        x = 150
        y = 250
        file = infile.readlines()
        tem_user = []
        for player in range(len(file)):
            each = file[player]
            for j in range(len(each)):
                if each[j] == ":":
                    tem_user.append(each[j + 1:-1])
        # write the player name inside leaderboard
        for each in tem_user[-4:]:
            new_pen.penup()
            new_pen.goto(x, y)
            new_pen.color("blue")
            new_pen.pendown()
            new_pen.write(each, align="left", font=("Arial", 24, "bold"))
            y = y - 30
    new_pen.hideturtle()


# store number of moves players want to use
tem_user_moves = []


def player_moves():
    """
        display the player moves in status area
        write the number of moves player wants to use
    """
    new_pen = turtle.Turtle()
    new_pen.speed(10)
    new_pen.penup()
    new_pen.goto(-200, -320)
    new_pen.pendown()
    with open("leaderboard.txt", mode="r") as file:
        read_file = file.readlines()
        for score in range(len(read_file)):
            each_line = read_file[score]
            for each in range(len(each_line)):
                if each_line[each] == ":":
                    tem_user_moves.append(each_line[0:each])
    # display the player moves data
    new_pen.write(f"Player Moves: {tem_user_moves[-1]}", align="center",
                  font=("Arial", 24, "bold"))
    new_pen.hideturtle()
    return tem_user_moves


def image_pieces():
    """
        construct and draw the puzzle board
        depends on the number of puzzle pieces
    """
    new_pen = turtle.Turtle()
    new_pen.color("black")
    start_x = -330
    start_y = 250
    new_pen.speed(10)
    new_pen.penup()
    new_pen.goto(start_x, start_y)
    new_pen.pendown()
    puzzle_locations = []
    start_x = -330
    start_y = 250
    # draw the puzzle board based on the number of puzzle pieces
    for i in range(int(math.sqrt(int(pieces_count[0])))):
        for j in range(int(math.sqrt(int(pieces_count[0])))):
            for h in range(4):
                puzzle_locations.append([new_pen.pos()])
                new_pen.speed(10)
                new_pen.forward(int(tile_length[0]))
                new_pen.right(90)
                new_pen.hideturtle()
            new_pen = turtle.Turtle()
            new_pen.speed(10)
            start_x += int(tile_length[0])
            new_pen.penup()
            new_pen.goto(start_x, start_y)
            new_pen.pendown()
            new_pen.hideturtle()
        new_pen = turtle.Turtle()
        new_pen.speed(10)
        start_y -= int(tile_length[0])
        start_x = -330
        new_pen.penup()
        new_pen.goto(start_x, start_y)
        new_pen.pendown()
        new_pen.hideturtle()


def coordinates():
    """
        coordinates for all four type of puzzle boards
    """
    # if the number of puzzle pieces is 4, draw a 2x2 puzzle board
    if int(pieces_count[0]) == 4:
        coordinates_2x2 = [[
            [[-330.0, 250.0], [-232.0, 250.0], [-232.0, 152.0], [-330.0, 152.0]],
            [[-232.0, 250.0], [-134.0, 250.0], [-134.0, 152.0], [-232.0, 152.0]],
        ],
            [
                [[-330.0, 152.0], [-232.0, 152.0], [-232.0, 54.0], [-330.0, 54.0]],
                [[-232.0, 152.0], [-134.0, 152.0], [-134.0, 54.0], [-232.0, 54.0]],
            ]
        ]
        new_coordinates = coordinates_2x2
        return new_coordinates
    # if the number of puzzle pieces is 9, draw a 3x3 puzzle board
    elif int(pieces_count[0]) == 9:
        coordinates_3x3 = [[
            [[-330.0, 250.0], [-232.0, 250.0], [-232.0, 152.0], [-330.0, 152.0]],
            [[-232.0, 250.0], [-134.0, 250.0], [-134.0, 152.0], [-232.0, 152.0]],
            [[-134.0, 250.0], [-36.0, 250.0], [-36.0, 152.0], [-134.0, 152.0]],
        ],
            [
                [[-330.0, 152.0], [-232.0, 152.0], [-232.0, 54.0], [-330.0, 54.0]],
                [[-232.0, 152.0], [-134.0, 152.0], [-134.0, 54.0], [-232.0, 54.0]],
                [[-134.0, 152.0], [-36.0, 152.0], [-36.0, 54.0], [-134.0, 54.0]],
            ],
            [
                [[-330.0, 54.0], [-232.0, 54.0], [-232.0, -44.0], [-330.0, -44.0]],
                [[-232.0, 54.0], [-134.0, 54.0], [-134.0, -44.0], [-232.0, -44.0]],
                [[-134.0, 54.0], [-36.0, 54.0], [-36.0, -44.0], [-134.0, -44.0]],
            ]
        ]
        new_coordinates = coordinates_3x3
        return new_coordinates
    # if the number of puzzle pieces is 16, draw a 4x4 puzzle board
    elif int(pieces_count[0]) == 16:
        coordinates_4x4 = [[
            [[-330.0, 250.0], [-232.0, 250.0], [-232.0, 152.0], [-330.0, 152.0]],
            [[-232.0, 250.0], [-134.0, 250.0], [-134.0, 152.0], [-232.0, 152.0]],
            [[-134.0, 250.0], [-36.0, 250.0], [-36.0, 152.0], [-134.0, 152.0]],
            [[-36.0, 250.0], [62.0, 250.0], [62.0, 152.0], [-36.0, 152.0]],
        ],
            [
                [[-330.0, 152.0], [-232.0, 152.0], [-232.0, 54.0], [-330.0, 54.0]],
                [[-232.0, 152.0], [-134.0, 152.0], [-134.0, 54.0], [-232.0, 54.0]],
                [[-134.0, 152.0], [-36.0, 152.0], [-36.0, 54.0], [-134.0, 54.0]],
                [[-36.0, 152.0], [62.0, 152.0], [62.0, 54.0], [-36.0, 54.0]],
            ],
            [
                [[-330.0, 54.0], [-232.0, 54.0], [-232.0, -44.0], [-330.0, -44.0]],
                [[-232.0, 54.0], [-134.0, 54.0], [-134.0, -44.0], [-232.0, -44.0]],
                [[-134.0, 54.0], [-36.0, 54.0], [-36.0, -44.0], [-134.0, -44.0]],
                [[-36.0, 54.0], [62.0, 54.0], [62.0, -44.0], [-36.0, -44.0]],
            ],
            [
                [[-330.0, -44.0], [-232.0, -44.0], [-232.0, -142.0], [-330.0, -142.0]],
                [[-232.0, -44.0], [-134.0, -44.0], [-134.0, -142.0], [-232.0, -142.0]],
                [[-134.0, -44.0], [-36.0, -44.0], [-36.0, -142.0], [-134.0, -142.0]],
                [[-36.0, -44.0], [62.0, -44.0], [62.0, -142.0], [-36.0, -142.0]]
            ]
        ]
        new_coordinates = coordinates_4x4
        return new_coordinates


def puzzle_pieces():
    """
        display all the puzzle images based on the number of puzzle pieces
    """
    global coordinates2
    coordinates2 = coordinates()
    total_len = len(images)
    for i in range(len(coordinates2)):
        for j in range(len(coordinates2[i])):
            pieces_pen = turtle.Turtle()
            pieces_pen.speed(10)
            pieces_pen.penup()
            random_piece = random.randint(0, total_len - 1)
            # calculate the mid-point of each square
            center_y = (coordinates2[i][j][0][1] - coordinates2[i][j][3][1]) / 2 + coordinates2[i][j][3][1]
            center_x = (coordinates2[i][j][0][0] - coordinates2[i][j][1][0]) / 2 + coordinates2[i][j][1][0]
            # tell turtle to go to the mid-point then draw the image
            pieces_pen.goto(center_x, center_y)
            pieces_pen.pendown()
            x = random_piece
            screen.addshape(str(images[x]))
            pieces_pen.shape(str(images[x]))
            coordinates2[i][j].append([center_x, center_y])
            coordinates2[i][j].append(images[x])
            images.remove(images[x])
            pieces_pen.penup()
            total_len -= 1
            if total_len < 0:
                break
    return coordinates2


def click(x, y):
    """
        click the puzzle pieces to shift the puzzle position
        if it's next to a blank image
        limited shifting direction depends on the location of the image
    """
    global coordinates2
    # if the puzzle board size is 4x4
    if len(coordinates2[0]) == 4:
        for i in range(len(coordinates2)):
            for j in range(len(coordinates2[i])):
                # find the position of the image and square
                if coordinates2[i][j][0][0] < x < coordinates2[i][j][1][0] \
                        and coordinates2[i][j][3][1] < y < coordinates2[i][j][0][1]:
                    image_name = coordinates2[i][j][-1]
                    # find the image that is next to the blank image
                    if image_name != f'Images/{title[0]}/blank.gif':
                        # if the clicked image is at left top corner
                        if i == 0 and j == 0:
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][
                                                                                         -1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click top middle area
                        if i == 0 and 0 < j < len(coordinates2[i]) - 1:
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][
                                                                                         -1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][
                                                                                         -1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click right top corner
                        if i == 0 and j == 3:
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][
                                                                                         -1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click left middle area
                        if 0 < i < len(coordinates2) - 1 and j == 0:
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click right middle area
                        if 0 < i < len(coordinates2) - 1 and j == 3:
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])

                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)

                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])

                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)

                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click right bottom corner
                        if i == 3 and j == 3:
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click left bottom corner
                        if i == 3 and j == 0:
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click bottom middle area
                        if i == 3 and 0 < j < len(coordinates2[i]) - 1:
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click second row middle area
                        if i == 1 and 0 < j < len(coordinates2[i]) - 1:
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click third row middle area
                        if i == 2 and 0 < j < len(coordinates2[i]) - 1:
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
    # if the puzzle board size is 3x3
    if len(coordinates2[0]) == 3:
        for i in range(len(coordinates2)):
            for j in range(len(coordinates2[i])):
                # find the position of the image and square
                if coordinates2[i][j][0][0] < x < coordinates2[i][j][1][0] \
                        and coordinates2[i][j][3][1] < y < coordinates2[i][j][0][1]:
                    image_name = coordinates2[i][j][-1]
                    # find the image that is next to the blank image
                    if image_name != f'Images/{title[0]}/blank.gif':
                        # if user click bottom middle area
                        if i == 2 and 0 < j < len(coordinates2[i]):
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click right middle area
                        if 0 < i < len(coordinates2) and j == 2:
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])

                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)

                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])

                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)

                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click left middle area
                        if 0 < i < len(coordinates2) and j == 0:
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click top middle area
                        if i == 0 and 0 < j < len(coordinates2[i]):
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][
                                                                                         -1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][
                                                                                         -1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click left top corner
                        if i == 0 and j == 0:
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][
                                                                                         -1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click right top corner
                        if i == 0 and j == 2:
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][
                                                                                         -1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click left bottom corner
                        if i == 2 and j == 0:
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click right bottom corner
                        if i == 2 and j == 2:
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
    # if the puzzle board size is 2x2
    if len(coordinates2[0]) == 2:
        for i in range(len(coordinates2)):
            for j in range(len(coordinates2[i])):
                # find the position of the image and square
                if coordinates2[i][j][0][0] < x < coordinates2[i][j][1][0] \
                        and coordinates2[i][j][3][1] < y < coordinates2[i][j][0][1]:
                    image_name = coordinates2[i][j][-1]
                    # find the image that is next to the blank image
                    if image_name != f'Images/{title[0]}/blank.gif':
                        # if user click left top corner
                        if i == 0 and j == 0:
                            print(coordinates2[i + 1][j][-1])
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][
                                                                                         -1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click right top corner
                        if i == 0 and j == 1:
                            # the clicked image could shift down to exchange spot with blank image
                            if coordinates2[i + 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i + 1][j][-1] = coordinates2[i + 1][j][-1], \
                                                                                     coordinates2[i][j][
                                                                                         -1]
                                pic1 = str(coordinates2[i + 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i + 1][j][-2][0], coordinates2[i + 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click left bottom corner
                        if i == 1 and j == 0:
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift right to exchange spot with blank image
                            if coordinates2[i][j + 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j + 1][-1] = coordinates2[i][j + 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j + 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j + 1][-2][0], coordinates2[i][j + 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                        # if user click right bottom corner
                        if i == 1 and j == 1:
                            # the clicked image could shift up to exchange spot with blank image
                            if coordinates2[i - 1][j][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i - 1][j][-1] = coordinates2[i - 1][j][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i - 1][j][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i - 1][j][-2][0], coordinates2[i - 1][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)
                            # the clicked image could shift left to exchange spot with blank image
                            if coordinates2[i][j - 1][-1] == f'Images/{title[0]}/blank.gif':
                                coordinates2[i][j][-1], coordinates2[i][j - 1][-1] = coordinates2[i][j - 1][-1], \
                                                                                     coordinates2[i][j][-1]
                                pic1 = str(coordinates2[i][j - 1][-1])
                                pic2 = str(coordinates2[i][j][-1])
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j - 1][-2][0], coordinates2[i][j - 1][-2][1])
                                curr.pendown()
                                screen.addshape(pic1)
                                curr.shape(pic1)
                                curr = turtle.Turtle()
                                curr.speed(10)
                                curr.penup()
                                curr.goto(coordinates2[i][j][-2][0], coordinates2[i][j][-2][1])
                                curr.pendown()
                                screen.addshape(pic2)
                                curr.shape(pic2)

    # to activate the reset button
    if 85 < x < 172 and -352 < y < -270:
        click_reset()
        turtle.onscreenclick(click)
    # to activate the load button
    if 185 < x < 272 and -352 < y < -270:
        click_load()
    # to activate the quit button
    if 288 < x < 372 and -340 < y < -281:
        new_pen = turtle.Turtle()
        screen.addshape("Resources/quitmsg.gif")
        new_pen.shape("Resources/quitmsg.gif")
        time.sleep(4)
        turtle.bye()


def click_reset():
    """
        reset button will reorganize the puzzle pieces in the correct order
    """
    # find the mid-point of each square
    centerx = []
    centery = []
    center = []
    for i in range(len(coordinates2)):
        for j in range(len(coordinates2[i])):
            center_y = (coordinates2[i][j][0][1] - coordinates2[i][j][3][1]) / 2 + coordinates2[i][j][3][1]
            center_x = (coordinates2[i][j][0][0] - coordinates2[i][j][1][0]) / 2 + coordinates2[i][j][1][0]
            centerx.append(center_x)
            centery.append(center_y)
    for each in range(len(centerx)):
        center.append([centerx[each], centery[each]])
    print(center)
    # draw all the puzzle pieces again in the correct order
    for k in range(len(center)):
        new_pen = turtle.Turtle()
        new_pen.penup()
        new_pen.speed(10)
        new_pen.goto(center[k][0], center[k][1])
        new_pen.pendown()
        screen.addshape(str(images2[k]))
        new_pen.shape(str(images2[k]))


def click_load():
    """
        load button will open a text input box to retrieve the file name
        rerun the corresponding functions to load the new puzzle pieces
    """
    load_puzzle = turtle.textinput("Load Puzzle", f"Enter the name of the puzzle you wish to load. Choices are:\n"
                                                  f"luigi.puz\n"
                                                  f"fifteen.puz\n"
                                                  f"mario.puz\n"
                                                  f"smiley.puz\n"
                                                  f"yoshi.puz\n")
    # change the default_puz list according to the user input
    if load_puzzle == "smiley.puz":
        default_puz.append("smiley.puz")
        screen.clear()
        starter()
        gaming_arena()
        scoreboard()
        status_area()
        quitbutton_gif(quitbutton)
        loadbutton_gif(loadbutton)
        resetbutton_gif(resetbutton)
        thumbnail_gif(thumbnail[0])
        leaderboard()
        username()
        player_moves()
        image_pieces()
        puzzle_pieces()
        coordinates()
        turtle.onscreenclick(click)
    elif load_puzzle == "luigi.puz":
        default_puz.append("luigi.puz")
        screen.clear()
        starter()
        gaming_arena()
        scoreboard()
        status_area()
        quitbutton_gif(quitbutton)
        loadbutton_gif(loadbutton)
        resetbutton_gif(resetbutton)
        thumbnail_gif(thumbnail[0])
        leaderboard()
        username()
        player_moves()
        image_pieces()
        puzzle_pieces()
        coordinates()
        turtle.onscreenclick(click)
    elif load_puzzle == "fifteen.puz":
        default_puz.append("fifteen.puz")
        screen.clear()
        starter()
        gaming_arena()
        scoreboard()
        status_area()
        quitbutton_gif(quitbutton)
        loadbutton_gif(loadbutton)
        resetbutton_gif(resetbutton)
        thumbnail_gif(thumbnail[0])
        leaderboard()
        username()
        player_moves()
        image_pieces()
        puzzle_pieces()
        coordinates()
        turtle.onscreenclick(click)
    elif load_puzzle == "yoshi.puz":
        default_puz.append("yoshi.puz")
        screen.clear()
        starter()
        gaming_arena()
        scoreboard()
        status_area()
        quitbutton_gif(quitbutton)
        loadbutton_gif(loadbutton)
        resetbutton_gif(resetbutton)
        thumbnail_gif(thumbnail[0])
        leaderboard()
        username()
        player_moves()
        image_pieces()
        puzzle_pieces()
        coordinates()
        turtle.onscreenclick(click)
    elif load_puzzle == "mario.puz":
        default_puz.append("mario.puz")
        screen.clear()
        starter()
        gaming_arena()
        scoreboard()
        status_area()
        quitbutton_gif(quitbutton)
        loadbutton_gif(loadbutton)
        resetbutton_gif(resetbutton)
        thumbnail_gif(thumbnail[0])
        leaderboard()
        username()
        player_moves()
        image_pieces()
        puzzle_pieces()
        coordinates()
        turtle.onscreenclick(click)
    # if the file name does not exist, raise an error image
    else:
        file_error_pen = turtle.Turtle()
        screen.addshape("Resources/file_error.gif")
        file_error_pen.shape("Resources/file_error.gif")
        time.sleep(4)
        file_error_pen.hideturtle()
        with open("5001_puzzle.err", mode="a") as infile:
            infile.write(f"{datetime.date.today()}:Error: file {load_puzzle} does not exist!\n")


def main():
    global default_puz
    splash_screen()
    starter()
    user_data()
    gaming_arena()
    scoreboard()
    status_area()
    quitbutton_gif(quitbutton)
    loadbutton_gif(loadbutton)
    resetbutton_gif(resetbutton)
    thumbnail_gif(thumbnail[0])
    leaderboard()
    username()
    player_moves()
    image_pieces()
    puzzle_pieces()
    coordinates()
    turtle.onscreenclick(click)
    turtle.mainloop()


if __name__ == "__main__":
    main()
