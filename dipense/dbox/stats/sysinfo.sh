#!/bin/bash
cat << _EOF_
<html>
    <head>
        <title>index</title>
    </head>
    <body>
        System info
    </body>
</html>
_EOF_

echo

who

echo

# NUMBER 2

# Shell function are a way to group command for later execution using a single name for the group. They are executed just like a regular command, when a name of a function is called the list of commandassociated within that function will execute

report_uptime () {
    echo -n "Report up_time "
    uptime
    return
}

report_disk_space () {
    echo -n "Report disk "
    df -h
    return
}

report_home_space () {
    echo -n "Report home "
    # du -sh /home/*
    du -sh $HOME
    return
}

report_uptime

echo

report_disk_space

echo
# ERROR
# report_home_space

# -------- OR -------

"$(report_uptime)"
"$(report_disk_space)"
# "$(report_home_space)"


sudo TIME_STAMP


# NUMBER 3

# if statement is called branching

x=8
if [ $x = 7 ]; then
     echo "Equal to 7";
elfi [[ $x == 8 ]]; then
    echo "0"
else
    echo "Does not equal";
fi

# to see if whether a command you type on terminal is executed without error, type 
# echo $?
# if it shows 0, that mean "no error i.e true"
# if it shows 1 or any in between 1 - 255, that mean "error occured i.e false"

# NB:
# 0 is positive answer
# between 1 - 255 is negative answer


# NUMBER 4

# man test

# with test command they are in -f, -e, -eq, -x, etc
# test command usually have single opening and closing bracket [ ]

# with compound command they are in &&, ||, !, etc
# compound command usually have double opening and closing bracket [[ ]]
