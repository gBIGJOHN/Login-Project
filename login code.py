email = input("Enter your email: ")

if email == 'fake@gmail.com':
    is_correct = True
else:
    is_correct = False

if is_correct:
    print("Email is CORRECT")
else:
    print("Email is INCORRECT")

password = input('Enter your password: ')

if password == '1234':
    is_correct = True
else:
    is_correct = False

if is_correct:
    print('Password is CORRECT')
else:
    print('Password is INCORRECT')

question = input("What is 5 + 3? ")

if question == "8":
    print("You passed the test. You're not a robot!")
else:
    print("Hmm... that’s suspicious. Are you a robot?")

username = input("Enter your username: ")

if username == "username":
    print("Login successful. Now verify your identity.")

    code = "1234"
    user_code = input("Enter the 4-digit verification code: ")

    if user_code == code:
        print("Access granted!")
    else:
        print("Incorrect code. Access denied.")
else:
    print("Wrong username or password.")
