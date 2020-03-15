const getDevices = async () => 
{
  	const response = await fetch('http://192.168.87.189:5000');
  	const myJson = await response.json(); //extract JSON from the http response
  	var btn=document.createElement("button");
	 
	// create popover
  	btn.innerHTML = `${myJson.device_name}@${myJson.location}`;
  	btn.type = "button";
  	btn.className = "btn btn-primary btn-sm";
  	btn.id="node_1";
  	var hover_container = document.getElementById("node_popover");
  	hover_container.appendChild(btn);

	jQuery("#node_1")
	 .popover({
	   trigger: 'click',
	   title: '',
	   content: 'Turn on relay',
	   placement: 'right'
	});
}

function fillIPField()
{
	document.getElementById("serverField").value = '192.168.87.189:5000';
}