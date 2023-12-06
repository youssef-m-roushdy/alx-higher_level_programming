#!/usr/bin/python3
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    argv = sys.argv[1:]
    save_to_json_file(argv, "add_item.json")
    loaded_data = load_from_json_file("add_item.json")
    print(loaded_data)


if __name__ == "__main__":
    main()
