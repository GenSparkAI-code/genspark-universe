import argparse

from genspark.pipeline.pipeline import Pipeline


def main():

    parser = argparse.ArgumentParser(
        prog="genspark",
        description="GenSpark Universe",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    next_parser = subparsers.add_parser(
        "next",
        help="Generate new concepts",
    )

    next_parser.add_argument(
        "count",
        type=int,
    )

    args = parser.parse_args()

    if args.command == "next":

        Pipeline().run(
            args.count
        )


if __name__ == "__main__":
    main()