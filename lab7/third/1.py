import pygame
import os
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (106, 90, 205)
GRAY = (128, 128, 128)
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load("images/bg.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
text_backgroung = pygame.image.load("images/frame.png")


FPS = 60
clock = pygame.time.Clock()
running = True
screen.fill(BLACK)

music_files = []
s_n = []
songs = os.listdir("music/songs")
for song in songs:
    music_files.append(os.path.join("music/songs", song))
    song_name = os.path.splitext(song)[0]
    s_n.append(song_name)

music_icons = []
icons = os.listdir("images/forsong")
for icon in icons:
    music_icons.append(os.path.join("images/forsong", icon))

current_song_index = 0
current_icon_index = 0
pygame.mixer.music.load(music_files[current_song_index])
pygame.mixer.music.play()

icon_size = (SCREEN_WIDTH // 1.5, SCREEN_HEIGHT // 1.5)
current_icon = pygame.image.load(music_icons[current_icon_index])
current_icon = pygame.transform.scale(current_icon, icon_size)


fontsize = 10
font = pygame.font.SysFont("Sylfaen", fontsize)
current_song_title = font.render(s_n[current_song_index], True, (255, 255, 255))
text_width, text_height = current_song_title.get_size()
scale_factor = min((SCREEN_WIDTH - 40) / text_width, SCREEN_HEIGHT / text_height)
font = pygame.font.SysFont("Sylfaen", int(fontsize * scale_factor))
current_song_title = font.render(s_n[current_song_index], True, (255, 255, 255))

button_size = (SCREEN_WIDTH // text_height, SCREEN_HEIGHT // text_height)
D = button_size[0]
next_button_rect = pygame.image.load("images/chh.png")

pause_button_rect = pygame.image.load("images/pause.png")
prev_button_rect = pygame.image.load("images/chh.png")
prev_button_rect = pygame.transform.rotate(prev_button_rect, 180)
next_button_rect = pygame.transform.scale(next_button_rect, button_size)
pause_button_rect = pygame.transform.scale(pause_button_rect, button_size)
prev_button_rect = pygame.transform.scale(prev_button_rect, button_size)
button_y = SCREEN_HEIGHT - 0.4* (SCREEN_HEIGHT - icon_size[1])
button_spacing = 20
button_center = SCREEN_WIDTH // 2
next_button_pos = (button_center + D + button_spacing, button_y)
pause_button_pos = (button_center - D // 2, button_y)
prev_button_pos = (button_center - 2*D - button_spacing, button_y)
x = (SCREEN_WIDTH - text_width * scale_factor)
y = button_y - text_height*scale_factor*2
text_position = (x, y)

text_backgroung = pygame.transform.scale(text_backgroung, (SCREEN_WIDTH,  (SCREEN_HEIGHT - (SCREEN_HEIGHT - icon_size[1]) )))

current_icon_rect = current_icon.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - icon_size[1]))
icon_pos = current_icon_rect

frame = pygame.image.load("images/frame.png")
frame_size = (icon_size[0] + (20*scale_factor), icon_size[1] + (20*scale_factor))
frame = pygame.transform.scale(frame, frame_size)
while running: 
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if next_button_rect.get_rect(topleft=next_button_pos).collidepoint(event.pos):
                current_song_index = (current_song_index + 1) % len(music_files)
                current_icon_index = (current_icon_index + 1) % len(music_icons)
                pygame.mixer.music.load(music_files[current_song_index])
                current_icon = pygame.image.load(music_icons[current_icon_index])
                current_icon = pygame.transform.scale(current_icon, icon_size)
                screen.blit(current_icon, (icon_pos))
                pygame.mixer.music.play()
            elif prev_button_rect.get_rect(topleft=prev_button_pos).collidepoint(event.pos):
                current_song_index = (current_song_index - 1) % len(music_files)
                current_icon_index = (current_icon_index - 1) % len(music_icons)
                pygame.mixer.music.load(music_files[current_song_index])
                current_icon = pygame.image.load(music_icons[current_icon_index])
                current_icon = pygame.transform.scale(current_icon, icon_size)
                screen.blit(current_icon, (icon_pos))
                pygame.mixer.music.play()
            elif pause_button_rect.get_rect(topleft=pause_button_pos).collidepoint(event.pos):
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
        elif pressed[pygame.K_RIGHT]:
            current_song_index = (current_song_index + 1) % len(music_files)
            current_icon_index = (current_icon_index + 1) % len(music_icons)
            pygame.mixer.music.load(music_files[current_song_index])
            current_icon = pygame.image.load(music_icons[current_icon_index])
            current_icon = pygame.transform.scale(current_icon, icon_size)
            screen.blit(current_icon, (icon_pos))
            pygame.mixer.music.play()
        elif pressed[pygame.K_LEFT]:
            current_song_index = (current_song_index - 1) % len(music_files)
            current_icon_index = (current_icon_index - 1) % len(music_icons)
            pygame.mixer.music.load(music_files[current_song_index])
            current_icon = pygame.image.load(music_icons[current_icon_index])
            current_icon = pygame.transform.scale(current_icon, icon_size)
            screen.blit(current_icon, (icon_pos))
            pygame.mixer.music.play()
        elif pressed[pygame.K_SPACE]:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()

    screen.fill(BLACK)
    screen.blit(background_image, (0, 0))
    screen.blit(text_backgroung, (0, (SCREEN_HEIGHT - 0.5*(SCREEN_HEIGHT - icon_size[1]))))
    # pygame.draw.rect(screen, GRAY, (icon_pos[0] - 10, icon_pos[1] - 10, frame_size[0], frame_size[1]))
    screen.blit(frame, ((icon_pos[0] - 10, icon_pos[1] - 10)))
    screen.blit(current_icon, (icon_pos))
    screen.blit(next_button_rect, next_button_pos)
    screen.blit(pause_button_rect, pause_button_pos)
    screen.blit(prev_button_rect, prev_button_pos)
    current_song_title = font.render(s_n[current_song_index], True, WHITE)
    screen.blit(current_song_title, text_position)

    pygame.display.update()
    clock.tick(FPS)