#resources

from  flask import Flask ,jsonify,request
from flask_restful import Resource,Api

app=Flask(__name__)

api=Api(app)


class Message(Resource):
    def get(self):
        return  jsonify({"Greetings Developer !" :" You are now Enetering  a JAvaScript Platform"})
    

#returns the square value of any number

class square(Resource):
    def get(self,num):
        return jsonify({f'Square of {num}': num **2})
        
api.add_resource(Message ,'/')
api.add_resource(square ,'/<int:num>')
    

if __name__ =="__main__":
    app.run(debug=True)
       