# API_DASHBOARD
Hướng dẫn chạy project trực tiếp tại 2 file README.md trong thư mục front-end và back-end
## Hướng dẫn deploy EC2 [video hướng dẫn](https://youtu.be/RHslOkDfEK8)
## Hướng dẫn deploy bằng lệnh docker-compose [video hướng dẫn](https://youtu.be/E_N624pi8ZE)
### Clone code
```
git clone https://github.com/TrnHunhTnPht/Nhom13-DETAI23-API-DASHBOARD.git
```
<img width="682" alt="Clone code về máy" src="https://github.com/TrnHunhTnPht/Nhom13-DETAI23-API-DASHBOARD/assets/87574012/0eddb643-bd66-4420-9356-6d18ce704b7e">

### Mở Docker desktop
<img width="1382" alt="Docker desktop" src="https://github.com/TrnHunhTnPht/Nhom13-DETAI23-API-DASHBOARD/assets/87574012/5051027a-c513-484b-ba2a-1b39a01ae538">

### Kiểm tra docker bằng terminal
```
docker info
```
<img width="682" alt="Check docker" src="https://github.com/TrnHunhTnPht/Nhom13-DETAI23-API-DASHBOARD/assets/87574012/4bb70fe7-2695-41d4-8899-1c4d29baa1ed">

### Mở terminal tại thư mục chứa code
```
cd Nhom13-DETAI23-API-DASHBOARD
```
<img width="682" alt="Mở terminal tại thư mục chứ code" src="https://github.com/TrnHunhTnPht/Nhom13-DETAI23-API-DASHBOARD/assets/87574012/043470d2-664e-4068-9c94-9bbeb0d4aada">

### Tiến hành deploy 
```
docker-compose up --build
```

#### Front-end: http://localhost:8080/
#### Back-end: http://localhost:8000/docs
##### Admin: admin@admin.com Password: 1
##### User: Tự đăng kí tài khoản

<img width="682" alt="Tiến hành chạy lệnh docker-compose" src="https://github.com/TrnHunhTnPht/Nhom13-DETAI23-API-DASHBOARD/assets/87574012/7488da6b-ffd6-44a2-a7b1-38a169529ee8">
<img width="682" alt="image" src="https://github.com/TrnHunhTnPht/Nhom13-DETAI23-API-DASHBOARD/assets/87574012/816dca65-07cd-4967-b15b-4773539e4cb3">
<img width="1382" alt="image" src="https://github.com/TrnHunhTnPht/Nhom13-DETAI23-API-DASHBOARD/assets/87574012/2254ac5d-d299-4043-a04c-b9c023126084">
<img width="1382" alt="image" src="https://github.com/TrnHunhTnPht/Nhom13-DETAI23-API-DASHBOARD/assets/87574012/0fc77bdc-c27d-4a02-abfc-615939a97cd6">
<img width="1382" alt="image" src="https://github.com/TrnHunhTnPht/Nhom13-DETAI23-API-DASHBOARD/assets/87574012/24d2968f-4e1a-4ad7-812b-af57c2e25bed">
<img width="1680" alt="image" src="https://github.com/TrnHunhTnPht/Nhom13-DETAI23-API-DASHBOARD/assets/87574012/1964399e-2ffa-45be-aed7-d4edfda643b9">
<img width="1680" alt="image" src="https://github.com/TrnHunhTnPht/Nhom13-DETAI23-API-DASHBOARD/assets/87574012/b07e4043-067e-4aaa-9ac6-40516ed912ef">


### References: 
* https://github.com/Princekrampah/fastAPIMongoDB_todoAPP
* https://www.youtube.com/watch?v=jVzXUVB2gP0
* https://www.youtube.com/watch?v=KIEd5KtOLZQ
* https://youtu.be/FN6mR6TAZN4
* https://codepen.io/uiswarup/pen/XWdXGGV
