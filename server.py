from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Final Project')

@app.route('/emotionDetector')
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    responce = emotion_detector('Bunnies are cute')
    responce_string = 'For the given statement, the system responce is '
    + f"'anger': {responce['anger']}, "
    + f"'disgust': {responce['disgust']}, "
    + f"'fear': {responce['fear']}, "
    + f"'joy': {responce['joy']}, "
    + f"'sadness': {responce['sadness']}. "
    + f"The dominant emotion is {responce['dominant_emotion']}"

    return responce_string

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
