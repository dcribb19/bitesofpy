from pathlib import Path
import csv
import json
from json.decoder import JSONDecodeError

EXCEPTION = 'exception caught'
TMP = Path('/tmp')


def _read_json(json_file):
    '''
    Read json_file and return data from mounts > collected
    or raise exception for invalid json
    '''
    with open(json_file, 'rb') as f:
        try:
            data = json.load(f)
            return data['mounts']['collected']
        except JSONDecodeError:
            print(EXCEPTION)
            raise


def convert_to_csv(json_file):
    """Read/load the json_file (local file downloaded to /tmp) and
       convert/write it to defined csv_file.
        The data is in mounts > collected

       Catch bad JSON (JSONDecodeError) file content, in that case print the defined
       EXCEPTION string ('exception caught') to stdout reraising the exception.
       This is to make sure you actually caught this exception.

       Example csv output:
       creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId
       32158,ability_mount_drake_blue,False,True,True,False,44178,Albino Drake,4,60025
       63502,ability_mount_hordescorpionamber,True,...
       ...
    """  # noqa E501
    csv_file = TMP / json_file.name.replace('.json', '.csv')
    data = _read_json(json_file)

    headers = data[0].keys()
    rows = [list(item.values()) for item in data]

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
