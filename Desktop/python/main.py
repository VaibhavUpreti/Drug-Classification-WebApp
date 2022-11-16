from flask import Flask

app = Flask(__name__)

def generate_html(message):
    html = """
        <html>
        <body>
            <div style='text-align:center;font-size:80px;'>
                <image height="1000" width="1200" src="https://qph.cf2.quoracdn.net/main-qimg-46bfd216a91ff910ced60b59f966ce5f-lq">
            </div>
        </body>
        </html>""".format(message)
    return html

def greet():
    greeting = 'Mujhe kya mei toh batak hoon'
    return greeting

@app.route('/')
def hello_world():
    html = generate_html(greet())
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)