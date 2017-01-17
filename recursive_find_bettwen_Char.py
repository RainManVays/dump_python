
strr = "asdasgnksfg sd #ITEM1# ,ADFASF (#ITEM2#)  "

def find_beetween_Char(row, s):
    if len(row) >= 3:
        find_item = row.partition(s)[-1].partition(s)[0]
        print(find_item)
        find_beetween_Char(
            row[row.find(s + find_item + s) + len(s + find_item + s):], s)

find_beetween_Char(strr, '#')
