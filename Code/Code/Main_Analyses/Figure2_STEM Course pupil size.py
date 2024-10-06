import warnings
import sys
import os
# import logging
import xlsxwriter as xw
# import deepdish as dd # error
import numpy as np

import brainiak.eventseg.event
import nibabel as nib
from nilearn.input_data import NiftiMasker

import scipy.io
from scipy import stats
from scipy.stats import norm, zscore, pearsonr
from scipy.signal import gaussian, convolve
from sklearn import decomposition
from sklearn.model_selection import LeaveOneOut, KFold

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
import seaborn as sns
import pandas as pd

dataFile01 = '/Users/lansenn/Desktop/PPT/pre_mat/extr_fill_data_Test001.mat'
dataFile02 = '/Users/lansenn/Desktop/PPT/pre_mat/extr_fill_data_Test002.mat'
dataFile03 = '/Users/lansenn/Desktop/PPT/pre_mat/extr_fill_data_Test003.mat'

dataFile05 = '/Users/lansenn/Desktop/PPT/pre_mat/extr_fill_data_Test005.mat'
dataFile06 = '/Users/lansenn/Desktop/PPT/pre_mat/extr_fill_data_Test006.mat'
dataFile07 = '/Users/lansenn/Desktop/PPT/pre_mat/extr_fill_data_Test007.mat'
dataFile08 = '/Users/lansenn/Desktop/PPT/pre_mat/extr_fill_data_Test008.mat'
dataFile09 = '/Users/lansenn/Desktop/PPT/pre_mat/extr_fill_data_Test009.mat'
dataFile10 = '/Users/lansenn/Desktop/PPT/pre_mat/extr_fill_data_Test010.mat'
dataFile11 = '/Users/lansenn/Desktop/PPT/pre_mat/extr_fill_data_Test011.mat'
dataFile12 = '/Users/lansenn/Desktop/PPT/pre_mat/extr_fill_data_Test012.mat'

dataFile_37='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ301.mat'
dataFile_38='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ302.mat'
dataFile_39='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ303.mat'
dataFile_40='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ304.mat'
dataFile_41='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ305.mat'
dataFile_42='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ306.mat'
dataFile_43='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ307.mat'
dataFile_44='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ308.mat'
dataFile_45='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ309.mat'
dataFile_46='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ310.mat'
dataFile_47='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ317.mat'
dataFile_48='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ318.mat'
dataFile_49='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ319.mat'
dataFile_50='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ320.mat'
dataFile_51='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ321.mat'
dataFile_52='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ322.mat'
dataFile_53='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ323.mat'
dataFile_54='/Users/lansenn/Desktop/PPT/extract3/extr_fill_data_TestZ324.mat'

data1 = scipy.io.loadmat(dataFile01)
data2 = scipy.io.loadmat(dataFile02)
data3 = scipy.io.loadmat(dataFile03)

data5 = scipy.io.loadmat(dataFile05)
data6 = scipy.io.loadmat(dataFile06)
data7 = scipy.io.loadmat(dataFile07)
data8 = scipy.io.loadmat(dataFile08)
data9 = scipy.io.loadmat(dataFile09)
data10 = scipy.io.loadmat(dataFile10)
data11 = scipy.io.loadmat(dataFile11)
data12 = scipy.io.loadmat(dataFile12)

data_37 = scipy.io.loadmat(dataFile_37)
data_38 = scipy.io.loadmat(dataFile_38)
data_39 = scipy.io.loadmat(dataFile_39)
data_40 = scipy.io.loadmat(dataFile_40)
data_41 = scipy.io.loadmat(dataFile_41)
data_42 = scipy.io.loadmat(dataFile_42)
data_43 = scipy.io.loadmat(dataFile_43)
data_44 = scipy.io.loadmat(dataFile_44)
data_45 = scipy.io.loadmat(dataFile_45)
data_46 = scipy.io.loadmat(dataFile_46)
data_47 = scipy.io.loadmat(dataFile_47)
data_48 = scipy.io.loadmat(dataFile_48)
data_49 = scipy.io.loadmat(dataFile_49)
data_50 = scipy.io.loadmat(dataFile_50)
data_51 = scipy.io.loadmat(dataFile_51)
data_52 = scipy.io.loadmat(dataFile_52)
data_53 = scipy.io.loadmat(dataFile_53)
data_54 = scipy.io.loadmat(dataFile_54)
data1X = data1['GJX_student']
data1Y = data1['GJY_student']
data1P = data1['GJP_student']
data2X = data2['GJX_student']
data2Y = data2['GJY_student']
data2P = data2['GJP_student']
data3X = data3['GJX_student']
data3Y = data3['GJY_student']
data3P = data3['GJP_student']

