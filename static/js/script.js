function submitForm(event) {
    event.preventDefault();
    let city = document.getElementById("city").value;
    window.location.href = "/" + city;
}