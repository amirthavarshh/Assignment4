user_input=input("enter text to write to the file:")
with open(user_input,"w") as file:
    file.write(user_input + "\n")
additional_input=input("enter additional text to append:")
with open(user_input,"a") as file:
    file.write(additional_input + "\n")
print("final content of output.txt:")
with open(user_input,"r") as file:
    content=file.read()
    print(content)
