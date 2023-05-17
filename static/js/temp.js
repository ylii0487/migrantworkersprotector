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

document.querySelector('.dropdown-button').addEventListener('click', function() {
  this.classList.toggle('active');
});


function scrollPage() {
  if (window.scrollY === 0) {
    // User is at the top, scroll down
    window.scrollTo({
      top: document.body.offsetHeight,
      behavior: 'smooth'
    });
  } else {
    // User is at the bottom, scroll to top
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }
}

window.addEventListener('scroll', function() {
    const scrollButton = document.getElementById('scroll-button');
    const scrollIcon = document.getElementById('scroll-icon');
    if (window.scrollY > 0) {

    if ((window.innerHeight + window.scrollY) <= document.body.offsetHeight) {
        scrollIcon.className='fa fa-angle-up';
    }

  } else {
    scrollIcon.className = 'fa fa-angle-down';

  }
});



