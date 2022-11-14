import json

try:
    f = open('/usr/local/voevent_reciver_config/config.json')
    config = json.load(f)
    db_user = config['Database_user']
    db_password = config['Database_password']
    db_host = config['Database_host']
    db_port = config['Database_port']
    db_name = config['Database_name']
    print("readed config file")
    print(db_user)
    print(db_password)
    print(db_host)
    print(db_port)
    print(db_name)
except:
    print("can't read the json config file")