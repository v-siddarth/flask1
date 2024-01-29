# create simple flask application
from flask import Flask

# create app
app=Flask(__name__) #entry point __name__

@app.route('/')
def home():
    return "helllo world"
if __name__ =="__main__":
    app.run()
    
