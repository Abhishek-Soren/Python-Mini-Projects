#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#loop through names in the file
with open("./Input/Names/invited_names.txt", mode="rt") as names:
    for name in names:
        curr_name = name.strip() #so that there no next line attached
        with open("./Input/Letters/starting_letter.txt", "rt") as letter_format:
            text = letter_format.read()
            new_text = text.replace("[name]", curr_name)

        with open(f"./Output/ReadyToSend/letter_for_{curr_name}.txt", "w") as letter_send:
             letter_send.write(new_text)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp