import os
from pathlib import Path
import argparse
import pathify
from enum import Enum

class CliAction(Enum):
    encode = 'encode'
    decode = 'decode'

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        'action',
        type=CliAction
    )
    argparser.add_argument(
        'src',
        type=Path,
    )
    argparser.add_argument(
        '--output',
        type=Path,
        required=False,
        default=None
    )
    args = argparser.parse_args()

    match args.action:
        case CliAction.encode:
            assert args.src.is_file() and args.src.exists()
            output = args.output if args.output else (args.src.parent / f"{args.src.name}.d")
            if not output.exists():
                os.makedirs(output)
            assert not any(Path(output).iterdir())

            pathify.encode(args.src, output)
        
        case CliAction.decode:
            assert args.src.is_dir() and args.src.exists()
            output = args.output if args.output else (args.src.parent / args.src.name.removesuffix('.d'))
            assert not output.is_dir() and not output.exists()

            pathify.decode(args.src, output)

if __name__=="__main__":
    main()