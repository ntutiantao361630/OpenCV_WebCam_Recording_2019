# ------import Library-----
import easygui as eg  # 寫視窗用的
import cv2  # opencv
from datetime import datetime  # 叫出時間的功能，給錄影命名
from datetime import timedelta  # 將時間格式，H:M:S
import time  # 計時器，計算程式運行時間
import MyFunctions as func  # 個人函數
import os  # 系統函數，打開Output Folder

# -----initialize------
func.CheckOutputFolder()  # 檢查是否有Output Folder
func.CheckIni()  # 檢查有沒有ini

# -----Read ini-----
Setting = func.readIni()  # 讀取ini的設定

# -----set variable-----
operation = ["Start", "Open Output", "Exit"]  # list，按鍵
Exit = False  # Boolean，預設離開是假
camNumber = int(Setting["camera"])
timeInMinutes = int(Setting["recordduration"])

# -----main program-----
while not Exit:

    act = eg.buttonbox("Welcome to USBCam streaming system",
                       choices=operation)  # 跳出選單
    if act is None or act == operation[2]:  # 判斷選項，是否離開程式
        print("Exit")
        Exit = True

    if act == operation[0]:  # 判斷選項，是否開始錄影
        now = datetime.now()  # 取得現在時間
        vid_capture = cv2.VideoCapture(camNumber, cv2.CAP_DSHOW)  # 設定攝影機
        vid_cod = cv2.VideoWriter_fourcc(*'mp4v')  # set encode format
        count = 0  # 計數器
        speed = 8  # 快轉倍速

        # setting video file names
        videoName = now.strftime("%m.%d.%Y_%H.%M.%S") + ".mp4"
        videoPath = ".\\Output\\Record\\" + videoName
        timelapseName = "TL_" + videoName
        timelapsePath = ".\\Output\\TimeLapse\\" + timelapseName

        # set output file format Path, encode, FPS, Solution
        output = cv2.VideoWriter(videoPath, vid_cod, 20.0, (640, 480))
        TLoutput = cv2.VideoWriter(timelapsePath, vid_cod, 20.0, (640, 480))

        timeout = time.time() + 60 * timeInMinutes  # 終止時間，現在時間+錄影時間
        tStart = time.time()  # 開始時間，現在時間
        while True:
            check, frame = vid_capture.read()  # 錄影
            cv2.imshow("Streaming", frame)  # 開啟錄影時間
            output.write(frame)  # 寫入檔案
            if (count % speed == 0):
                TLoutput.write(frame)  # 寫入縮時檔案
            count += 1
            key = cv2.waitKey(1)
            if key == ord('q') or time.time() > timeout:  # 等待按下q或是達到錄影時間
                break

        tEnd = time.time()  # 取得結束時間
        duration = tEnd - tStart  # 計算錄影時間
        vid_capture.release()  # 釋放記憶體
        output.release()  # 釋放記憶體
        TLoutput.release()  # 釋放記憶體
        cv2.destroyAllWindows()  # 關閉所有視窗
        eg.msgbox("Record Duration: " + str(timedelta(seconds=duration)))  # 顯示錄影時間

    if act == operation[1]:
        os.startfile(".\\Output")  # 開啟錄影資料夾
