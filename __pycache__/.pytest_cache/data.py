def check_number():
  """Checks if a given number is positive, negative, or zero."""

  number = int(input("Enter a number: "))

  if number > 0:
    print("Positive")
  elif number < 0:
    print("Negative")
  else:
    print("Zero")

if __name__ == "__main__":
  check_number()