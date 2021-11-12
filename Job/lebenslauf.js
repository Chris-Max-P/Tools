window.onload = function() {
  initLebenslauf();
}

let lebenslauf_dict = {}; //TODO read JSON from file

function initLebenslauf() {
  let lebenslauf_html = ``;
  for (const [station, start_to_end] of Object.entries(lebenslauf_dict)) {
    lebenslauf_html += `
      <div class="container left">
        <div class="content">
          <h2>${start_to_end}</h2>
          <p>${station}</p>
        </div>
      </div>`;
  }
  document.getElementById('timeline').innerHTML =lebenslauf_html;
}