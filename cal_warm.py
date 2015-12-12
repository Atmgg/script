#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import xlrd

temprature_dict = {}
wind_direction_dict = {}
wind_speed_dict = {}
total_cloud_dict = {}
low_cloud_dict = {}


def get_hour(index):
    if index < 5:
        Hour = index + 20
    else:
        Hour = index - 4

    sHour = str(Hour)
    if len(sHour) == 1:
        sHour = '0' + sHour

    return sHour

def get_cloud_hour(index):
    if index == 1:
        Hour = 8
    elif index == 2:
        Hour = 14
    elif index == 3:
        Hour = 20

    sHour = str(Hour)
    if len(sHour) == 1:
        sHour = '0' + sHour

    return sHour

def get_time_str(sYear, sMonth, sDay, sHour):
    sTimeStr = "%s年%s月%s日%s时" %(sYear, sMonth[1] if sMonth[0] == '0' else sMonth, sDay, sHour)
    return sTimeStr

def get_table_data(sExcelName):

    data = xlrd.open_workbook(sExcelName)
    table = data.sheets()[0]

    nrows = table.nrows
    ncols = table.ncols

    for i in range( nrows ):
        row = table.row_values(i)
    
        # 处理温度
        if row[0] == "温度":
            for j in range(i+1, i+100):
                row_temprature = table.row_values(j)
                if row_temprature[0] == "":
                    break;
                if row_temprature[0] != "日期":
                    sDay = str(int(row_temprature[0]))
    
                    for k in range(1, 25):
                        sHour = get_hour(k)
                        sTimeStr = get_time_str(sYear, sMonth, sDay, sHour)
                        sResStr = str(row_temprature[k]/10)
                        temprature_dict[sTimeStr] = sResStr
                        # print sTimeStr+':'+sResStr
        # 处理2分钟风
        if row[0] == "2分钟风":
            for j in range(i+1, nrows):
                row_temprature = table.row_values(j)
                if row_temprature[0] == "" and row_temprature[1] == "":
                    break;
                elif row_temprature[0] == "":
                    continue;
                if row_temprature[0] != "日期":
                    sDay = str(int(row_temprature[0]))
    
                    for k in range(1, 25):
                        sHour = get_hour(k)
                        sTimeStr = get_time_str(sYear, sMonth, sDay, sHour)
                        if True == isinstance(row_temprature[k], int):
                            sResStr = str(int(row_temprature[k]))
                        elif True == isinstance(row_temprature[k], float):
                            sResStr = str(int(row_temprature[k]))
                        else:
                            sResStr = str(row_temprature[k])

                        if(sResStr[len(sResStr) - 1] == '.'):
                            sResStr = sResStr[0:len(sResStr) - 1]
    
                        if len(sResStr) < 6:
                            for m in range(len(sResStr), 6):
                                sResStr = '0' + sResStr
    
                        elif len(sResStr) > 6:
                            print "ERR: invalid format, size %u, timestring %s, resstr %s"  %(len(sResStr), sTimeStr, sResStr) 
    
                        sDirect = sResStr[0:3]
                        sSpeed = sResStr[3:6]
    
                        if sDirect.upper() == "PPC":
                            sDirect = 'C'
    
                        sResStr = str(row_temprature[k])
                        wind_direction_dict[sTimeStr] = sDirect
                        wind_speed_dict[sTimeStr] = str(float(sSpeed)/10.0)
                        # print sTimeStr+':'+sDirect
                        # print sTimeStr+':'+str(float(sSpeed)/10.0)
    
        # 总云量
        if row[0] == "总云量":
            for j in range(i+1, i+50):
                row_temprature = table.row_values(j)
                if row_temprature[0] == "" or row_temprature[0] == "低云量":
                    break;
                if row_temprature[0] != "日期":
                    sDay = str(int(row_temprature[0]))
    
                    for k in range(1, 4):
                        sHour = get_cloud_hour(k)
                        sTimeStr = get_time_str(sYear, sMonth, sDay, sHour)
                        sResStr = str(int(row_temprature[k]))
                        total_cloud_dict[sTimeStr] = sResStr
                        # print sTimeStr+':'+sResStr
    
        # 低云量
        if row[0] == "低云量":
            for j in range(i+1, i+50):
                row_temprature = table.row_values(j)
                if row_temprature[0] == "":
                    break;
                if row_temprature[0] != "日期":
                    sDay = str(int(row_temprature[0]))
    
                    for k in range(1, 4):
                        sHour = get_cloud_hour(k)
                        sTimeStr = get_time_str(sYear, sMonth, sDay, sHour)
                        sResStr = str(int(row_temprature[k]))
                        low_cloud_dict[sTimeStr] = sResStr
                        # print sTimeStr+':'+sResStr


sYear = '2012'

for i in range(1, 13):
    sMonth = str(i)
    if len(sMonth) == 1:
        sMonth = '0' + sMonth
    sExcel = sYear+sMonth+'.xls'
    get_table_data(sExcel)
    # print "process %s succ" %(sExcel)

for month in range(1, 13):
    for day in range(1, 31):
        for hour in range(0, 25):
            sHour = str(hour)
            if len(sHour) == 1:
                sHour = '0' + sHour
            key = get_time_str( sYear, str(month), str(day), sHour)
            if temprature_dict.has_key(key):
                #print "%s\t%s\t%s\t%s" %(key, wind_direction_dict[key] if wind_direction_dict.has_key(key) else "NULL", \
                #wind_speed_dict[key] if wind_speed_dict.has_key(key) else "NULL", \
                #temprature_dict[key] )
                pass;

            if total_cloud_dict.has_key(key):
                print "%s\t%s\t%s" %(key, total_cloud_dict[key], low_cloud_dict[key] if low_cloud_dict.has_key(key) else "NULL")
                pass;
