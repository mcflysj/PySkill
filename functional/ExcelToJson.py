#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import threading
import xlrd
from Tkinter import *
from FileDialog import *
import tkMessageBox


class ExcelToJson(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.singleLabel = Label(self, text="single：")
        self.batchLabel  = Label(self, text="batch：")
        self.single_convertButton = Button(self, text="select file", command=self.single_convert)
        self.batch_convertButton = Button(self, text="select doc", command=self.batch_convert)

        self.singleLabel.grid(row=1, column=0)
        self.single_convertButton.grid(row=1, column=1)
        self.batchLabel.grid(row=2, column=0)
        self.batch_convertButton.grid(row=2, column=1)

    def single_convert(self):
        fd = LoadFileDialog(self)
        filename = fd.go()

        if filename:
            self.do_convert_base(filename)
            tkMessageBox.showinfo("Excel To Json", "success")

    def batch_convert(self):
        fd = FileDialog(self)
        dir = fd.go()

        if dir:
            filenames = self.get_files(dir, '.xls')
            # print(filenames)
            # 获取开启的线程数
            threadnum = self.get_thread_num(len(filenames))
            # 根据线程数对原有 filenames列表进行拆分，分配给不同线程
            threadlist = self.split_list(filenames, threadnum)

            for list in threadlist:
                try:
                    t1 = threading.Thread(target=ExcelToJson.do_convert, args=(self, list))
                    t1.start()
                    t1.join()
                except:
                    print("Error: unable create thread")

            tkMessageBox.showinfo("Excel To Json", "success")

    @staticmethod
    def get_files(self, dir, filter):
        filenames = []
        list = os.listdir(dir)

        for file in list:
            filepath = os.path.join(dir, file)
            if os.path.isdir(filepath):
                continue
            if filepath.find(filter) == -1:
                continue
            filenames.append(filepath)

        return filenames

    @staticmethod
    def get_thread_num(self, filenum):
        if filenum <= 2:
            return 1
        threadnum = (filenum / 3) + 1
        if threadnum > 5:
            return 5
        return threadnum

    @staticmethod
    def split_list(self, filelist, num):
        threadlist = []
        listnum = []
        remaindernum = len(filelist) - 3 * (num - 1)
        for i in range(1, num):
            listnum.append([(i - 1) * 3, 3 * i])

        for list in listnum:
            threadlist.append(filelist[list[0]:list[1]])

        threadlist.append(filelist[(0 - remaindernum):])
        return threadlist

    def do_convert(self, filelist):
        for file in filelist:
            self.do_convert_base(file)

    @staticmethod
    def do_convert_base(self, filename):
        excel_file = xlrd.open_workbook(filename)
        (filename, exten) = os.path.splitext(filename)
        outputfile = filename + '.json'
        output = open(outputfile, 'w+', buffering=2048)

        table = excel_file.sheet_by_index(0)
        nrows = table.nrows
        ncols = table.ncols
        title_table = table.row_values(0)

        output.write('[\n')

        for i in range(1, nrows):
            output.write('  {\n')
            for j in range(ncols):
                temp = ''
                value = table.row(i)[j].value

                if  isinstance(value, float):
                    temp = "    \"%s\":%f,\n" % (title_table[j], value)
                elif isinstance(value, unicode):
                    temp = "    \"%s\":\"%s\",\n" % (title_table[j], value.encode('utf-8'))
                else:
                    temp = "    \"%s\":\"%s\",\n" % (title_table[j], value)

                output.write(temp)

            if i == (nrows - 1):
                output.write('  }\n')
            else:
                output.write('  },\n')

        output.write(']\n')
        output.close()


app = ExcelToJson()
app.master.title('Excel To Json')
app.mainloop()

