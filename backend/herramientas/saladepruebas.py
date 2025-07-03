from transformers import pipeline   # generador de resumenes
from datetime import datetime



summarizer = pipeline("summarization",model="facebook/bart-large-cnn")

diagnosticoES = """  
Letter format might not be top of mind when you begin writing an important letter or email, 
but an appropriate presentation is critical to ensure your message is ultimately well received.
 A printed letter is usually reserved for important professional communications, such as recommendation letters, 
 cover letters, resignation letters, and business correspondence, so you'll want to know how to write one professionally.

Correct formatting is especially important if you're sending a hard copy to the recipient rather than an email 
because the letter needs to fit the page, look professional, and be clear, concise, and easy to read.

Review information on what you need to include when writing a professional letter, examples,
 and advice on the appropriate font, salutation, spacing, closing, and signature for business correspondence. 

"""



summary = summarizer(diagnosticoES, max_length=50, min_length=30)

print(summary[0]['summary_text'])


'''fechaPrueba = "1955-11-03"
print(fechaPrueba,"\n",datetime(fechaPrueba))'''