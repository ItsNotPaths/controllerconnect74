import socket, random, pygame
from tkinter import Tk

'''

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object

host = socket.gethostname() # Get local machine name

port = 12345 # Reserve a port for your service

client_socket.connect((host, port)) # Connect to the server

client_socket.close() # Clean up the connection
'''

# Function to get the client's controller input data
def get_client_controller_input():
	pass
    # Use a library like PyGame or PyAutoGUI to get controller inputs from the client
    # Return the controller inputs as a string or JSON object

# Function to process the received controller input data
def process_controller_input(data):
	pass
    # Parse the controller input data from the received data
    # Use a library like PyGame, PyAutoGUI, or PyDirectInput to simulate the inputs

def setup_pygame(): # we draw everything to screen then draw screen onto window, which is the final scaled display surface
    global keycodes, keynames, screen, clock, window, MonitorInfo, WindowInfo, Root, UIRoot, screen_width, screen_height
    pygame.init()
    pygame.display.set_caption('project74 CLIENT')
    MonitorInfo = pygame.display.Info()
    MonitorInfo = (MonitorInfo.current_w, MonitorInfo.current_h)
    if MonitorInfo[0] < 1920:
        WindowInfo = (1920 / 2, 1080 / 12)
        MonitorInfo = (1920, 1080)
    else:
        WindowInfo = MonitorInfo[0] / 2, MonitorInfo[1] / 12
    screen = pygame.Surface((1920, 1080))
    screen_width = 1920
    screen_height = 1080
    window = pygame.display.set_mode((WindowInfo[0], WindowInfo[1]))
    clock = pygame.time.Clock()
    keycodes = open('pygame keycodes.txt', 'r')
    keycodes = keycodes.readlines()
    keynames = open('pygame keynames.txt', 'r')
    keynames = keynames.readlines()
    for i, v in enumerate(keycodes):
        keycodes[i] = keycodes[i].strip()
        keynames[i] = keynames[i].strip()
    return(screen, clock)

def tick(framerate):
    clock.tick(framerate)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(), exit()

def getkeys():
    global keysPressed
    keysPressed = list()
    keys = pygame.key.get_pressed()
    for i in keycodes:
        if keys[eval(i)]:
            keysPressed.append(i)

def get_mouse():
    global mousestate, mx, my
    # 1 means i just clicked, 2 means ive held click, 0 means im not clicking
    if mousestate == 1:
        if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
            mousestate = 2
        else:
            mousestate = 0
    if mousestate == 0:
        if pygame.mouse.get_pressed(num_buttons=3)[0] == True:
            mousestate = 1
    if pygame.mouse.get_pressed(num_buttons=3)[0] == False:
        mousestate = 0
    OldRange = WindowInfo[0]
    NewRange = 960
    mx = (((pygame.mouse.get_pos()[0]) * 1920) / WindowInfo[0])
    my = (((pygame.mouse.get_pos()[1]) * 1080) / WindowInfo[1])
    # mouse x and y offset for resolution

def render():
	global copyimg, screen, buttondark, dark
	screen.fill('black')
	screen.blit(copyimg, (10, 10))
	if buttondark:
		screen.blit(dark, (10, 10))
	for i, v in enumerate(reversed(msgs)):
		screen.blit(Font.render(v, False, (250, 250, 250)), (100, 60 - ((i * 30))))

def flipscreen():
    window.blit(screen, (0, 0))
    pygame.display.update()

def renderlogic():
	global mx, my, mousestate, buttondark, port
	buttondark = False
	if mx < WindowInfo[0] / 6:
		buttondark = True
		if mousestate == 1:
			port = Tk().clipboard_get()
			port = int(port)

screen, clock = setup_pygame()

port = 'none'

mx = 0
my = 0
mousestate = 0

screen_width = 1080
screen_height = 720
copyimg = pygame.transform.scale(pygame.image.load('copy.png').convert_alpha(), (70, 70))

dark = pygame.Surface((70, 70), 32)
dark.set_alpha(200, pygame.RLEACCEL)

Font = pygame.font.SysFont('pixel', 30)
Font.set_bold(False)

msgs = []
msgs.append('press the button to copy your port number in')

while True:
	tick(256)
	get_mouse()
	renderlogic()
	render()
	flipscreen()
	if port != 'none':
		msgs.append('attempting connection')
		render()
		flipscreen()
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object

		host = socket.gethostname() # Get local machine name

		client_socket.connect((host, port)) # Connect to the server

		msgs.append('connected!')

# Continuously exchange controller input data
while True:
    # Get controller input data from the client
    client_input = get_client_controller_input()
    client_socket.sendall(client_input)

    # Receive controller input data from the server
    data = client_socket.recv(1024)
    if not data:
        break
    # Process the received controller input data
    process_controller_input(data)