import json
import get_data
import xlsxwriter
import csv
from xml.etree.ElementTree import Element
import redis

def data_json(data):
    with open("data.json","w",encoding="utf-8") as f:
        json.dump(data,f)
        print("数据装载完成....")

def data_xls(data):
    workbook = xlsxwriter.Workbook("data.xlsx")
    worksheet = workbook.add_worksheet()
    formatter = workbook.add_format()
    formatter.set_border(1)
    formatter.set_align("center")
    title_formatter = workbook.add_format()
    title_formatter.set_border(1)
    title_formatter.set_bg_color('#cccccc')
    title_formatter.set_align('center')
    title_formatter.set_bold()
    ave_formatter = workbook.add_format()
    ave_formatter.set_border(1)
    ave_formatter.set_align('center')
    ave_formatter.set_num_format('0.00')
    title = []
    for key in data.keys():
        title.append(key)
    worksheet.write_row('A1',title,title_formatter)
    job_item = []
    for value in data.values():
        job_item.append(value[0])
    worksheet.write_row('A2',job_item,title_formatter)
    workbook.close()
def csv_data(data):
    with open("data.csv","w",encoding="utf-8") as f:
        data_csv = csv.writer(f)
        title = []
        for key in data.keys():
            title.append(key)
        data_csv.writerow(title)
        job_item = []
        for value in data.values():
            job_item.append(value[0])
        job_item = [tuple(job_item)]
        data_csv.writerows(job_item)
def xml_data(data):
    pass
def redis_data(data):
    pass

def mysql_data(data):
    pass
def mongodb_data(data):
    pass
if __name__ == '__main__':
    #以下是测试存为json格式
    html = get_data.get_html("http://jobs.zhaopin.com/CC272558088J00110143501.htm?ssidkey=y&ss=409&ff=03&sg=58c01b8c215e46eb9fdcfd6d5ae4136d&so=1")
    data = get_data.get_data(html)
    csv_data(data)







