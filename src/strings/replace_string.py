username = input("Enter your username: ")
template_string = "Hello <<username>>, How are you?"
if(len(username) < 3) :
  print("User name should be atleast 3 characters.")
else: 
  print(template_string.replace("<<username>>",username))