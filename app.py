from flask import Flask, request, jsonify, send_file
import os, urllib
import image_processing

app = Flask(__name__)

    #  request
    # {
    #     "url":"https://listiyo.com/img/anasayfa/16.png",
    #     "type":"convert",
    #     "width":"500"
    # }
    # 
    # response
    # {
    #   "dosya":"https://bizimsunucu/resimler/16.jpg"
    # }
#count how many files exist
fileCount = len(os.listdir('./resimler'))
print(fileCount)

@app.route("/", methods=['POST'])
def pull_image():
    global fileCount
    params = request.get_json()
    
    file_ext = "." + params['url'].split('?', 1)[0].split(".")[-1]
    filename = f"./resimler/{fileCount+1}{file_ext}"

    try:
        urllib.request.urlretrieve(params['url'], filename)
        fileCount += 1
    except:
        return jsonify({"e":f"something went wrong"})
    
    if "width" in params:
        image_processing.resize_image(filename, params['width'])
    if file_ext != ".jpg":
        image_processing.convert_image(filename)

    return jsonify({"dosya":f"http://127.0.0.1:5000/resimler/{fileCount}.jpg"})

@app.route("/resimler/<path:filename>")
def get_image(filename):
    img_path = os.path.join("./resimler", filename)
    return send_file(img_path, mimetype='jpg')


