import io
import json
import pathlib
from typing import Any, Dict, List, Union

import ruamel.yaml


def process_element(
    data: Union[bool, str, int], path: str, result: io.StringIO
) -> None:
    if isinstance(data, str):
        result.write(f'{path} = "{data}"\n')
    else:
        result.write(f"{path} = {data}\n")


def process_list(data: List[Any], path: str, result: io.StringIO) -> None:
    for i, v in enumerate(data):
        new_path = f"{path}[{i}]"
        if isinstance(v, dict):
            process_dict(v, new_path, result)
        elif isinstance(v, list):
            process_list(v, new_path, result)
        else:
            process_element(v, new_path, result)


def process_dict(data: Dict[str, Any], path: str, result: io.StringIO) -> None:
    for k, v in data.items():
        new_path = f'{path}["{k}"]'
        if isinstance(v, dict):
            process_dict(v, new_path, result)
        elif isinstance(v, list):
            process_list(v, new_path, result)
        else:
            process_element(v, new_path, result)


def process_file(filepath: pathlib.Path, mode: str, root: str) -> str:
    result = io.StringIO()

    if mode == "json":
        loader = json.load
    elif mode == "yaml":
        loader = ruamel.yaml.safe_load
    else:
        raise ValueError(f"don't know what format {mode} is. Supported: json, yaml")

    with open(filepath, "r") as f:
        data = loader(f)

    process_dict(data, root, result)
    return result.getvalue()
