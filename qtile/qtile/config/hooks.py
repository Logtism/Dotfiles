from libqtile import hook
import subprocess
import os


@hook.subscribe.startup_once
def startup_once():
    scripts_dir = os.path.join(os.path.expanduser('~'), '.config', 'qtile', 'scripts')
    subprocess.call(os.path.join(scripts_dir, 'autostart.sh'))


@hook.subscribe.startup
def startup():
    pass


@hook.subscribe.client_new
def client_new(window):
    pass