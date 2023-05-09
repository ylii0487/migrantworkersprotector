function show(evt, linkName) {
  var i, x, tablinks;
  x = document.getElementsByClassName("myImage");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  imglinks = document.getElementsByClassName("imglink");
  for (i = 0; i < x.length; i++) {
    imglinks[i].className = imglinks[i].className.replace("w3-grey", "");
  }
  document.getElementById(linkName).style.display = "block";
  evt.currentTarget.className += " w3-grey";
}

// Click on the first tablink on load

document.getElementsByClassName("imglink")[0].click()