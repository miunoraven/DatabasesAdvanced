#!/bin/bash

mongo_status= 'sudo systemctl status mongod'

echo "${mongo_status}"

if [[ "${mongo_status}" == *"active/running"* ]]

then

    echo "MongoDB is running"

else

    sudo systemctl start mongod
    echo "start MongoDB"

fi