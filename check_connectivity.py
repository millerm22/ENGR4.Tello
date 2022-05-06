from djitellopy import Tello

if __name__ == '__main__':

    print('1. C.onnection test:')
    tello = Tello()
    tello.connect()
    print('\n')

    print('2. Video stream test:')
    tello.streamon()
    print('\n')

    tello.end()
    
# a successful connection will respond with:
# 1. Connection test:
# Send command: command
# Response: b'ok'
# 2. Video stream test:
# Send command: streamon
# Response: b'ok'
