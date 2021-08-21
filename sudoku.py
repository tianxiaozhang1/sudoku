import pygame, sys, random

def logo():
    #Display the logo
    BCK1 = RUYAOQING      

    pygame.draw.rect(screen, BCK1, pygame.Rect(20, 20, 300, 68))
    #S
    pygame.draw.rect(screen, BOARD, pygame.Rect(20+10+48*0, 20+10, 40, 48))
    pygame.draw.rect(screen, BCK1, pygame.Rect(20+10+48*0+10, 20+10+10, 30, 8))
    pygame.draw.rect(screen, BCK1, pygame.Rect(20+10+48*0, 20+10+28, 30, 10))
    #U
    pygame.draw.rect(screen, BOARD, pygame.Rect(20+10+48*1, 20+10, 40, 48))
    pygame.draw.rect(screen, BCK1, pygame.Rect(20+10+48*1+10, 20+10, 20, 38))
    #D
    pygame.draw.rect(screen, BOARD, pygame.Rect(20+10+48*2, 20+10, 40, 48))
    pygame.draw.rect(screen, BCK1, pygame.Rect(20+10+48*2+30, 20+10, 10, 10))
    pygame.draw.rect(screen, BCK1, pygame.Rect(20+10+48*2+30, 20+10+38, 10, 10))
    pygame.draw.rect(screen, BCK1, pygame.Rect(20+10+48*2+10, 20+10+10, 20, 28))
    #O
    pygame.draw.rect(screen, BOARD, pygame.Rect(20+10+48*3, 20+10, 40, 48))
    pygame.draw.rect(screen, BCK1, pygame.Rect(20+10+48*3+10, 20+10+10, 20, 28))
    #K
    pygame.draw.rect(screen, BOARD, pygame.Rect(20+10+48*4, 20+10, 10, 48))
    pygame.draw.rect(screen, BOARD, pygame.Rect(20+10+48*4+30, 20+10, 10, 10))
    pygame.draw.rect(screen, BOARD, pygame.Rect(20+10+48*4+20, 20+10+10, 10, 8))
    pygame.draw.rect(screen, BOARD, pygame.Rect(20+10+48*4+10, 20+10+18, 10, 10))
    pygame.draw.rect(screen, BOARD, pygame.Rect(20+10+48*4+20, 20+10+28, 10, 10))
    pygame.draw.rect(screen, BOARD, pygame.Rect(20+10+48*4+30, 20+10+38, 10, 10))
    #U
    pygame.draw.rect(screen, BOARD, pygame.Rect(20+10+48*5, 20+10, 40, 48))
    pygame.draw.rect(screen, BCK1, pygame.Rect(20+10+48*5+10, 20+10, 20, 38))

def draw_numbers(number, sqx, sqy, pad_num = False, pad_hover = False, user_colour = False, victory_colour = False):

    #Bottom right corner number pad
    if pad_num == True:
        number_colour = BOARD
        if len(puzzle) > 0:
            SQ_COLOUR = RUYAOQING
        else:
            SQ_COLOUR = BOARD1

        i2 = number - 1

        x_pos = 977+i2%3*100
        y_pos = 735+i2//3*100

    #The highlighted number on the pad while mouse is over
    elif pad_hover == True:
        if len(puzzle) > 0:
            number_colour = RUYAOQING
        else:
            number_colour = BOARD1
        if len(puzzle) > 0:
            SQ_COLOUR = BOARD
        else:
            SQ_COLOUR = BOARD1

        i2 = number - 1
        x_pos = 977+i2%3*100
        y_pos = 735+i2//3*100

    #Regular gameplay numbers
    else:
        number_colour = GREY
        SQ_x = sqy%2 + sqx%2
        if SQ_x%2 == 0:
            SQ_COLOUR = BOARD2
        else:
            SQ_COLOUR = BOARD1
        x_pos = 45+sqx*100+(sqx//3)*8
        y_pos = 119+sqy*100+(sqy//3)*8

    if user_colour == True:
        number_colour = RUYAOQING
    
    if victory_colour == True:
        number_colour = RED

    #Displaying numbers 1 to 9
    if number == 1:
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos, y_pos, 50, 58))
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos+21, y_pos, 12, 12))
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos+7, y_pos+10, 26, 12))
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos+17, y_pos+22, 16, 24))
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos, y_pos+46, 50, 12))

    if number == 2:
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos, y_pos, 50, 58))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos, y_pos+12, 38, 10))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos+12, y_pos+34, 38, 12))
    
    if number == 3:
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos, y_pos, 50, 58))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos, y_pos+12, 38, 10))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos, y_pos+22, 12, 12))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos, y_pos+34, 38, 12))

    if number == 4:
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos, y_pos, 50, 58))
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos+36, y_pos, 14, 58))
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos+8, y_pos, 14, 22))
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos, y_pos+22, 36, 12))

    if number == 5:
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos, y_pos, 50, 58))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos+12, y_pos+12, 38, 10))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos, y_pos+34, 38, 12))

    if number == 6:
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos, y_pos, 50, 58))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos+12, y_pos+12, 38, 10))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos+12, y_pos+34, 26, 12))
    
    if number == 7:
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos, y_pos, 50, 58))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos, y_pos+12, 38, 46))

    if number == 8:
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos, y_pos, 50, 58))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos+12, y_pos+12, 26, 10))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos+12, y_pos+34, 26, 12))
    
    if number == 9:
        pygame.draw.rect(screen, number_colour, pygame.Rect(x_pos, y_pos, 50, 58))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos+12, y_pos+12, 26, 10))
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos, y_pos+34, 38, 12))

def undo_hover():
    #Undo button

    if 956 <= pygame.mouse.get_pos()[0] <= 956+292 and 412 <= pygame.mouse.get_pos()[1] <= 412+66:
        if dragging == False:
            if len(game_log) > 0:
                B5C = YELLOW_HI
                B5T = BOARD
            else:
                B5C = BOARD1
                B5T = BOARD

    else:
        if len(game_log) > 0:
            B5C = BOARD1
            B5T = YELLOW
        else:
            B5C = BOARD1
            B5T = BOARD

    if len(puzzle) == 0:
        B5C = YELLOW
        B5T = BOARD

    if dragging == True:
        if len(game_log) > 0:
            B5C = BOARD1
            B5T = YELLOW
        else:
            B5C = BOARD1
            B5T = BOARD

    if game_won == True:
        B5C = BOARD1
        B5T = BOARD

    pygame.draw.rect(screen, B5C, pygame.Rect(960-4, 412+72*0, 292, 66))
    #U
    pygame.draw.rect(screen, B5T, pygame.Rect(960-4+160, 412+72*0+18, 24, 30))
    pygame.draw.rect(screen, B5C, pygame.Rect(960-4+160+6, 412+72*0+18, 12, 24))
    #N
    pygame.draw.rect(screen, B5T, pygame.Rect(960-4+160+30*1, 412+72*0+18, 24, 30))
    pygame.draw.rect(screen, B5C, pygame.Rect(960-4+160+30*1+6, 412+72*0+18+6, 12, 24))
    #D
    pygame.draw.rect(screen, B5T, pygame.Rect(960-4+160+30*2, 412+72*0+18, 24, 30))
    pygame.draw.rect(screen, B5C, pygame.Rect(960-4+160+30*2+6, 412+72*0+18+6, 12, 18))
    pygame.draw.rect(screen, B5C, pygame.Rect(960-4+160+30*2+18, 412+72*0+18, 6, 6))
    pygame.draw.rect(screen, B5C, pygame.Rect(960-4+160+30*2+18, 412+72*0+18+24, 6, 6))
    #O
    pygame.draw.rect(screen, B5T, pygame.Rect(960-4+160+30*3, 412+72*0+18, 24, 30))
    pygame.draw.rect(screen, B5C, pygame.Rect(960-4+160+30*3+6, 412+72*0+18+6, 12, 18))

