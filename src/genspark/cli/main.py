import argparse

from genspark.planner.generator import Generator


def main():

    parser = argparse.ArgumentParser(
        prog="genspark"
    )

    sub = parser.add_subparsers(dest="command")

    next_parser = sub.add_parser("next")
    next_parser.add_argument(
        "count",
        type=int,
    )

    args = parser.parse_args()

    if args.command != "next":
        parser.print_help()
        return

    Generator().generate(args.count)