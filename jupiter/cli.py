from argparse import ArgumentParser

parser = ArgumentParser(
    prog="jupiter",
    description="This is a simulator for automatically negotiation.")

# parser.add_argument(
#     "message",
#     action="store",
#     help="The message string.")

parser.add_argument(
    "--stack-trace",
    dest="stacktrace",
    action="store_true",
    help="Display the stack trace when error occured.")

parser.add_argument(
    "--test",
    dest="test",
    action="store_true",
    help="Execute sample program.")

# 引数を解析する
# import sys
# args = parser.parse_args(sys.argv)
# args = parser.parse_args()

# if args.test:
#     print('Hello')
# else:
#     print('こんにちは')