def restart_hover():
    #Restart button

    if 956 <= pygame.mouse.get_pos()[0] <= 956+292 and 412+72 <= pygame.mouse.get_pos()[1] <= 412+72+66:
        if dragging == False:
            if len(puzzle) > 0:
                B6C = ORANGE_HI
                B6T = BOARD
            else:
                B6C = ORANGE
                B6T = BOARD

    else:
        if len(puzzle) > 0:
            B6C = BOARD1
            B6T = ORANGE
        else:
            B6C = ORANGE
            B6T = BOARD

    if dragging == True:
        B6C = BOARD1
        B6T = ORANGE    

    pygame.draw.rect(screen, B6C, pygame.Rect(960-4, 412+72*1, 292, 66))
    #R
    pygame.draw.rect(screen, B6T, pygame.Rect(960-4+160-30*3, 412+72*1+18, 24, 30))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*3+18, 412+72*1+18, 6, 6))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*3+18, 412+72*1+18+11, 6, 6))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*3+6, 412+72*1+18+6, 12, 5))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*3+6, 412+72*1+18+6+11, 12, 13))
    #E
    pygame.draw.rect(screen, B6T, pygame.Rect(960-4+160-30*2, 412+72*1+18, 24, 30))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*2+18, 412+72*1+18+11, 6, 6))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*2+6, 412+72*1+18+6, 18, 5))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*2+6, 412+72*1+18+6+11, 18, 7))
    #S
    pygame.draw.rect(screen, B6T, pygame.Rect(960-4+160-30*1, 412+72*1+18, 24, 30))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*1, 412+72*1+18, 6, 6))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*1+6, 412+72*1+18+6, 18, 5))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*1, 412+72*1+18+11, 6, 6))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*1+18, 412+72*1+18+11, 6, 6))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*1, 412+72*1+18+17, 18, 7))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160-30*1+18, 412+72*1+18+24, 6, 6))
    #T
    pygame.draw.rect(screen, B6T, pygame.Rect(960-4+160, 412+72*1+18, 24, 6))
    pygame.draw.rect(screen, B6T, pygame.Rect(960-4+160+9, 412+72*1+24, 6, 24))
    #A
    pygame.draw.rect(screen, B6T, pygame.Rect(960-4+160+30, 412+72*1+18, 24, 30))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160+30, 412+72*1+18, 6, 6))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160+30+18, 412+72*1+18, 6, 6))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160+30+6, 412+72*1+18+6, 12, 5))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160+30+6, 412+72*1+18+6+11, 12, 13))
    #R
    pygame.draw.rect(screen, B6T, pygame.Rect(960-4+160+30*2, 412+72*1+18, 24, 30))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160+30*2+18, 412+72*1+18, 6, 6))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160+30*2+18, 412+72*1+18+11, 6, 5))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160+30*2+6, 412+72*1+18+6, 12, 5))
    pygame.draw.rect(screen, B6C, pygame.Rect(960-4+160+30*2+6, 412+72*1+18+6+11, 12, 13))
    #T
    pygame.draw.rect(screen, B6T, pygame.Rect(960-4+160+30*3, 412+72*1+18, 24, 6))
    pygame.draw.rect(screen, B6T, pygame.Rect(960-4+160+30*3+9, 412+72*1+24, 6, 24))

def pause_hover():
    #Pause button

    B7C = GREEN
    B7T = BOARD

    if 956 <= pygame.mouse.get_pos()[0] <= 956+292 and 412+72*2+3 <= pygame.mouse.get_pos()[1] <= 412+72*2+66+3:
        if dragging == False:
            if len(puzzle) > 0:
                if game_on == True:
                    B7C = GREEN_HI
                    B7T = BOARD
                else:
                    B7C = PINK_HI
                    B7T = BOARD

    else:
        if len(puzzle) > 0:
            if game_on == True:
                B7C = BOARD1
                B7T = GREEN
            else:
                B7C = BOARD1
                B7T = PINK

    if dragging == True:
        B7C = BOARD1
        B7T = GREEN

    if game_won == True:
        B7C = BOARD1
        B7T = BOARD

    pygame.draw.rect(screen, B7C, pygame.Rect(960-4, 412+72*2, 292, 66))

    if game_on == True or len(puzzle) == 0:
        #P
        pygame.draw.rect(screen, B7T, pygame.Rect(960-4+160-30, 412+72*2+18, 24, 30))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160-30+6, 412+72*2+18+6, 12, 5))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160-30+6, 412+72*2+18+6+11, 18, 13))
        #A
        pygame.draw.rect(screen, B7T, pygame.Rect(960-4+160, 412+72*2+18, 24, 30))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160, 412+72*2+18, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+18, 412+72*2+18, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+6, 412+72*2+18+6, 12, 5))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+6, 412+72*2+18+6+11, 12, 13))
        #U
        pygame.draw.rect(screen, B7T, pygame.Rect(960-4+160+30, 412+72*2+18, 24, 30))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+30+6, 412+72*2+18, 12, 24))
        #S
        pygame.draw.rect(screen, B7T, pygame.Rect(960-4+160+30*2, 412+72*2+18, 24, 30))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+30*2, 412+72*2+18, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+30*2+6, 412+72*2+18+6, 18, 5))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+30*2, 412+72*2+18+11, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+30*2+18, 412+72*2+18+11, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+30*2, 412+72*2+18+17, 18, 7))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+30*2+18, 412+72*2+18+24, 6, 6))
        #E
        pygame.draw.rect(screen, B7T, pygame.Rect(960-4+160+30*3, 412+72*2+18, 24, 30))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+30*3+18, 412+72*2+18+11, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+30*3+6, 412+72*2+18+6, 18, 5))
        pygame.draw.rect(screen, B7C, pygame.Rect(960-4+160+30*3+6, 412+72*2+18+6+11, 18, 7))
    else:
        #R
        pygame.draw.rect(screen, B7T, pygame.Rect(1146-30*3, 412+72*2+18, 24, 30))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*3+18, 412+72*2+18, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*3+18, 412+72*2+18+11, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*3+6, 412+72*2+18+6, 12, 5))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*3+6, 412+72*2+18+6+11, 12, 13))
        #E
        pygame.draw.rect(screen, B7T, pygame.Rect(1146-30*2, 412+72*2+18, 24, 30))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*2+18, 412+72*2+18+11, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*2+6, 412+72*2+18+6, 18, 5))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*2+6, 412+72*2+18+6+11, 18, 7))
        #S
        pygame.draw.rect(screen, B7T, pygame.Rect(1146-30*1, 412+72*2+18, 24, 30))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*1, 412+72*2+18, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*1+6, 412+72*2+18+6, 18, 5))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*1, 412+72*2+18+11, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*1+18, 412+72*2+18+11, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*1, 412+72*2+18+17, 18, 7))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146-30*1+18, 412+72*2+18+24, 6, 6))
        #U
        pygame.draw.rect(screen, B7T, pygame.Rect(1146, 412+72*2+18, 24, 30))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146+6, 412+72*2+18, 12, 24))
        #M
        pygame.draw.rect(screen, B7T, pygame.Rect(1146+30*1, 412+72*2+18, 24, 30))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146+30*1+6, 412+72*2+18+6, 3, 24))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146+30*1+15, 412+72*2+18+6, 3, 24))
        #E
        pygame.draw.rect(screen, B7T, pygame.Rect(1146+30*2, 412+72*2+18, 24, 30))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146+30*2+18, 412+72*2+18+11, 6, 6))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146+30*2+6, 412+72*2+18+6, 18, 5))
        pygame.draw.rect(screen, B7C, pygame.Rect(1146+30*2+6, 412+72*2+18+6+11, 18, 7))

def show_clock_hover():
    #Show clock button
    
    B8C = BLUE
    B8T = BOARD

    if 956 <= pygame.mouse.get_pos()[0] <= 956+292 and 412+72*3 <= pygame.mouse.get_pos()[1] <= 412+72*3+66+3:
        if dragging == False:
            if len(puzzle) > 0:
                B8C = BLUE_HI
                B8T = BOARD
    else:
        if show_clock == True:
            if len(puzzle) == 0:
                B8C = BLUE
                B8T = BOARD
            elif len(puzzle) > 0 == True:
                B8C = BLUE
                B8T = BOARD
            else:
                B8C = BOARD1
                B8T = BLUE  
        else:
            B8C = BOARD1
            B8T = BOARD
    
    if dragging == True:
        if show_clock == True:
            B8C = BOARD1
            B8T = BLUE
        else:
            B8C = BOARD1
            B8T = BOARD

    if game_won == True:
        B8C = BOARD1
        B8T = BOARD

    pygame.draw.rect(screen, B8C, pygame.Rect(960-4, 412+72*3, 292, 72))
    #S
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*0+6, 414+72*3+9, 18, 4))
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*0, 414+72*3+9+4, 6, 4))
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*0+6, 414+72*3+9+8, 12, 5))
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*0+18, 414+72*3+9+13, 6, 5))
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*0, 414+72*3+9+18, 18, 4))
    #H
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+30*1+160, 414+72*3+9, 24, 22))
    pygame.draw.rect(screen, B8C, pygame.Rect(960-4+30*1+160+6, 414+72*3+9, 12, 8))
    pygame.draw.rect(screen, B8C, pygame.Rect(960-4+30*1+160+6, 414+72*3+9+13, 12, 10))
    #O
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*2, 414+72*3+9, 24, 22))
    pygame.draw.rect(screen, B8C, pygame.Rect(960-4+160+30*2+6, 414+72*3+9+4, 12, 14))
    #W
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*3, 414+72*3+9, 24, 22))
    pygame.draw.rect(screen, B8C, pygame.Rect(960-4+160+30*3+6, 414+72*3+9, 3, 18))
    pygame.draw.rect(screen, B8C, pygame.Rect(960-4+160+30*3+15, 414+72*3+9, 3, 18))
    pygame.draw.rect(screen, B8C, pygame.Rect(960-4+160+30*3, 414+72*3+9+18, 6, 4))
    pygame.draw.rect(screen, B8C, pygame.Rect(960-4+160+30*3+18, 414+72*3+9+18, 6, 4))
    #C
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160-30*1, 411+72*3+40, 24, 22))
    pygame.draw.rect(screen, B8C, pygame.Rect(960-4+160-30*1+6, 411+72*3+40+4, 18, 14))
    #L
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160-30*0, 411+72*3+40, 24, 22))
    pygame.draw.rect(screen, B8C, pygame.Rect(960-4+160-30*0+6, 411+72*3+40, 18, 18))
    #O
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*1, 411+72*3+40, 24, 22))
    pygame.draw.rect(screen, B8C, pygame.Rect(960-4+160+30*1+6, 411+72*3+40+4, 12, 14))
    #C
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*2, 411+72*3+40, 24, 22))
    pygame.draw.rect(screen, B8C, pygame.Rect(960-4+160+30*2+6, 411+72*3+40+4, 18, 14))
    #K
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*3, 411+72*3+40, 6, 22))
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*3+6, 411+72*3+40+8, 6, 5))
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*3+12, 411+72*3+40+4, 6, 4))
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*3+18, 411+72*3+40, 6, 4))
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*3+12, 411+72*3+40+13, 6, 5))
    pygame.draw.rect(screen, B8T, pygame.Rect(960-4+160+30*3+18, 411+72*3+40+18, 6, 4))

