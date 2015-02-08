#######################################################
## Wrapper module for PiCamera to be used by chidren ##
##                                                   ##
## Written by Yolanda Robla  -  v0.  1               ##
##            info@ysoft.biz                         ##
#######################################################
##
## v0.1 - Initial release                    - 15/08/13
##

import time
import picamera

class Camara:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.path = '/home/pi/Desktop/'
        self.extension = '.jpg'

    def foto(self, nombre_archivo):
        self.camera.capture(self.path+nombre_archivo+self.extension)

    def preparar(self):
        self.camera.start_preview()

    def parar(self):
        self.camera.stop_preview()

    def rafaga(self, nombre_archivo, num_fotos=1, tiempo_foto=1):
        for i in range(0, num_fotos):
            nom_archivo = '%s_%03d' % (nombre_archivo, i)
            self.camera.capture(self.path+nom_archivo+self.extension)
            time.sleep(tiempo_foto)

    def video(self, nombre_archivo, tiempo):
        self.camera.start_recording(self.path+nombre_archivo+'.h264')
        self.camera.wait_recording(tiempo)
        self.camera.stop_recording()
