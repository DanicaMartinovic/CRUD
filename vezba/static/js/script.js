const modal = document.getElementById("myModal");

function openForm() {
  document.getElementById("myModal").style.display = "block";
}
function closeForm() {
  document.getElementById("myModal").style.display = "none";
}
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}