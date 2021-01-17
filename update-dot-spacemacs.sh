#!/bin/bash

wget https://github.com/syl20bnr/spacemacs/blob/develop/core/templates/.spacemacs.template
mv .spacemacs .spacemacs.bak
python3 update-dot-spacemacs.py > .spacemacs
