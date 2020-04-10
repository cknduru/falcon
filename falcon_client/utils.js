function getServerIp()
{
	return 'http://192.168.87.189:5000';
}

function sendCommand(cmd)
{
	$.ajax({
	  type: "POST",
	  url: getServerIp(),
	  data: JSON.stringify({command : cmd}),
	  contentType: 'application/json',
	  success: function (response_data) { console.log(`${cmd} -> server`); }  
	});
}

const fetchData = async (ip) => 
{
  	const response = await fetch(getServerIp())
  						   .then(response => response.json())
  						   .then(response => CallbackdisplayDevices(response));

}

function toggleVisibility(component, show)
{
	document.getElementById(component).style.display = show;
}

function playMusic()
{
	sendCommand('playMusic');
}

function toggleLights(placement)
{
	sendCommand(`toggleLights ${placement}`);
}

function shutdownDevice(device)
{
	// todo: send command is currently hardcoded to only send to one device
	// this should be expanded
    if (device == 'deviceDropdownMenu1')
    {
    	sendCommand('shutdown')
    	return;
    }

    console.log(`Unknown shutdown device: ${device}`)
}

function displayDevices()
{
	// get ip from form
	let serverIp = document.getElementById("serverField").value;
	fetchData(serverIp);
}

function CallbackdisplayDevices(node)
{
	// disable connect button to prevent multiple presses
  	document.getElementById("btnConnectServer").disabled = true;
  	
  	// display drop down
  	var btn = document.getElementById("deviceDropdownMenu1");
  	toggleVisibility("deviceDropdownMenu1", "block");
  	btn.innerHTML = `${node.device_name}@${node.location}`;
}

function fillIPField()
{
	document.getElementById("serverField").value = getServerIp();
	toggleVisibility("deviceDropdownMenu1", "none");
}