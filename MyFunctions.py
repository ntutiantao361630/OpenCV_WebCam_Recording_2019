from pathlib import Path
import configparser
import os
pwd = os.getcwd()
config = configparser.RawConfigParser()


def CheckOutputFolder():
    ls = os.listdir(pwd)
    for item in ls:
        if item == "Output":
            # print("found")
            break
        else:
            continue
    else:
        OutputMkdir()


def OutputMkdir():
    outputPath = os.path.join(pwd, "Output")
    os.mkdir(outputPath)
    recordPath = os.path.join(outputPath, "Record")
    os.mkdir(recordPath)
    TLPath = os.path.join(outputPath, "TimeLapse")
    os.mkdir(TLPath)


def CheckIni():
    ls = os.listdir(pwd)
    for item in ls:
        if item == "setting.ini":
            # print("found")
            break
        else:
            continue
    else:
        makeIni()
        # print("no ini")


def makeIni():
    IniPath = os.path.join(pwd, "setting.ini")
    Path(IniPath).touch()
    iniWriter = open(IniPath, "w")
    iniWriter.write("[General Config]\n")
    iniWriter.write("camera = 0\n")
    iniWriter.write("RecordDuration = 30\n")
    iniWriter.write(";Time unit needs to be minutes\n\n")
    iniWriter.write("var2 = 2\n")
    iniWriter.write(";reserve variable")
    iniWriter.close()
    return IniPath


def readIni():

    iniPath = os.path.join(pwd, "setting.ini")
    config.read(iniPath)
    sec = config.items("General Config")
    setting = dict()
    for item in sec:
        setting[item[0]] = item[1]
    return setting


if __name__ == '__main__':

    print(readIni())
