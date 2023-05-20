# FROM python:3.9

# WORKDIR /app

# COPY requirements.txt ./

# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD uvicorn app.index:app --host 0.0.0.0

# Chọn hình ảnh cơ sở cho backend
FROM python:3.9

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép các tệp yêu cầu vào thư mục làm việc
COPY requirements.txt ./

# Cài đặt các gói phụ thuộc cho backend
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn backend vào thư mục làm việc
COPY . .

# Chạy lệnh để khởi chạy backend
CMD ["uvicorn", "app.index:app", "--host", "0.0.0.0", "--port", "8000"]
