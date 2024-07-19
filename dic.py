from flask import Flask, request, render_template_string
app = Flask(__name__)
HTML = '''
<!DOCTYPE html>
<html lang = "en">
    <head>
        <title>En-to-Th(forgot to change language)</title>
        <meta charset = "utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <style>
            html, body {
                width: 100%;
                height: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            
            h1, h2 {
                color:cornflowerblue
            }
            
            body {
                font-family:Arial, Helvetica, sans-serif;
                font-size: 20px;
                background-image: url(https://pbs.twimg.com/media/F7WIfWgb0AAWOSW?format=jpg&name=large);
                background-repeat: no-repeat;
                background-position: left top;
                background-size: cover;
                text-align: center;
            }
            
            .translator {
                vertical-align: middle;
            }
            
            input::placeholder {
                color:deeppink;
            }
            
            input, button {
                padding: 0; /* Reset padding */
                border: 1px solid transparent; /* Reset border, adjust as needed */
                box-sizing: border-box; /* Include padding and border in the height */
                font-size: 30px;
                height: 8vh;
            }
            
            input {
                color: blueviolet;
                width: 50vw;
                background-color: aquamarine;
                padding-left: 10px;
            }
            
            button {
                width: 15vw;
                background-color: chartreuse;
                color: blueviolet;
            }
            
            button:hover {
                color: white;
                border: solid black;
            }
            
            @media (max-width: 370px) {
                body {
                    font-size: 8px;
                }
            
                input, button {
                    font-size: 10px;
                }
            }
            
            @media (min-width: 370px) and (max-width: 500px) {
                body {
                    font-size: 10px;
                }
            
                input, button {
                    font-size: 12px;
                }
            }
            
            @media (min-width: 500px) and (max-width: 700px) {
                body {
                    font-size: 12px;
                }
            
                input, button {
                    font-size: 14px;
                }
            }
            
            @media (min-width: 700px) and (max-width: 900px) {
                input, button {
                    font-size: 20px;
                }
            }
        </style>
    </head>
    <body>
        <main class = "translator">
            <h1>Translate(forgot to change language)</h1>
            <h2>English to Thai</h2>
            <form method = "post" action = "/EntoTh">
                <input type = "text" name = "s1" id = "s" placeholder = "Enter English mistyped sentence">
                <button type = "submit">translate</button>
            </form>
            <h2>Result: {{translatedword1}}</h2>
            <h2>Thai to English</h2>
            <form method = "post" action = "/ThtoEn">
                <input type = "text" name = "s2" id = "s" placeholder = "Enter Thai mistyped sentence">
                <button type = "submit">translate</button>
            </form>
            <h2>Result: {{translatedword2}}</h2>
        </main>
    </body>
</html>
'''

@app.route('/')
def home():
    return HTML

@app.route('/EntoTh', methods = ['POST'])
def EntoTh():
    s = request.form.get('s1', type = str)
    result = ""
    dic = {"1" : "ๅ", "2" : "/", "3" : "-", "4" : "ภ", "5" : "ถ", "6" : "ุ", "7" : "ึ", "8" : "ค", "9" : "ต", "0" : "จ", "-" : "ข", "=" : "ช"
       , "!" : "+", "@" : "๑", "#" : "๒", "$" : "๓", "%" : "๔", "^" : "ู", "&" : "฿", "*" : "๕", "(" : "๖", ")" : "๗", "_" : "๘", "+" : "๙"
       , "q" : "ๆ", "w" : "ไ", "e" : "ำ", "r" : "พ", "t" : "ะ", "y" : "ั", "u" : "ี", "i" : "ร", "o" : "น", "p" : "ย", "[" : "บ", "]" : "ล", "\\" : "ฃ"
       , "Q" : "๐", "W" : "\"", "E" : "ฎ", "R" : "ฑ", "T" : "ธ", "Y" : "ํ", "U" : "๊", "I" : "ณ", "O" : "ฯ", "P" : "ญ", "{" : "ฐ", "}" : ",", "|" : "ฅ"
       , "a" : "ฟ", "s" : "ห", "d" : "ก", "f" : "ด", "g" : "เ", "h" : "้", "j" : "่", "k" : "า", "l" : "ส", ";" : "ว", "\'" : "ง"
       , "A" : "ฤ", "S" : "ฆ", "D" : "ฏ", "F" : "โ", "G" : "ฌ", "H" : "็", "J" : "๋", "K" : "ษ", "L" : "ศ", ":" : "ซ", "\"" : "."
       , "z" : "ผ", "x" : "ป", "c" : "แ", "v" : "อ", "b" : "ิ", "n" : "ื", "m" : "ท", "," : "ม", "." : "ใ", "/" : "ฝ"
       , "Z" : "(", "X" : ")", "C" : "ฉ", "V" : "ฮ", "B" : "ฺ", "N" : "์", "M" : "?", "<" : "ฒ", ">" : "ฬ", "?" : "ฦ", " " : " "}
    for i in s:
        result += dic[i]
    return render_template_string(HTML, translatedword1 = result)

@app.route('/ThtoEn', methods = ['POST'])
def ThtoEn():
    s = request.form.get('s2', type = str)
    result = ""
    dic = {'ๅ': '1', '/': '2', '-': '3', 'ภ': '4', 'ถ': '5', 'ุ': '6', 'ึ': '7', 'ค': '8', 'ต': '9', 'จ': '0', 'ข': '-', 'ช': '='
           , '+': '!', '๑': '@', '๒': '#', '๓': '$', '๔': '%', 'ู': '^', '฿': '&', '๕': '*', '๖': '(', '๗': ')', '๘': '_', '๙': '+'
           , 'ๆ': 'q', 'ไ': 'w', 'ำ': 'e', 'พ': 'r', 'ะ': 't', 'ั': 'y', 'ี': 'u', 'ร': 'i', 'น': 'o', 'ย': 'p', 'บ': '[', 'ล': ']', 'ฃ': '\\'
           , '๐': 'Q', '\"': 'W', 'ฎ': 'E', 'ฑ': 'R', 'ธ': 'T', 'ํ': 'Y', '๊': 'U', 'ณ': 'I', 'ฯ': 'O', 'ญ': 'P', 'ฐ': '{', ',': '}', ' ': ' ', 'ฅ': '|'
           , 'ฟ': 'a', 'ห': 's', 'ก': 'd', 'ด': 'f', 'เ': 'g', '้': 'h', '่': 'j', 'า': 'k', 'ส': 'l', 'ว': ';', 'ง': "\'"
           , 'ฤ': 'A', 'ฆ': 'S', 'ฏ': 'D', 'โ': 'F', 'ฌ': 'G', '็': 'H', '๋': 'J', 'ษ': 'K', 'ศ': 'L', 'ซ': ':', '.': '\"'
           , 'ผ': 'z', 'ป': 'x', 'แ': 'c', 'อ': 'v', 'ิ': 'b', 'ื': 'n', 'ท': 'm', 'ม': ',', 'ใ': '.', 'ฝ': '/'
           , '(': 'Z', ')': 'X', 'ฉ': 'C', 'ฮ': 'V', 'ฺ': 'B', '์': 'N', '?': 'M', 'ฒ': '<', 'ฬ': '>', 'ฦ': '?', " " : " "}
    for i in s:
        result += dic[i]
    return render_template_string(HTML, translatedword2 = result)

if __name__ == '__main__':
    app.run(debug=True)
    