def new_game_switch(new_game_on):
    #Switched on when mouse is over one of the difficulties
    
    if new_game_on == True:
        mouse_pos = (pygame.mouse.get_pos()[1]-104)//72
        if mouse_pos < 0:
            mouse_pos = 0
        if mouse_pos > 3:
            mouse_pos = 3
        B0T = GREY_SET[mouse_pos]
    else:
        B0T = BOARD

    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4, 24-4, 292, 68))
    #N
    pygame.draw.rect(screen, B0T, pygame.Rect(960-4-30*4+18+160, 101-80+18, 24, 30))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4-30*4+18+160+6, 101-80+18+6, 12, 24))
    #E
    pygame.draw.rect(screen, B0T, pygame.Rect(960-4-30*3+18+160, 101-80+18, 24, 30))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4-30*3+18+160+18, 101-80+18+11, 6, 6))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4-30*3+18+160+6, 101-80+18+6, 18, 5))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4-30*3+18+160+6, 101-80+18+6+11, 18, 7))
    #W
    pygame.draw.rect(screen, B0T, pygame.Rect(960-4+160-30*2+18, 101-80*1+18, 24, 30))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+160-30*2+18+6, 101-80*1+18, 3, 24))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+160-30*2+18+15, 101-80*1+18, 3, 24))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+160-30*2+18, 101-80*1+18+24, 6, 6))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+160-30*2+18+18, 101-80*1+18+24, 6, 6))

    #G
    pygame.draw.rect(screen, B0T, pygame.Rect(960-4+160, 101-80+18, 24, 30))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+160+6, 101-80+18+6, 18, 18))
    pygame.draw.rect(screen, B0T, pygame.Rect(960-4+160+18, 101-80+18+11, 6, 13))
    pygame.draw.rect(screen, B0T, pygame.Rect(960-4+160+12, 101-80+18+11, 6, 6))
    #A
    pygame.draw.rect(screen, B0T, pygame.Rect(960-4+160+30*1, 101-80+18, 24, 30))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+160+30*1, 101-80+18, 6, 6))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+160+30*1+18, 101-80+18, 6, 6))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+160+30*1+6, 101-80+18+6, 12, 5))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+160+30*1+6, 101-80+18+17, 12, 13))
    #M
    pygame.draw.rect(screen, B0T, pygame.Rect(960-4+160+30*2, 101-80*1+18, 24, 30))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+160+30*2+6, 101-80*1+18+6, 3, 24))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+160+30*2+15, 101-80*1+18+6, 3, 24))
    #E
    pygame.draw.rect(screen, B0T, pygame.Rect(960-4+30*3+160, 101-80+18, 24, 30))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+30*3+160+18, 101-80+18+11, 6, 6))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+30*3+160+6, 101-80+18+6, 18, 5))
    pygame.draw.rect(screen, BOARD1, pygame.Rect(960-4+30*3+160+6, 101-80+18+6+11, 18, 7))

def easy_hover():
    #Easy button

    if 956 <= pygame.mouse.get_pos()[0] <= 956+292 and 104 <= pygame.mouse.get_pos()[1] <= 104+66:
        if dragging == False:
            B1C = GREY1_HI
            B1T = BOARD
            new_game_switch(True)
    else:
        if len(puzzle) > 0:
            B1C = BOARD1
            B1T = BOARD
        else:            
            B1C = GREY1
            B1T = BOARD

    if dragging == True:
        B1C = BOARD1
        B1T = BOARD

    pygame.draw.rect(screen, B1C, pygame.Rect(960-4, 104, 292, 66))
    #E
    pygame.draw.rect(screen, B1T, pygame.Rect(960-4+160, 104+18, 24, 30))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+18, 104+18+11, 6, 6))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+6, 104+18+6, 18, 5))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+6, 104+18+6+11, 18, 7))
    #A
    pygame.draw.rect(screen, B1T, pygame.Rect(960-4+160+30*1, 104+18, 24, 30))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*1, 104+18, 6, 6))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*1+18, 104+18, 6, 6))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*1+6, 104+18+6, 12, 5))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*1+6, 104+18+17, 12, 13))
    #S
    pygame.draw.rect(screen, B1T, pygame.Rect(960-4+160+30*2, 104+18, 24, 30))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*2, 104+18, 6, 6))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*2+6, 104+18+6, 18, 5))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*2, 104+18+11, 6, 6))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*2+18, 104+18+11, 6, 6))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*2, 104+18+17, 18, 7))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*2+18, 104+18+24, 6, 6))
    #Y
    pygame.draw.rect(screen, B1T, pygame.Rect(960-4+160+30*3, 104+18, 24, 30))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*3+6, 104+18, 12, 11))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*3, 104+18+17, 9, 13))
    pygame.draw.rect(screen, B1C, pygame.Rect(960-4+160+30*3+15, 104+18+17, 9, 13))

def medium_hover():
    #Medium button

    if 956 <= pygame.mouse.get_pos()[0] <= 956+292 and 104+74 <= pygame.mouse.get_pos()[1] <= 104+74+66:
        if dragging == False:
            B2C = GREY2_HI
            B2T = BOARD
            new_game_switch(True)
    else:
        if len(puzzle) > 0:
            B2C = BOARD1
            B2T = BOARD
        else:            
            B2C = GREY2
            B2T = BOARD
    
    if dragging == True:
        B2C = BOARD1
        B2T = BOARD

    pygame.draw.rect(screen, B2C, pygame.Rect(1302-4-16+4-330, 104+74, 292, 66))
    #M
    pygame.draw.rect(screen, B2T, pygame.Rect(960-4+160-30*2+18, 104+74*1+18, 24, 30))
    pygame.draw.rect(screen, B2C, pygame.Rect(960-4+160-30*2+6+18, 104+74*1+18+6, 3, 24))
    pygame.draw.rect(screen, B2C, pygame.Rect(960-4+160-30*2+15+18, 104+74*1+18+6, 3, 24))
    #E
    pygame.draw.rect(screen, B2T, pygame.Rect(960-4+160-30*1+18, 104+74*1+18, 24, 30))
    pygame.draw.rect(screen, B2C, pygame.Rect(960-4+160-30*1+18+18, 104+74*1+18+11, 6, 6))
    pygame.draw.rect(screen, B2C, pygame.Rect(960-4+160-30*1+18+6, 104+74*1+18+6, 18, 5))
    pygame.draw.rect(screen, B2C, pygame.Rect(960-4+160-30*1+18+6, 104+74*1+18+6+11, 18, 7))
    #D
    pygame.draw.rect(screen, B2T, pygame.Rect(960-4+160+18, 104+74*1+18, 24, 30))
    pygame.draw.rect(screen, B2C, pygame.Rect(960-4+160+18+18, 104+74*1+18, 6, 6))
    pygame.draw.rect(screen, B2C, pygame.Rect(960-4+160+18+18, 104+74*1+18+24, 6, 6))
    pygame.draw.rect(screen, B2C, pygame.Rect(960-4+160+18+6, 104+74*1+18+6, 12, 18))
    #I
    pygame.draw.rect(screen, B2T, pygame.Rect(960-4+160+30*1+18, 104+74*1+18, 6, 30))
    #U
    pygame.draw.rect(screen, B2T, pygame.Rect(960-4+160+30*2, 104+74*1+18, 24, 30))
    pygame.draw.rect(screen, B2C, pygame.Rect(960-4+160+30*2+6, 104+74*1+18, 12, 24))
    #M
    pygame.draw.rect(screen, B2T, pygame.Rect(960-4+160+30*3, 104+74*1+18, 24, 30))
    pygame.draw.rect(screen, B2C, pygame.Rect(960-4+160+30*3+6, 104+74*1+18+6, 3, 24))
    pygame.draw.rect(screen, B2C, pygame.Rect(960-4+160+30*3+15, 104+74*1+18+6, 3, 24))

