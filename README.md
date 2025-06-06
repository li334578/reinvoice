说明
该项目基于chineseocr https://github.com/chineseocr/chineseocr

# 发票 OCR 项目

该项目是一个基于 Python 和 Flask 的发票 OCR（光学字符识别）系统，支持使用 OpenCV 和 Keras 进行文本检测，并使用 PyTorch 进行模型推理。

## 环境要求

- Python 3.9
- Flask
- OpenCV
- PyTorch
- 其他依赖项请参考 `requirements.txt`

## 安装步骤

1. 克隆仓库：
   ```bash
   git clone https://github.com/Ghosts-Tom/reinvoice.git
   cd invoice
   ```

2. 安装所需依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 运行应用

使用以下命令运行应用：
```bash
py -3.9 app.py
```

服务器将在 `http://127.0.0.1:11111` 上启动。

## API 测试

### 使用 Postman 测试 API

如果你不熟悉 Postman，请按照以下步骤进行测试：

1. **下载并安装 Postman**：
   - 访问 [Postman 官网](https://www.postman.com/downloads/) 下载并安装 Postman。

2. **打开 Postman**：
   - 安装完成后，打开 Postman 应用程序。

3. **创建新请求**：
   - 点击左上角的"New"按钮，选择"Request"。
   - 在请求名称中输入"Invoice OCR Test"，然后点击"Save"。

4. **设置请求方法**：
   - 在请求 URL 输入框中，输入 `http://127.0.0.1:11111/invoice-ocr`。
   - 确保请求方法设置为 `POST`。

5. **设置请求体**：
   - 在请求体部分，选择 `form-data`。
   - 添加一个键值对，键名为 `file`，值类型选择 `File`。
   - 点击"Select Files"按钮，选择你要上传的发票图片文件。

6. **发送请求**：
   - 点击"Send"按钮，Postman 将发送请求到你的 Flask 服务。
   - 如果一切正常，你将收到一个 JSON 响应，包含 OCR 识别结果。

7. **查看响应**：
   - 在 Postman 的响应部分，你可以看到返回的 JSON 数据，包含识别结果。

## 项目结构

- `app.py`: 主应用程序文件。
- `model_postE_invoice.py`: 电子发票模型处理文件。
- `model_postM_invoice.py`: 纸质发票模型处理文件。
- `model_post_type.py`: 发票类型模型处理文件。
- `config.py`: 配置文件。
- `requirements.txt`: 项目依赖项列表。
- `README.md`: 项目说明文件。
- `LICENSE`: 许可证文件。

## 许可证

该项目采用 MIT 许可证 - 详情请参阅 LICENSE 文件。



