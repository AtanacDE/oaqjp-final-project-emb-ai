from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    emotions_display = ', '.join(
        [f"'{emotion}': {score}" for emotion, score in response.items() if emotion != 'dominant_emotion']
    )

    return f"For the given statement, the system response is {emotions_display}. The dominant emotion is {response['dominant_emotion']}"

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)