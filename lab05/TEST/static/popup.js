function showForm(formFile) {
  fetch(formFile)
    .then(response => response.text())
    .then(data => {
      document.getElementById("popup-content").innerHTML = data;
      document.getElementById("popup-container").style.display = "block";
    });
}

function closePopup() {
  document.getElementById("popup-container").style.display = "none";
}