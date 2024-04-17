#!/usr/bin/env python3

import subprocess

subprocess.call([ 'pip', 'install' , 'inquirer', '-q' ])

from facefusion-2.3.0 import installer

if __name__ == '__main__':
	installer.cli()
