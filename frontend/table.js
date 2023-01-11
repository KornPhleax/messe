// Logout request
function clicklogout(target) {
	
	fetch("https://test.familie-michels.de/logout", {
	method: "get",
	headers: { "Content-Type": "application/json", "Token": token }
	})
  .then(res => {state = res.status
	if ( state == "204"){
		location.href='index.html';
	}
	else {
		alert("Logout Failed")
	}
})
  .catch(err => alert(err))

  };

// Get Token from localStorage
const token = localStorage.getItem("token");

// Send request to get data
 fetch("https://test.familie-michels.de/get_all_users", {
	method: "get",
	headers: { "Content-Type": "application/json", "Token": token }
	})

  .then(res => res.json())
  .then(json => {
	result = JSON.stringify(json)
	data = JSON.parse(result)

	// Add data to table	
	for (var i = 0; i < data.length; i++) {
		document.getElementsByClassName("data-table-content")[0].innerHTML += '<tr class="data-table-row">'
		for (key in data[i]) {
			document.getElementsByClassName("data-table-row")[i+1].innerHTML += '<td class="table-datacell datatype-string">' + data[i][key] + '</td>'
		}
		document.getElementsByClassName("data-table-content")[0].innerHTML += '</tr>'
	}

  })
  .catch(err => alert(err))




