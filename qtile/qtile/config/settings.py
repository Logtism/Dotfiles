from . import bars

# Config
num_of_screens = 1
bar_type = bars.basic
battery = False


# Apps
terminal = 'alacritty'
editor = 'nvim'
app_launcher = "dmenu_run -fn 'Noto Sans' -nb '#2F343F' -sb '#006699' -nf '#006699' -sf '#fff'"
file_manager_term = 'ranger'
file_manager_gui = 'dbus-run-session thunar'
lock_command = 'light-locker-command -l'
