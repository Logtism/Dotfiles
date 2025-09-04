from libqtile import widget, bar


top_bar_size = 26
top_bar_opacity = 0.8


colors = {
    'background': ['#2F343F', '#2F343F'],
    'text': ['#a9a9a9', '#a9a9a9'],
    'bold_text': ['#c0c5c3', '#c0c5c3'],
    'inactive_text': ['#f3f4f5', '#f3f4f5'],
    'icon': ['#3384d0', '#3384d0']
}


widget_defaults = {
    'font': 'Noto Sans',
    'background': colors['background'],
    'foreground': colors['text']
}


def widget_args(**kwargs):
    return {**widget_defaults, **kwargs}


def sep():
    return widget.Sep(
        **widget_args(
            padding=10,
            foreground=colors['bold_text']
        )
    )


def icon(icon_text):
    return widget.TextBox(
        **widget_args(
            font='FontAwesome',
            fontsize=16,
            text=icon_text,
            padding=0,
            foreground=colors['icon']
        )
    )


def get_widgets(primary):
    widgets = []

    widgets.append(
        widget.GroupBox(
            **widget_args(
                font='FontAwesome',
                fontsize=16,
                margin_x=0,
                border_width=0,
                disable_drag=True,
                use_mouse_wheel=False,
                highlight_method='text',
                foreground=colors['bold_text'],
                active=colors['text'],
                inactive=colors['inactive_text'],
            )
        )
    )
    widgets.append(sep())
    widgets.append(
        widget.CurrentLayout(
            **widget_args(
                font='Noto Sans Bold',
                foreground=colors['bold_text']
            )
        )
    )
    widgets.append(sep())
    widgets.append(widget.WindowName(**widget_args()))
    widgets.append(widget.Spacer(**widget_args(length=bar.STRETCH)))
    widgets.append(sep())
    widgets.append(icon(''))
    widgets.append(
        widget.GenPollCommand(
            **widget_args(
                cmd='uname -r',
                shell=True,
                update_interval=3600
            )
        )
    )
    widgets.append(
        widget.GenPollCommand(
            **widget_args(
                cmd='PURGE_COUNT="$(vkpurge list | wc -l)"; if [ $PURGE_COUNT -ne "0" ]; then echo "($PURGE_COUNT)"; fi',
                shell=True,
                update_interval=3600
            )
        )
    )
    widgets.append(sep())
    widgets.append(icon(''))
    widgets.append(
        widget.CPU(
            **widget_args(
                format='{freq_current:.2f}GHz {load_percent:.1f}%',
                core='all',
                update_interval=1
            )
        )
    )
    widgets.append(sep())
    widgets.append(icon(''))
    widgets.append(
        widget.Memory(
            **widget_args(
                format='{MemUsed:.0f}MB/{MemTotal:.0f}MB',
                update_interval=1
            )
        )
    )
    widgets.append(sep())
    widgets.append(icon(''))
    widgets.append(
        widget.Net(
            **widget_args(
                prefix='M',
                format='{down:.2f}{down_suffix} {up:.2f}{up_suffix}',
                update_interval=1
            )
        )
    )
    widgets.append(sep())
    widgets.append(icon(''))
    widgets.append(
        widget.Clock(
            **widget_args(
                format='%a %Y-%m-%d %I:%M:%S %p'
            )
        )
    )
    widgets.append(sep())
    if primary:
        widgets.append(widget.Systray(**widget_args()))

    return widgets


def get_bar(primary):
    return bar.Bar(
        widgets=get_widgets(primary),
        size=top_bar_size,
        opacity=top_bar_opacity
    )
