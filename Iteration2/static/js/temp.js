function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
}

function handleChange(input) {
    if (input.value < 15) input.value = 15;
    if (input.value > 100) input.value = 100;
}





