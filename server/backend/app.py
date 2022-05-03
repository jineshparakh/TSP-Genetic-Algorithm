# from GeneticAlgorithmTSP.GeneticAlgorithm import GeneticAlgorithm
from os import sendfile
from flask import Flask, request, send_file
from GeneticAlgorithmTSP import TSP
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/findSolution', methods=["POST"])
def findTSPSolution():
    data = request.json
    print(data)
    return TSP.findTSPSolution(data)

@app.route('/getImage', methods=['POST'])
def getPlot():
    return send_file(request.json['Location'])

if __name__ == "__main__":
    app.run(host='localhost', port=5000)