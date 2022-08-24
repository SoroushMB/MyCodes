attempts = 0
correct_pin = "1986"

while attempts < 3:
	entered_pin = input("Enter Pin: ")
	if entered_pin == correct_pin:
		print("You've successfully logged in!")
		break
	else:
		print("Incorrect! Try again...")
		attempts += 1
	if attempts >= 3:
		print("You failed to enter the password!")

			
				
					
						
								