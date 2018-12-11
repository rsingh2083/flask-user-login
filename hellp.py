# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 11:00:07 2018

@author: v-rahsi
"""

from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)