if [[ "$1" == '-i' ]]; then
    echo 'if [ -z "$STY" ]; then cd '"$(pwd)"'&&./launch.sh; fi' >> ~/.bashrc
    echo 'installed start hook to .bashrc'
    return 0
fi

# pull updates and start new instance if updates are available
git_status=$(git pull)

if [[ "$git_status" != "Already up-to-date." ]]; then
    # exec creates new process instance and exits this one
    exec launch.sh
fi

# kill any old instance of Falcon
pkill screen > /dev/null

FOLDER_SERVER='falcon_server'
FOLDER_CLIENT='falcon_client'

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