data5X = data5['GJX_student']
data5Y = data5['GJY_student']
data5P = data5['GJP_student']
data6X = data6['GJX_student']
data6Y = data6['GJY_student']
data6P = data6['GJP_student']
data7X = data7['GJX_student']
data7Y = data7['GJY_student']
data7P = data7['GJP_student']
data8X = data8['GJX_student']
data8Y = data8['GJY_student']
data8P = data8['GJP_student']
data9X = data9['GJX_student']
data9Y = data9['GJY_student']
data9P = data9['GJP_student']
data10X = data10['GJX_student']
data10Y = data10['GJY_student']
data10P = data10['GJP_student']
data11X = data11['GJX_student']
data11Y = data11['GJY_student']
data11P = data11['GJP_student']
data12X = data12['GJX_student']
data12Y = data12['GJY_student']
data12P = data12['GJP_student']

data_37X=data_37['GJX_student']
data_37Y=data_37['GJY_student']
data_37P=data_37['GJP_student']
data_38X=data_38['GJX_student']
data_38Y=data_38['GJY_student']
data_38P=data_38['GJP_student']
data_39X=data_39['GJX_student']
data_39Y=data_39['GJY_student']
data_39P=data_39['GJP_student']
data_40X=data_40['GJX_student']
data_40Y=data_40['GJY_student']
data_40P=data_40['GJP_student']
data_41X=data_41['GJX_student']
data_41Y=data_41['GJY_student']
data_41P=data_41['GJP_student']
data_42X=data_42['GJX_student']
data_42Y=data_42['GJY_student']
data_42P=data_42['GJP_student']
data_43X=data_43['GJX_student']
data_43Y=data_43['GJY_student']
data_43P=data_43['GJP_student']
data_44X=data_44['GJX_student']
data_44Y=data_44['GJY_student']
data_44P=data_44['GJP_student']
data_45X=data_45['GJX_student']
data_45Y=data_45['GJY_student']
data_45P=data_45['GJP_student']
data_46X=data_46['GJX_student']
data_46Y=data_46['GJY_student']
data_46P=data_46['GJP_student']
data_47X=data_47['GJX_student']
data_47Y=data_47['GJY_student']
data_47P=data_47['GJP_student']
data_48X=data_48['GJX_student']
data_48Y=data_48['GJY_student']
data_48P=data_48['GJP_student']
data_49X=data_49['GJX_student']
data_49Y=data_49['GJY_student']
data_49P=data_49['GJP_student']
data_50X=data_50['GJX_student']
data_50Y=data_50['GJY_student']
data_50P=data_50['GJP_student']
data_51X=data_51['GJX_student']
data_51Y=data_51['GJY_student']
data_51P=data_51['GJP_student']
data_52X=data_52['GJX_student']
data_52Y=data_52['GJY_student']
data_52P=data_52['GJP_student']
data_53X=data_53['GJX_student']
data_53Y=data_53['GJY_student']
data_53P=data_53['GJP_student']
data_54X=data_54['GJX_student']
data_54Y=data_54['GJY_student']
data_54P=data_54['GJP_student']

data1 = np.concatenate((data1X[0:763001:100],data1Y[0:763001:100],data1P[0:763001:100]),axis=1)
data2 = np.concatenate((data2X[0:763001:100],data2Y[0:763001:100],data2P[0:763001:100]),axis=1)
data3 = np.concatenate((data3X[0:763001:100],data3Y[0:763001:100],data3P[0:763001:100]),axis=1)

data5 = np.concatenate((data5X[0:763001:100],data5Y[0:763001:100],data5P[0:763001:100]),axis=1)
data6 = np.concatenate((data6X[0:763001:100],data6Y[0:763001:100],data6P[0:763001:100]),axis=1)
data7 = np.concatenate((data7X[0:763001:100],data7Y[0:763001:100],data7P[0:763001:100]),axis=1)
data8 = np.concatenate((data8X[0:763001:100],data8Y[0:763001:100],data8P[0:763001:100]),axis=1)
data9 = np.concatenate((data9X[0:763001:100],data9Y[0:763001:100],data9P[0:763001:100]),axis=1)
data10 = np.concatenate((data10X[0:763001:100],data10Y[0:763001:100],data10P[0:763001:100]),axis=1)
data11 = np.concatenate((data11X[0:763001:100],data11Y[0:763001:100],data11P[0:763001:100]),axis=1)
data12 = np.concatenate((data12X[0:763001:100],data12Y[0:763001:100],data12P[0:763001:100]),axis=1)

