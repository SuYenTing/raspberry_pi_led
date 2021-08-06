import RPi.GPIO as GPIO
import time

# 使用板上定義的腳位號碼
GPIO.setmode(GPIO.BOARD)

# 腳位Led燈對應
RED_PIN = 11
YELLOW_PIN = 12
GRN_PIN = 13

# 腳位起始值設定為低電位
GPIO.setup(RED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(YELLOW_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GRN_PIN, GPIO.OUT, initial=GPIO.LOW)

# LED燈號控制
def led_status(action='停止發亮'):

    # 同時發亮
    if action == '同時發亮':
        
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(YELLOW_PIN, GPIO.HIGH)
        GPIO.output(GRN_PIN, GPIO.HIGH)

    # 輪流發亮
    elif action == '輪流發亮':

        GPIO.output(RED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(RED_PIN, GPIO.LOW)

        GPIO.output(YELLOW_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(YELLOW_PIN, GPIO.LOW)

        GPIO.output(GRN_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(GRN_PIN, GPIO.LOW)

    # 連續閃爍
    elif action == '閃爍發亮':

        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(YELLOW_PIN, GPIO.HIGH)
        GPIO.output(GRN_PIN, GPIO.HIGH)
        time.sleep(1)

        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_PIN, GPIO.LOW)
        GPIO.output(GRN_PIN, GPIO.LOW)
        time.sleep(1)

    # 停止發亮
    elif action == '停止發亮':

        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_PIN, GPIO.LOW)
        GPIO.output(GRN_PIN, GPIO.LOW)

# 腳位設定狀態清除
def gpio_cleanup():
    GPIO.cleanup()