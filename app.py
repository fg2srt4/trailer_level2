from quart import Quart
import imu as imu

app = Quart(__name__)

@app.route('/')
def get_orientation():
    orientation = imu.orientation()
    return orientation

app.run(host='0.0.0.0')
