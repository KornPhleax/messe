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
  
  const json = JSON.stringify(props);
  console.log(json);
  location.href = "danke.html"

  
}

