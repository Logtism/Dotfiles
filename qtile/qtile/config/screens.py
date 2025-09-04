from .settings import num_of_screens, bar_type
from libqtile.config import Screen
from libqtile import bar


screens = []


for i in range(num_of_screens):
    screens.append(Screen(top=bar_type.get_bar(primary=i==0)))
