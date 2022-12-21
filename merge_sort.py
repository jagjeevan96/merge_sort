import pygame
import random

# initialise the font module
pygame.font.init()
# initialise window
width = 900
height = 600
screen = pygame.display.set_mode([width, height])

# set the current window caption
pygame.display.set_caption('Sorting Algorithm Visualiser')

# set array size
size = 150

# create array with 150 entries
array = [0] * size
# array colors
arr_clr = [(0, 204, 102)] * size
clr_ind = 0
clr = [(252, 132, 3), (255, 255, 255),
       (255, 255, 255), (40, 3, 252)]

# create a font object from the system fonts
fnt = pygame.font.SysFont("Arial", 20)


def create_arr():
    for i in range(size):
        arr_clr[i] = clr[0]
        array[i] = random.randrange(1, 75)


def refill():
    screen.fill((0, 0, 0))
    draw_merge()
    pygame.display.update()
    pygame.time.delay(20)


# create merge sort algorithm
def mergesort(array, left, right):
    mid = (left + right) // 2
    if left < right:
        mergesort(array, left, mid)
        mergesort(array, mid + 1, right)
        merge(array, left, mid,
              mid + 1, right)


def merge(array, x1, y1, x2, y2):
    i = x1
    j = x2
    temp = []
    pygame.event.pump()
    while i <= y1 and j <= y2:
        arr_clr[i] = clr[1]
        arr_clr[j] = clr[1]
        refill()
        arr_clr[i] = clr[0]
        arr_clr[j] = clr[0]
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= y1:
        arr_clr[i] = clr[1]
        refill()
        arr_clr[i] = clr[0]
        temp.append(array[i])
        i += 1
    while j <= y2:
        arr_clr[j] = clr[1]
        refill()
        arr_clr[j] = clr[0]
        temp.append(array[j])
        j += 1
    j = 0
    for i in range(x1, y2 + 1):
        pygame.event.pump()
        array[i] = temp[j]
        j += 1
        arr_clr[i] = clr[2]
        refill()
        if y2-x1 == len(array)-2:
            arr_clr[i] = clr[3]
        else:
            arr_clr[i] = clr[0]


def draw_merge():
    # render and position text
    txt = fnt.render("Merge Sort", 1, (255, 255, 255))
    screen.blit(txt, (20, 20))
    txt1 = fnt.render("'Enter' to start", 1, (255, 255, 255))
    screen.blit(txt1, (20, 40))
    txt2 = fnt.render("'Spacebar' for new array", 1, (255, 255, 255))
    screen.blit(txt2, (20, 60))
    element_width = (width-size)//size
    boundry_arr = width / size
    boundry_grp = height / 100

    # draw the array values as lines
    for i in range(size):
        pygame.draw.line(screen, arr_clr[i],
                         (boundry_arr * i-3, 100),
                         (boundry_arr * i-3, array[i]*boundry_grp + 100),
                         element_width)


def main():
    run = True
    create_arr()

    while run:
        screen.fill((0, 0, 0))
    # event handler stores all event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    create_arr()
                if event.key == pygame.K_RETURN:
                    mergesort(array, 1, len(array)-1)
        draw_merge()
        pygame.display.update()


main()
pygame.quit()
