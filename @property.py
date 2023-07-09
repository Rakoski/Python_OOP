class Robot:
    def __init__(self, battery_level):
        self._battery_level = battery_level

    def level_bateria(self):
        return self._battery_level

    # ou, com o @property
    @property
    def __level_bateria__(self):
        return self._battery_level


#     The @property decorator is like a magical button that you can press to get information about something specific,
#     like the battery level of the robot.

#     When you press the button, it immediately shows you the current battery level on the robot's display screen.

#     The @property decorator allows you to define a method that behaves like this magical button,
#     giving you access to certain information from the object without needing to call it like a regular method.

# Sem o @property
robot = Robot(75)
print(robot.level_bateria())

# Com o @property
level = Robot(59)
print(level.__level_bateria__)