def hard_hover():
    #Hard button

    if 956 <= pygame.mouse.get_pos()[0] <= 956+292 and 104+74*2 <= pygame.mouse.get_pos()[1] <= 104+74*2+66:
        if dragging == False:
            B3C = GREY3_HI
            B3T = BOARD
            new_game_switch(True)
    else:
        if len(puzzle) > 0:
            B3C = BOARD1
            B3T = BOARD
        else:            
            B3C = GREY3
            B3T = BOARD

    if dragging == True:
        B3C = BOARD1
        B3T = BOARD

    pygame.draw.rect(screen, B3C, pygame.Rect(1302-4-16+4-330, 104+74*2, 292, 66))
    #H
    pygame.draw.rect(screen, B3T, pygame.Rect(960-4+160, 104+74*2+18, 24, 30))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+6, 104+74*2+18, 12, 11))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+6, 104+74*2+18+17, 12, 13))
    #A
    pygame.draw.rect(screen, B3T, pygame.Rect(960-4+160+30*1, 104+74*2+18, 24, 30))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+30*1, 104+74*2+18, 6, 6))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+30*1+18, 104+74*2+18, 6, 6))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+30*1+6, 104+74*2+18+6, 12, 5))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+30*1+6, 104+74*2+18+17, 12, 13))
    #R
    pygame.draw.rect(screen, B3T, pygame.Rect(960-4+160+30*2, 104+74*2+18, 24, 30))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+30*2+18, 104+74*2+18, 6, 6))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+30*2+18, 104+74*2+18+11, 6, 6))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+30*2+6, 104+74*2+18+6, 12, 5))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+30*2+6, 104+74*2+18+6+11, 12, 13))
    #D
    pygame.draw.rect(screen, B3T, pygame.Rect(960-4+160+30*3, 104+74*2+18, 24, 30))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+30*3+18, 104+74*2+18, 6, 6))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+30*3+18, 104+74*2+18+24, 6, 6))
    pygame.draw.rect(screen, B3C, pygame.Rect(960-4+160+30*3+6, 104+74*2+18+6, 12, 18))

def expert_hover():
    #Expert button
    if 956 <= pygame.mouse.get_pos()[0] <= 956+292 and 104+74*3 <= pygame.mouse.get_pos()[1] <= 104+74*3+66:
        if dragging == False:
            B4C = GREY4_HI
            B4T = BOARD
            new_game_switch(True)
    else:
        if len(puzzle) > 0:
            B4C = BOARD1
            B4T = BOARD
        else:            
            B4C = GREY4
            B4T = BOARD
        
    if dragging == True:
        B4C = BOARD1
        B4T = BOARD

    pygame.draw.rect(screen, B4C, pygame.Rect(1302-4-16+4-330, 104+74*3, 292, 66))
    #E
    pygame.draw.rect(screen, B4T, pygame.Rect(960-4+160-30*2, 104+74*3+18, 24, 30))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160-30*2+18, 104+74*3+18+11, 6, 6))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160-30*2+6, 104+74*3+18+6, 18, 5))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160-30*2+6, 104+74*3+18+6+11, 18, 7))
    #X
    pygame.draw.rect(screen, B4T, pygame.Rect(960-4+160-30*1, 104+74*3+18, 6, 11))
    pygame.draw.rect(screen, B4T, pygame.Rect(960-4+160-30*1+18, 104+74*3+18, 6, 11))
    pygame.draw.rect(screen, B4T, pygame.Rect(960-4+160-30*1+6, 104+74*3+18+11, 12, 6))
    pygame.draw.rect(screen, B4T, pygame.Rect(960-4+160-30*1, 104+74*3+18+17, 6, 13))
    pygame.draw.rect(screen, B4T, pygame.Rect(960-4+160-30*1+18, 104+74*3+18+17, 6, 13))
    #P
    pygame.draw.rect(screen, B4T, pygame.Rect(960-4+160, 104+74*3+18, 24, 30))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160+18, 104+74*3+18, 6, 6))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160+6, 104+74*3+18+6, 12, 5))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160+6, 104+74*3+18+6+11, 18, 13))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160+18, 104+74*3+18+11, 6, 6))
    #E
    pygame.draw.rect(screen, B4T, pygame.Rect(960-4+160+30*1, 104+74*3+18, 24, 30))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160+30*1+18, 104+74*3+18+11, 6, 6))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160+30*1+6, 104+74*3+18+6, 18, 5))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160+30*1+6, 104+74*3+18+6+11, 18, 7))
    #R
    pygame.draw.rect(screen, B4T, pygame.Rect(960-4+160+30*2, 104+74*3+18, 24, 30))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160+30*2+18, 104+74*3+18, 6, 6))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160+30*2+18, 104+74*3+18+11, 6, 6))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160+30*2+6, 104+74*3+18+6, 12, 5))
    pygame.draw.rect(screen, B4C, pygame.Rect(960-4+160+30*2+6, 104+74*3+18+6+11, 12, 13))
    #T
    pygame.draw.rect(screen, B4T, pygame.Rect(960-4+160+30*3, 104+74*3+18, 24, 6))
    pygame.draw.rect(screen, B4T, pygame.Rect(960-4+160+30*3+9, 104+74*3+24, 6, 24))

def mouse_to_coordinates(mouse_pos):
    #Converts mouse position to the location on the puzzle

    mouse_x = mouse_pos[0] - 20
    mouse_y = mouse_pos[1] - 98
    if mouse_x > 328:
        mouse_x -= 8 * (mouse_x//320)
    if mouse_y > 406:
        mouse_y -= 8 * (mouse_y//320)
    
    mouse_x = mouse_x//100
    mouse_y = mouse_y//100

    return mouse_x, mouse_y

def board_hover(mouse_pos, just_clicked, hovering = False, clicking = False, unclicking = False, dragging = False):
    #Any square/number not on the original puzzle will be highlighted, indicating it's enter-able
    #A darker border when clicked

    xy = mouse_to_coordinates(mouse_pos)
    mouse_x = xy[0]
    mouse_y = xy[1]

    x_pos = mouse_x * 100 + 20
    if mouse_x >= 3:
        x_pos += 8 * (mouse_x//3)
    y_pos = mouse_y * 100 + 98
    if mouse_y >= 3:
        y_pos += 8 * (mouse_y//3)

    SQ_x = mouse_x%2 + mouse_y%2
    if SQ_x%2 == 0:
        SQ_COLOUR = BOARD2
    else:
        SQ_COLOUR = BOARD1

    if game_on == True:

        clear_board(hover_clear = True)

        if dragging == False and backup_puzzle[mouse_y][mouse_x] == -1:
            
            if hovering == True:
                if len(just_clicked) > 0 and mouse_x == just_clicked[0] and mouse_y == just_clicked[1]:
                    pass
                else:
                    pygame.draw.rect(screen, RUYAOQING_LT, pygame.Rect(x_pos, y_pos, 100, 100)) 
                    pygame.draw.rect(screen, HILIGHT_OUT, pygame.Rect(x_pos+4, y_pos+4, 92, 92)) 
                
            if clicking == True:
                pygame.draw.rect(screen, RUYAOQING, pygame.Rect(x_pos, y_pos, 100, 100)) 
                
            pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos+8, y_pos+8, 84, 84)) 

            if unclicking == True:
                pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos, y_pos, 100, 100)) 

            if puzzle[mouse_y][mouse_x] != -1:
                draw_numbers(puzzle[mouse_y][mouse_x], mouse_x, mouse_y, user_colour = True)

        if dragging == True and 20 <= pygame.mouse.get_pos()[0] < 936 and 98 <= pygame.mouse.get_pos()[1] < 1014:
            if backup_puzzle[mouse_y][mouse_x] == -1:
                pygame.draw.rect(screen, RUYAOQING_LT, pygame.Rect(x_pos, y_pos, 100, 100)) 
                pygame.draw.rect(screen, HILIGHT_OUT, pygame.Rect(x_pos+4, y_pos+4, 92, 92)) 
                pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos+8, y_pos+8, 84, 84)) 
                if puzzle[mouse_y][mouse_x] != -1:
                    draw_numbers(puzzle[mouse_y][mouse_x], mouse_x, mouse_y, user_colour = True)

        return mouse_x, mouse_y

def numberpad_hover(drag_number = -1):
    #When mouse is over the number pad - highlight the one being considered
    
    for i2 in range(9):
        if len(puzzle) > 0:
            SQ_COLOUR = RUYAOQING
        else:
            SQ_COLOUR = BOARD1
        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(956+i2%3*100, 718+i2//3*100, 92, 92))
        draw_numbers(i2+1, i2%3, i2//3, pad_num = True)

    if game_on == True:
        if len(puzzle) > 0 and 956 <= pygame.mouse.get_pos()[0] <= 956+292 and 718 <= pygame.mouse.get_pos()[1] <= 1010 and dragging == False:

            if (pygame.mouse.get_pos()[0]-956)%100 > 92 or (pygame.mouse.get_pos()[1]-718)%100 > 92:
                pass
            else:
                row_hl = (pygame.mouse.get_pos()[1]-718)//100
                col_hl = (pygame.mouse.get_pos()[0]-956)//100

                num_hl = row_hl*3+col_hl 

                pygame.draw.rect(screen, BOARD, pygame.Rect(956+num_hl%3*100, 718+num_hl//3*100, 92, 92))
                draw_numbers(num_hl+1, num_hl%3, num_hl//3, pad_hover = True)

    if dragging == True:
        pygame.draw.rect(screen, BOARD, pygame.Rect(956+drag_number%3*100, 718+drag_number//3*100, 92, 92))
        draw_numbers(drag_number+1, drag_number%3, drag_number//3, pad_hover = True)

def next_empty(puzzle):
    #Part of the puzzle designing process

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None 

def create_sudoku(puzzle):
    #A new puzzle is created by recursively solving an empty puzzle
    row, col = next_empty(puzzle)

    if row is None: 
        return True 
    
    #The number list is shuffled every time to avoid creating the identical one every time
    one_to_nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(one_to_nine)

    for guess in one_to_nine: 
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if create_sudoku(puzzle):
                return True
        
        puzzle[row][col] = -1

def is_valid(puzzle, guess, row1, col1):
    #Part of the puzzle designing process

    row_vals = puzzle[row1]
    if guess in row_vals:
        return False 

    col_vals = [puzzle[i][col1] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row1 // 3) * 3
    col_start = (col1 // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def clear_board(hover_clear = False, unpause = False):
    #Needed when starting a new game/or returning after pausing
    #Or removing the border on a square after the mouse hover

    for i in range(9):
        for j in range(9):

            do_it = True
            
            #During the game
            if hover_clear == True and unpause == False:
                #Don't clear up the squares with assigned numbers
                if backup_puzzle[j][i] != -1:
                    do_it = False

            if do_it == True:
                i_pos = i * 100 + 20
                if i >= 3:
                    i_pos += 8 * (i//3)
                j_pos = j * 100 + 98
                if j >= 3:
                    j_pos += 8 * (j//3)

                SQ_x = i%2 + j%2
                if SQ_x%2 == 0:
                    SQ_COLOUR = BOARD2
                else:
                    SQ_COLOUR = BOARD1
                pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(i_pos, j_pos, 100, 100)) 

                if len(puzzle) > 0 and hover_clear == True:
                    if puzzle[j][i] != -1:
                        draw_numbers(puzzle[j][i], i, j, user_colour = True)
                    if unpause == True and backup_puzzle[j][i] != -1:
                        draw_numbers(puzzle[j][i], i, j)

def square_enter_mode(x, y):

    SQ_x = x%2 + y%2
    if SQ_x%2 == 0:
        SQ_COLOUR = BOARD2
    else:
        SQ_COLOUR = BOARD1
    pygame.draw.rect(screen, ORANGE, pygame.Rect(20+y*100+y//3*8, 98+x*100+x//3*8, 100, 100))
    pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(20+y*100+y//3*8+10, 98+x*100+x//3*8+10, 80, 80))

def single_position(puzzle):
    #Easy technique

    i = random.randint(0, 8)
    j = random.randint(0, 8)

    if puzzle[i][j] > 0:

        box_num = i//3*3+j//3+1 - 1 

        neighbours = []

        if box_num//3 == 0:
            neighbours.append(box_num+3)
            neighbours.append(box_num+6)
        elif box_num//3 == 1:
            neighbours.append(box_num-3)
            neighbours.append(box_num+3)
        elif box_num//3 == 2:
            neighbours.append(box_num-3)
            neighbours.append(box_num-6)
        
        if box_num%3 == 0:
            neighbours.append(box_num+1)
            neighbours.append(box_num+2)
        elif box_num%3 == 1:
            neighbours.append(box_num+1)
            neighbours.append(box_num-1)
        elif box_num%3 == 2:
            neighbours.append(box_num-1)
            neighbours.append(box_num-2)

        neighbours_detected = 0

        for n1 in neighbours:
            row1 = n1//3
            col1 = n1%3

            for i1 in range(row1*3, row1*3+3):
                for j1 in range(col1*3, col1*3+3):
            
                    if puzzle[j1][i1] == puzzle[i][j]:
                        neighbours_detected += 1
        
        if neighbours_detected >= 3:
            puzzle[i][j] = -1

def candidate_lines(puzzle):
    #Medium technique

    for i in range(9):
        row = i//3*3+1
        col = i%3*3+1
        if puzzle[row][col] > 0:
            inner_list = []
            if row == 1:
                inner_list.append([row+1, col])
            if row == 7:
                inner_list.append([row-1, col])
            if col == 1:
                inner_list.append([row, col+1])
            if col == 7:
                inner_list.append([row, col-1])
            
            for j in inner_list:
                if puzzle[j[0]][j[1]] > 0:
                    if j[0] == row:
                        pos_ft = j[1] - col

                    if j[1] == col:
                        pos_ft = j[0] - row
                        if puzzle[row][col] in puzzle[row-pos_ft] and puzzle[j[0]][j[1]] in puzzle[row-pos_ft]:
                            
                            tar_sq1 = i+3*pos_ft
                            tar_sq2 = i+(3*2)*pos_ft

                            row1 = tar_sq1//3
                            col1 = tar_sq1%3
                            for i1 in range(row1*3, row1*3+3):
                                for j1 in range(col1*3, col1*3+3):
                                    if puzzle[i1][j1] == puzzle[row][col] or puzzle[i1][j1] == puzzle[j[0]][j[1]]:
                                        puzzle[i1][j1] = -1

                            row2 = tar_sq2//3
                            col2 = tar_sq2%3
                            for i2 in range(row2*3, row2*3+3):
                                for j2 in range(col2*3, col2*3+3):
                                    if puzzle[i2][j2] == puzzle[row][col] or puzzle[i2][j2] == puzzle[j[0]][j[1]]:
                                        puzzle[i2][j2] = -1

                            puzzle[row][col] = -1
                            puzzle[j[0]][j[1]] = -1

def double_pair(puzzle):
    #Medium technique

    for i in range(3):
        dp_counter = 2
        for j in puzzle[i*3]:
            if j > 0 and j in puzzle[i*3+1] and j in puzzle[i*3+2] and dp_counter > 0:
                puzzle[i*3][puzzle[i*3].index(j)] = -1
                puzzle[i*3+1][puzzle[i*3+1].index(j)] = -1
                puzzle[i*3+2][puzzle[i*3+2].index(j)] = -1
                dp_counter -= 1

def naked_pair(puzzle):
    #Hard technique

    #Which 3x3 on horizontal scale
    for i in range(3):
        #Which 3x3 on vertical scale
        for j in range(3):
            
            #Which horizontal triplet in that box
            k = random.randint(0, 2)
            
            num_one = puzzle[i*3+k][j*3]
            num_two = puzzle[i*3+k][j*3+2]

            hor_set = [0, 1, 2]
            ver_set = [0, 1, 2]
            hor_set.remove(i)
            ver_set.remove(j)

            hor_items = []
            ver_items = []
            
            for i1 in range(3):
                hor_items.append(ver_set[0]*3+i1)
                ver_items.append(hor_set[0]*3+i1)
            for i2 in range(3):
                hor_items.append(ver_set[1]*3+i2)
                ver_items.append(hor_set[1]*3+i2)
            
            remove_list = []

            for i3 in ver_items:
                match_num = 0
                for j3 in hor_items:
                
                    if puzzle[j3][i3] == num_one or puzzle[j3][i3] == num_two:
                        match_num += 1
                
                #Found both hence can remove values at (i*3+k, i3)
                if match_num == 2:
                    remove_list.append([i*3+k, i3])
                    
            #Positive case
            if len(remove_list) > 0:
                puzzle[i*3+k][j*3] = -1
                puzzle[i*3+k][j*3+2] = -1

                for i4 in remove_list:
                    puzzle[i4[0]][i4[1]] = -1

def sword_fish(puzzle, length):
    #Expert technique
    #Two in one function: length == 2 is X-Wings, length == 3 is Swordfish

    box_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(box_list)
    pivot_candidates = []
    pivot_list = []
    pivot_positions = []

    for i in range(length):
        box_option = box_list.pop()
        pivot_list.append(box_option)
        row1 = box_option//3
        col1 = box_option%3

        pivot_candidates.append([])
        for i1 in range(row1*3, row1*3+3):
            for j1 in range(col1*3, col1*3+3):
                pivot_candidates[-1].append(puzzle[i1][j1])
    
    mutual_nums = list((set(pivot_candidates[0]).intersection(*pivot_candidates)))
    
    pivot = random.choice(mutual_nums)
    
    x_coordinates = []
    y_coordinates = []

    for i2 in range(length):
        x_coordinates.append(pivot_list[i2]%3*3+(pivot_candidates[i2].index(pivot))%3)
        y_coordinates.append(pivot_list[i2]//3*3+(pivot_candidates[i2].index(pivot))//3)
    
    for i3 in x_coordinates:
        for j3 in y_coordinates:
            puzzle[i3][j3] = -1

def new_game(difficulty, backup_puzzle = [], replay = False):
    #Start a new game
    
    #Clean up first
    pygame.draw.rect(screen, BOARD, pygame.Rect(680, 39, 246, 30))
    clear_board()

    if replay == False:

        puzzle = []
        answer_puzzle = []
        backup_puzzle = []

        while len(puzzle) < 9:
            puzzle.append([])
            answer_puzzle.append([])
            backup_puzzle.append([])

        for row in puzzle:
            while len(row) < 9:
                row.append(-1)

        #First generate a complete board, the remove depending on difficulty
        create_sudoku(puzzle)

        #Answer puzzle remains the complete puzzle with all 81 numbers
        for rowx1 in range(9):
            for itemx1 in range(9):
                answer_puzzle[rowx1].append(puzzle[rowx1][itemx1])

        #Easy
        if difficulty == 0:
            removal_num = 306
            while removal_num > 0:
                single_position(puzzle)
                removal_num -= 1

        #Medium
        if difficulty == 1:
            candidate_lines(puzzle)

            double_pair(puzzle)

            removal_num = 108
            while removal_num > 0:
                single_position(puzzle)
                removal_num -= 1

        #Hard
        if difficulty == 2:
            naked_pair(puzzle)

            candidate_lines(puzzle)
            
            double_pair(puzzle)

            removal_num = 86
            while removal_num > 0:
                single_position(puzzle)
                removal_num -= 1

        #Expert   
        if difficulty == 3:
            removal_num = 3
            while removal_num > 0:
                sword_fish(puzzle, 3)
                sword_fish(puzzle, 2)
                removal_num -= 1
            
            naked_pair(puzzle)

            candidate_lines(puzzle)
            
            double_pair(puzzle)
            
            removal_num = 202
            while removal_num > 0:
                single_position(puzzle)
                removal_num -= 1

        #For medium and up, make sure each row doesn't have too few and too many numbers (highly unlikely to be too few for easy)
        if difficulty > 0:

            #Both limits refer to the number of empty squares in a row
            upper_limit = 3
            if difficulty == 3:
                upper_limit = 5
            lower_limit = 6

            for rowx2 in range(9):
                if puzzle[rowx2].count(-1) > lower_limit:

                    num_to_change = puzzle[rowx2].count(-1) - lower_limit

                    for ix2 in range(9):
                        if puzzle[rowx2][ix2] < 0:
                            puzzle[rowx2][ix2] = answer_puzzle[rowx2][ix2]
                            num_to_change -= 1
                            if num_to_change == 0:
                                break

                if puzzle[rowx2].count(-1) < upper_limit:

                    num_to_change = upper_limit - puzzle[rowx2].count(-1)
                    
                    for ix2 in range(9):
                        if puzzle[rowx2][ix2] > 0:
                            puzzle[rowx2][ix2] = -1
                            num_to_change -= 1
                            if num_to_change == 0:
                                break
        
        #Backup puzzle is the copy of all "non-player" numbers, identical to the puzzle when it just began
        for rowx2 in range(9):
            for itemx2 in range(9):
                backup_puzzle[rowx2].append(puzzle[rowx2][itemx2])

        #Display the puzzle once ready
        time1 = 0
        while time1 < 81:

            clock.tick(88)

            i = time1%9
            j = time1//9

            pygame.display.update()

            draw_numbers(puzzle[j][i],i,j)
            
            time1 += 1

        return puzzle, answer_puzzle, backup_puzzle
    
    #Display the same puzzle for a replay
    else:
        
        time1 = 0
        while time1 < 81:

            clock.tick(88)

            i = time1%9
            j = time1//9

            pygame.display.update()

            draw_numbers(backup_puzzle[j][i],i,j)
            
            time1 += 1

def clock_number(num, left):
    #Graphics for the game clock

    N_COLOUR = RUYAOQING_LT
    top = 28

    if num == 1:
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+10, top+4+7, 23, 30))
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+10+9, top+4+7, 6, 30))
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+10+4, top+4+7+6, 5, 5))
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+10, top+4+7+24, 23, 6))

    if num == 2:
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 30))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+10, top+4+13, 17, 5))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+16, top+4+24, 17, 7))

    if num == 3:
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 30))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+10, top+4+13, 17, 5))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+10, top+4+18, 6, 6))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+10, top+4+24, 17, 7))
        
    if num == 4:
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+10, top+4+7, 23, 30))
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+27, top+4+7, 6, 30))
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+10, top+4+18, 23, 6))
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+14, top+4+7, 6, 11))

    if num == 5:
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 30))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+16, top+4+13, 17, 5))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+10, top+4+24, 17, 7))
        
    if num == 6:
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 30))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+16, top+4+13, 17, 5))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+16, top+4+24, 11, 7))

    if num == 7:
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 30))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+10, top+4+13, 17, 24))

    if num == 8:
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 30))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+16, top+4+13, 11, 5))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+16, top+4+24, 11, 7))

    if num == 9:
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 30))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+16, top+4+13, 11, 5))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+10, top+4+24, 17, 7))

    if num == 0:
        pygame.draw.rect(screen, N_COLOUR, pygame.Rect(left+3+10, top+4+7, 23, 30))
        pygame.draw.rect(screen, BOARD, pygame.Rect(left+3+16, top+4+13, 11, 18))
        
