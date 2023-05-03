//var points = [];
let currentLocation = "";
let found = [];
let image_name = "";


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
  document.getElementById("tips").innerHTML = "<span style='font-size: 20px; font-family: Georgia,sans-serif'>You have found <b>0 / 0</b></span><br> <br>";
  image_name = evt.currentTarget.id;



  //canvas render
  let canvas = document.getElementById("gameCanvas");
  console.debug("canvas ", canvas);
  let ctx = canvas.getContext("2d");


  ctx.clearRect(0, 0, 1080, 700);
  let image = new Image();
  image.src = "/static/images/game/" + linkName + ".png";
  console.debug("image ", image);
  image.onload = () => {
    console.debug("image load");
    ctx.drawImage(image, 0, 0, 1080, 700);

    //drawAnswers(ctx, currentLocation);

  };
  return image_name;
}

// Click on the first tablink on load
document.getElementsByClassName("imglink")[0].click()

function display_answer_image(){
  window.location.href = 'Game_Answers'
}

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
      if (isFound(point) == false) {
        return point;
      } else {
        return "Already Found";
      }
      return point;
    }
  }

  return null;
};

let isFound = function(current) {
  for(const point of found) {
    if (point.x == current.x && point.y == current.y && point.location == current.location) {
      return true;
    }
  }
  return false;
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

  //drawCircle(ctx, x, y, "#FF0000");

  let answer = getAnswer(currentLocation, x, y);

  if(answer == "Already Found"){
    tipsContainer.innerHTML = "<span style='font-size: 20px; font-family: Georgia,sans-serif'>Already Found, Please Choose Again!</span>"
  }else {
    if (answer != null) {
      ctx.fillStyle = "#FFFFFF";
      ctx.font = "20px Georgia";
      ctx.fillText(answer.answer, answer.x - 20, answer.y - 20);

      /*if (confirm(answer.answer) === true) {
          confirm.hide();

      }*/

      found.push(answer);

      let answers = getLocationAnswers(currentLocation);

      tipsContainer.innerHTML = "<span style='font-size: 20px; font-family: Georgia,sans-serif'>You have found <b>" + found.length + "/" + answers.length + "</b></span><br> <br>";
      tipsContainer.innerHTML = tipsContainer.innerHTML + "<span style='font-size: 20px; font-family: Georgia,sans-serif'> Number " + answer.id + " shows the safety hazard: <b>" + answer.answer + "</b></span>";


      if (found.length === answers.length) {
        if (confirm("Congratulations！You Found All Safety Hazards!") === true) {
          window.location.href = 'Game_Answers'

        } else {
          confirm.hide();
        }
      }
    } else {
      tipsContainer.innerHTML = "<span style='font-size: 20px; font-family: Georgia,sans-serif'>Wrong Answer, Please Choose Again!</span>"
    }

  }

});



