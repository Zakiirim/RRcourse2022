#Exercise 3 
#Write names of all US states in UPPERCASE and lowercase to a file. 
#Write how to do this without typing all 50 names manually. 
#Separate code from input and from output.

#there is a state object in base R. We can use toupper and tolower functions
toupper(state.name)
tolower(state.name)

states_names <- data.frame(uppercase = toupper(state.name), 
                           lowercase = tolower(state.name))

write.csv(states_names, "us_state_names.csv")