def game_clock(time_elapsed):
    #Displaying the game clock

    N_COLOUR = RUYAOQING_LT

    minute = time_elapsed//60
    second = time_elapsed%60

    minute_1 = (minute - (minute//100*100))//10
    minute_2 = minute%10
    second_1 = (second - (second//100*100))//10
    second_2 = second%10

    clock_number(minute_1, 798)
    clock_number(minute_2, 824)
    pygame.draw.rect(screen, N_COLOUR, pygame.Rect(866, 28+17, 5, 5))
    pygame.draw.rect(screen, N_COLOUR, pygame.Rect(866, 28+19+9, 5, 5))
    clock_number(second_1, 864)
    clock_number(second_2, 890)

def keyboard_entry(number, entering_x, entering_y, undo = False):
    #When a number 1-9 is entered

    if backup_puzzle[entering_y][entering_x] == -1:
        x_pos = entering_x * 100 + 20
        if entering_x >= 3:
            x_pos += 8 * (entering_x//3)
        y_pos = entering_y * 100 + 98
        if entering_y >= 3:
            y_pos += 8 * (entering_y//3)

        SQ_x = entering_x%2 + entering_y%2
        if SQ_x%2 == 0:
            SQ_COLOUR = BOARD2
        else:
            SQ_COLOUR = BOARD1

        pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos, y_pos, 100, 100)) 

        if undo == False:
            game_log.append([entering_x, entering_y, puzzle[entering_y][entering_x], number])

        puzzle[entering_y][entering_x] = number
        draw_numbers(number, entering_x, entering_y, user_colour = True)
        
def completion_test(game_on):
    #If the player's puzzle is entirely filled, it's compared to the answer puzzle -- if they're identical, player wins
    #Doesn't address the situation when a puzzle has multiple (almost identical) solutions

    full_counter = 0
    for i in range(9):
        if puzzle[i].count(-1) == 0:
            full_counter += 1
    if full_counter == 9:
        if puzzle == answer_puzzle:
            game_on = False
            outcome(1)

    return game_on
    
def outcome(result):
    #Graphics for winning or losing a game
    #A game is considered to be lost after 100 minutes of no success

    pygame.draw.rect(screen, BOARD, pygame.Rect(680, 39, 246, 30))

    B1C = BOARD
    if result == 1:
        B1T = RUYAOQING
        
        #Y
        pygame.draw.rect(screen, B1T, pygame.Rect(920-30*6+18-12, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(920-30*6+18-12+6, 39, 12, 11))
        pygame.draw.rect(screen, B1C, pygame.Rect(920-30*6+18-12, 39+17, 9, 13))
        pygame.draw.rect(screen, B1C, pygame.Rect(920-30*6+18-12+15, 39+17, 9, 13))
        #O
        pygame.draw.rect(screen, B1T, pygame.Rect(920-30*5+18-12, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(920-30*5+18-12+6, 39+6, 12, 18))
        #U
        pygame.draw.rect(screen, B1T, pygame.Rect(920-30*4+18-12, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(920-30*4+18-12+6, 39, 12, 24))
        #W
        pygame.draw.rect(screen, B1T, pygame.Rect(920-30*3+18, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(920-30*3+18+6, 39, 3, 24))
        pygame.draw.rect(screen, B1C, pygame.Rect(920-30*3+18+15, 39, 3, 24))
        pygame.draw.rect(screen, B1C, pygame.Rect(920-30*3+18, 39+24, 6, 6))
        pygame.draw.rect(screen, B1C, pygame.Rect(920-30*3+18+18, 39+24, 6, 6))
        #I
        pygame.draw.rect(screen, B1T, pygame.Rect(920-30*2+18, 39, 6, 30))
        #N
        pygame.draw.rect(screen, B1T, pygame.Rect(920-30*1, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(920-30*1+6, 39+6, 12, 24))
        #!
        pygame.draw.rect(screen, B1T, pygame.Rect(920, 39, 6, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(920, 39+17, 6, 6))

    else:
        B1T = GREY
        #G
        pygame.draw.rect(screen, B1T, pygame.Rect(890-30*7, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(890-30*7+6, 39+6, 18, 18))
        pygame.draw.rect(screen, B1T, pygame.Rect(890-30*7+18, 39+11, 6, 13))
        pygame.draw.rect(screen, B1T, pygame.Rect(890-30*7+12, 39+11, 6, 6))
        #A
        pygame.draw.rect(screen, B1T, pygame.Rect(890-30*6, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(890-30*6, 39, 6, 6))
        pygame.draw.rect(screen, B1C, pygame.Rect(890-30*6+18, 39, 6, 6))
        pygame.draw.rect(screen, B1C, pygame.Rect(890-30*6+6, 39+6, 12, 5))
        pygame.draw.rect(screen, B1C, pygame.Rect(890-30*6+6, 39+17, 12, 13))
        #M
        pygame.draw.rect(screen, B1T, pygame.Rect(890-30*5, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(890-30*5+6, 39+6, 3, 24))
        pygame.draw.rect(screen, B1C, pygame.Rect(890-30*5+15, 39+6, 3, 24))
        #E
        pygame.draw.rect(screen, B1T, pygame.Rect(890-30*4, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(890-30*4+18, 39+11, 6, 6))
        pygame.draw.rect(screen, B1C, pygame.Rect(890-30*4+6, 39+6, 18, 5))
        pygame.draw.rect(screen, B1C, pygame.Rect(890-30*4+6, 39+6+11, 18, 7))

        #O
        pygame.draw.rect(screen, B1T, pygame.Rect(902-30*3, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(902-30*3+6, 39+6, 12, 18))
        #V
        pygame.draw.rect(screen, B1T, pygame.Rect(902-30*2, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(902-30*2+6, 39, 12, 24))
        pygame.draw.rect(screen, B1C, pygame.Rect(902-30*2, 39+24, 6, 6))
        pygame.draw.rect(screen, B1C, pygame.Rect(902-30*2+18, 39+24, 6, 6))

        #E
        pygame.draw.rect(screen, B1T, pygame.Rect(902-30*1, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(902-30*1+18, 39+11, 6, 6))
        pygame.draw.rect(screen, B1C, pygame.Rect(902-30*1+6, 39+6, 18, 5))
        pygame.draw.rect(screen, B1C, pygame.Rect(902-30*1+6, 39+6+11, 18, 7))
        #R
        pygame.draw.rect(screen, B1T, pygame.Rect(902, 39, 24, 30))
        pygame.draw.rect(screen, B1C, pygame.Rect(902+18, 39, 6, 6))
        pygame.draw.rect(screen, B1C, pygame.Rect(902+18, 39+11, 6, 6))
        pygame.draw.rect(screen, B1C, pygame.Rect(902+6, 39+6, 12, 5))
        pygame.draw.rect(screen, B1C, pygame.Rect(902+6, 39+6+11, 12, 13))

def pause_mosaic():
    #Cover all numbers when the game is paused

    for i in range(9):
        for j in range(9):
    
            x_pos = i * 100 + 20
            if i >= 3:
                x_pos += 8 * (i//3)
            y_pos = j * 100 + 98
            if j >= 3:
                y_pos += 8 * (j//3)

            SQ_x = i%2 + j%2
            if SQ_x%2 == 0:
                SQ_COLOUR = BOARD2
            else:
                SQ_COLOUR = BOARD1
                
            pygame.draw.rect(screen, SQ_COLOUR, pygame.Rect(x_pos, y_pos, 100, 100)) 

            if puzzle[j][i] != -1:
                if backup_puzzle[j][i] == -1:
                    pygame.draw.rect(screen, RUYAOQING, pygame.Rect(x_pos+21, y_pos+21, 58, 58))
                else:
                    pygame.draw.rect(screen, GREY, pygame.Rect(x_pos+21, y_pos+21, 58, 58))
                
def display_background(drag_number):
    #Displaying everything on screen for the dragging process

    pygame.draw.rect(screen, BACKGROUND, pygame.Rect(0, 0, 1616-330-14, 976+58))
    pygame.draw.rect(screen, BOARD, pygame.Rect(10, 10, 1596-330-14, 956+58))

    logo()
    clear_board()

    for i in range(9):
        for j in range(9):
            if backup_puzzle[j][i] > -1:
                draw_numbers(backup_puzzle[j][i], i, j)
            elif puzzle[j][i] > -1:
                draw_numbers(puzzle[j][i], i, j, user_colour = True)

    easy_hover()
    medium_hover()
    hard_hover()
    expert_hover()

    new_game_switch(False)

    undo_hover()
    restart_hover()
    pause_hover()
    show_clock_hover()

    board_hover(pygame.mouse.get_pos(), False, dragging = True)

    game_clock(int(time_elapsed))

    if dragging == False:
        drag_number = -1

    numberpad_hover(drag_number)

def dragging_number(drag_number, x_margin, y_margin):
    #When a number is dragged from the number pad to anywhere on the puzzle

    display_background(drag_number)

    x_pos = pygame.mouse.get_pos()[0] - x_margin
    y_pos = pygame.mouse.get_pos()[1] - y_margin

    drag_number += 1

    DRAG_COLOUR = RUYAOQING_LT

    #Numbers need to be redrawn because in the "draw_numbers" function, some numbers are drawn with short-cuts,
    #Which is not suitable when a number is above other objects, non-transparency would be immediately visible

    if drag_number == 1:
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+21, y_pos, 12, 10))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+7, y_pos+10, 26, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+17, y_pos+22, 16, 24))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+46, 50, 12))
    
    if drag_number == 2:
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos, 50, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+38, y_pos+12, 12, 10))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+22, 50, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+34, 12, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+46, 50, 12))
    
    if drag_number == 3:
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos, 50, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+38, y_pos+12, 12, 34))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+12, y_pos+22, 26, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+46, 50, 12))
    
    if drag_number == 4:
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+8, y_pos, 14, 22))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+36, y_pos, 14, 58))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+22, 36, 12))

    if drag_number == 5:
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos, 50, 12))        
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+22, 50, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+38, y_pos+34, 12, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+46, 50, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+12, 12, 10))

    if drag_number == 6:
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos, 50, 12))        
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+22, 50, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+38, y_pos+34, 12, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+46, 50, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+12, 12, 34))

    if drag_number == 7:
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos, 50, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+38, y_pos+12, 12, 46))
    
    if drag_number == 8:
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos, 50, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+12, 12, 46))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+38, y_pos+12, 12, 46))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+12, y_pos+22, 26, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+12, y_pos+46, 26, 12))
    
    if drag_number == 9:
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos, 50, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+12, 12, 22))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+38, y_pos+12, 12, 46))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos+12, y_pos+22, 26, 12))
        pygame.draw.rect(screen, DRAG_COLOUR, pygame.Rect(x_pos, y_pos+46, 38, 12))

    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((1616-330-14, 976+58))
