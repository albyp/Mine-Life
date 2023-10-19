import os
import pygame

pygame.init()

# color library
navy = (5, 40, 80)
sage = (50, 160, 75)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (200, 115, 10)

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Mine Life Idle")
background = navy
framerate = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

# game state
drill_area = 0
blast_bcm = 0
score = 0

# game_attributes
game_attributes = {
    'drill': {
        'fleet': 1,
        'mod': 5,
        'value': 5,
        'mod_incr': 5,
        'speed': 10
    },
    'blast': {
        'fleet': 1,
        'mod': 20,
        'value': 20,
        'mod_incr': 20,
        'speed': 5
    },
    'dig': {
        'fleet': 1,
        'mod': 100,
        'value': 100,
        'mod_incr': 100,
        'speed': 2
    },
    'dump': {
        'fleet': 1,
        'mod': 100,
        'value': 100,
        'mod_incr': 100,
        'speed': 1
    }
}

# game variables
draw_drill = False
draw_blast = False
draw_dig = False
draw_dump = False
drill_length = 0
blast_length = 0
dig_length = 0
dump_length = 0

# game data
pages = ['production', 'processing', 'maintenance']
items_production = ['drill', 'blast', 'dig', 'dump']
items_processing = ['feed', 'crush', 'refine']
items_maintenance = ['drill fleet', 'flast fleet', 'dig fleet', 'truck fleet']

# Images
image_dict = {}
folder_path = 'Assets'
image_filenames = ['drill.png', 'blast.png', 'dig.png', 'truck.png']
for filename in image_filenames:
    image_path = os.path.join(folder_path, filename)
    image = pygame.image.load(image_path).convert_alpha()
    image = pygame.transform.scale(image, (45, 45))
    image_dict[filename] = image

# Background
background_image = pygame.image.load('Assets\\background\\00016-218459808.png').convert()

# draw function for status items
def draw_status(item, value):
    pass

# draw function for progress items
def draw_task(color, y_coord, task_image, draw, length, speed, global_variable, value):
    max_length = 380
  
    if draw and length < max_length:
        length += speed
    elif length >= max_length:
        draw = False
        length = 0
        global drill_area, blast_bcm
        if global_variable == drill_area:
          drill_area += value
        elif global_variable == blast_bcm:
          blast_bcm += value
          drill_area -= value
          

    task = pygame.draw.rect(screen, color, (25, y_coord, 50, 50)) # button
    screen.blit(task_image, (27.5, y_coord + 2.5, 45, 45)) # image
    pygame.draw.rect(screen, color, (100, y_coord, 400, 50)) # loading bar
    pygame.draw.rect(screen, navy, (110, y_coord + 10, 380, 30)) # loading bar
    pygame.draw.rect(screen, orange, (110, y_coord + 10, length, 30))# loading bar progress
    return task, length, draw

drill_image = image_dict['drill.png']
blast_image = image_dict['blast.png']
digger_image = image_dict['dig.png']
dump_image = image_dict['truck.png']

# running loop
running = True
while running:
    timer.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if task_drill.collidepoint(event.pos):
                draw_drill = True
            if task_blast.collidepoint(event.pos):
                draw_blast = True
            if task_dig.collidepoint(event.pos):
                draw_dig = True
            if task_dump.collidepoint(event.pos):
                draw_dump = True

    screen.blit(background_image, (0, 0))

    task_drill, drill_length, draw_drill = draw_task(sage, 100, drill_image, draw_drill, drill_length, game_attributes['drill']['speed'], drill_area, game_attributes['drill']['value'])
    task_blast, blast_length, draw_blast = draw_task(sage, 175, blast_image, draw_blast, blast_length, game_attributes['blast']['speed'], blast_bcm, game_attributes['blast']['value'])
    task_dig, dig_length, draw_dig = draw_task(sage, 250, digger_image, draw_dig, dig_length, game_attributes['dig']['speed'], None, None)
    task_dump, dump_length, draw_dump = draw_task(sage, 325, dump_image, draw_dump, dump_length, game_attributes['dump']['speed'], None, None)

    score_drill_area = font.render('Drill area: '+str(round(drill_area, 0)), True, white, navy)
    screen.blit(score_drill_area, (10, 5))
    score_blast_area = font.render('Blast bcm: '+str(round(blast_bcm, 0)), True, white, navy)
    screen.blit(score_blast_area, (10, 21))

    pygame.display.flip()

pygame.quit()
