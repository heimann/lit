import os
import click
from phue import Bridge

hue_username = os.getenv("HUE_USERNAME")
hue_ip = os.getenv("HUE_IP")

b = Bridge(hue_ip, hue_username)

@click.command()
def work():
    b.set_light(3, 'bri', 250)
    b.set_light(3, 'on', True)


if __name__ == '__main__':
    work()


