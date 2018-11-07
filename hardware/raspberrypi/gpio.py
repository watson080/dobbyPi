import wiringpi2

def get_white_sw():
    if(wiringpi2.digitalRead(0) == 0):
        wiringpi2.delay(50)
        if(wiringpi2.digitalRead(0) == 1):
            return True
        elif(wiringpi2.digitalRead(0) == 0):
            return False

def get_black_sw():
    if(wiringpi2.digitalRead(2) == 0):
        wiringpi2.delay(50)
        if(wiringpi2.digitalRead(2) == 1):
            return True
        elif(wiringpi2.digitalRead(2) == 0):
            return False





