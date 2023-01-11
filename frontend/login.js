
  // Zurück Button
  function clickback(target) {
    location.href='index.html';
  };

  // Input Felder
  function validate(target) {

    const body = {
    "user": document.getElementById("user").value,
    "password": document.getElementById("password").value
    }

    // Try to login
    fetch("https://test.familie-michels.de/authenticate_user", {
      method: "post",
      body: JSON.stringify(body),
      headers: { "Content-Type": "application/json" }
      })

    .then(res => res.json())
    .then(json => {
      token = json.token
      if (token !== null) {
        localStorage.setItem("token",token);
        location.href = "table.html";
      }
      else {alert("Login failed")}
    })
    .catch(err => alert(err) )
    
  }