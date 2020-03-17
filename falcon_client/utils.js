function toggleVisibility(component, show)
{
	document.getElementById(component).style.display = show;
}

function playMusic()
{
	alert("play music");
}

function toggleLights(placement)
{
	alert(`toggling lights at ${placement}`);
}

const getDevices = async () => 
{
  	const response = await fetch('http://192.168.87.189:5000');
  	const myJson = await response.json(); //extract JSON from the http response

  	document.getElementById("btnConnectServer").disabled = true;
  	
  	var btn = document.getElementById("dropdownMenuButton");
  	toggleVisibility("dropdownMenuButton", "block");
	 
	// create popover
  	btn.innerHTML = `${myJson.device_name}@${myJson.location}`;
}

function fillIPField()
{
	document.getElementById("serverField").value = '192.168.87.189:5000';
	toggleVisibility("dropdownMenuButton", "none");
}