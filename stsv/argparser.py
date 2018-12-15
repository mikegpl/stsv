from argparse import ArgumentParser

DEFAULT_WORKING_DIRECTORY = '.'
DEFAULT_SELECTED_DIRECTORY = 'selected'
DEFAULT_DISCARDED_DIRECTORY = 'discarded'
DEFAULT_RESOLUTION = '1920x1080'


def parse():
    parser = ArgumentParser(description="SwipeToSelectViewer - package for easier cleanups of your photos library")
    parser.add_argument(dest='extension',
                        type=str,
                        help='Extension of your photos files.')
    parser.add_argument('-res',
                        dest='resolution',
                        type=str,
                        default=DEFAULT_RESOLUTION,
                        help='Resolution of your screen. Default format is \'WIDTHxHEIGHT\'.',
                        required=False
                        )
    parser.add_argument('-dir',
                        dest='directory',
                        type=str,
                        default=DEFAULT_WORKING_DIRECTORY,
                        help='Location of your pictures. For now, only \'.\' works correctly.',
                        required=False)
    parser.add_argument('-s',
                        dest='selected',
                        type=str,
                        help='Target directory name for selected photos.',
                        default=DEFAULT_SELECTED_DIRECTORY,
                        required=False)
    parser.add_argument('-d',
                        dest='discarded',
                        type=str,
                        help='Target directory name for discarded photos.',
                        default=DEFAULT_DISCARDED_DIRECTORY,
                        required=False)
    args = vars(parser.parse_args())
    results = ['extension', 'resolution', 'directory', 'selected', 'discarded']
    return [args.get(result) for result in results]


if __name__ == '__main__':
    print("This is stsv's parser")
