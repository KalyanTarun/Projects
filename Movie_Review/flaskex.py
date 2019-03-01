# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 15:32:14 2018

@author: Tarun
"""
from flask import Flask
from flask import render_template
from flask import request
import sentiment_mod as s


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('add_user.html')
    

@app.route('/post_user',methods=['POST'])
def post_user():
    text=request.form['username']
    return ''.join(s.sentiment(text))

if __name__ =="__main__":
    app.run()
       
