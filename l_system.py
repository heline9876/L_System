import turtle as tur


def apply_rules(axiom, rules, depth=1):
    result = axiom
    
    for _ in range(depth):
        result = "".join(rules[car] if car in rules else car for car in result)
    print(result, "\n")
    return result


def turtle_interprate(l_string, rules, line_length=5, rotate=50, number_of_iteration=3, start_point=[0, -500]):
    if start_point == []:
        start_point = [0, -500]
    result = ""
    saved_state = []
    
    tur.mode(mode="logo")
    tur.tracer(0)
    tur.screensize(10000, 10000)
    tur.bgcolor("#080808")
    
    franklin.clear()
    franklin.penup()
    franklin.pencolor("green")
    franklin.goto(start_point[0], start_point[1])
    franklin.pendown()
    
    result = apply_rules(l_string, rules, number_of_iteration)
    i = 0
    print(len(result))
    
    for car in result:
        i += 1
        if car == "[":
            state = [franklin.heading(), franklin.position()]
            saved_state.append(state)
        elif car == "]":
            state = saved_state.pop()
            franklin.setheading(state[0])
            franklin.setposition(state[1][0], state[1][1])
        elif car == "F":
            franklin.forward(line_length)
        elif car == "f":
            franklin.penup()
            franklin.forward(line_length)
            franklin.pendown()
        elif car == "+":
            franklin.lt(rotate)
        elif car == "-":
            franklin.rt(rotate)
    print(i)
    tur.mainloop()

tur.mode(mode="logo")
tur.tracer(0)
tur.bgcolor("#080808")

franklin = tur.Turtle()
franklin.hideturtle()