import pygame
from enum import Enum
from enum import IntEnum
import random
#from pygame.constants import (
#    MOUSEBUTTONDOWN, QUIT, MOUSEMOTION, KEYDOWN
#)

pygame.init()
full_SET = []

class Number(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3

class Shading(Enum):
    SOLID = 'solid'
    STRIPED = 'striped'
    EMPTY = 'empty'

class Shape(Enum):
    SQUIGGLE = 'squiggle'
    DIAMOND = 'diamond'
    OVAL = 'oval'

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    PURPLE = 'purple'

class SetCard:
    def __init__(self, card_color, card_shape, card_shading, card_number, card_picture):
        self.color = card_color
        self.shape = card_shape
        self.shading = card_shading
        self.number = card_number
        self.picture = card_picture


for color in Color:
    for shading in Shading:
        for shape in Shape:
            for number in Number:
                pic_name = str(color) + '_' + str(shape) + '_' + str(shading) + '_' + str(number) + '.png'
                full_SET.append(SetCard(Color(color), Shape(shape), Shading(shading), Number(number), pic_name))

#for i in range(0, len(full_SET)):
#    print('Color: ', full_SET[i].color)
#    print('Shape: ', full_SET[i].shape)
#    print('Shading: ', full_SET[i].shading)
#    print('Number: ', full_SET[i].number)
#    print('Picture: ', full_SET[i].picture)

background_color = (255,255,255)
width = 1200
height = 800

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption('SET Game')
#background = pygame.Surface((width,height))
#screen.blit(pygame.image.load(str(full_SET[i].color) + '_' +
  #                            str(full_SET[i].shape) + '_' +
 #                             str(full_SET[i].shading) + '_' +
 #                             str(full_SET[i].number) + '.png'), (50,50))




w = 0
h = 0
p = 0

#shuffled = []


def randomized_deck(full_SET):
    temp = []
    temp = full_SET.copy()
    random.shuffle(temp)
    return temp

#shuffled = randomized_deck(full_SET)

def is_set(card1, card2, card3):

    colors = [card1.color, card2.color, card3.color]
    numbers = [card1.number, card2.number, card3.number]
    shapes = [card1.shape, card2.shape, card3.shape]
    shadings = [card1.shading, card2.shading, card3.shading]
    card_is_set = [card1, card2, card3]
    #for card in card_is_set:
        #print(card.color)
        #print(card.number)
        #print(card.shape)
       # print(card.shading)
    if (((all(colors[0] != value for value in colors[1:]) & (colors[1] != colors[2]))| (colors[0] == colors[1] == colors[2])) &
        ((all(numbers[0] != value for value in numbers[1:]) & (numbers[1] != numbers[2]))| (numbers[0] == numbers[1] == numbers[2])) &
        ((all(shapes[0] != value for value in shapes[1:]) & (shapes[1] != shapes[2]))| (shapes[0] == shapes[1] == shapes[2])) &
        ((all(shadings[0] != value for value in shadings[1:]) & (shadings[1] != shadings[2])) | (shadings[0] == shadings[1] == shadings[2]))):
        print('This is a set')
        return True

    return False
    print('NOT A SET')

def rectangle_on(position):
    #print(type(position))
    x = 0
    y = 0
    x_change = 200
    x_start = 3
    y_start = 8
    y_change = 120
    if (position == 1) | (position == 5) | (position == 9):
        x = x_start
       # print("yes")
    elif (position == 2) | (position == 6) | (position == 10):
        x = x_start + x_change
    elif (position == 3) | (position == 7) | (position == 11):
        x = x_start + (x_change*2)
    elif (position == 4) | (position == 8) | (position == 12):
        x = x_start + (x_change*3)
    elif position == 13:
        x = 100
    elif position == 14:
        x = 281
    elif position == 15:
        x = 462
    #print(x)

    if (position == 1) | (position == 2) | (position == 3) | (position == 4):
        y = y_start
    elif (position == 5) | (position == 6) | (position == 7) | (position == 8):
        y = y_start+y_change
    elif (position == 9) | (position == 10) | (position == 11) | (position == 12):
        y = y_start+(y_change*2)
    elif (position == 13) | (position == 14) | (position == 15):
        y = y_start+(y_change*3)
    #print(y)

    pygame.draw.rect(screen, (0, 255, 0), (x, y, 179, 104), 2)


def rectangle_off(position):
    print("yes")
    x = 0
    y = 0
    x_change = 200
    x_start = 3
    y_start = 8
    y_change = 120

    if (position == 1) | (position == 5) | (position == 9):
        x = x_start
    elif (position == 2) | (position == 6) | (position == 10):
        x = x_start + (x_change*1)
    elif (position == 3) | (position == 7) | (position == 11):
        x = x_start + (x_change*2)
    elif (position == 4) | (position == 8) | (position == 12):
        x = x_start + (x_change*3)
    elif (position == 13):
        x = 100
    elif (position == 14):
        x = 281
    elif (position == 15):
        x = 462
    if (position == 1) | (position == 2) | (position == 3) | (position == 4):
        y = y_start
    elif (position == 5) | (position == 6) | (position == 7) | (position == 8):
        y = y_start + y_change
    elif (position == 9) | (position == 10) | (position == 11) | (position == 12):
        y = y_start + (y_change * 2)
    elif (position == 13) | (position == 14) | (position == 15):
        y = y_start + (y_change * 3)

    pygame.draw.rect(screen, (255, 255, 255), (x, y, 179, 104), 2)

def display_deck(deck, num_cards):
    h = 0
    p = 0
    for first in range(0, 3):
        w = 0
        for second in range(0, 4):
            screen.blit(pygame.image.load(str(deck[p].color) + '_' +
                                          str(deck[p].shape) + '_' +
                                          str(deck[p].shading) + '_' +
                                          str(deck[p].number) + '.jpg'), (5 + w, 10 + h))
            p += 1
            pygame.display.flip()

            w += 200

        h += 120
    if num_cards == 15:
        w = 0
        for j in range(0, 3):
            screen.blit(pygame.image.load(str(deck[p].color) + '_' +
                                          str(deck[p].shape) + '_' +
                                          str(deck[p].shading) + '_' +
                                          str(deck[p].number) + '.jpg'), (108 + w, 10 + h))
            p += 1
            pygame.display.flip()

            w += 200

def which_clicked(pos, num_cards):
    lower_width = 5
    upper_width = 180
    lower_height = 10
    upper_height = 110

    h = 0
    card = 1
    for i in range(0,3):
        lower_width = 5
        upper_width = 180
        for j in range(0,4):
            if (pos[1]> lower_height) & (pos[1] < upper_height) & (pos[0] > lower_width) & (pos[0] < upper_width):
                return card
            lower_width += 200
            upper_width += 200
            card += 1
        lower_height += 120
        upper_height += 120
    if num_cards == 15:
        lower_width = 108
        upper_width = lower_width + 175
        for i in range(0,3):
            if (pos[1] > lower_height) & (pos[1] < upper_height) & (pos[0] > lower_width) & (pos[0] < upper_width):
                return card
            lower_width += 200
            upper_width += 200
            card += 1
    return 0

def set_available(temp):
    print(len(temp))
    length = len(temp)
    for i in range(0,length - 2):
        for j in range(i+1,length):
            for k in range(j+1,length):
                print(i,j,k)
                set = False
                set = is_set(temp[i],temp[j],temp[k])
                print(set)
                if set:
                    print(temp[i].color, temp[i].shape, temp[i].shading, temp[i].number)
                    print(temp[j].color, temp[j].shape, temp[j].shading, temp[j].number)
                    print(temp[k].color, temp[k].shape, temp[k].shading, temp[k].number)
                    print("TRUE")
                    return True
    return False
                    #return [i,j,k]




screen.fill(background_color)
#for i in range(0, 3):
 #   w = 0
 #   for j in range(0,4):

  #      screen.blit(pygame.image.load(str(shuffled[p].color) + '_' +
  #                                  str(shuffled[p].shape) + '_' +
  #                                  str(shuffled[p].shading) + '_' +
  #                                  str(shuffled[p].number) + '.jpg'), (5+ w,10 + h))
   #     p += 1
   #     pygame.display.flip()

   #     w += 200

  #  h += 120


running = True

def no_set_button():
    pygame.draw.rect(screen, (0, 0, 255), (50, 700, 50, 50))
def is_no_set_pressed(pos):
    print("NO SET PRESSED")
    if (pos[1] > 700) & (pos[1] < 750) & (pos[0] > 50) & (pos[0] < 100):
        print("NO Set")
        return True


deck = []
num_cards = 12
cards_clicked = []
deck = randomized_deck(full_SET).copy()
change = 1
no_set_button()
while running:
    for event in pygame.event.get():
        if change == 1:
            print("change occured")
            display_deck(deck, num_cards)
            change = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked = which_clicked(pos, num_cards)
            print(clicked)
            if clicked != 0:
                if clicked not in cards_clicked:
                    cards_clicked.append(clicked)
                    rectangle_on(clicked)
                elif clicked in cards_clicked:
                    cards_clicked.remove(clicked)
                    rectangle_off(clicked)
            elif is_no_set_pressed(pos):
                print("inside")
                if not set_available(deck[:num_cards]):
                    num_cards = 15
                    change = 1
        if len(cards_clicked) == 3:
            if is_set(deck[cards_clicked[0]-1], deck[cards_clicked[1]-1], deck[cards_clicked[2]-1]):

                deck[cards_clicked[0] - 1] = deck[num_cards]
                deck[cards_clicked[1] - 1] = deck[num_cards + 1]
                deck[cards_clicked[2] - 1] = deck[num_cards + 2]

                del deck[num_cards:(num_cards+3)]

                rectangle_off(cards_clicked[0])
                rectangle_off(cards_clicked[1])
                rectangle_off(cards_clicked[2])
                if ((cards_clicked[0] != 13 |cards_clicked[0] != 14 |cards_clicked[0] != 15)
                   | (cards_clicked[1] != 13 |cards_clicked[1] != 14 |cards_clicked[1] != 15)
                   | (cards_clicked[2] != 13 |cards_clicked[2] != 14 |cards_clicked[2] != 15)):
                   num_cards = 12
                change = 1


                cards_clicked.clear()
        pygame.display.flip()




       # if event.type == pygame.MOUSEBUTTONDOWN:
      #      pos = pygame.mouse.get_pos()
       #     if pos[1]>10 & pos[1] < 110 & pos[0] > 5 & pos[0] < 180:
        #        pygame.draw.rect(screen, (0,255,0), (3, 8, 179, 104), 2)

      #      print (pos[1])



        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


