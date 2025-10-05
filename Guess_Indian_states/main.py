import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India states game")
image_path = "india_map_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)

#TO know the x and y co-ordinates of the screen
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()


# guessed_states = []
# state_data = pd.read_csv("states_data.csv")
# states = state_data["State"].to_list()
#
# while len(guessed_states)<32:
#
#     answer = screen.textinput(title=f"{len(guessed_states)}/34 are correct.", prompt="Enter State Name. Type exit to see the missed states").upper()
#     print(answer)
#
#     if answer == 'EXIT':
#         break
#     if answer in states:
#         if answer not in guessed_states:
#             guessed_states.append(answer)
#             row = state_data[state_data["State"]==answer]
#             trt = turtle.Turtle()
#             trt.hideturtle()
#             trt.penup()
#             trt.goto(int(row['x'].item()), int(row['y'].item()))
#             trt.write(answer)
#
# states_missed = list(set(states)-set(guessed_states))
#
# states_to_learn = pd.DataFrame(states_missed)
# states_to_learn.to_csv("States_to_learn.csv")