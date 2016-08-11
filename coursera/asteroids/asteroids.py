# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = True

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 100)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.forward = 0
        
    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size,
                                      self.pos, self.image_size, self.angle); 

    def update(self):
        self.forward = angle_to_vector(self.angle)        
        self.pos[0] += self.vel[0]
        self.pos[0] = self.pos[0]%800
        self.pos[1] += self.vel[1]
        self.pos[1] = self.pos[1]%600        
        self.angle +=self.angle_vel
       
        if self.thrust:
            self.vel[0] += self.forward[0]*0.3
            self.vel[1] += self.forward[1]*0.3

        self.vel[0] *= 0.97
        self.vel[1] *= 0.97
        
    def change_angle_vel(self, num):
        self.angle_vel = num
        
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
        
    def set_thrust_on(self):
        global ship_thrust_sound
        self.thrust = True
        self.image_center[0] += 90      
        ship_thrust_sound.play()
        
    def set_thrust_off(self):
        global ship_thrust_sound
        self.thrust = False  
        self.image_center[0] -= 90 
        ship_thrust_sound.rewind()      
        
    def shoot(self):
        global missile_group  
        missile_vel = [self.vel[0]+self.forward[0]*3,self.vel[1]+self.forward[1]*3]
        missile_pos=[35*self.forward[0],35*self.forward[1]]
        missile_pos = [self.pos[0],self.pos[1]]        
        a_missile = Sprite([self.pos[0]+(self.forward[0]*35),self.pos[1]+(self.forward[1]*35)],
                           missile_vel, 0, 0, missile_image, missile_info, 
                           missile_sound)
        missile_group.add(a_missile)
        
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.sound = sound
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size,
                                      self.pos, self.image_size, self.angle); 
    
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[0] = self.pos[0]%800
        self.pos[1] += self.vel[1]
        self.pos[1] = self.pos[1]%600        
        self.angle +=self.angle_vel  
        self.age = self.age + 1
        if(self.age>=self.lifespan):
            return True
        else:
            return False
        
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
        
    def collide(self, other_object):
        distance = dist(self.pos, other_object.get_position())
        if(distance> self.radius + other_object.get_radius()):
            return False
        else:
            return True
        
           
def draw(canvas):
    global time, score, lives, rock_group, my_ship, missile_group, started
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
 
    # draw ship and sprites
    my_ship.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    process_sprite_group(canvas, rock_group)
    process_sprite_group(canvas, missile_group)    
    if(group_collide(rock_group, my_ship)):
        lives = lives -1
    collisons = group_group_collide(rock_group, missile_group) 
    score = score + collisons
    canvas.draw_text('Score: '+str(score), [650, 50], 20, 'Blue')
    canvas.draw_text('Lives: '+str(lives), [50, 50], 20, 'Blue')    
    
    if(lives<=0):
        started = False
        for rock in set(rock_group):
            rock_group.remove(rock)
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), 
                          [WIDTH/2,HEIGHT/2], splash_info.get_size()); 
        soundtrack.play()
    
def process_sprite_group(canvas, group):
    for g in set(group):
        if(g.update()):
            group.remove(g)
        g.draw(canvas)
        
def group_collide(group, other_object):
    for obj_in_grp in set(group):
        if(obj_in_grp.collide(other_object)):
            group.remove(obj_in_grp)
            return True
    return False

def group_group_collide(group_one, group_two):
    count = 0
    to_remove = set()
    for obj_in_grp in set(group_one):
        if(group_collide(group_two, obj_in_grp)):
            count = count + 1
            to_remove.add(obj_in_grp)
    for obj in to_remove:
        group_one.discard(obj)
    return count
            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group, my_ship
    if(len(rock_group)<6 and started):
        pos= [random.randrange(0,WIDTH),random.randrange(0,HEIGHT)]
        velocity = random.randint(10, 20)
        velocity = velocity/10.0
        angle = random.randint(0, 10)
        angle = angle/10.0
        spin = random.randint(-5, 5)    
        spin = spin/100.0
        distance = dist(pos, my_ship.get_position())
        if(distance >150):
            a_rock = Sprite(pos, 
                            [velocity, velocity], angle, spin, 
                            asteroid_image, 
                            asteroid_info)
            rock_group.add(a_rock)
    
def keydown_handler(key):
    global my_ship
    change_to_angle=0.05
    if (key==simplegui.KEY_MAP['left']):
        my_ship.change_angle_vel(-1*change_to_angle)
    if (key==simplegui.KEY_MAP['right']):
        my_ship.change_angle_vel(change_to_angle)
    if (key==simplegui.KEY_MAP['up']):
        my_ship.set_thrust_on() 
    if (key==simplegui.KEY_MAP['space']):
        my_ship.shoot()         
         

def keyup_handler(key):
    global my_ship
    if (key==simplegui.KEY_MAP['left'] or key==simplegui.KEY_MAP['right']):
        my_ship.change_angle_vel(0)
    if (key==simplegui.KEY_MAP['up']):
        my_ship.set_thrust_off()          

def mouse_handler(position):
    global started, score, lives, my_ship
    if not started:
        started = True
        soundtrack.rewind()
        score = 0
        lives = 3
        my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
        
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set()
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0.1, missile_image, missile_info, missile_sound)
missile_group = set()

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.set_mouseclick_handler(mouse_handler)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
