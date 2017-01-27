import os
from argparse import ArgumentParser

HEADER_WIN = b'MZ'
HEADER_ELF = b'ELF'


def list_folder(folder_path):
    files = []
    for root, dirname, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            real_filepath = os.path.abspath(os.path.realpath(filepath))
            files.append(real_filepath)
    return files


def is_file_executable(filepath):
	try:
	    with open(filepath, 'rb') as file_handler:
	        file_header = file_handler.read(4)
	        return (HEADER_WIN in file_header or
	                HEADER_ELF in file_header)
	except IOError as err:
		print('Exception catched. Skipping file {}'.format(filepath))


def find_executable_files(list_of_files):
    files = [filepath for filepath in list_of_files if
             is_file_executable(filepath)]
    return files


def list_files_extension(list_of_files):
    extensions = set([os.path.splitext(filepath)[1] for
                      filepath in list_of_files])
    return extensions


def make_report_file(report_filepath, list_of_files, extensions):
    with open(report_filepath, 'w') as report:
        if extensions:
            for extension in extensions:
                report.write('{}\n'.format(extension))
            report.write('-----\n')
        for filepath in list_of_files:
            report.write('{}\n'.format(filepath))


if __name__ == "__main__":
    parser = ArgumentParser(description='List all executable files in folder')
    parser.add_argument('path_to_folder', nargs='?', default='./',
                        help='path to folder to search in (default is current folder)')
    parser.add_argument('path_to_report', nargs='?', default='./found_binaries.txt',
                        help='path to report file (default is %(default)s)')
    parser.add_argument('-e', '--extensions', action='store_true', default=False,
                        help='list all found extensions to report file')
    args = parser.parse_args()

    folder_fullpath = os.path.abspath(os.path.realpath(args.path_to_folder))
    report_fullpath = os.path.abspath(os.path.realpath(args.path_to_report))
    if not os.path.isdir(folder_fullpath):
        print('Check twice, because folder not found: {}'.format(folder_fullpath))
        exit(-1)

    files_from_folder = list_folder(folder_fullpath)
    print('Found {} files'.format(len(files_from_folder)))
    executable_files = find_executable_files(files_from_folder)
    print('Executable files found {}'.format(len(executable_files)))

    if args.extensions:
        extensions = list_files_extension(executable_files)
    else:
        extensions = []

    make_report_file(report_fullpath, executable_files, extensions)
