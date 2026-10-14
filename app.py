from flask import Flask

app = Flask(__name__)

def check_palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

@app.route("/")
def home():
    return "Palindrome checker is running. Try /check/madam"

@app.route("/check/<word>")
def check(word):
    return f"{word}: {check_palindrome(word.lower())}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
