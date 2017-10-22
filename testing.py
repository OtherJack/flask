from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
  return "HELLO NAPIER", 200 OK

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
