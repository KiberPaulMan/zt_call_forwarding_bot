from smb.SMBConnection import SMBConnection
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

FILE_PATH = '//10.101.2.17/it$/Отдел ИТ/! Инфо !/'

user_id = os.getenv('USER_ID')
password = os.getenv('PASSWORD')
client_machine_name = os.getenv('CLIENT_MACHINE_NAME')
remote_machine_name = os.getenv('REMOTE_MACHINE_NAME')
server_ip = os.getenv('SERVER_IP')
domain = os.getenv('DOMAIN')
file_id = os.getenv('FILE_ID')


def get_file_path_from_remote_server() -> str:
    f_path = ''
    conn = SMBConnection(user_id, password, client_machine_name, remote_machine_name, use_ntlm_v2=True, domain=domain)
    conn.connect(server_ip, 139)
    filelist = conn.listPath('Отдел ИТ$', '/! Инфо !')

    for data in filelist:
        if data.file_id == int(file_id):
            f_path = data.filename

    return FILE_PATH + f_path if f_path else ''
