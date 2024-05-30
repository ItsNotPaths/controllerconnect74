import socket, random, pygame, subprocess, time
from tkinter import Tk

'''
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object

host = socket.gethostname() # Get local machine name 

port = random.randint(49152, 49200) # Reserve a port for your service

server_socket.bind((host, port)) # Bind the socket to the host and port

erver_socket.listen(5) # Listen for incoming connections
print(f"Server listening on {host}:{port}")

client_socket, addr = server_socket.accept() # Wait for a connection
print(f"Got connection from {addr}")
'''

def process_controller_input(data): # Function to process the received controller input data
    pass
    # Parse the controller input data from the received data
    # Use a library like PyGame, PyAutoGUI, or PyDirectInput to simulate the inputs

def get_server_controller_input(): # Function to get the server's controller input data
    pass
    # Use a library like PyGame or PyAutoGUI to get controller inputs from the server
    # Return the controller inputs as a string or JSON object

def setup_pygame(): # we draw everything to screen then draw screen onto window, which is the final scaled display surface
    global keycodes, keynames, screen, clock, window, MonitorInfo, WindowInfo, Root, UIRoot, screen_width, screen_height
    pygame.init()
    pygame.display.set_caption('project74 SERVER')
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

def copy2clip(txt): # gracously provided via stack overflow by https://stackoverflow.com/users/3617098/binyamin
    cmd = 'echo '+txt.strip()+ '|clip'
    return subprocess.check_call(cmd, shell = True)

def render():
    global copyimg, screen, buttondark, dark, Font, msgs
    screen.fill('black')
    for i, v in enumerate(reversed(msgs)):
        screen.blit(Font.render(v, False, (250, 250, 250)), (10, 60 - ((i * 30))))

def flipscreen():
    window.blit(screen, (0, 0))
    pygame.display.update()

def renderlogic():
    global mx, my, mousestate, buttondark, port

def communication():
    global data, server_input, client_socket
    data = client_socket.recv(1024)
    if not data:
        return
    # Process the received controller input data
    process_controller_input(data)

    # Get controller input data from the server
    server_input = get_server_controller_input()
    client_socket.sendall(server_input)

def connect():
    global server_socket, host, port, client_socket, addr
    print('1')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object

    print('2')
    host = socket.gethostname() # Get local machine name 

    print('3')
    port = random.randint(49152, 49200) # Reserve a port for your service

    print('4')
    server_socket.bind((host, port)) # Bind the socket to the host and port

    print('5')
    server_socket.listen(5) # Listen for incoming connections
    print(f"Server listening on {host}:{port}" + "app will hang until connection is made")

    print('6')
    client_socket, addr = server_socket.accept() # Wait for a connection
    print(f"Got connection from {addr}")











screen, clock = setup_pygame()

port = random.randint(49152, 49200)
copy2clip(str(port))

mx = 0
my = 0
mousestate = 0

Font = pygame.font.SysFont('pixel', 30)
Font.set_bold(False)

msgs = []

screen_width = 1080
screen_height = 720
copyimg = pygame.transform.scale(pygame.image.load('copy.png').convert_alpha(), (70, 70))

dark = pygame.Surface((70, 70), 32)
dark.set_alpha(200, pygame.RLEACCEL)






msgs.append('port number has been copied to your clipboard')
msgs.append('press c to start connection attempt')











while True:
    tick(256)
    get_mouse()
    getkeys()
    renderlogic()
    render()
    flipscreen()
    if 'pygame.K_c' in keysPressed:
        msgs.append('attempting to connect, app will hang during attempt')
        render()
        flipscreen()
        connect()
        msgs.append('connected!')



# Clean up the connection
client_socket.close()
