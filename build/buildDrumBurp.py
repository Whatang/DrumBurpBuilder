'''
Created on Mar 8, 2015

@author: mike_000
'''

import sys
import os
import platform
import subprocess
import optparse
import zipfile
PYTHON = sys.executable

class BuildSettings(object):
    def __init__(self):
        self.db_root = None
        self.output_dir = None
        self.spec_path = None
        self.working_dir = None
        self.clean = False

    @classmethod
    def read_args(cls):
        settings = cls()
        parser = optparse.OptionParser()
        parser.set_description("Build a DrumBurp executable.")
        parser.add_option('-o', '--output', default = None,
                          help = 'Path to output build directory.')
        parser.add_option('-s', '--spec', default = None,
                          help = 'Path to spec file.')
        parser.add_option('-b', '--build', default = None,
                          help = 'Path to build dir.')
        parser.add_option('-c', '--clean', action = 'store_true',
                          help = 'Do a clean build.')
        opts, args = parser.parse_args()
        if not args:
            parser.print_usage()
            parser.exit(0)
        if len(args) > 1:
            parser.print_usage()
            parser.exit("Only one path to DB root please", 1)
        settings.db_root = os.path.abspath(args[0])
        settings.clean = opts.clean
        if opts.output:
            settings.output_dir = opts.output
        else:
            settings.output_dir = os.path.join(os.path.dirname(__file__))
        settings.output_dir = os.path.join(settings.output_dir,
                                           settings.get_output_name())
        if opts.spec:
            settings.spec_path = opts.spec
        if opts.build:
            settings.working_dir = opts.build
        return settings

    def db_path(self, *args):
        return os.path.join(self.db_root, *args)

    def db_icon_path(self):
        return self.db_path('src', 'GUI', 'Icons', 'drumburp.ico')

    def db_script(self):
        return self.db_path('src', 'DrumBurp.py')

    @staticmethod
    def build_type():
        name = platform.system()
        is_64 = sys.maxsize > 2 ** 32
        return name + "%d" % (64 if is_64 else 32)

    def _get_version(self):
        sys.path.append(self.db_path('src'))
        try:
            import DBVersion
        except ImportError:
            raise RuntimeError("Could not import DrumBurp version info")
        return DBVersion.DB_VERSION

    def get_output_name(self):
        name = 'DrumBurp'
        name += '-' + self.build_type()
        name += '-v' + self._get_version()
        return name

    def output_path(self, *args):
        return os.path.join(self.output_dir, *args)

    def built_exec(self):
        return self.output_path('DrumBurp' + self._exec_suffix())

    def packaged_file(self):
        return self.output_path(self.get_output_name() + ".zip")

    def _exec_suffix(self):
        if platform.system() == "Windows":
            return ".exe"
        else:
            return ""

def pyinstaller_path():
    if platform.system() == "Windows":
        return os.path.join(os.path.dirname(PYTHON), "Scripts",
                            "pyinstaller.exe")
    else:
        return os.path.join(os.path.dirname(PYTHON), "bin", "pyinstaller")

def make_source_zip(settings):
    pass

def build(settings):
    pyinstaller = pyinstaller_path()
    args = [pyinstaller, '-w',  # Windows
            '-F',  # One file
            '-y',  # Overwrite without asking
            '-i', settings.db_icon_path(),  # Path to icon
            '--distpath', settings.output_dir,  # Output directory
            ]
    if settings.working_dir:
        args.append('--workpath')
        args.append(settings.working_dir)
    if settings.spec_path:
        args.append('--specpath')
        args.append(settings.spec_path)
    if settings.clean:
        args.append('--clean')
    # Input file
    args.append(settings.db_script())
    print " ".join(args)
    subprocess.call(args)

def package(settings):
    with zipfile.ZipFile(settings.packaged_file(), mode = 'w',
                         compression = zipfile.ZIP_DEFLATED) as packaged:
        packaged.write(settings.built_exec(),
                       arcname = os.path.basename(settings.built_exec()))
        packaged.write(settings.db_path('COPYING.txt'),
                       arcname = 'COPYING.txt')
        packaged.write(settings.db_path('README.txt'),
                       arcname = 'README.txt')

def main():
    settings = BuildSettings.read_args()
    make_source_zip(settings)
    build(settings)
    package(settings)

if __name__ == '__main__':
    main()
