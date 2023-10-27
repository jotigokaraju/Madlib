#Joti Gokaraju
#Computer Science 20, P5
#10/20/2023
#MadLib Assignment
#Streamlit App To Create a Madlib Project
#Note: File Containing Random Words is From Online Library


#Import Statements
import random
import streamlit as st



#Function Definitions

#Function For Computer to Choose Words
def random_choice(type):
    
    #Pick A Random Adjective
    if type == "adjective":
        #Open Adjective File
        with open("1syllableadjectives.txt", "r") as file: 
            read_doc = file.read() 
            words = list(map(str, read_doc.split())) 
            return(random.choice(words))
    
    #Pick A Random Verb  
    elif type == "verbs":
        
        #Open Verbs File
        with open("1syllableverbs.txt", "r") as file: 
            read_doc = file.read() 
            words = list(map(str, read_doc.split())) 
            return(random.choice(words))
    
    #Pick a Random Noun
    else:
        
        #Open Nouns File
        with open("1syllablenouns.txt", "r") as file: 
            read_doc = file.read() 
            words = list(map(str, read_doc.split())) 
            return(random.choice(words))



#Function to Create Madlibs with Variables
def return_poem(peom_type, adjective_1,
    adjective_2, verb_1, verb_2,
    noun_1, noun_2, sound):
    
    if poem_type == "Old McDonald":
        st.write(f'''Old {adjective_1} McDonald had a {noun_1}, {sound}
                and on that {noun_1} he had a {noun_2}, {sound}
                with a {verb_1} {verb_1} here
                and a {verb_2} {verb_2} there,
                here a {verb_1}, there a {verb_2},
                everywhere a {verb_1} {verb_1},
                Old {adjective_2} McDonald had a {noun_1}, {sound}.''')
    
    elif poem_type == "Humpty Dumpty":      
        st.write(f'''Humpty Dumpty {verb_1} on a wall.
                Humpty Dumpty had a {adjective_1} {verb_2}.
                All the king's {noun_2} and all the king's {noun_1}
                Couldn't put Humpty together again.''')
    



#App Creation
        
#Titles     
st.header("Madlibs")
st.subheader("By Joti Gokaraju")
st.divider()


#Variables

#Select Poem to Use for Madlib
poem_type = st.selectbox(
   "What Poem Would You Like to Use",
   ("Old McDonald", "Humpty Dumpty"),
   index=None,
   placeholder="Select Poem...")
st.write('You Selected:', poem_type)


#Collect Variables for Old McDonald
if poem_type == "Old McDonald":
    st.write("If You Would Like the Computer to Choose A Word, Leave Blank (Except Sound)")
    
    #Inputs
    adjective_1 = st.text_input("Choose An Adjective (Desrciptive):", value="", key="Enter")
    adjective_2 = st.text_input("Choose Another Adjective (Descriptive):", value="", key="Enter!")
    verb_1 = st.text_input("Chose A Verb (Sound Verb):", value="")
    verb_2 = st.text_input("Chose Another Verb (Sound Verb):", value="")
    noun_1 = st.text_input("Chose A Noun (Object or Animal):", value="")
    noun_2 = st.text_input("Chose Another Noun (Object or Animal):", value="")
    sound = st.text_input("Chose A Sound (like E-I-E-I-O):", value="")

#Collect Variables for Humpty Dumpty
elif poem_type == "Humpty Dumpty":
    st.write("If You Would Like the Computer to Choose A Word, Leave Blank")
    
    #Inputs
    adjective_1 = st.text_input("Choose An Adjective (i.e. Great):", value="")
    verb_1 = st.text_input("Chose A Verb (i.e. Sat):", value="")
    verb_2 = st.text_input("Chose Another Verb (i.e. Fall):", value="")
    noun_1 = st.text_input("Chose A Noun (Group Object Noun i.e. Horses):", value="")
    noun_2 = st.text_input("Chose Another Noun (Group Object Noun i.e. Horses):", value="")
    
    #Assign Placeholder Variable to Unused Variables to Prevent Program From Crashing
    adjective_2 = "placeholder"
    sound = "placeholder"
    


#Button to Create Madlib
if st.button("Run!", type="primary"):
    
    #If Variable Boxes are Left Blank, Assign Them A Random Value By Sending Through Random Function
    if adjective_1 == "":
        adjective_1 = random_choice("adjective")
    if verb_1 == "":
        verb_1 = random_choice("verb")
    if noun_1 == "":
        noun_1 = random_choice("noun")
    if adjective_2 == "":
        adjective_2 = random_choice("adjective")
    if verb_2 == "":
        verb_2 = random_choice("verb")
    if noun_2 == "":
        noun_2 = random_choice("noun")
    
    #Divider
    st.divider()
    
    #Send Variables to Create Madlib Function
    return_poem(poem_type, adjective_1, adjective_2, verb_1, verb_2, noun_1, noun_2, sound)




#Footer
st.write("*Note: Computer Chosen Words Can Be Obscure or Vulgar at Times*")

    

