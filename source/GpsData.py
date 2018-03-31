import time
import serial
import string
from pynmea import nmea
import socket



class GpsData():



    def connectServer(self):
        self.host = '127.0.0.1'
        self.port = 14551
        self.mySocket = socket.socket()
        self.mySocket.connect((self.host, self.port))
        print("connected")


    def dataRecv(self):
        self.gpgga = nmea.GPGGA()
        while True:
            data = self.mySocket.recv(1024).decode()

            if data[0:6] == '$GPGGA':
                ##method for parsing the sentence
                print("#########################Data Starting#########################")
                print(data)
                self.gpgga.parse(data)

                lats = self.gpgga.latitude
                print("Latitude values : " + str(lats))

                lat_dir = self.gpgga.lat_direction
                print("Latitude direction : " + str(lat_dir))

                longitude = self.gpgga.longitude
                print("Longitude values : " + str(longitude))

                long_dir = self.gpgga.lon_direction
                print("Longitude direction : " + str(long_dir))

                time_stamp = self.gpgga.timestamp
                print("GPS time stamp : " + str(time_stamp))

                alt = self.gpgga.antenna_altitude
                print("Antenna altitude : " + str(alt))

                lat_deg = lats[0:2]
                lat_mins = lats[2:4]
                lat_secs = round(float(lats[5:]) * 60 / 10000, 2)

                latitude_string = lat_deg + u'\N{DEGREE SIGN}' + lat_mins + string.printable[68] + str(lat_secs) + \
                                  string.printable[63]
                print("Latitude : " + str(latitude_string))

                lon_deg = longitude[0:3]
                lon_mins = longitude[3:5]
                lon_secs = round(float(longitude[6:]) * 60 / 10000, 2)
                lon_str = lon_deg + u'\N{DEGREE SIGN}' + lon_mins + string.printable[68] + str(lon_secs) + \
                          string.printable[63]
                print("Longitude : " + str(lon_str))
                print("####################Data Ending##################")



g=GpsData()
g.connectServer()
g.dataRecv()