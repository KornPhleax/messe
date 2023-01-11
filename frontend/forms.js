const checkbox = document.querySelector('.my-form input[id="terms"]');
const btns = document.querySelectorAll(".my-form button");


checkbox.addEventListener("change", function() {
  const checked = this.checked;
  for (const btn of btns) {
    checked ? (btn.disabled = false) : (btn.disabled = true);
  }
});

function clicklogin(target) { // Target refers to the clicked element
  location.href='login.html';
};


// Get input from forms and parse to json
const form = document.forms[0];

form.onsubmit = e => {
  e.preventDefault();
  const fd = new FormData();
  const props = {};
  const news = [];
  for (let element of form.elements) {
    if (element.type == "checkbox" && element.checked && element.id !== "terms"){
      news.push(element.name);
    }
    if (element.type !== "submit" && element.type !== "checkbox" && element.value !== "" ){
      props[element.name] = element.value;
    }

  }
  props["Newslist"] = news;
  
  const body = JSON.stringify(props);
  console.log(body);

  fetch("https://test.familie-michels.de/add_person", {
    method: "post",
    body: body,
    headers: { "Content-Type": "application/json" }
    })

  .then(res => res.json())
  .then(json => {
    console.log(json)
    if (json.message == "User was created" ){
      location.href = "danke.html"
    }
    else {
      alert("Ein Fehler ist aufgetreten, bitte versuchen Sie es erneut")
    }
  })
  .catch(err => alert(err) )
  
}

  //



