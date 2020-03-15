FOLDER_SERVER='falcon_server'
FOLDER_CLIENT='falcon_client'

pushd .
cd $FOLDER_SERVER
source venv/bin/activate
screen -dmS flask_server flask run --host=0.0.0.0
popd
pushd .
cd $FOLDER_CLIENT
screen -dmS flask_client sudo python3 -m http.server 8080
popd
source ~/.bashrc

sleep 2
screen -ls
