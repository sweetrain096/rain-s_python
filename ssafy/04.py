import socket
import time
import math


# User and Game Server Information
NICKNAME = '파이썬'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()


angles = {0 : 0, 20 : 1/12, 35 : 2/12, 40 : 3/12, 45 : 4/12, 55 : 5/12, 60 : 6/12,
          65 : 7/12, 70 : 8/12, 75 : 9/12, 80 : 10/12, 85 : 11/12, 90 : 12/12}

def find_angle(angle):
    print(angle)
    if angle >= 0 and angle <=17:
        angle = 0
    if angle <=27:
        angle = 20
    elif angle <=37:
        angle = 35
    elif angle <= 42:
        angle = 40
    elif angle <= 50:
        angle = 45
    elif angle <= 57:
        angle = 55
    elif angle <= 62:
        angle = 60
    elif angle <= 67:
        angle = 65
    elif angle <= 72:
        angle = 70
    elif angle <= 77:
        angle = 75
    elif angle <= 82:
        angle = 80
    elif angle <= 88:
        angle = 85
    elif angle <= 90:
        angle = 90
    return angle

def check_position(white, now_ball):
    if white[0] > now_ball[0] and white[1] > now_ball[1] and now_ball[0] >= 130:
        target = [130, 0]
        case = 1
    elif white[0] > now_ball[0] and white[1] > now_ball[1]:
        target = [0, 0]
        case = 1
    elif white[0] > now_ball[0] and white[1] < now_ball[1] and now_ball[0] >= 130:
        target = [130, 130]
        case = 2
    elif white[0] > now_ball[0] and white[1] < now_ball[1]:
        target = [0, 130]
        case = 2
    elif white[0] < now_ball[0] and white[1] > now_ball[1] and now_ball[0] <= 130:
        target = [130, 0]
        case = 3
    elif white[0] < now_ball[0] and white[1] > now_ball[1]:
        target = [260, 0]
        case = 3
    elif white[0] < now_ball[0] and white[1] < now_ball[1] and now_ball[0] <= 130:
        target = [130, 130]
        case = 4
    else:
        target = [260, 130]
        case = 4
    return target, case

angle = -393939
# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    white = gameData.balls[0]
    print('white', white)
    for i in range(1, NUMBER_OF_BALLS):
        if gameData.balls[i] == [0, 0]:
            continue
        print('now', gameData.balls[i])
        target, case = check_position(white, gameData.balls[i])
        print('target', target)
        angle2 = math.atan2(target[0] - gameData.balls[i][0], target[1] - gameData.balls[i][1]) * (180 / math.pi)


        if case == 1:
            angle2 += 180
            angle2 = find_angle(angle2)
            check = 15 * angles[angle2] / 2
            dx = gameData.balls[i][0] - white[0]
            dy = gameData.balls[i][1] - white[1] + check
            angle = math.atan2(dx, dy) * (180 / math.pi)
            # power = 150

        elif case == 3:
            print(angle2)
            angle2 -= 90
            angle2 = find_angle(angle2)
            check = 15 * angles[angle2] / 2
            dx = gameData.balls[i][0] - white[0]
            dy = gameData.balls[i][1] - white[1] + check
            angle = math.atan2(dx, dy) * (180 / math.pi)

        elif case == 4:
            print(case)
            angle2 = find_angle(angle2)
            print(angle2)
            check = 15 * angles[angle2] / 2
            dx = gameData.balls[i][0] - white[0]
            dy = gameData.balls[i][1] - white[1] - check
            angle = math.atan2(dx, dy) * (180 / math.pi)
            print(angle)
            # power = 200

        length = math.sqrt((dx * dx) + (dy * dy))
        print('length', length)
        if length > 195:
            power = 100
        elif length > 190:
            power = 200
        elif length > 110:
            power = 120
        elif length > 100:
            power = 150
        elif length >70:
            power = 80
        elif length >= 50:
            power = 100
        elif length < 20:
            power = 120
        elif length < 50:
            power = 100

        print('angle', angle)
        if angle != -393939:
            break




    # power = 200
    ######################################################################################
    # 주어진 정보를 바탕으로 샷을 할 방향과 세기를 결정해서 angle, power 값으로 지정 #
    ######################################################################################
    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        play(conn, gameData)
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
