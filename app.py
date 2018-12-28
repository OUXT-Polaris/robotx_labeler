from flask import Flask
from flask import render_template
import glob
import os
import rosbag

app = Flask(__name__)

def read_rosbag(path):
    bag = rosbag.Bag(path)
    return
 
@app.route('/')
def hello_world():
    bagfile_paths = glob.glob('/home/masaya/robotx_data/all/*.bag')
    bagfiles = []
    sizes = []
    for path in bagfile_paths:
        bagfiles.append(os.path.basename(path))
        size = str(os.path.getsize(path)/1073741824.0)+' GB'
        sizes.append(size)
    bagdatas = [{"filename":filename, "path":path} for (filename, path) in zip(bagfiles, bagfile_paths)]
    return render_template('index.html',bagfiles=bagfiles,sizes=sizes)
 
if __name__ == '__main__':
    app.run()