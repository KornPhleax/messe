//data = [{"Vorname":"test","Name":"maister","Strasse":"maintreet 5","PLZ":"32442","Ort":"Hausen","Email":"sepp@mailer.de","Telefon":"0175988397398","Newslist":["Fersnseher","Drucker"]}, {"Vorname":"tnochmal","Name":"maister","Strasse":"maintreet 5","PLZ":"32442","Ort":"Hausen","Email":"sepp@mailer.de","Telefon":"0175988397398","Newslist":["Fersnseher","Drucker"]}]
//data = [{"Vorname":"Peter","Name":"Neuer","Strasse":"Siglstraße 3","PLZ":"34324","Ort":"Hausen","Email":"peter@neuer.de","Telefon":"015173837383738","Newslist":["Kameras","Monitore"]}]
function clicklogout(target) { // Target refers to the clicked element
	
	fetch("https://test.familie-michels.de/logout", {
	method: "get",
	headers: { "Content-Type": "application/json", "Token": token }
	})
  .then(res => {state = res.status
	console.log(state)
	if ( state == "204"){
		location.href='index.html';
	}
	else {
		alert("Logout Failed")
	}
})
  .catch(err => alert(err))

  };


const token = localStorage.getItem("token");


 fetch("https://test.familie-michels.de/get_all_users", {
	method: "get",
	headers: { "Content-Type": "application/json", "Token": token }
	})

  .then(res => res.json())
  .then(json => {
	result = JSON.stringify(json)
	data = JSON.parse(result)
	console.log(data)

	// Add data to table	
	for (var i = 0; i < data.length; i++) {
		console.log(i)
		document.getElementsByClassName("data-table-content")[0].innerHTML += '<tr class="data-table-row">'
		for (key in data[i]) {
			document.getElementsByClassName("data-table-row")[i+1].innerHTML += '<td class="table-datacell datatype-string">' + data[i][key] + '</td>'
		}
		document.getElementsByClassName("data-table-content")[0].innerHTML += '</tr>'
	}

  })
  .catch(err => alert(err))

  




