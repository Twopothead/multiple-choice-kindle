#!/bin/bash
if [[ $# -lt 1 ]]; then
        echo "args count must > 1"  
        echo "Usage: bash generate.sh ./test/test.xls"  
        exit  
else
    python xls2tex.py $1 > contents.txt
    bash handle_special_chars.sh
    cat ./stsq-tex-template/template/stsq_template_firsthalf.txt ./contents.txt ./stsq-tex-template/template/stsq_template_secondhalf.txt > ./stsq-tex-template/stsq-template.tex
    cd ./stsq-tex-template/ && make
    pwd
    # mv ./stsq-template.pdf .. && cd ..
    mv ./stsq-template.pdf ..
    # cp ./stsq-template.pdf ../"$1"
fi
# bash generate.sh test/781.xls
#python xls2tex.py asset/model-754-762-771-782-783-79.xls > contents.txt