import pygame as pg
import sys
from random import choice, random
from os import path
from settings import *
from sprites import *
from tilemap import *

def draw_player_health(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

class Game:
    def __init__(self):
        pg.mixer.pre_init(44100, -16, 4, 2048)
        pg.init()
        self.name = ''
        self.read_data()
        self.font_name1 = pg.font.Font(None, round((WIDTH/1000)*35))
        self.font_kill = pg.font.Font(None, round((WIDTH/1000)*28))
        self.font_error = pg.font.Font('img\Impacted2.0.ttf', round((WIDTH/1000)*15))
        self.screen = pg.display.set_mode()
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.sign = False
        self.error = ""
        self.active = False

    def read_data(self):
        file = open('info/sign.txt', 'r')
        var = file.readline()
        file.close()

        file = open('info/kill.txt', 'r')
        self.kill = int(file.readline())
        file.close()
        
        if var == 'False':
            self.gamemode_check = 'signin'
            wfile = open('info/sign.txt', 'w')
            wfile.write('True')
            wfile.close()
        else:
            self.gamemode_check = 'menu'
            rfile = open('info/username.txt', 'r')
            self.name = rfile.readline()
            rfile.close()

    def draw_text(self, text, font_name, size, color, x, y, align="topleft"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        snd_folder = path.join(game_folder, 'snd')
        music_folder = path.join(game_folder, 'music')
        menu_img_folder = path.join(game_folder, 'menu_img')
        self.map_folder = path.join(game_folder, 'maps')
        self.title_font = path.join(img_folder, 'ZOMBIE.TTF')
        self.hud_font = path.join(img_folder, 'Impacted2.0.ttf')
        self.sign_in_1  = pg.image.load(path.join(menu_img_folder, 'sign_in_1.png')).convert_alpha()
        self.sign_in_1 = pg.transform.scale(self.sign_in_1, (WIDTH, HEIGHT))
        self.sign_in_2  = pg.image.load(path.join(menu_img_folder, 'sign_in_2.png')).convert_alpha()
        self.sign_in_2 = pg.transform.scale(self.sign_in_2, (WIDTH, HEIGHT))
        self.menu  = pg.image.load(path.join(menu_img_folder, 'menu.png')).convert_alpha()
        self.menu = pg.transform.scale(self.menu, (WIDTH, HEIGHT))
        self.menu_background  = pg.image.load(path.join(menu_img_folder, 'menu_background.png')).convert_alpha()
        self.menu_background = pg.transform.scale(self.menu_background, (WIDTH, HEIGHT))
        self.help = pg.image.load(path.join(menu_img_folder, 'help.png')).convert_alpha()
        self.help = pg.transform.scale(self.help, ((WIDTH/100)*55, HEIGHT))
        self.options = pg.image.load(path.join(menu_img_folder, 'options.png')).convert_alpha()
        self.options = pg.transform.scale(self.options, ((WIDTH/100)*55, HEIGHT))
        self.music_on = pg.image.load(path.join(menu_img_folder, 'music_on.png')).convert_alpha()
        self.music_on = pg.transform.scale(self.music_on, ((WIDTH/100)*13, (HEIGHT/100)*10))
        self.music_off = pg.image.load(path.join(menu_img_folder, 'music_off.png')).convert_alpha()
        self.music_off = pg.transform.scale(self.music_off, ((WIDTH/100)*13, (HEIGHT/100)*10))
        self.music_on_game = pg.transform.scale(self.music_on, ((WIDTH/100)*6.5, (HEIGHT/100)*5))
        self.music_off_game = pg.transform.scale(self.music_off, ((WIDTH/100)*6.5, (HEIGHT/100)*5))
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.paused_img = pg.image.load(path.join(menu_img_folder, 'pause.png')).convert_alpha()
        self.paused_img = pg.transform.scale(self.paused_img, ((WIDTH/100)*27.5, HEIGHT/2))
        self.dim_screen.fill((0, 0, 0, 180))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.bullet_images = {}
        self.bullet_images['lg'] = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        self.bullet_images['sm'] = pg.transform.scale(self.bullet_images['lg'], (10, 10))
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.splat = pg.image.load(path.join(img_folder, SPLAT)).convert_alpha()
        self.splat = pg.transform.scale(self.splat, (64, 64))
        self.gun_flashes = []
        for img in MUZZLE_FLASHES:
            self.gun_flashes.append(pg.image.load(path.join(img_folder, img)).convert_alpha())
        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(img_folder, ITEM_IMAGES[item])).convert_alpha()
        # lighting effect
        self.fog = pg.Surface((WIDTH, HEIGHT))
        self.fog.fill(NIGHT_COLOR)
        self.light_mask = pg.image.load(path.join(img_folder, LIGHT_MASK)).convert_alpha()
        self.light_mask = pg.transform.scale(self.light_mask, LIGHT_RADIUS)
        self.light_rect = self.light_mask.get_rect()
        # Sound loading
        pg.mixer.music.load(path.join(music_folder, BG_MUSIC))
        self.effects_sounds = {}
        for type in EFFECTS_SOUNDS:
            self.effects_sounds[type] = pg.mixer.Sound(path.join(snd_folder, EFFECTS_SOUNDS[type]))
        self.weapon_sounds = {}
        for weapon in WEAPON_SOUNDS:
            self.weapon_sounds[weapon] = []
            for snd in WEAPON_SOUNDS[weapon]:
                s = pg.mixer.Sound(path.join(snd_folder, snd))
                s.set_volume(0.3)
                self.weapon_sounds[weapon].append(s)
        self.zombie_moan_sounds = []
        for snd in ZOMBIE_MOAN_SOUNDS:
            s = pg.mixer.Sound(path.join(snd_folder, snd))
            s.set_volume(0.2)
            self.zombie_moan_sounds.append(s)
        self.player_hit_sounds = []
        for snd in PLAYER_HIT_SOUNDS:
            self.player_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, snd)))
        self.zombie_hit_sounds = []
        for snd in ZOMBIE_HIT_SOUNDS:
            self.zombie_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, snd)))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.map = TiledMap(path.join(self.map_folder, 'level1.tmx'))
        self.map_img = self.map.make_map()
        self.map.rect = self.map_img.get_rect()
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'zombie':
                Mob(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            if tile_object.name in ['health', 'shotgun']:
                Item(self, obj_center, tile_object.name)
        self.camera = Camera(self.map.width, self.map.height)
        self.paused = False
        self.night = False
        self.effects_sounds['level_start'].play()

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        self.help_check = False
        self.option_check = False
        self.music_check = 'on'
        pg.mixer.music.play(loops=-1)
        if self.gamemode_check == 'menu':
            while self.playing:
                self.dt = self.clock.tick(FPS) / 1000.0
                self.events()
                self.menu_update()
                if self.gamemode_check != 'menu':
                    break
        
        elif self.gamemode_check == 'game':
            while self.playing:
                self.dt = self.clock.tick(FPS) / 1000.0
                self.events()
                if not self.paused:
                    self.update()
                self.draw()
                if self.gamemode_check != 'game':
                    break
            self.gamemode_check = 'menu'

        else:
            while self.playing:
                self.dt = self.clock.tick(FPS) / 1000.0
                self.events()
                self.signin()
                if self.gamemode_check != 'signin':
                    break

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        # game over?
        if len(self.mobs) == 0:
            self.playing = False
        # player hits items
        hits = pg.sprite.spritecollide(self.player, self.items, False)
        for hit in hits:
            if hit.type == 'health' and self.player.health < PLAYER_HEALTH:
                hit.kill()
                self.effects_sounds['health_up'].play()
                self.player.add_health(HEALTH_PACK_AMOUNT)
            if hit.type == 'shotgun':
                hit.kill()
                self.effects_sounds['gun_pickup'].play()
                self.player.weapon = 'shotgun'
        # mobs hit player
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            if random() < 0.7:
                choice(self.player_hit_sounds).play()
            self.player.health -= MOB_DAMAGE
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.hit()
            self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)
        # bullets hit mobs
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for mob in hits:
            # hit.health -= WEAPONS[self.player.weapon]['damage'] * len(hits[hit])
            for bullet in hits[mob]:
                mob.health -= bullet.damage
            mob.vel = vec(0, 0)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def render_fog(self):
        # draw the light mask (gradient) onto fog image
        self.fog.fill(NIGHT_COLOR)
        self.light_rect.center = self.camera.apply(self.player).center
        self.fog.blit(self.light_mask, self.light_rect)
        self.screen.blit(self.fog, (0, 0), special_flags=pg.BLEND_MULT)

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply(self.map))
        # self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        # pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        if self.night:
            self.render_fog()
        # HUD functions
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        self.draw_text('Zombies: {}'.format(len(self.mobs)), self.hud_font, 30, WHITE,
                       WIDTH - 10, 10, align="topright")
        if self.paused:
            self.screen.blit(self.dim_screen, (0, 0))
            self.screen.blit(self.paused_img, ((WIDTH/10)*3.5, HEIGHT/4))
            if self.night == True:
                self.screen.blit(self.music_on_game, ((WIDTH/1000)*462, (HEIGHT/100)*60))
            else:
                self.screen.blit(self.music_off_game, ((WIDTH/1000)*462, (HEIGHT/100)*60))
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if self.gamemode_check == 'game':
                    if event.key == pg.K_p or event.key == pg.K_ESCAPE:
                        self.paused = not self.paused
                    if event.key == pg.K_n:
                        self.night = not self.night

                if self.gamemode_check == 'menu' and ( self.help_check == True or self.option_check == True ):
                    if event.key == pg.K_ESCAPE:
                        self.help_check = False
                        self.option_check = False

                elif self.gamemode_check == 'signin':
                    if event.key == pg.K_RETURN:
                        if len(self.name) > 2:
                            self.sign = True
                            self.gamemode_check = 'menu'
                            self.savename()
                        else:
                            self.error = "Your name must be bigger than 2 characters !"
                    if self.active:
                        if event.key == pg.K_BACKSPACE:
                            self.name  = self.name [:-1]
                        elif event.key != pg.K_BACKSPACE and event.key != pg.K_RETURN:
                            if len(self.name ) < 11:
                                self.name  += event.unicode

            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if self.gamemode_check == 'menu':
                    if self.help_check == False and self.option_check == False:
                        if pos[0] > (WIDTH/100)*5 and pos[0] < (WIDTH/100)*25 and pos[1] > (HEIGHT/100)*30 and pos[1] < (HEIGHT/100)*39:
                            self.gamemode_check = 'game'
                            self.new()
                        elif pos[0] > (WIDTH/100)*5 and pos[0] < (WIDTH/100)*20 and pos[1] > (HEIGHT/100)*40 and pos[1] < (HEIGHT/100)*50:
                            self.option_check = True
                        elif pos[0] > (WIDTH/100)*5 and pos[0] < (WIDTH/100)*20 and pos[1] > (HEIGHT/100)*52 and pos[1] < (HEIGHT/100)*62:
                            self.help_check = True
                        elif pos[0] > (WIDTH/100)*5 and pos[0] < (WIDTH/100)*20 and pos[1] > (HEIGHT/100)*63 and pos[1] < (HEIGHT/100)*73:
                            file = open('info/kill.txt', 'w')
                            file.write(str(self.kill))
                            file.close()
                            quit()
                        elif pos[0] > 0 and pos[0] < (WIDTH/100)*12 and pos[1] > (HEIGHT/100)*93 and pos[1] < HEIGHT:
                            self.sign = False
                            self.gamemode_check = 'signin'

                    elif self.help_check == True or self.option_check == True:
                        if pos[0] > (WIDTH//100)*72 and pos[0] < (WIDTH//100)*78 and pos[1] > 0 and pos[1] < (HEIGHT/100)*10:
                            self.help_check = False
                            self.option_check = False
                        elif pos[0] > (WIDTH//100)*42 and pos[0] < (WIDTH//100)*56 and pos[1] > 65 and pos[1] < (HEIGHT/100)*75:
                            if self.music_check == 'on':
                                self.music_check = 'off'
                            else:
                                self.music_check = 'on'
                elif self.gamemode_check == 'game':
                    if self.paused:
                        if pos[0] > (WIDTH/100)*43 and pos[0] < (WIDTH/100)*55 and pos[1] > (HEIGHT/100)*37 and pos[1] < (HEIGHT/100)*44:
                            self.paused = not self.paused
                        elif pos[0] > (WIDTH/100)*60 and pos[0] < (WIDTH/1000)*627 and pos[1] > (HEIGHT/1000)*245 and pos[1] < (HEIGHT/1000)*295:
                            self.paused = not self.paused
                        elif pos[0] > (WIDTH/100)*43 and pos[0] < (WIDTH/100)*55 and pos[1] > (HEIGHT/100)*46 and pos[1] < (HEIGHT/100)*53:
                            self.gamemode_check = 'menu'
                        elif pos[0] > (WIDTH/100)*46 and pos[0] < (WIDTH/100)*53 and pos[1] > (HEIGHT/100)*60 and pos[1] < (HEIGHT/100)*65:
                            self.night = not self.night

                else:
                    if (WIDTH/1000)*288 < pos[0] < (WIDTH/1000)*555 and (HEIGHT/100)*40 < pos[1] < (HEIGHT/1000)*482:
                        self.active = True

                    elif (WIDTH/1000)*555 < pos[0] < (WIDTH/1000)*685 and (HEIGHT/1000)*398 < pos[1] < (HEIGHT/1000)*482:
                        if len(self.name ) > 2:
                            self.sign = True
                            self.gamemode_check = 'menu'
                            self.savename()
                        else:
                            self.error = "Your name must be bigger than 2 characters !"
                    else:
                        if pos[0] != 0 and pos[1] != 0:
                            self.active = False

    def menu_update(self):
        if self.help_check == True:
            self.screen.blit(self.menu_background, (0, 0))
            self.screen.blit(self.help, ((WIDTH/100)*20, 0))
        elif self.option_check == True:
            self.screen.blit(self.menu_background, (0, 0))
            self.screen.blit(self.options, ((WIDTH/100)*20, 0))
            if self.music_check == 'on':
                self.screen.blit(self.music_on, ((WIDTH/1000)*425, (HEIGHT/100)*66))
            else:
                self.screen.blit(self.music_off, ((WIDTH/1000)*425, (HEIGHT/100)*66))

        else:
            name_txt = self.font_name1.render(self.name , True, (0, 0, 0))
            kill_txt = self.font_kill.render(str(self.kill) , True, (0, 0, 0))
            self.screen.blit(self.menu, (0,0))
            self.screen.blit(name_txt, ((WIDTH/100)*4, (HEIGHT/1000)*55))
            self.screen.blit(kill_txt, ((WIDTH/100)*4, (HEIGHT/1000)*137))
        
        pg.display.update()


    def signin(self):
        if self.sign == False:
            self.screen.blit(self.sign_in_2 ,(0,0))
            name_txt = self.font_name1.render(self.name , True, (0,0,0))
            error_txt = self.font_error.render(self.error, True, (236,28,36))

            if self.active == True:
                self.screen.blit(self.sign_in_1,(0,0))

            elif self.active == False:
                self.screen.blit(self.sign_in_2,(0,0))

            self.screen.blit(name_txt, ((WIDTH/100)*31, (HEIGHT/1000)*425))
            self.screen.blit(error_txt, ((WIDTH/100)*34, (HEIGHT/100)*52))

            pg.display.update()

    def savename(self):
        wfile = open('info/sign.txt', 'w')
        wfile.write('True')
        wfile.close()

        file = open('info/username.txt', 'w')
        file.write(self.name)
        file.close()

g = Game()
while True:
    g.run()