from flask import Flask, render_template, request
# Ensure the import path matches your actual folder structure. 
# Based on your snippet, it looks like it is inside a package named EmotionDetection
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Emotion_detector function kept in response variable
    response = emotion_detector(text_to_analyze)
        
    # Get values out of dictionary
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # If dominant_emotion is None 
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    
    else:
        # Formatted string using the emotions
        return f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5200)