# 使用 Python 官方镜像作为基础
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 将该服务的 requirements 文件复制到容器中
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制当前文件夹下所有文件到容器
COPY . .

# 启动 data_loader 服务
CMD ["python", "data_loader_service.py"]
