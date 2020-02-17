import MPU9250 as imu
import math



def orientation():
    mpu9250 = imu.MPU9250()

    xAverages = []
    yAverages = []

    while True:

        accel = mpu9250.readAccel()
        #print('Accel X: %.2f' % accel['x'])
        #print('Accel Y: %.2f' % accel['y'])

        xAverages.append(math.degrees(accel['x']))
        yAverages.append(math.degrees(accel['y']))


        if len(xAverages) == 100:
            xAverageValue = sum(xAverages) / len(xAverages)
            yAverageValue = sum(yAverages) / len(yAverages)
            print('Roll: %f' % xAverageValue)
            print('Pitch: %f' % yAverageValue)
            return {'Roll': '%.2f' % xAverageValue, 'Pitch': '%.2f' % yAverageValue}
            break