data_37 = np.concatenate((data_37X[0:763001:100],data_37Y[0:763001:100],data_37P[0:763001:100]),axis=1)
data_38 = np.concatenate((data_38X[0:763001:100],data_38Y[0:763001:100],data_38P[0:763001:100]),axis=1)
data_39 = np.concatenate((data_39X[0:763001:100],data_39Y[0:763001:100],data_39P[0:763001:100]),axis=1)
data_40 = np.concatenate((data_40X[0:763001:100],data_40Y[0:763001:100],data_40P[0:763001:100]),axis=1)
data_41 = np.concatenate((data_41X[0:763001:100],data_41Y[0:763001:100],data_41P[0:763001:100]),axis=1)
data_42 = np.concatenate((data_42X[0:763001:100],data_42Y[0:763001:100],data_42P[0:763001:100]),axis=1)
data_43 = np.concatenate((data_43X[0:763001:100],data_43Y[0:763001:100],data_43P[0:763001:100]),axis=1)
data_44 = np.concatenate((data_44X[0:763001:100],data_44Y[0:763001:100],data_44P[0:763001:100]),axis=1)
data_45 = np.concatenate((data_45X[0:763001:100],data_45Y[0:763001:100],data_45P[0:763001:100]),axis=1)
data_46 = np.concatenate((data_46X[0:763001:100],data_46Y[0:763001:100],data_46P[0:763001:100]),axis=1)
data_47 = np.concatenate((data_47X[0:763001:100],data_47Y[0:763001:100],data_47P[0:763001:100]),axis=1)
data_48 = np.concatenate((data_48X[0:763001:100],data_48Y[0:763001:100],data_48P[0:763001:100]),axis=1)
data_49 = np.concatenate((data_49X[0:763001:100],data_49Y[0:763001:100],data_49P[0:763001:100]),axis=1)
data_50 = np.concatenate((data_50X[0:763001:100],data_50Y[0:763001:100],data_50P[0:763001:100]),axis=1)
data_51 = np.concatenate((data_51X[0:763001:100],data_51Y[0:763001:100],data_51P[0:763001:100]),axis=1)
data_52 = np.concatenate((data_52X[0:763001:100],data_52Y[0:763001:100],data_52P[0:763001:100]),axis=1)
data_53 = np.concatenate((data_53X[0:763001:100],data_53Y[0:763001:100],data_53P[0:763001:100]),axis=1)
data_54 = np.concatenate((data_54X[0:763001:100],data_54Y[0:763001:100],data_54P[0:763001:100]),axis=1)

C=np.array([data1.T,data2.T,data3.T,data5.T,data6.T,data7.T,data8.T,data9.T,data10.T,data11.T,data12.T,
            data_37.T,data_38.T,data_39.T,data_40.T,data_41.T,data_42.T,data_43.T,data_44.T,data_45.T,data_46.T,data_47.T,data_48.T,data_49.T,data_50.T,data_51.T,data_52.T,data_53.T,data_54.T])

D3=C.transpose(1,2,0)
k=12
D3_means = np.mean(D3,axis=2)
D_P = D3[2, :, :]
D_X = D3[0, :, :]
D_Y = D3[1, :, :]
nTRs = D3.shape[1]
#D_all=np.concatenate((D1,D2,D3,D4),axis=2)
nSubj = D3.shape[2]
Result = np.zeros(shape=(D3.shape[2],5))
for m in range(D3.shape[2]):
    subj_id_test = m
    subj_id_train = [
        subj_id for subj_id in range(nSubj)
        if subj_id not in [subj_id_test]
    ]
    D_train = D3[:, :, subj_id_train]
    D_test = D3[:, :, subj_id_test]

    D_group_train = np.mean(D_train, axis=2)
    D_P_test = D_P[:, subj_id_test]
    hmm_sim = brainiak.eventseg.event.EventSegment(k)
    hmm_sim.fit(D_group_train.T)

    D_test = stats.zscore(D_test, axis=1, ddof=1)
    test_segments, test_ll = hmm_sim.find_events(D_test.T)
    predtest_seg = test_segments
    testbounds = np.where(np.diff(np.argmax(predtest_seg, axis=1)))[0]
    a = 0
    test_1 = testbounds
    while test_1[0] <= 25:
        a = 1
        test_1 = test_1[a:]
    test_ = test_1
    b = len(test_) - 1
    while test_[b] >= 7605:
        b = b - 1
        test_ = test_[:b + 1]

    pre2bou_ = np.zeros(len(test_))
    pre1bou_ = np.zeros(len(test_))
    boundary_ = np.zeros(len(test_))
    post1bou_ = np.zeros(len(test_))
    post2bou_ = np.zeros(len(test_))
    for i in range(len(test_)):
        pre2bou_[i] = np.mean(D_P_test[(test_[i] - 25):test_[i] - 15])
        pre1bou_[i] = np.mean(D_P_test[(test_[i] - 15):test_[i] - 5])
        boundary_[i] = np.mean(D_P_test[(test_[i] - 5):test_[i] + 5])
        post1bou_[i] = np.mean(D_P_test[(test_[i] + 5):test_[i] + 15])
        post2bou_[i] = np.mean(D_P_test[(test_[i] + 15):test_[i] + 25])

    Result[m][0] = np.mean(pre2bou_)
    Result[m][1] = np.mean(pre1bou_)
    Result[m][2] = np.mean(boundary_)
    Result[m][3] = np.mean(post1bou_)
    Result[m][4] = np.mean(post2bou_)
    print(Result)

workbook = xw.Workbook('pupil size STEM Course.xls', {'nan_inf_to_errors': True})  # 创建工作簿
worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
worksheet1.activate()  # 激活表
title = ['姓名', '年龄', '性别']  # 设置表头
data = Result

worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
i = 2  # 从第二行开始写入数据
for j in range(len(data)):
    insertData = [data[j][0], data[j][1], data[j][2], data[j][3], data[j][4]]
    row = 'A' + str(i)
    worksheet1.write_row(row, insertData)
    i += 1
workbook.close()  # 关闭表