import turtle


def main():
    """DRAWS CIRCLE"""
    posi = turtle.Turtle()
    posi.speed(0)
    sc = turtle.Screen()
    sc.setup(500, 500, 0, 0)
    sc.setworldcoordinates(0,0,500,500)

    x = 0
    y = 0
    r1 = 0
    b1 = 0
    g1 = 0
    while True:
        row = input("How many circle per side? ('done' to end)")
        posi.clear()
        if row == "done":
            break
        elif row.isdecimal() and int(row) > 0: #checks if the input is valid
            row_ = int(row)
            radius= 500/(2*row_)
            x = radius
            for c in range (row_):
                for i in range(row_):
                    posi.speed(0)
                    posi.up()
                    posi.goto(x + i*radius*2, y)
                    posi.down()
                    posi.begin_fill()
                    posi.color(r1 + 1/row_*i, g1, b1)
                    posi.circle(radius)
                    posi.end_fill()
                y += radius*2
                b1 += 1/row_
            b1 = 0 # RESETS b1 TO 0
            y = 0 # RESETS Y TO 02
        else:
            print("invalid entry")
    sc.mainloop()
        
        
            
        
# def loops_si(posi, x, y, radius, r1, g1, b1, row):
#     """"""
#     for i in range (row):
#         loops_br(posi, x, y + i*radius*2, radius, r1, g1, b1 + 1/row*i, row)
#         
# def loops_go(posi, x, y, radius, r1, g1, b1):
#     """create a grid of circles, but with colors."""
#     while posiue:
#         row = input("how many circle per side? ('done' to end)")
#         posi.clear()
#         if row == "done" :
#             break
#         elif row.isdecimal(): #checks if the input is valid
#             loops_si(posi, x, y, radius, r1, g1, b1, int(row))
#         else :
#             print("invalid enposiy")
#                 
main()





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




