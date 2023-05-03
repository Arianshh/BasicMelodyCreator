import math
from simulation import Simulation, Movement

WIDTH, HEIGHT = 640, 480
R = 100
movement = Movement(radius=100, speed_x=6, speed_y=5)
initial_x = WIDTH / 2 + R * math.cos(math.radians(movement.angle_x))
initial_y = HEIGHT / 2 + R * math.sin(math.radians(movement.angle_y))

simulation = Simulation(60, WIDTH, HEIGHT, movement, initial_x, initial_y)
simulation.initialize()

while True:
    simulation.run()
    simulation.clock.tick(simulation.frame_per_second)
