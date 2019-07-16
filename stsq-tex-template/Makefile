my_thesis:= 2017-math-one
.PHONY	: clean
ok:
	xelatex stsq-template.tex
	# xelatex 2019-math-one.tex　＃　应当xelatex两次，但这里可以先节省时间
clean:
	if [ -f $(my_thesis).pdf ];then rm $(my_thesis).pdf;fi
	if [ -f $(my_thesis).toc ];then rm $(my_thesis).toc;fi
	if [ -f $(my_thesis).log ];then rm $(my_thesis).log;fi
	if [ -f $(my_thesis).aux ];then rm $(my_thesis).aux;fi
	if [ -f $(my_thesis).bib ];then rm $(my_thesis).bib;fi
	if [ -f $(my_thesis).out ];then rm $(my_thesis).out;fi
	if [ -f $(my_thesis).pyg ];then rm $(my_thesis).pyg;fi
	if [ -f $(my_thesis).log ];then rm $(my_thesis).log;fi
