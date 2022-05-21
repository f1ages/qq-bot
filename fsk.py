#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask,request,jsonify
import json
import ans_check

app = Flask(__name__)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

@app.route('/', methods=['POST'])
def index():
    try:
        data=json_to_info(request.data.decode('utf-8'))
        #print(data)
        if(data!=None):
            ans_check.main(data)
            #xcx.main(data)
            if(data['post_type']=='message'):
                print(data)

        return jsonify({'code': 1, 'message': 'sucess'})

    except Exception as e:
        return jsonify({'code': 0, 'message': str(e)})

def json_to_info(msg):
    for i in range(len(msg)):

        if msg[i]=="}":
            print(i)
        if msg[i]=="{" and msg[-2]=="}":
            return json.loads(msg[i:])
    return None

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    # app.run(debug=True)
    app.run(host='10.0.24.10', port=5071)
