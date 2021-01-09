from typing import Dict, Any


def rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:
    new_dict = {}
    for k, v in data.items():
        if isinstance(k, str):
            if k.startswith('@'):
                k = k.replace('@', '')
        if isinstance(v, dict):
            v = rename_keys(v)
        if isinstance(v, list):
            new_list = []
            for item in v:
                if isinstance(item, dict):
                    new_list.append(rename_keys(item))
                else:
                    new_list.append(item)
            v = new_list
        new_dict[k] = v
    return new_dict
