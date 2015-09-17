import json
import xmltodict
import sys


def convert(xml=None, file_name=None):
    if file_name:
        with open(file_name) as f:
            data = ''.join(f.readlines())
            return convert(xml=data)
    else:
        return json.dumps(xmltodict.parse(xml),
                          sort_keys=True,
                          indent=4,
                          ensure_ascii=False)

if len(sys.argv) < 2:
    print('Ingresa al menos un argumento')
else:
    convert(file_name=sys.argv[1])
