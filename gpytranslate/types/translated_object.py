import json
from typing import Union


class TranslatedObject(dict):
    def __getattr__(self: Union[str, dict, list], attr: str):
        if isinstance(self, list):
            return [TranslatedObject(elem) for elem in self]
        return (
            TranslatedObject(dict.get(self, attr)) if isinstance(dict.get(self, attr), dict) else dict.get(self, attr)
        )

    def __str__(self):
        return json.dumps({k: v if len(str(v)) < 200 else "..." for k, v in self.items()}, indent=4)

    __setattr__ = dict.__setitem__

    __delattr__ = dict.__delitem__
