#!/bin/bash

TEMPLATE="https://raw.githubusercontent.com/syl20bnr/spacemacs/develop/core/templates/.spacemacs.template"
wget -q $TEMPLATE -O .spacemacs.template

if [ $? -ne 0 ]; then
    echo "download .spacemacs.template failed"
    exit 1
else
    echo "download .spacemacs.template successful"
    mv -v .spacemacs .spacemacs.bak
    python3 update-dot-spacemacs.py > .spacemacs && echo "generate .spacemacs successful" || echo "generate .spacemacs failed"
fi
