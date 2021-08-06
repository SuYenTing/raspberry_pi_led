# 樹莓派LED燈控制介面與程式

## 一、簡介

以Python Flask建立一個控制樹莓派LED燈號的介面，使用者可透過點選按鈕，來操控LED燈號顯示方式。另外為方便快速部署，已包成Docker，可在樹莓派上直接部署使用。

![flask_index](/img/flask_index.png)

## 二、LED電路及GPIO配置

* 電路配置圖：

![gpio_layout](/img/gpio_layout.jpg)

* 電子材料：
    * 杜邦線公對母*6條
    * LED燈*3顆(我自己挑紅、黃、綠三種顏色作區別)
    * 電阻(330歐姆)*3個
    * 麵包板*1個

* 電路配置(以LED紅燈為例)：

```
樹莓派PIN#11 -> 電阻(330歐姆) -> LED正極(長腳) -> LED(短腳) -> 樹莓派PIN#6
```

* GPIO連接位置(針腳對應表可參考[Wiki](https://en.wikipedia.org/wiki/Raspberry_Pi#General_purpose_input-output_(GPIO)_connector))
    * LED紅燈接法
        * 正極(長腳)：PIN#11(GPIO#17)
        * 負極(短腳)：PIN#6
    * LED黃燈接法
        * 正極(長腳)：PIN#12(GPIO#18)
        * 負極(短腳)：PIN#34
    * LED綠燈接法
        * 正極(長腳)：PIN#13(GPIO#27)
        * 負極(短腳)：PIN#39


## 三、控制介面部署方式

* 方法1. 以Docker部署

首先確認樹莓派已安裝好Docker及Docker-compose。安裝好後，在`./raspberry_pi_led`資料夾路徑下，輸入指令：

```
docker-compose up -d
```

即可完成部署，部署完後在網址列輸入`127.0.0.1:5000`即可看到LED燈號控制畫面。

* 方法2. 以Python執行Flask

首先確認樹莓派已安裝Python3環境及`./raspberry_pi_led/requirements.txt`列出的套件。確認好後，在`./raspberry_pi_led/app`資料夾路徑下，輸入指令：

```
python3 app.py
```

即可部署好Flask，部署完後在網址列輸入`127.0.0.1:5000`即可看到LED燈號控制畫面。

## 四、程式檔案說明

* app
    * templates
        * index.html：Flask首頁模板
    * app.py：Flask主程式
    * led_status：樹莓派GPIO燈號控制程式
    * requirements：部署所需套件
* img
    * flask_index.png：Flask前台控制畫面圖
    * gpio_layout.jpg：樹莓派LED電路及GPIO配置
* docker-compose.yml：docker-compose部署設定檔
* dockerfile-flask：docker file設定檔
