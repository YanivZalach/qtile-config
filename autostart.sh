#!/bin/bash


# Function to check if a process is already running and run it if not
function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}


# Uncomment the following line if you need to change your keyboard layout to Hebrew (IL)
# setxkbmap -layout il


#Uncomment the following line if you want to start sxhkd to replace Qtile native key-bindings
#run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &



picom --config $HOME/.config/qtile/picom.conf &


#starting user applications at boot time
run chrome &
#run volumeicon &
# run thunar &  # Start Thunar file manager


# Please be cautious while adding applications to start at boot time.
# Only add applications you need on startup to avoid unnecessary resource usage.

