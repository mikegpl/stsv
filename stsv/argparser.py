from argparse import ArgumentParser

PICS_DIRECTORY = "."


def parse():
    parser = ArgumentParser(description="SwipeToSelectViewer - package for easier cleanups of your photos library")
    parser.add_argument(dest='extension',
                        type=str,
                        help='Extension of your photos files')
    parser.add_argument('-s',
                        dest='selected',
                        type=str,
                        help='target directory name for selected photos',
                        default='selected',
                        required=False)
    parser.add_argument('-d',
                        dest='discarded',
                        type=str,
                        help='target directory name for discarded photos',
                        default='discarded',
                        required=False)
    args = vars(parser.parse_args())
    return args.get('extension'), PICS_DIRECTORY, args.get('selected'), args.get('discarded')


if __name__ == '__main__':
    print("This is stsv's parser")
