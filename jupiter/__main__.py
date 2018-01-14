import sys
import traceback
from .cli import parser
from .jupiter.jupiter import Jupiter
from .jupiter.jupiter import test


def main(argv=sys.argv):

    if len(argv) < 2:
        parser.parse_args(["-h"])
        sys.exit(0)

    # 自動でコマンドライン引数を読み取る 引数必要なし
    args = parser.parse_args()

    try:
        # exit_code = program(args)
        exit_code = test()
        sys.exit(exit_code)

    except Exception as e:
        error_type = type(e).__name__
        stack_trace = traceback.format_exc()

        if args.stacktrace:
            print("{:=^30}".format(" STACK TRACE "))
            print(stack_trace.strip())

        else:
            sys.stderr.write(
                "{0}: {1}\n".format(e_type, e.message))
            sys.exit(1)
