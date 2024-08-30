import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

phonebook = {
    'rusakov': (os.getenv('RUSAKOV'), 'Русаков Виктор'),
    'erdnev': (os.getenv('ERDNEV'), 'Эрднев Владислав'),
    'kohan': (os.getenv('KOHAN'), 'Кохан Антон'),
    # 'shaykamalov': (os.getenv('SHAYKAMALOV'), 'Шайкамалов Александр'),
}

white_users_id = {
    'rusakov': int(os.getenv('RUSAKOV_TG_ID')),
    'erdnev': int(os.getenv('ERDNEV_TG_ID')),
    'kohan': int(os.getenv('KOHAN_TG_ID')),
    # 'shaykamalov': int(os.getenv('SHAYKAMALOV_TG_ID')),
    'putincev': int(os.getenv('PUTINCEV_TG_ID')),
}
