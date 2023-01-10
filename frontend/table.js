data = [{"Vorname":"test","Name":"maister","Strasse":"maintreet 5","PLZ":"32442","Ort":"Hausen","Email":"sepp@mailer.de","Telefon":"0175988397398","Newslist":["Fersnseher","Drucker"]}, {"Vorname":"tnochmal","Name":"maister","Strasse":"maintreet 5","PLZ":"32442","Ort":"Hausen","Email":"sepp@mailer.de","Telefon":"0175988397398","Newslist":["Fersnseher","Drucker"]}]

function clicklogout(target) { // Target refers to the clicked element
	location.href='index.html';
  };


const token = localStorage.getItem("token");
console.log(token)

fetch("http://localhost:5000/get_all_users", {
	method: "get",
	headers: { "Content-Type": "application/json", "Token": token }
	})

  .then(res => res.json())
  .then(json => {
	console.log(json)
  })
  .catch(err => alert(err))


for (var i = 0; i < data.length; i++) {
	document.write('<tr class="data-table-row">');
	for (key in data[i]) {
  	document.write('<td class="table-datacell datatype-string">' + data[i][key] + '</td>');
  }
	document.write('</tr>');
}