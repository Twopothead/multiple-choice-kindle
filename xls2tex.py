def danxuan(question,text1,text2,text3,text4,AnswEr):
#     if(problem_type==u'单选题' or problem_type==u'多选题' ):
        print("\qs　【单选】",question,"\\xx")
        print( "\\fourch{ ",text1,"} { ",text2,"} {",text3,"} {",text4,"}" )
        print("\\begin{solution}",AnswEr,"\end{solution}")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        return
def duoxuan(question,text1,text2,text3,text4,AnswEr):
        print("\qs 【多选】",question,"\\xx")
        print( "\\fourch{ ",text1,"} { ",text2,"} {",text3,"} {",text4,"}" )
        print("\\begin{solution}",AnswEr,"\end{solution}")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        return
def panduan(question,yesno):
    # if(problem_type==u'判断题'):
        print("\qs",question,"\\xx")
        print("\\begin{solution}",yesno,"\end{solution}")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        return
    
def process_problem(xls_data):
    table = xls_data.sheet_by_name(u'单选题')
    for i in range(1,table.nrows):
        danxuan(table.row_values(i)[0],
            table.row_values(i)[1],table.row_values(i)[2],table.row_values(i)[3],table.row_values(i)[4],
            table.row_values(i)[9])
    table = xls_data.sheet_by_name(u'多选题')
    for i in range(1,table.nrows):
        duoxuan(table.row_values(i)[0],
            table.row_values(i)[1],table.row_values(i)[2],table.row_values(i)[3],table.row_values(i)[4],
            table.row_values(i)[9])
    table = xls_data.sheet_by_name(u'判断题')
    for i in range(1,table.nrows):
        panduan(table.row_values(i)[0],table.row_values(i)[1])
    return
import xlrd
import sys
if(len(sys.argv)<=1):
        print("usage:  $ python xls2tex.py test.xls")
else:
        # print ("%","processing ",sys.argv[1],".............%")
        data = xlrd.open_workbook(sys.argv[1])
        process_problem(data)
# data = xlrd.open_workbook(r"./asset/model-754-762-771-782-783-79.xls")
# process_problem(data)

