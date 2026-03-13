password = ''
correct_password = "12345"
i=0

while(i<5):
    password = int(input(("Entre password")))
    if password == correct_password:
        print("Access granted") 
    else:
        print("Access denied")
        

    

    