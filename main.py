import os
from text.opencv_dnn_detect import OpenCVDnnDetector
from text.keras_detect import KerasDetector
from model_post_type import PostTypeModel
from model_postE_invoice import PostEInvoiceModel

def main():
    print("Starting OCR program...")
    
    # 初始化检测器
    print("Initializing detectors...")
    opencv_detector = OpenCVDnnDetector()
    keras_detector = KerasDetector()
    
    # 初始化模型
    print("Initializing models...")
    post_type_model = PostTypeModel()
    post_e_invoice_model = PostEInvoiceModel()
    
    # 测试图片路径
    test_image_path = "test_images/test.jpg"  # 请确保这个路径下有测试图片
    
    if not os.path.exists(test_image_path):
        print(f"Error: Test image not found at {test_image_path}")
        return
    
    print(f"Processing image: {test_image_path}")
    
    # 使用OpenCV DNN进行文本检测
    print("Running OpenCV DNN text detection...")
    opencv_results = opencv_detector.detect(test_image_path)
    print("OpenCV DNN results:", opencv_results)
    
    # 使用Keras进行文本检测
    print("Running Keras text detection...")
    keras_results = keras_detector.detect(test_image_path)
    print("Keras results:", keras_results)
    
    # 使用PostType模型进行分类
    print("Running PostType classification...")
    post_type_results = post_type_model.predict(test_image_path)
    print("PostType results:", post_type_results)
    
    # 使用PostEInvoice模型进行处理
    print("Running PostEInvoice processing...")
    post_e_invoice_results = post_e_invoice_model.process(test_image_path)
    print("PostEInvoice results:", post_e_invoice_results)
    
    print("Program completed successfully!")

if __name__ == "__main__":
    main() 