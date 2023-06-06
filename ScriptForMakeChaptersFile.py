
import os
import requests

# # Define the URL of the text data
url = "https://www.gutenberg.org/cache/epub/70911/pg70911.txt"

# # 
# Create a folder named "data" to store the files

folder_name = "data"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Download the text data
response = requests.get(url)
text_data = response.text

#if we use text file 
# text_data= open('urltextfile.txt','r')
# p = text_data.read()


# Split the text data into chapters but first.. the acutal chapters are start from conclusion which is after the index and page numbers 
# where i found 216 character which is last word before the actual chapter start
# so i decide to split into 2 part and the 2nd part is actual chapters
chapterparts = text_data.split("216")
# i use 2nd part of text data 
chapters = chapterparts[1].split("CHAPTER ")

# Remove any empty strings
chapters = [chapter for chapter in chapters if chapter]
# print(type(chapters))

# Save each chapter as a separate .txt file in separate chapter folder to increase model efficiency and reduce the code for each chapter indexes
for i, chapter in enumerate(chapters):
    if i==0:
        # i use this beacuse i==o is a empty chapter beacuse first index element of array is empty string
        pass
    else:
        chapter_text = "CHAPTER " + chapter
        subfolder_name = f"CHAPTER{i}"
        #here i made sub folders 
        if not os.path.exists(f"data/{subfolder_name}"):
            os.makedirs(f"data/{subfolder_name}")
            #here i save each chapter as a separate.txt file
        file_name = os.path.join(f"data/{subfolder_name}", f"chapter{i}.txt")
        with open(file_name, "w", encoding="utf-8") as file:  # Open the file in binary mode and use UTF-8 encoding
            file.write(chapter_text)
        print(f"Chapter {i + 1} saved as {file_name}")
