from transformers import pipeline
from googletrans import Translator

translator = Translator()
summarizer = pipeline("summarization",model="facebook/bart-large-cnn")

diagnosticoES = """ Specialty: Cardiology
Diagnosis:
The patient presented with initial heart problems as a result of a sedentary lifestyle. Medications were prescribed to reduce heart pressure, and the recommendation was made for a more active lifestyle.

Medication:
Matracoatraline 3 times a day indefinitely
Cloacacoaoao once every 24 hours indefinitely
Oaaaaclanine once every twelve hours for seven days

Recommendations:
Low-fat diet, increased intake of protein and natural fats.
Exercise at least three times a week.
"""

diagnosticoTest = '''

'''

summary = summarizer(diagnosticoTest, max_length=50, min_length=30)


trad = translator.translate(summary,dest='es')
print(summary)
#print(trad.text())