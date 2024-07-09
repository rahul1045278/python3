import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols):
  """
  Generates a random password based on user-specified criteria.

  Args:
      length: The desired length of the password.
      include_uppercase: True if uppercase letters should be included.
      include_lowercase: True if lowercase letters should be included.
      include_digits: True if digits should be included.
      include_symbols: True if symbols should be included.

  Returns:
      A randomly generated password meeting the specified criteria.
  """
  # Define character sets based on user options
  characters = ""
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_lowercase:
    characters += string.ascii_lowercase
  if include_digits:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation

  # Validate character set selection
  if not characters:
    raise ValueError("Please select at least one character type (uppercase, lowercase, digits, or symbols).")

  # Generate random password
  password = ''.join(random.choice(characters) for _ in range(length))
  return password

# Get user input
while True:
  try:
    length = int(input("Enter desired password length (minimum 8 characters): "))
    if length < 8:
      raise ValueError("Password length must be at least 8 characters.")
    include_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
    include_lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
    include_digits = input("Include digits (y/n)? ").lower() == 'y'
    include_symbols = input("Include symbols (y/n)? ").lower() == 'y'
    break
  except ValueError as e:
    print(e)
    print("Please enter valid values.")

# Generate and display password
password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
print(f"Your generated password is: {password}")
