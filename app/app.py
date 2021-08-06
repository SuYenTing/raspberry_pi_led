# 樹莓派LED燈號控制-Flask介面
# 載入套件
from flask import Flask, request, render_template
from flask_apscheduler import APScheduler

# 載入自定義套件
from led_status import led_status, gpio_cleanup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    # GET: 直接返回首頁頁面
    if request.method == 'GET':
        return render_template('index.html')

    # POST: 依據使用者按鈕選擇的動作來更換Job引數
    elif request.method == 'POST':

        action = request.form.get('action')
        scheduler.modify_job(id='ledJob', args=[action])
        message = '目前動作: LED燈' + action
        return render_template('index.html', message=message)

# 排程起始設定
scheduler = APScheduler()
scheduler.api_enabled = True
scheduler.init_app(app)

# 設定任務
# 利用排程interval的方式來達成無窮迴圈
@scheduler.task('interval', id='ledJob', seconds=1, args=('停止發亮',), max_instances=1)
def ledJob(action):
    led_status(action)

# 啟用排程
scheduler.start()

if __name__ == '__main__':
    
    try:
        # app.run()
        app.run(host='0.0.0.0', port=5000)

    finally:
        # 腳位設定狀態清除
        gpio_cleanup()