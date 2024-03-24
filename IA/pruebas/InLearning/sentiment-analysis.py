import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

#Descargamos el paquete de vader_lexicon
nltk.download('vader_lexicon')

def analyze_sentiment(text):
    #Iniciamos el analizador de intensidad de sentimientos VADER
    sia = SentimentIntensityAnalyzer()

    #Computamos e imprimimos los resultados
    sentiment = sia.polarity_scores(text)
    print(sentiment)

#Probamos la funcion con una entrada de texto simple
analyze_sentiment("I'm not entirely sure of what I'm writting, but despite the feeling, I must keep on for there are those who believe in me.")