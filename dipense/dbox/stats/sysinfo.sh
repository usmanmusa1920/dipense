#!/bin/bash
home="$HOME"

echo
echo -n "Who: "
echo
who
echo

report_uptime () {
    # This report system up time of running
    echo -n "Report up time: "
    echo
    uptime
    return
}

report_disk_space () {
    # Function for showing system disk space
    echo -n "Report disk: "
    echo
    df -h
    return
}

report_home_space () {
    # This function display system usage for home dir
    echo -n "Report home: "
    echo
    du -sh $HOME # or
    # du -sh /home/*
    return
}

report_uptime
# "$(report_uptime)"
echo
report_disk_space
# "$(report_disk_space)"
echo
# report_home_space
# "$(report_home_space)"


# To see if whether a command type on terminal is executed without error, type `echo $?`
# if it shows 0, that mean "no error i.e true", else (1 or any in between 1 - 255), that mean "error occured i.e false"


# man test

# with test command they are in -f, -e, -eq, -x, etc
# test command usually have single opening and closing bracket [ ]

# with compound command they are in &&, ||, !, etc
# compound command usually have double opening and closing bracket [[ ]]


if [ "$1" == "baby" ]; then
    if [ -f "baby.sh" ]; then
        . baby.sh
    else
        echo
    fi
elif [ "$1" == "html" ]; then
    if [ -f "html.sh" ]; then
        . html.sh
    else
        echo
    fi
elif [ "$1" == "em" ]; then
    echo
else
    echo "Failed to run file specified ($1)."
fi
