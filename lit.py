import os
import pprint
import click
from phue import Bridge

hue_username = os.getenv("HUE_USERNAME")
hue_ip = os.getenv("HUE_IP")

b = Bridge(hue_ip, hue_username)

def get_light_state(light):
    return {
        "id": light.light_id,
        "name": light.name,
        "on": light.on,
        "brightness": light.brightness,
        "xy": light.xy,
        "hue": light.hue,
        "saturation": light.saturation
    }


@click.group()
@click.pass_context
def main(ctx):
    click.echo("Hello")

@main.command()
def state():
    lights = b.lights
    scene = {
        'name': [get_light_state(l) for l in lights]
    }
    pprint.pprint(scene)


@click.argument('light', type=click.INT)
@main.command()
def flick(light):
    state = b.get_light(light, 'on')
    b.set_light(light, 'on', not state)
