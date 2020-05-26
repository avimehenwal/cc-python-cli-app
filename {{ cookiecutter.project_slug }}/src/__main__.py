# lazy way to ignore coverage in this file
if True: # pragma: no cover
    def main():
        import sys

        from src.cli import app

        sys.exit(app().run(sys.argv[1:]))

    if __name__ == '__main__':
        main()