// Get DOM elements
const input = document.querySelector(".input");
const buttons = document.querySelectorAll(".button");

// Add event listeners to all buttons
buttons.forEach((button) => {
  button.addEventListener("click", () => handleButtonClick(button.textContent));
});

// Handle button clicks
function handleButtonClick(value) {
  if (value === "C") {
    // Clear the input
    input.value = "";
  } else if (value === "=") {
    // Calculate the result
    calculateResult();
  } else {
    // Append the value to the input
    input.value += value;
  }
}

// Calculate using the Flask API
async function calculateResult() {
  const expression = input.value.trim();

  if (!expression) {
    alert("Please enter a calculation");
    return;
  }

  try {
    // Parse the expression into num1, operator, num2
    const parsed = parseExpression(expression);
    if (!parsed) {
      throw new Error("Invalid expression format. Use format like 12+34");
    }

    // Call your Flask API
    const response = await fetch("http://127.0.0.1:5000", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        num1: parsed.num1,
        operator: parsed.operator,
        num2: parsed.num2,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || "Error in calculation");
    }

    // Display the result based on your Flask response format
    if (data.status === "success") {
      input.value = data.result;
      console.log("Calculation:", data.calculation);
    } else {
      throw new Error(data.message || "Unknown error occurred");
    }
  } catch (error) {
    alert(`Error: ${error.message}`);
    console.error("Calculation error:", error);
  }
}

// Helper function to parse expression into components
function parseExpression(expression) {
  // Enhanced regex to handle decimals and negative numbers
  const match = expression.match(/(-?\d+\.?\d*)([+\-*/%])(-?\d+\.?\d*)/);

  if (!match || match.length < 4) {
    return null;
  }

  return {
    num1: match[1], // Keep as string to let Flask handle conversion
    operator: match[2],
    num2: match[3],
  };
}
