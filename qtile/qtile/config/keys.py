from .settings import terminal, app_launcher, file_manager_gui, lock_command
from libqtile.config import Key
from libqtile.lazy import lazy
from .groups import groups


super_key = 'mod4'
alt = 'mod1'
shift = 'shift'
control = 'control'


keys = [
    # Qtile stuff
    Key([super_key, shift], 'r', lazy.restart()),

    # Switch screens
    Key([super_key, control], 'Right', lazy.next_screen()),
    Key([super_key, control], 'Left', lazy.prev_screen()),

    # Switch window
    Key([super_key], 'Up', lazy.layout.up()),
    Key([super_key], 'Left', lazy.layout.left()),
    Key([super_key], 'Right', lazy.layout.right()),
    Key([super_key], 'Down', lazy.layout.down()),

    # Move window
    Key([super_key, shift], 'Up', lazy.layout.shuffle_up()),
    Key([super_key, shift], 'Left', lazy.layout.shuffle_left()),
    Key([super_key, shift], 'Right', lazy.layout.shuffle_right()),
    Key([super_key, shift], 'Down', lazy.layout.shuffle_down()),

    # Grow windows
    Key([super_key, control, shift], 'Up', lazy.layout.grow_up()),
    Key([super_key, control, shift], 'Left', lazy.layout.grow_left()),
    Key([super_key, control, shift], 'Right', lazy.layout.grow_right()),
    Key([super_key, control, shift], 'Down', lazy.layout.grow_down()),

    # Change layout
    Key([super_key, shift], 'tab', lazy.next_layout()),

    # Floating
    Key([super_key, shift], 'f', lazy.window.toggle_floating()),

    Key([super_key], 'q', lazy.window.kill()),

    Key([super_key], 'p', lazy.spawn(app_launcher)),
    Key([super_key], 'Return', lazy.spawn(terminal)),
    Key([super_key], 'e', lazy.spawn(file_manager_gui)),
    Key([super_key], 'l', lazy.spawn(lock_command)),
]


for group in groups:
    # Switch group
    keys.append(Key([super_key], group.name, lazy.group[group.name].toscreen()))
    # Move window to diff group without switch
    keys.append(
        Key(
            [super_key, alt], group.name, lazy.window.togroup(group.name, switch_group=False)
        )
    )
    # Move window to diff group and switch
    keys.append(
        Key(
            [super_key, alt, control], group.name, lazy.window.togroup(group.name, switch_group=True)
        )
    )
