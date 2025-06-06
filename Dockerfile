# 第一步：构建依赖镜像
FROM python:3.9-slim as dependencies

WORKDIR /app

COPY requirements.txt .
RUN pip install --user -r requirements.txt

# 第二步：构建应用镜像
FROM python:3.9-slim

WORKDIR /app

# 从上一阶段复制依赖
COPY --from=dependencies /root/.local /root/.local

# 将你的代码复制进来
COPY . .

# 设置环境变量
ENV PATH="/root/.local/bin:$PATH"

# 启动命令
CMD ["python", "app.py"]