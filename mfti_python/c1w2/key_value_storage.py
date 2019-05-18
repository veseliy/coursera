import os
import tempfile
import json
import argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.exists(storage_path):
    with open(storage_path, 'r') as f:
        data = f.read()
else:
    data = ''

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--value')
args = parser.parse_args()

if args.value is None:
    if data == '':
        print(None)
    else:
        args_dict = json.loads(data)
        if args.key in args_dict.keys():
            print(', '.join(args_dict.get(str(args.key))))
        else:
            print(None)
else:
    with open(storage_path, 'w') as f:
        if data == '':
            args_dict = {args.key: [args.value]}
        else:
            args_dict = json.loads(data)
            if args.key in args_dict.keys():
                args_dict[args.key].append(args.value)
            else:
                args_dict[args.key] = [args.value]
        f.write(json.dumps(args_dict))