clock = pygame.time.Clock()
pygame.display.set_caption('Sudoku')

#Colours
BACKGROUND = (202, 202, 196)

BOARD = (232, 232, 222)

BOARD1 = (212, 212, 202)
BOARD2 = (222, 222, 212)

GREY = (102, 102, 98)
LIGHTGREY = (152, 152, 158)

RUYAOQING = (128, 164, 146)
RUYAOQING_LT = (158, 192, 176)

HILIGHT_OUT = (188, 212, 206)
HILIGHT_IN = (208, 212, 206)

#NUM_COLOURS = [(0, 0, 0), (186, 26, 52), (204, 92, 32), (202, 182, 28), (42, 110, 62), (16, 138, 150), (0, 108, 136), (108, 32, 108), (186, 90, 138), (100, 78, 50)]

#BLUE = (0, 108, 136)
#BLUE = (52, 88, 116)

C1 = (186, 26, 52)

GREY1 = (168, 182, 202)
GREY1_HI = (118, 124, 188)
GREY2 = (148, 162, 182)
GREY2_HI = (104, 108, 178)
GREY3 = (128, 142, 162)
GREY3_HI = (90, 92, 168)
GREY4 = (108, 122, 142)
GREY4_HI = (74, 76, 156)
GREY_SET = [(118, 124, 188), (104, 108, 178), (90, 92, 168), (74, 76, 156)]

RED = (186, 26, 52)
RED2 = (200, 22, 28)
RED_DARK = (66, 22, 26)
BLACK = (26, 36, 46)

