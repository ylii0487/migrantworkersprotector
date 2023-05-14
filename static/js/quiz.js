// Get the HTML elements
const questionContainers = document.querySelectorAll(".question-container");
const answerContainers = document.querySelectorAll(".answer-container");
const prevButton = document.getElementById("prev-btn");
const nextButton = document.getElementById("next-btn");
const submitButton = document.getElementById("submit-btn");
const resultContainer = document.getElementById("result-container");
const resultText = document.getElementById("result-text");

// Set the initial question index and disable the previous button
let currentQuestion = 0;
prevButton.disabled = true;

// Array to store the user's answers
const userAnswers = [];

// Function to show a specific question and hide the others
function showQuestion(questionIndex) {
  questionContainers.forEach((container, index) => {
    if (index === questionIndex) {
      container.style.display = "block";
    } else {
      container.style.display = "none";
    }
  });
}

// Function to show the previous question if the user has answered it
function showPreviousQuestion() {
  if (currentQuestion === 0) {
    return; // Do not allow going back from the first question
  }

  currentQuestion--;

// Check if the user has already answered the previous question
  while (userAnswers[currentQuestion] === undefined && currentQuestion > 0) {
    currentQuestion--; // Skip unanswered questions
  }

  showQuestion(currentQuestion);

  if (currentQuestion === 0) {
    prevButton.disabled = true;
  }

  nextButton.style.display = "inline-block";
  submitButton.style.display = "none";

// Select the user's previous answer
  const selectedAnswer = answerContainers[currentQuestion].querySelector(input[value = "${userAnswers[currentQuestion]}"]);
  selectedAnswer.checked = true;
}

// Function to show the next question based on the user's previous answer
function showNextQuestion() {
  const selectedAnswer = answerContainers[currentQuestion].querySelector("input:checked");

  if (selectedAnswer === null) {
    alert("Please select an answer");
    return;
  }

  userAnswers[currentQuestion] = selectedAnswer.value;

  let nextQuestionIndex;

  if (selectedAnswer.value === "Financial Problem") {
    nextQuestionIndex = currentQuestion + 1;
  } else if (selectedAnswer.value === "Emotional Problem") {
    nextQuestionIndex = currentQuestion + 2;
  } else if (selectedAnswer.value === "Safety Problem") {
    nextQuestionIndex = currentQuestion + 3;
  } else {
    nextQuestionIndex = currentQuestion + 4;
  }

  currentQuestion = nextQuestionIndex;

  if (currentQuestion >= questionContainers.length) {
    currentQuestion = questionContainers.length - 1;
  }

  showQuestion(currentQuestion);

  prevButton.disabled = false;

  if (currentQuestion === questionContainers.length - 1) {
    nextButton.style.display = "none";
    submitButton.style.display = "inline-block";
  }

// Select the user's previous answer if they go back
  if (userAnswers[currentQuestion] !== undefined) {
    const selectedAnswer = answerContainers[currentQuestion].querySelector(input[value = "${userAnswers[currentQuestion]}"]);
    selectedAnswer.checked = true;
  }
}

function showResult() {
  let help_type = document.querySelector('input[name="help_type"]:checked').value;
  let help_topic = document.querySelector('input[name="topic"]:checked').value;
  let help_fix = document.querySelector('input[name="fix"]:checked').value;

  let url = `/AskForHelp_Result/${help_type}/${help_topic}/${help_fix}`;

  // Make an HTTP GET request to the backend with the URL parameter
  fetch(url, {
    method: 'GET'
  })
  .then(response => response.text())
  .then(data => {
    // Handle the response from the backend
    resultText.textContent = 'Submit';
    resultContainer.style.display = "block";
  })
  .catch(error => {
    console.error('Error:', error);
  });
}

function redirectToResult() {
  let help_type = document.querySelector('input[name="help_type"]:checked').value;
  let help_topic = document.querySelector('input[name="topic"]:checked').value;
  let help_fix = document.querySelector('input[name="fix"]:checked').value;
  window.location.href = "/AskForHelp_Result/" + help_type+"/" + help_topic+"/" + help_fix;
}

// Event listeners for the buttons
prevButton.addEventListener("click", showPreviousQuestion);
nextButton.addEventListener("click", showNextQuestion);
submitButton.addEventListener("click", showResult);

// Show the first question
showQuestion(currentQuestion);
