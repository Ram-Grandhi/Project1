from flask import Flask

app = Flask(__name__)
print(__name__)
print(app)

'''shows hello world at http://127.0.0.1:5000/
@app.route(rule,options) : rule - url to bind with index function, options: list of 
parameters to be forwarded to the underlying Rule object
'''
@app.route("/")
def index():
    return "hello world"
app.add_url_rule('/','index',index)


def kiran():
    return "Hello World"
app.add_url_rule('/sharath','kiran',kiran)

'''Alternative routing: app.add_url_rule('/',)'''
# def index():
#     return "hello world"
# app.add_url_rule('/','index',index)

if __name__ == "__main__":
         app.run()