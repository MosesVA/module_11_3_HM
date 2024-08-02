class Light:
    def on(self):
        print("Свет ВКЛ.")

    def off(self):
        print("Свет ВЫКЛ.")


class Fan:
    def on(self):
        print("Вентилятор ВКЛ.")

    def off(self):
        print("Вентилятор ВыКЛ.")


class Command:
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.on()


class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.off()


class RemoteControl:
    def __init__(self):
        self.commands = {}

    def add_command(self, command_name, command):
        self.commands[command_name] = command

    def press_button(self, command_name):
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"Команда '{command_name}' не найдена")


if __name__ == "__main__":
    living_room_light = Light()
    living_room_fan = Fan()

    light_on = LightOnCommand(living_room_light)
    light_off = LightOffCommand(living_room_light)
    fan_on = FanOnCommand(living_room_fan)
    fan_off = FanOffCommand(living_room_fan)

    remote_control = RemoteControl()

    remote_control.add_command("Включить свет", light_on)
    remote_control.add_command("Выключить свет", light_off)
    remote_control.add_command("Включить вентилятор", fan_on)
    remote_control.add_command("Выключить вентилятор", fan_off)

    remote_control.press_button("Включить свет")
    remote_control.press_button("Включить вентилятор")
    remote_control.press_button("Выключить свет")
    remote_control.press_button("Выключить вентилятор")
    remote_control.press_button("Включить телевизор")
