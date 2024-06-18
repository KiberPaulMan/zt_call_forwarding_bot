#### Сборка образа с репозитория:
1. docker build -t telegram_bot_image .
   
#### Запуск контейнера из собранного образа:
2. docker run -d --name telegram_bot_docker --network host  --privileged telegram_bot_image
   
#### Исполнение комманд внутри docker-контейнера:
3. docker exec -it telegram_bot_docker bash
	
#### Создание файла .env и копирование в него чувствительных данных в следующем формате:
4.
```python
# TELEGRAM_BOT_TOKEN
BOT_TOKEN=**********

# MTS_API_AUTH
MTS_API_LOGIN=********
MTS_API_PASSWORD=*********

# USER_PHONES
RUSAKOV=*********
ERDNEV=*********
KOHAN=*********
SHAYKAMALOV=*********
WORK_PHONE=*********

# ID_TELEGRAM_USERS
RUSAKOV_TG_ID=*********
ERDNEV_TG_ID=*********
KOHAN_TG_ID=*********
SHAYKAMALOV_TG_ID=*********
PUTINCEV_TG_ID=*********

#REMOTE FILE PATH
FILE_PATH=/mnt/win_share/duty.xlsx
```

#### Монтирование сетевой папки с дежурствами в /mnt/win_share, где username и password - учетные данные с правами доступа:
6. mount -t cifs -o username=***,password=***,rw,iocharset=utf8 '//dca.zt.ru/Отдел ИТ$/! Инфо !/' /mnt/win_share
 
