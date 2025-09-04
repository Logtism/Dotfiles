from .keys import super_key, alt, control
from libqtile.config import Drag
from libqtile.lazy import lazy


follow_mouse_focus = False
bring_front_click = False
cursor_wrap = False


left_click = 'Button1'
middle_click = 'Button2'
right_click = 'Button3'


mouse = [
    Drag(
        [super_key], middle_click,
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [super_key], right_click,
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    )
]
