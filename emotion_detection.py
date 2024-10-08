import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/\
           v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id":\
               "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }



    result = requests.post(url, json=input_json, 
                           headers=headers, timeout=15)
    return result.text

if __name__ == "__main__":
    print(emotion_detector('I love this new technology.'))