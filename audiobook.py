# You need to install the following packages using pip install "the name of the package" in terminal

import pyttsx3
import PyPDF2

# The coted statment is the name of a file that i want to be set on my audio book app you can change yours.
with open('Back to my Root.pdf','rb') as book:
# Changes for saving audio
    full_text = ""



    reader = PyPDF2.PdfFileReader(book)

    audio_reader = pyttsx3.init()
    audio_reader.setProperty('rate',170)

# If you wnat to change the sound to female
    #voices = audio_reader.getProperty("voices")
    #audio_reader.setProperty("voice",voices[1].id)

    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extract_text()
#Changes for saving audio      
        full_text += content
#Changes for saving audio
    audio_reader.save_to_file(full_text,'Back_to_my_root.mp3')
    audio_reader.runAndWait()
