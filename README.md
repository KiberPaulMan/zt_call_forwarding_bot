#### Сборка образа с репозитория:
1. docker build -t telegram_bot_image .
   
#### Запуск контейнера из собранного образа:
2. docker run -d --name telegram_bot_docker --network host  --privileged telegram_bot_image
   
#### Исполнение комманд внутри docker-контейнера:
3. docker exec -it telegram_bot_docker bash
	
#### Монтирование сетевой папки с дежурствами в /mnt/win_share, где username и password - учетные данные с правами доступа:
4. mount -t cifs -o username=***,password=***,rw,iocharset=utf8 '//dca.zt.ru/Отдел ИТ$/! Инфо !/' /mnt/win_share
 
