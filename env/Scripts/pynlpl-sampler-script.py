#!c:\users\vkoltunova\documents\lingua\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'PyNLPl==1.1.8','console_scripts','pynlpl-sampler'
__requires__ = 'PyNLPl==1.1.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('PyNLPl==1.1.8', 'console_scripts', 'pynlpl-sampler')()
    )
