# takes a ctx.lists format from a python file and convert it to a talon-list

import re
import sys
from pathlib import Path
from typing import List, Tuple


def convert_to_talon_list(lines: List[str]) -> List[Tuple[str, str]]:
    result = []
    parse_list = False
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("ctx.lists"):
            # get the list name
            match = re.search(r'ctx.lists\["(user|self)\.(.*?)"\]', line)
            if match:
                list_name = match.group(2)
                parse_list = True
            else:
                raise ValueError(f"Could not find list name in line: {line}")
        elif parse_list:
            if line.startswith("{"):
                continue
            elif line.startswith("}"):
                break
            else:
                match = re.search(r'"(.*?)": "(.*?)"', line)
                if match:
                    result.append((match.group(1), match.group(2)))
                else:
                    raise ValueError(f"Could not parse line: {line}")
    return result, list_name


# read line from files
file_path = sys.argv[1]
lines = Path(file_path).read_text().split("\n")
result, list_name = convert_to_talon_list(lines)
print(f"list: user.{list_name}")
print("-")
print("")
for item in result:
    print(f"{item[0]}: {item[1]}")
