import requests
import json

def emotion_detector(text_to_analyse): # Define a function named emotion_detector that takes a string input (text_to_analyse)
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'# URL of the emotion_detect servic
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}# Set the headers required for the API request
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Send a POST request to the API
    response = requests.post(url, json=myobj, headers=header)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Getting the dictionary of emotions from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Taking out the specific scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find max() to find dom emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return dictionary in suitable format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }