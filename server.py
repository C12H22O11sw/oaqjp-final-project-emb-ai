''' A lightweight server to detect the emotion of a user-provided prompt
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Final Project')

@app.route('/emotionDetector')
def detect_emotions():
    ''' Generate a responce message explaining the emotion of the user's prompt text
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # handle invalid response
    if not response['dominant_emotion']:
        return 'Invalid text! Please try again!'


    response_string = 'For the given statement, the system response is ' \
    + f"'anger': {response['anger']}, " \
    + f"'disgust': {response['disgust']}, " \
    + f"'fear': {response['fear']}, " \
    + f"'joy': {response['joy']}, " \
    + f"'sadness': {response['sadness']}. " \
    + f"The dominant emotion is {response['dominant_emotion']}"

    return response_string

@app.route("/")
def render_index_page():
    ''' Render the index page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
