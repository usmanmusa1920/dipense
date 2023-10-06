#!/bin/bash
home="$HOME"

echo
echo -n "Who: "
echo
who
echo

# Shell function are a way to group command for later execution using a single name for the group. They are executed just like a regular command, when a name of a function is called the list of command associated within that function will execute.

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
echo
report_disk_space
echo
# report_home_space
# -------- OR -------
# "$(report_uptime)"
# echo
# "$(report_disk_space)"
# echo
# "$(report_home_space)"


# To see if whether a command you type on terminal is executed without error, type `echo $?` (it is return code)
# if it shows 0, that mean "no error i.e true"
# if it shows 1 or any in between 1 - 255, that mean "error occured i.e false"

# NB:
# 0 is positive answer
# between 1 - 255 is negative answer


# man test

# with test command they are in -f, -e, -eq, -x, etc
# test command usually have single opening and closing bracket [ ]

# with compound command they are in &&, ||, !, etc
# compound command usually have double opening and closing bracket [[ ]]
# Check command-line argument


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
