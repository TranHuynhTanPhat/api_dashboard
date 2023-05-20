FROM node:lts-alpine
# make the 'app' folder the current working directory
WORKDIR /app
# copy 'package.json' to install dependencies
COPY package*.json ./
# install dependencies
RUN npm install
# copy files and folders to the current working directory (i.e. 'app' folder)
COPY . .
# build app for production with minification
RUN npm run build
EXPOSE 8080

# CMD [ "http-server", "dist" ]
CMD npm run serve --reload
# # Chọn hình ảnh cơ sở cho frontend
# FROM node:14 as build-stage

# # Sao chép mã nguồn frontend vào thư mục làm việc
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY . .
# RUN npm run build

# # Hình ảnh cuối cùng sử dụng Nginx để phục vụ frontend
# FROM nginx:1.21
# COPY --from=build-stage /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]