YELLOW = (202, 182, 28)
YELLOW_HI = (212, 192, 62)
ORANGE = (204, 92, 32)
ORANGE_HI = (212, 106, 60)
GREEN = (42, 110, 62)
GREEN_HI = (72, 112, 62)
PINK = (168, 56, 102)
PINK_HI = (182, 52, 112)
BLUE = (0, 108, 136)
BLUE_HI = (42, 112, 132)

puzzle = []
answer_puzzle = []
backup_puzzle = []

game_log = []
global game_on
game_on = False
game_won = False
new_game_on = False
ready_to_enter = False
show_clock = True
just_clicked = []

dragging = False
drag_number = 0
time_elapsed = 0

#Part of the process of the dragging graphics
x_margin = -1
y_margin = -1

pygame.draw.rect(screen, BACKGROUND, pygame.Rect(0, 0, 1616-330-14, 976+58))
pygame.draw.rect(screen, BOARD, pygame.Rect(10, 10, 1596-330-14, 956+58))

clear_board()

logo()

while True:
        
    if dragging == True:
        dragging_number(drag_number, x_margin, y_margin)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        cur_mouse_x = pygame.mouse.get_pos()[0]
        cur_mouse_y = pygame.mouse.get_pos()[1]

        #Left mouse button released
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and dragging == True:

            if 20 <= cur_mouse_x < 936 and 98 <= cur_mouse_y < 1014:
                xy = mouse_to_coordinates(pygame.mouse.get_pos())
                mouse_x = xy[0]
                mouse_y = xy[1]

                #If released above a square that can change, update the number
                if backup_puzzle[mouse_y][mouse_x] == -1:
                    keyboard_entry(drag_number+1, mouse_x, mouse_y)

            dragging = False
            display_background(drag_number)

            #See if game is won
            game_on = completion_test(game_on)
            if game_on == False:
                game_won = True

        #Clicking left mouse button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            #Buttons on the right
            if 956 <= cur_mouse_x <= 956+292:

                #Game difficulty buttons
                if cur_mouse_y <= 104+74*3+66:

                    time_elapsed = 0
                    game_log = []
                    game_won = False

                    #Easy
                    if 104 <= cur_mouse_y <= 104+66:
                        game_on = True
                        ready_to_enter = False
                        package = new_game(0)
                        puzzle = package[0]
                    
                    #Medium
                    if 104+74 <= cur_mouse_y <= 104+74+66:
                        game_on = True
                        ready_to_enter = False
                        package = new_game(1)
                        puzzle = package[0]
                    
                    #Hard
                    if 104+74*2 <= cur_mouse_y <= 104+74*2+66:
                        game_on = True
                        ready_to_enter = False
                        package = new_game(2)
                        puzzle = package[0]

                    #Expert
                    if 104+74*3 <= cur_mouse_y:
                        game_on = True
                        ready_to_enter = False
                        package = new_game(3)
                        puzzle = package[0]
                    
                    if len(package) > 0:
                        answer_puzzle = package[1]
                        backup_puzzle = package[2]

                #Undo
                if 412 <= cur_mouse_y <= 412+66:
                    if len(game_log) > 0 and game_won == False:
                        undo_info = game_log.pop()
                        keyboard_entry(undo_info[2], undo_info[0], undo_info[1], undo = True)
                        
                #Restart
                if 412+72*1 <= cur_mouse_y <= 412+72*1+66:
                    if len(backup_puzzle) > 0:
                        time_elapsed = 0
                        game_on = True
                        game_won = False
                        ready_to_enter = False
                        game_log = []

                        for i9 in range(9):
                            for j9 in range(9):
                                if backup_puzzle[i9][j9] == -1:
                                    puzzle[i9][j9] = -1

                        new_game(0, backup_puzzle, replay = True)

                #Pause/Continue
                if 412+72*2+3 <= cur_mouse_y <= 412+72*2+66+3:
                    if len(backup_puzzle) > 0 and game_won == False:
                        if game_on == True:
                            game_on = False
                            pause_mosaic()
                        else:
                            game_on = True
                            clear_board(hover_clear = True, unpause = True)

                #Show Clock
                if 412+72*3+3 <= cur_mouse_y <= 412+72*3+66+3:
                    if game_won == False:
                        if show_clock == True:
                            show_clock = False
                            pygame.draw.rect(screen, BOARD, pygame.Rect(798, 28, 182, 60))
                        else:
                            show_clock = True
                            game_clock(int(time_elapsed))

            #Clicking an empty square
            if 20 <= cur_mouse_x <= 936 and 98 <= cur_mouse_y <= 1014 and game_on == True:
                
                xy = mouse_to_coordinates(pygame.mouse.get_pos())

                if len(just_clicked) > 0 and xy == just_clicked[0]:
                    just_clicked = []
                    ready_to_enter = False

                else:
                    just_clicked = []
                    just_clicked.append(xy)
                
                    ready_to_enter = True
                    entering_position = board_hover(pygame.mouse.get_pos(), just_clicked, clicking = True)
                    
                    entering_x = entering_position[0]
                    entering_y = entering_position[1]

            #Clicking on the number pad - either fill a square during "Entering mode" (After a square was clicked) or drag a number
            if len(puzzle) > 0 and 956 <= cur_mouse_x <= 956+292 and 718 <= cur_mouse_y <= 1010:
                
                if (pygame.mouse.get_pos()[0]-956)%100 < 92 or (pygame.mouse.get_pos()[1]-718)%100 < 92:

                    if 21 <= (pygame.mouse.get_pos()[0]-956)%100 <= 71 and 17 <= (pygame.mouse.get_pos()[1]-718)%100 <= 75:

                        row_hl = (cur_mouse_y-718)//100
                        col_hl = (cur_mouse_x-956)//100
                        num_hl = row_hl*3+col_hl+1 

                        x_margin = (pygame.mouse.get_pos()[0]-956)%100 - 21
                        y_margin = (pygame.mouse.get_pos()[1]-718)%100 - 17

                        dragging = True
                        drag_number = num_hl - 1

                    if ready_to_enter == True:
                        
                        keyboard_entry(num_hl, entering_x, entering_y)

                        just_clicked = []
                        ready_to_enter = False
                        game_on = completion_test(game_on)
                        if game_on == False:
                            game_won = True

        #Keyboard action
        if event.type == pygame.KEYDOWN:
            
            #Used for testing
            if event.key == pygame.K_SPACE:
                print(" ")
                for xxx in answer_puzzle:
                    print(xxx)

            #Entering a number
            if ready_to_enter == True:
                if event.key == pygame.K_1:
                    keyboard_entry(1, entering_x, entering_y)                    
                if event.key == pygame.K_2:
                    keyboard_entry(2, entering_x, entering_y)                    
                if event.key == pygame.K_3:
                    keyboard_entry(3, entering_x, entering_y)                    
                if event.key == pygame.K_4:
                    keyboard_entry(4, entering_x, entering_y)                    
                if event.key == pygame.K_5:
                    keyboard_entry(5, entering_x, entering_y)                    
                if event.key == pygame.K_6:
                    keyboard_entry(6, entering_x, entering_y)                    
                if event.key == pygame.K_7:
                    keyboard_entry(7, entering_x, entering_y)                    
                if event.key == pygame.K_8:
                    keyboard_entry(8, entering_x, entering_y)                    
                if event.key == pygame.K_9:
                    keyboard_entry(9, entering_x, entering_y)                    
                
                #Multiple ways to remove an entered number to keep the program intuitive
                if event.key == pygame.K_DELETE or event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    keyboard_entry(-1, entering_x, entering_y)

                just_clicked = []
                ready_to_enter = False
                game_on = completion_test(game_on)
                if game_on == False:
                    game_won = True

    #Only update graphics (here) when nothing is being dragged (that's a dedicated bit)
    if dragging == False:
        new_game_switch(new_game_on)
        easy_hover()
        medium_hover()
        hard_hover()
        expert_hover()

        undo_hover()
        restart_hover()
        pause_hover()
        show_clock_hover()

        numberpad_hover()

        if 956 <= pygame.mouse.get_pos()[0] <= 956+292 and 718 <= pygame.mouse.get_pos()[1] <= 1010 and len(just_clicked) == 0:
            ready_to_enter = False

        #Mouse hovering over a number
        if 20 <= pygame.mouse.get_pos()[0] < 936 and 98 <= pygame.mouse.get_pos()[1] < 1014 and game_on == True:
            if len(just_clicked) == 0:
                ready_to_enter = True
                entering_position = board_hover(pygame.mouse.get_pos(), just_clicked, hovering = True, clicking = False)
                entering_x = entering_position[0]
                entering_y = entering_position[1]
        
    #Game clock
    if game_on == True:
        time_elapsed += 1/30
        if show_clock == True:
            game_clock(int(time_elapsed))
        if time_elapsed > 5999:
            game_on = False
            outcome(-1)

    pygame.display.update()

    clock.tick(30)
