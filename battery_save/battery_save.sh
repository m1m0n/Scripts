#!/bin/bash

display_usage() {  
        echo -e "Usage: battery_save.sh < n:ON || f:OFF || c:current mode >"
        } 

display_current_mode(){
        cmd=`cat /proc/sys/vm/laptop_mode`
        if [ $cmd = "1" ]
        then
            echo -e "Battery Save Mode is \e[1;32mON\e[0m"
        elif [ $cmd = "0" ]
        then
            echo -e "Battery Save Mode is \e[1;31mOFF\e[0m" 
        fi
}

if [  $# -ne 1 ] 
then    
        display_usage
        exit 1
else    
        if [ ${1,,} = "n" ]
        then
            sudo su -c "echo 1 > /proc/sys/vm/laptop_mode"
            notify-send "Conservation Mode" "ON"
            echo -e "Battery Save Mode is \e[1;32mON\e[0m"

        elif [ ${1,,} = "f" ]
        then
            sudo su -c "echo 0 > /proc/sys/vm/laptop_mode"
            notify-send "Conservation Mode" "OFF"
            echo -e "Battery Save Mode is \e[1;31mOFF\e[0m"

        elif [ ${1,,} = "c" ]
        then
            display_current_mode
            exit 1

        else
            display_usage
            exit 1
        fi
fi
