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
}

qtile() {
    window_manager_common

    rm -r $CONFIG_DIR/qtile
    ln -s $PWD/qtile/qtile $CONFIG_DIR/qtile
    echo "Installed qtile config"
}

printf "1) qtile\n> "
read option

if [ $option -eq "1" ]; then
    qtile
else
    echo "$option is not a valid option."
fi
