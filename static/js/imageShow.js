//var points = [];
var currentLocation = "";
var found = [];
var image_name = "";


function show(evt, linkName) {
  currentLocation = linkName;
  found = [];

  let i, tablinks;
  //update select style  
  tablinks = document.getElementsByClassName("imglink");
  for (i = 0; i < 5; i++) {
    tablinks[i].className = tablinks[i].className.replace("w3-grey", "");
  }


  evt.currentTarget.className += " w3-grey";
  document.getElementById("tips").innerHTML = "<span style='font-size: 20px; font-family: Georgia,sans-serif'>Click the image to choose unsafely behavior at <b>" + evt.currentTarget.id + "<b></span>";
  image_name = "<b>"+evt.currentTarget.id+"</b>";

  //canvas render
  let canvas = document.getElementById("gameCanvas");
  console.debug("canvas ", canvas);
  let ctx = canvas.getContext("2d");


  ctx.clearRect(100, 0, 1280, 700);
  let image = new Image();
  image.src = "/static/images/game/" + linkName + ".png";
  console.debug("image ", image);
  image.onload = () => {
    console.debug("image load");
    ctx.drawImage(image, 100, 0, 1280, 700);

    //drawAnswers(ctx, currentLocation);
  };
}

// Click on the first tablink on load
document.getElementsByClassName("imglink")[0].click()

let drawCircle = function(ctx, x, y, color) {
  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.arc(x, y, 10, 0, 2*Math.PI);
  ctx.fill();
};

// for debug
let drawAnswers = function(ctx, location) {
  console.debug("draw answers ", points);
  for(const point of points) {
    if (point.location != location) {
      continue;
    }

    ctx.beginPath();
    let x = point.x - point.width / 2.0;
    let y = point.y - point.height / 2.0;
    ctx.rect(x, y, point.width, point.height);
    ctx.stroke();
  }

};

let getLocationAnswers = function(location) {
  let result = [];
  for(const point of points) {
    if (point.location == location) {
      result.push(point);
    }
  }
  return result;
};


let getAnswer = function(location, x, y) {
  for(const point of points) {
    if (location != point.location) {
      continue;
    }
    let x_min = point.x - point.width / 2.0;
    let x_max = point.x + point.width / 2.0;
    let y_min = point.y - point.height / 2.0;
    let y_max = point.y + point.height / 2.0;

    if (x < x_max && x > x_min && y > y_min && y < y_max) {
      console.debug("hit ", point);
      return point;
    }
  }

  return null;
};


document.getElementById("gameCanvas").addEventListener("click", function(ev) {
  let canvas = document.getElementById("gameCanvas");
  let ctx = canvas.getContext("2d");

  let left = canvas.offsetLeft + canvas.clientLeft;
  let top = canvas.offsetTop + canvas.clientTop;
  console.debug("left ", left, ", top ", top);
  let x = ev.offsetX;
  let y = ev.offsetY;
  let tipsContainer = document.getElementById("tips");
  tipsContainer.innerHTML = image_name;
  //drawCircle(ctx, x, y, "#FF0000");

  let answer = getAnswer(currentLocation, x, y);


  if (answer != null) {
    ctx.fillStyle = "#FFFF00";
    ctx.font = "50px Georgia";
    ctx.fillText(answer.id, answer.x, answer.y);

    found.push(answer);

    let answers = getLocationAnswers(currentLocation);

    tipsContainer.innerHTML = "<span style='font-size: 20px; font-family: Georgia,sans-serif'>At "+ image_name + " workplace, you have found " + found.length + "/"  + answers.length + "</span><br> <br>";
    tipsContainer.innerHTML = tipsContainer.innerHTML + "<span style='font-size: 20px; font-family: Georgia,sans-serif'> Number "+ answer.id + " shows the safety hazard: <b>"+ answer.answer+"</b></span>";

    if(found.length == answers.length){
      let winBox = "";
      win
    }
  }else{
    tipsContainer.innerHTML = "<span style='font-size: 20px; font-family: Georgia,sans-serif'>Wrong Answer, Please Choose Again!</span>"
  }



});
