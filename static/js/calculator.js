// // Get the HTML elements
// const questionContainers = document.querySelectorAll(".question-container");
// const answerContainers = document.querySelectorAll(".answer-container");
// const prevButton = document.getElementById("prev-btn");
// const nextButton = document.getElementById("next-btn");
// const submitButton = document.getElementById("submit-btn");
// const resultContainer = document.getElementById("result-container");
// const resultText = document.getElementById("result-text");
//
// // Set the initial question index and disable the previous button
// let currentQuestion = 0;
// prevButton.disabled = true;
//
// // Function to show a specific question and hide the others
// function showQuestion(questionIndex) {
//   questionContainers.forEach((container, index) => {
//     if (index === questionIndex) {
//       container.style.display = "block";
//     } else {
//       container.style.display = "none";
//     }
//   });
// }
//
// // Function to show the previous question
// function showPreviousQuestion() {
//   currentQuestion--;
//   showQuestion(currentQuestion);
//   if (currentQuestion === 0) {
//     prevButton.disabled = true;
//   }
//   if (currentQuestion < questionContainers.length - 1) {
//     submitButton.style.display = "none";
//     nextButton.style.display = "inline-block";
//   }
// }
//
// Function to show the next question

const email_button = document.getElementById("email-button");

function calculateWage() {
  // let industry = document.querySelector('input[name="industry"]').value;
  // let employmentType = document.querySelector('input[name="employment-type"]').value;
  // let holidayPay = document.querySelector('input[name="holiday-pay"]').value;

  email_button.style.display= "inline-block";
  // if (industry !== "" && employmentType !== null && holidayPay !== null) {
  //
  //   email_button.style.display= "inline-block";
  //
  // }else{
  // alert("Please select answers");
  // }
}

// function displaySelectedValues() {
//   // Get the selected values
//   const industry = document.getElementById('industry').value;
//   const employmentType = document.querySelector('input[name="employment-type"]:checked').value;
//   const jobLevel = document.getElementById('job-level').value;
//
//   // Update the HTML elements with the selected values
//   document.getElementById('industry-value').textContent = industry;
//   document.getElementById('employment-type-value').textContent = employmentType;
//   document.getElementById('job-level-value').textContent = jobLevel;
// }

// Call the displaySelectedValues function when needed, such as on button click
document.getElementById('submit-btn').addEventListener('click', calculateWage);


// // Event listeners for the buttons
// prevButton.addEventListener("click", showPreviousQuestion);
// nextButton.addEventListener("click", showNextQuestion);
// submitButton.addEventListener("click", calculateWage);
//
// // Show the first question
// showQuestion(currentQuestion);

