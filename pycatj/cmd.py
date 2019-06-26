import argparse
import pathlib

from pycatj import pycatj


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Displays JSON files in a flat format (inspired by mattleibow/catj)"
    )
    parser.add_argument("filepath", type=str, help="File to process")
    parser.add_argument(
        "--format",
        dest="file_format",
        choices=["json", "yaml"],
        help="Format of the file",
    )
    parser.add_argument(
        "--root",
        dest="root",
        default="root",
        help="This is the root of your path, the var where you will load your data",
    )
    args = parser.parse_args()

    filepath = pathlib.Path(args.filepath)
    file_format = args.file_format
    if not file_format:
        file_format = filepath.suffix[1:]
    print(pycatj.process_file(filepath, file_format, args.root))


if __name__ == "__main__":
    main()
