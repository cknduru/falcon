if [[ "$1" == '-i' ]]; then
    echo 'if [ -z "$STY" ]; then cd '"$(pwd)"'&&./launch.sh -k; fi' >> ~/.bashrc
    echo 'installed start hook to .bashrc'
    return 0
fi

pkill screen

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
popd > /dev/null
source ~/.bashrc

sleep 2
screen -ls
