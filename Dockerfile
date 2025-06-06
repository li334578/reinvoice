# 使用官方 Python 镜像作为基础镜像
FROM python:3.9-slim

# 安装系统依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0 \
        libsm6 \
        libxrender1 \
        libxext6 \
        && rm -rf /var/lib/apt/lists/*

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器中的 /app 目录
COPY . /app

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口（根据你的 Web 框架设置）
EXPOSE 11111

# 启动应用
CMD ["python", "main.py"]