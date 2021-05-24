"""
Write a Python-script that:
1. Searches for files by a given pattern (pattern can include: *, ?)
2. Displays the search result
3. Gets access rights for each file that is found and displays the result

The script should have 2 obligatory functions:
- finder - a generator function searches for files by a given pattern
 in a given path returns an absolute path of a found file.
- display_result - displays founded files and files' permission
by a given list of absolute paths (You can find an example below).

Example call:
python task_3_ex_3.py /usr/bin -p '?ython*'

Example result:
...
/usr/bin/python3.6m -rwxr-xr-x
/usr/bin/python3.7m -rwxr-xr-x
Found 12 file(s).

Note: use of glob module is prohibited.

Hint: use os.walk, stat, fnmatch
"""
import os
import fnmatch
import stat
import argparse


def finder(filepath, pattern=None):
    result = []
    counter = 0
    dirs = os.walk(filepath)
    for path in dirs:
        for directory in path:
            for file in directory:
                if fnmatch.fnmatch(file, pattern):
                    found_path = os.path.join(path[0], file)
                    #rights = stat.filemode(os.stat(found_path).st_mode)
                    #result.append((found_path, rights))
                    result.append(found_path)
                    #counter += 1
    return result


def display_result(result):
    for path in result:
        print(path, stat.filemode(os.stat(path).st_mode))
    print(f"Found {len(result)} file(s).")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str)
    parser.add_argument("-p", type=str)
    args = parser.parse_args()
    result = finder(args.path, args.p)
    display_result(result)


if __name__ == '__main__':
    main()
