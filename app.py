from flask import Flask
from flask import render_template
import glob
import os
import rosbag
import decimal

bagfile_paths = glob.glob('/home/masaya/robotx_data/all/*.bag')
app = Flask(__name__)

def read_rosbag(path):
    bag = rosbag.Bag(path)
    return
 
@app.route('/')
def show_index():
    bagfiles = []
    sizes = []
    for path in bagfile_paths:
        bagfiles.append(os.path.basename(path))
        size = "{:.2f}".format(os.path.getsize(path)/1073741824.0) + " GB"
        sizes.append(size)
    bagdatas = [{"filename":filename, "path":path} for (filename, path) in zip(bagfiles, bagfile_paths)]
    return render_template('index.html',bagfiles=bagfiles,sizes=sizes)

@app.route("/rosbag/id=<int:id>/")
def show_rosbag_page(id):
    if id > len(bagfile_paths):
        return render_template('no_rosbag.html')
    return render_template('rosbag.html')

if __name__ == '__main__':
    app.run()