import os
import time


def main():
    content = '********豆豆我爱你*******豆豆我爱你********豆豆我爱你********豆豆我爱你*********'
    while True:
        # 清理屏幕上的输出
        os.system('clear')  # os.system('cls')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
