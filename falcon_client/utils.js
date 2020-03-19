function getServerIp()
{
	return 'http://192.168.87.189:5000';
}

function sendCommand(cmd)
{
	$.ajax({
	  type: "POST",
	  url: getServerIp(),
	  data: {cmd : 'testcmd'},
	});
}

function toggleVisibility(component, show)
{
	document.getElementById(component).style.display = show;
}

function playMusic()
{
	sendCommand('bah');
	alert("play music");
}

function toggleLights(placement)
{
	alert(`toggling lights at ${placement}`);
}

const displayDevices = async () => 
{
  	const response = await fetch(getServerIp());
  	const myJson = await response.json(); // extract JSON from the http response

  	document.getElementById("btnConnectServer").disabled = true;
  	
  	// display drop down
  	var btn = document.getElementById("dropdownMenuButton");
  	toggleVisibility("dropdownMenuButton", "block");
  	btn.innerHTML = `${myJson.device_name}@${myJson.location}`;
}

function fillIPField()
{
	document.getElementById("serverField").value = getServerIp();
	toggleVisibility("dropdownMenuButton", "none");
}