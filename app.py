#import library

from flask import Flask,jsonify
from flask_restful import Api,Resource

#inisialisai Objeck flask

app=Flask(__name__)
api=Api(app)

#inisialisasi variable data => multiple records
data= [
    {
        "judul" : "cara produktif",
        "konten" : "cara sederhana produktif",
        "img" : "https://res.cloudinary.com/dk0z4ums3/image/upload/v1648555158/attached_image/saluran-cerna-sehat-untuk-daya-tahan-tubuh-optimal.jpg"
        },
    {
        "judul" : "cara produktif1",
        "konten" : "cara sederhana produktif1",
         "img" : "https://res.cloudinary.com/dk0z4ums3/image/upload/v1648555158/attached_image/saluran-cerna-sehat-untuk-daya-tahan-tubuh-optimal.jpg"
        },
    {
        "judul" : "cara produktif2",
        "konten" : "cara sederhana produktif2",
         "img" : "https://res.cloudinary.com/dk0z4ums3/image/upload/v1648555158/attached_image/saluran-cerna-sehat-untuk-daya-tahan-tubuh-optimal.jpg"
        
        },
    {
        "judul" : "cara produktif3",
        "konten" : "cara sederhana produktif3",
         "img" : "https://res.cloudinary.com/dk0z4ums3/image/upload/v1648555158/attached_image/saluran-cerna-sehat-untuk-daya-tahan-tubuh-optimal.jpg"
        
        },
]

#membuat class data for end point

class GetAllData(Resource) : 
    def get(self):
        output = jsonify(data)
        return output
    
 #new class detail data
 
class  GetDetailData(Resource):
       def get(self,id):
         index = id
         chosenData=data[index]
         output =jsonify(chosenData)
         return output
    
    # def post(self):
    # def update(self):    
    
#inisialisasi endpoint / ini url for endpoint

api.add_resource(GetAllData,"/api/data", methods=["GET"])
api.add_resource(GetDetailData,"/api/data/<int:id>", methods=["GET"])

#Running
if __name__ == "__main__":
    app.run(debug=True, port=5100)