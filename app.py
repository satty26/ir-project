#import statements
import os
from collections.abc import Sequence
import math
import glob
import streamlit as st
import requests
from PIL import Image

st.set_page_config(
    page_title = "Information Retrieval System",
    page_icon = "🔍",
)

APP_FOLDER = "./"

txtCounter = len(glob.glob1(APP_FOLDER,"*.txt"))

# Initialising Dictionaries depending on number of text files
dictlist = [dict() for x in range(txtCounter)]

# Declaring maximum number of words in the file
file_size = 500000

file_name=[]

file_counter = -1

# All files in the desired folder
for files in os.listdir(APP_FOLDER):
    # Only checking for .txt files
    if files.endswith(".txt"):
        file_counter=file_counter+1
        
        with open(os.path.join(APP_FOLDER, files),'r') as file:
            
            file_name.append(files)
            
            word_counter=0           
            for line in file:
                for word in line.split():
                    # Converting whole string to uppercase
                    word=word.upper()
                    # Counting number of words
                    word_counter = word_counter+1
                    
                    # Checking if last character of word is not punctuation
                    last_char = word[-1]
#                     print(word)
                    empty_list=[]
                    # " . " will give wrong answer, so check it
                    if  ((not('A'<=last_char and last_char<='Z')) and(not('0'<=last_char and last_char<='9')) and len(word)!=1) :
                        dictlist[file_counter].setdefault(word[:-1],[]).append(word_counter)
            
                    else:
                        dictlist[file_counter].setdefault(word,[]).append(word_counter)

def answer(query):

    query=query.upper()
    # Splitting the query in parts
    words_list = []
    for words in query.split():
        last_char = words[-1]
        if  ((not('A'<=last_char and last_char<='Z')) and(not('0'<=last_char and last_char<='9')) and len(words)!=1) :
            words_list.append(words[:-1])
    #             words_list.append(words[-1])
        else:
            words_list.append(words)

    # Checking words in Dictionary
    query_len=len(words_list)
    # Checking for the sentence in every dictionary
    dic_num = -1
    print_found_message = 0
    for dic in dictlist:
        flag=1
        dic_num = dic_num+1
        ans_bitset=[0]*file_size
    #         print(ans_bitset)
        word_num = -1
        for word in words_list:
    #             print(word)
            word_num = word_num +1
            if word not in dic.keys():
                flag=0
                break
            else :
                for index in dic[word]:
                    if(index-word_num>=0):
                        ans_bitset[index-word_num]=ans_bitset[index-word_num]+1
        if flag == 1:
            for pos in range(file_size):
                if ans_bitset[pos]==query_len:
                    if print_found_message==0:
                        st.success("Match found!!")
                        print_found_message = 1
                    s = "Match found from word " + str(pos+1) + " in file " + str(file_name[dic_num][0:-4])
                    st.text(s)
    if print_found_message==0:
        st.error("No match found!")


def display():
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.image(Image.open('frankenstein img.jpeg'), caption = "Frankenstein by Marry Shelly")
    with col2:
        st.image(Image.open('emma img.jpeg'), caption = "Emma by Jane Austen")
    with col3:
        st.image(Image.open('pride and prejudice.jpeg'), caption = "Pride and Prejudice by Jane Austen")
    with col4:
        st.image(Image.open('adventures-of-huckleberry-finn.jpeg'), caption = "The Adventures of Huckleberry Finn by Mark Twain")
    with col5:
        st.image(Image.open('the-adventures-of-tom-sawyer.jpeg'), caption = "The Adventures of Tom Sawyer by Mark Twain")
        

#Taking query input



#Streamlit code
st.title('Information Retrieval System')
image = Image.open('hero.png')
st.image(image)

query = st.text_input("Please enter your query below.")
col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
with col4:
    search = st.button('Search')

with col5:
    corpus = st.button('Corpus')
if search:
    if(query==""):
        pass
    else:
        answer(query)

if corpus:
    display()
    