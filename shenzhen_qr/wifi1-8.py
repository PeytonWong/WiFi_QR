# -*-coding:utf-8-*-
import segno
from segno import helpers

QR_wifi = helpers.make_wifi(ssid='peyton-wifi', password='15678458024qq', security='WPA' or 'WPA2')
print('***************正在生成二维码**********************')
QR_wifi.show()
QR_wifi.save('ShenZhen_QRwifi.png', scale=10)
print('***************生成二维码成功**********************')

# print(QR_wifi.version, QR_wifi.designator)
