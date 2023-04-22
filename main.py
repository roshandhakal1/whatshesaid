import os
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
openai.api_key = "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"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["input_text"]
        transformed_text = transform_text(text)
        return jsonify(transformed_text)
    return render_template("index.html")

def transform_text(text):
    prompt = f"Pretend that you are a wise and professional 50-year-old lady who never gets mad ever, always talk calmly and as politely in absolute worst scenerio. dont use hateful or negative word at all. please note even though its negative remark, it should make it positive. rewrite it from her perspective without sounding too fake. it must be rewritten , not responded: {text}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=600,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)
