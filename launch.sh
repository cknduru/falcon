#!/bin/bash

if [[ "$1" == '-i' ]]; then
    (crontab -l 2>/dev/null; echo "@reboot cd /home/pi/falcon&&./launch.sh") | crontab -
    echo 'installed start hook to user crontab'
    return 0
fi

# pull updates
git_status=$(git pull)

if [[ "$git_status" != "Already up-to-date." ]]; then
    echo 'Updated Falcon'
fi

# kill any old instance of Falcon
pkill screen > /dev/null

ROOT_FOLDER="$(pwd)"
FOLDER_SERVER="$ROOT_FOLDER/falcon_server"
FOLDER_CLIENT="$ROOT_FOLDER/falcon_client"

pushd . > /dev/null
cd $FOLDER_SERVER
source venv/bin/activate
screen -dmS flask_server flask run --host=0.0.0.0
popd > /dev/null
pushd . > /dev/null
cd $FOLDER_CLIENT
screen -dmS falcon_client sudo python3 -m http.server 8080

# restore original env
deactivate

popd > /dev/null

sleep 2
screen -ls
