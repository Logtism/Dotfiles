from libqtile import layout


layout_theme = {
    'margin': 5,
    'border_width': 2,
    'border_focus': '#5e81ac',
    'border_normal': '#4c566a'
}


layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**{**layout_theme, **{'margin': 0}}),
    # layout.Bsp(**layout_theme),
    # layout.MonadWide(**layout_theme),
]
