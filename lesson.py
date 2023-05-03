# yml
import yaml

with open('config.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file)

# print(help(yaml))
with open('config.yml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)
    # print(data, type(data))
    print(data['web_server']['host'])