from flask import Flask ,jsonify,request
app=Flask(__name__) # LEts  flask know where to look for static files


# app Decorator(Determines the path inside the url patterns)
@app.route('/'methods=['GET','POST'])
def index():
   if(request.method =='GET'):
       data="Amen Brother :)"
       return jsonify({'A Message': data})

@app.route('/<int:num>',methods=['GET'])
def cube(num):
    return jsonify({f'cube number of {num}':num**3})


if __name__ =="__main__":
    app.run(debug=True)# Lets ou not have to restart the server anytime you make changes
    
    