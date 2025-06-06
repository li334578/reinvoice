import os
import torch
########################文字检测########################
##文字检测引擎 
pwd = os.getcwd()
opencvFlag = 'opencv'  # 使用opencv版本
IMGSIZE = (608,608)## yolo3 输入图像尺寸
## keras 版本anchors
keras_anchors = '8,11, 8,16, 8,23, 8,33, 8,48, 8,97, 8,139, 8,198, 8,283'
class_names = ['none','text',]
kerasTextModel_type = os.path.join(pwd,"models","text_type.h5")##keras版本模型发票类型权重文件
kerasTextEModel_invoice = os.path.join(pwd,"models","text_electronic.h5")##keras版本模型电子普票权重文件
kerasTextMModel_invoice = os.path.join(pwd,"models","text_machine.h5")##keras版本模型机打发票权重文件
kerasTextModel = os.path.join(pwd,"models","text_electronic.h5")

############## darknet yolo  ##############
darknetRoot = os.path.join(os.path.curdir,"darknet")## yolo 安装目录
yoloCfg     = "models/text.cfg"
yoloWeights = "models/text.weights"
yoloData    = os.path.join(pwd,"models","text.data")
############## darknet yolo  ##############

########################文字检测########################

## GPU选择及启动GPU序号
GPU = torch.cuda.is_available()  # 自动检测GPU
GPUID = 0

## nms选择,支持cython,gpu,python
nmsFlag = 'gpu' if GPU else 'cython'

##vgg文字方向检测模型
DETECTANGLE = True  # 是否进行文字方向检测
AngleModelPb = "models/Angle-model.pb"
AngleModelPbtxt = "models/Angle-model.pbtxt"

######################OCR模型######################
##是否启用LSTM crnn模型
##OCR模型是否调用LSTM层
LSTMFLAG = True
##模型选择 True:中英文模型 False:英文模型
ocrFlag = 'torch'  # 使用torch版本
chinsesModel = True
ocrModelKeras = os.path.join(pwd,"models","ocr-dense-keras.h5")  # keras版本OCR，暂时支持dense
if chinsesModel:
    if LSTMFLAG:
        ocrModel = os.path.join(pwd,"models","ocr-lstm.pth")
    else:
        ocrModel = os.path.join(pwd,"models","ocr-dense.pth")
else:
    ##纯英文模型
    LSTMFLAG = True
    ocrModel = os.path.join(pwd,"models","ocr-english.pth")
######################OCR模型######################
