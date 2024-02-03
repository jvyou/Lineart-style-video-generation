import cv2
import os

path = "./videos"
paths = "./news"
if not os.path.exists(paths):
    os.mkdir(paths)

line_color = (0, 0, 0)  # 黑色
bg_color = (255, 255, 255)  # 白色
number = 1  # 记录文件夹中视频的个数

for dirs in os.listdir(path):
    cap = cv2.VideoCapture(os.path.join(path, dirs))  # 获取视频
    fps = cap.get(cv2.CAP_PROP_FPS)  # 获取视频的帧率
    _, frame = cap.read()  # 先打开第一帧
    size = (frame.shape[1], frame.shape[0])  # 从第一帧中获取图片尺寸
    c = 1
    videowrite = cv2.VideoWriter(r'./news/test%s.mp4' % number, -1, fps, size)  # fps是帧数，size是图片尺寸
    print("开始读取第%s个视频！" % number)
    while True:
        ret, frame = cap.read()  # ret是获取这一帧有没有图片，frame是获取图片
        if ret:
            print("开始截取视频第：" + str(c) + " 帧")  # 这里就可以做一些操作了：显示截取的帧图片、保存截取帧到本地
            img = cv2.Canny(frame, 50, 120)  # 获取边缘
            frame[img != 255] = bg_color  # 将背景图设置为白色
            frame[img == 255] = line_color  # 将边缘（线条）设置为黑色
            videowrite.write(frame)  # 白线条，黑背景
            # videowrite.write(img)  # 黑线条，白背景
            # cv2.imwrite(os.path.join(paths, "%05d" % c + '.jpg'), frames)  # 这里是将截取的图像保存在本地
            c += 1
        else:
            print("所有帧数都已读取完毕！")
            break
    number += 1
    cap.release()
    videowrite.release()
print('end!')
