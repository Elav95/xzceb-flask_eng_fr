import machinetranslation
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = englishToFrench(textToTranslate)
    return "Translated text to French: {}".format(translatedText)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = frenchToEnglish(textToTranslate)
    return "Translated text to English: {}".format(translatedText)

@app.route("/")
def renderIndexPage():
   return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
