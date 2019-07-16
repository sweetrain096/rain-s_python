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


angles = {20 : 1/12, 35 : 2/12, 40 : 3/12, 45 : 4/12, 55 : 5/12, 60 : 6/12,
          65 : 7/12, 70 : 8/12, 75 : 9/12, 80 : 10/12, 85 : 11/12, 90 : 12/12}


def check_position(white, now_ball):
    if white[0] > now_ball[0] and white[1] > now_ball[1]:
        target = [0, 0]
    elif white[0] > now_ball[0] and white[1] < now_ball[1]:
        target = [0, 124]
    elif white[0] < now_ball[0] and white[1] > now_ball[1] :
        target = [254, 0]
    else:
        target = [254, 124]
    return target

angle = -393939
# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    white = gameData.balls[0]
    print(white)
    for i in range(1, NUMBER_OF_BALLS):
        if gameData.balls[i] == [0, 0]:
            continue
        target = check_position(white, gameData.balls[i])
        angle2 = math.atan2(target[0] - gameData.balls[i][0], target[1] - gameData.balls[i][1]) * (180 / math.pi)

        if target == [0, 0]:
            angle2 += 180
            check = 15 * angles[angle2] / 2
            angle = math.atan2(gameData.balls[1][0] - white[0], gameData.balls[1][1] - white[1] + check) * (
                        180 / math.pi)
            power = 150
        else:
            check = 15 * angles[angle2] / 2
            angle = math.atan2(gameData.balls[1][0] - white[0], gameData.balls[1][1] - white[1] - check) * (180 / math.pi)
            power = 200
        print(angle)
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
