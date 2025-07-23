function handleSubmit(event) {
  event.preventDefault();
  const amount = document.getElementById("amount").value;
  if (amount && amount > 0) {
    alert("You will donate: $" + amount + " USD" );
  } else {
    alert("Please enter a valid amount.");
  }
}