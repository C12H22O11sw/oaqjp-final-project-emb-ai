''' A package to estimate the emotion in a given string of text
'''

import requests

def emotion_detector(text_to_analyse):
    ''' REstimate the emotions from the given text using an IBM NLP API
    '''
    url = ('https://sn-watson-emotion.labs.skills.network/v1'
           '/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id": \
               "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    responce = requests.post(url, json=input_json,
                           headers=headers, timeout=15)

    # If status code is 400, return all keys as None
    if responce.status_code == 400:
        formatted_output = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }

        return formatted_output

    # If response is successful, return dictionary of emotions
    responce_json = responce.json()
    formatted_output = responce_json['emotionPredictions'][0]['emotion']
    dominant_emotion = max(formatted_output, key=formatted_output.get)
    formatted_output.update({'dominant_emotion': dominant_emotion})

    return formatted_output
