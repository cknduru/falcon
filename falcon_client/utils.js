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
	let myJson;
  	const response = await fetch(getServerIp())
  						   .then(response => response.json())
  						   .then(response => CallbackdisplayDevices(response));

  	return myJson;
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
  	var btn = document.getElementById("dropdownMenuButton");
  	toggleVisibility("dropdownMenuButton", "block");
  	btn.innerHTML = `${node.device_name}@${node.location}`;
}

function fillIPField()
{
	document.getElementById("serverField").value = getServerIp();
	toggleVisibility("dropdownMenuButton", "none");
}