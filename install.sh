#!/bin/bash

CONFIG_DIR=$HOME/.config

window_manager_common() {
    rm $HOME/.bashrc
    ln -s $PWD/common/bash/bashrc $HOME/.bashrc
    echo "Installed bash config"

    rm -r $CONFIG_DIR/fastfetch
    ln -s $PWD/common/fastfetch $CONFIG_DIR/fastfetch
    echo "Installed fastfetch config"

    rm -r $CONFIG_DIR/dunst
    ln -sf $PWD/common/dunst $CONFIG_DIR/dunst
    echo "Installed dunst config"

    rm -r $CONFIG_DIR/rofi
    ln -sf $PWD/common/rofi $CONFIG_DIR/rofi
    echo "Installed rofi config"

    rm $CONFIG_DIR/xfce4/xfconf/xfce-perchannel-xml/thunar.xml
    ln -sf $PWD/common/xfce4/xfconf/xfce-perchannel-xml/thunar.xml $CONFIG_DIR/xfce4/xfconf/xfce-perchannel-xml/thunar.xml
    echo "Installed thunar config"
}

qtile() {
    window_manager_common

    rm -r $CONFIG_DIR/qtile
    ln -s $PWD/qtile/qtile $CONFIG_DIR/qtile
    echo "Installed qtile config"
}

sway() {
    window_manager_common

    rm $CONFIG_DIR/sway
    ln -s $PWD/sway/sway $CONFIG_DIR/sway
    echo "Installed sway config"

    rm $CONFIG_DIR/swayidle
    ln -s $PWD/sway/swayidle $CONFIG_DIR/swayidle
    echo "Installed swayidle config"

    rm $CONFIG_DIR/waybar
    ln -s $PWD/sway/waybar $CONFIG_DIR/waybar
    echo "Installed waybar config"

    rm $CONFIG_DIR/xdg-desktop-portal
    ln -s $PWD/sway/xdg-desktop-portal $CONFIG_DIR/xdg-desktop-portal
    echo "Installed portals config"
}

printf "1) qtile 2) sway\n> "
read option

if [ $option -eq "1" ]; then
    qtile
elif [ $option -eq "2" ]; then
    sway
else
    echo "$option is not a valid option."
fi
