from transformers import pipeline   # generador de resumenes
resumidor = pipeline("summarization", model="facebook/bart-large-cnn")


def generadorResumen(texto):
    

    # Generar el resumen
    resumen = resumidor(texto, max_length=100, min_length=25, do_sample=False)

    # Mostrar el resultado
    print("Resumen:")
    print(resumen[0]['summary_text'])
    return resumen[0]['summary_text']
