import random
import warnings
import sys
import os
# import logging

# import deepdish as dd # error
import numpy as np
import xlsxwriter as xw
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

dataFile01 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test01.mat'
dataFile02 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test02.mat'
dataFile03 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test03.mat'

dataFile05 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test05.mat'
dataFile06 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test06.mat'
dataFile07 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test07.mat'
dataFile08 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test08.mat'
dataFile09 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test09.mat'
dataFile10 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test10.mat'
dataFile11 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test11.mat'
dataFile12 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test12.mat'
dataFile13 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test13.mat'
dataFile14 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test14.mat'
dataFile15 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test15.mat'
dataFile16 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test16.mat'
dataFile17 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test17.mat'
dataFile18 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test18.mat'
dataFile19 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test19.mat'
dataFile20 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test20.mat'
dataFile21 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test21.mat'
dataFile22 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test22.mat'
dataFile23 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test23.mat'
dataFile24 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test24.mat'
dataFile25 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test25.mat'
dataFile26 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test26.mat'
dataFile27 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test27.mat'
dataFile28 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test28.mat'
dataFile29 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test29.mat'
dataFile30 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test30.mat'
dataFile31 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test31.mat'
dataFile32 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test32.mat'
dataFile33 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test33.mat'
dataFile34 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test34.mat'
dataFile35 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test35.mat'
dataFile36 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test36.mat'
dataFile37 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test37.mat'
dataFile38 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test38.mat'
dataFile39 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test39.mat'
dataFile40 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test40.mat'
dataFile41 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test41.mat'
dataFile42 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test42.mat'
dataFile43 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test43.mat'
dataFile44 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test44.mat'
dataFile45 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test45.mat'
dataFile46 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test46.mat'
dataFile47 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test47.mat'
dataFile48 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test48.mat'
dataFile49 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test49.mat'
dataFile50 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test50.mat'
dataFile51 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test51.mat'
dataFile52 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test52.mat'
dataFile53 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test53.mat'
dataFile54 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test54.mat'
dataFile55 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test55.mat'
dataFile56 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test56.mat'
dataFile57 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test57.mat'
dataFile58 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test58.mat'
dataFile59 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test59.mat'
dataFile60 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test60.mat'
dataFile61 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test61.mat'
dataFile62 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test62.mat'
dataFile63 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test63.mat'
dataFile64 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test64.mat'
dataFile65 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test65.mat'
dataFile66 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test66.mat'
dataFile67 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test67.mat'
dataFile68 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test68.mat'
dataFile69 = '/Users/lansenn/Desktop/movie_mat/3extract/extr_fill_data_Test69.mat'
dataFile70 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test70.mat'
dataFile71 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test71.mat'
dataFile72 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test72.mat'
dataFile73 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test73.mat'

dataFile75 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test75.mat'
dataFile76 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test76.mat'
dataFile77 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test77.mat'
dataFile78 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test78.mat'
dataFile79 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test79.mat'
dataFile80 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test80.mat'
dataFile81 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test81.mat'
dataFile89 = '/Users/lansenn/Desktop/movie_mat/1extract/extr_fill_data_Test89.mat'
dataFile82 = '/Users/lansenn/Desktop/movie_mat/2extract/extr_fill_data_Test82.mat'

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
data13 = scipy.io.loadmat(dataFile13)
data14 = scipy.io.loadmat(dataFile14)
data15 = scipy.io.loadmat(dataFile15)
data16 = scipy.io.loadmat(dataFile16)
data17 = scipy.io.loadmat(dataFile17)
data18 = scipy.io.loadmat(dataFile18)
data19 = scipy.io.loadmat(dataFile19)
data20 = scipy.io.loadmat(dataFile20)
data21 = scipy.io.loadmat(dataFile21)
data22 = scipy.io.loadmat(dataFile22)
data23 = scipy.io.loadmat(dataFile23)
data24 = scipy.io.loadmat(dataFile24)
data25 = scipy.io.loadmat(dataFile25)
data26 = scipy.io.loadmat(dataFile26)
data27 = scipy.io.loadmat(dataFile27)
data28 = scipy.io.loadmat(dataFile28)
data29 = scipy.io.loadmat(dataFile29)
data30 = scipy.io.loadmat(dataFile30)
data31 = scipy.io.loadmat(dataFile31)
data32 = scipy.io.loadmat(dataFile32)
data33 = scipy.io.loadmat(dataFile33)
data34 = scipy.io.loadmat(dataFile34)
data35 = scipy.io.loadmat(dataFile35)
data36 = scipy.io.loadmat(dataFile36)
data37 = scipy.io.loadmat(dataFile37)
data38 = scipy.io.loadmat(dataFile38)
data39 = scipy.io.loadmat(dataFile39)
data40 = scipy.io.loadmat(dataFile40)
data41 = scipy.io.loadmat(dataFile41)
data42 = scipy.io.loadmat(dataFile42)
data43 = scipy.io.loadmat(dataFile43)
data44 = scipy.io.loadmat(dataFile44)
data45 = scipy.io.loadmat(dataFile45)
data46 = scipy.io.loadmat(dataFile46)
data47 = scipy.io.loadmat(dataFile47)
data48 = scipy.io.loadmat(dataFile48)
data49 = scipy.io.loadmat(dataFile49)
data50 = scipy.io.loadmat(dataFile50)
data51 = scipy.io.loadmat(dataFile51)
data52 = scipy.io.loadmat(dataFile52)
data53 = scipy.io.loadmat(dataFile53)
data54 = scipy.io.loadmat(dataFile54)
data55 = scipy.io.loadmat(dataFile55)
data56 = scipy.io.loadmat(dataFile56)
data57 = scipy.io.loadmat(dataFile57)
data58 = scipy.io.loadmat(dataFile58)
data59 = scipy.io.loadmat(dataFile59)
data60 = scipy.io.loadmat(dataFile60)
data61 = scipy.io.loadmat(dataFile61)
data62 = scipy.io.loadmat(dataFile62)
data63 = scipy.io.loadmat(dataFile63)
data64 = scipy.io.loadmat(dataFile64)
data65 = scipy.io.loadmat(dataFile65)
data66 = scipy.io.loadmat(dataFile66)
data67 = scipy.io.loadmat(dataFile67)
data68 = scipy.io.loadmat(dataFile68)
data69 = scipy.io.loadmat(dataFile69)
data70 = scipy.io.loadmat(dataFile70)
data71 = scipy.io.loadmat(dataFile71)
data73 = scipy.io.loadmat(dataFile73)
data72 = scipy.io.loadmat(dataFile72)
data75 = scipy.io.loadmat(dataFile75)
data76 = scipy.io.loadmat(dataFile76)
data77 = scipy.io.loadmat(dataFile77)
data78 = scipy.io.loadmat(dataFile78)
data79 = scipy.io.loadmat(dataFile79)
data80 = scipy.io.loadmat(dataFile80)
data81 = scipy.io.loadmat(dataFile81)
data82 = scipy.io.loadmat(dataFile82)
data89 = scipy.io.loadmat(dataFile89)
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
data13X = data13['GJX_student']
data13Y = data13['GJY_student']
data13P = data13['GJP_student']
data14X = data14['GJX_student']
data14Y = data14['GJY_student']
data14P = data14['GJP_student']
data15X = data15['GJX_student']
data15Y = data15['GJY_student']
data15P = data15['GJP_student']
data16X = data16['GJX_student']
data16Y = data16['GJY_student']
data16P = data16['GJP_student']
data17X = data17['GJX_student']
data17Y = data17['GJY_student']
data17P = data17['GJP_student']
data18X = data18['GJX_student']
data18Y = data18['GJY_student']
data18P = data18['GJP_student']
data19X = data19['GJX_student']
data19Y = data19['GJY_student']
data19P = data19['GJP_student']
data20X = data20['GJX_student']
data20Y = data20['GJY_student']
data20P = data20['GJP_student']
data21X = data21['GJX_student']
data21Y = data21['GJY_student']
data21P = data21['GJP_student']
data22X = data22['GJX_student']
data22Y = data22['GJY_student']
data22P = data22['GJP_student']
data23X = data23['GJX_student']
data23Y = data23['GJY_student']
data23P = data23['GJP_student']
data24X = data24['GJX_student']
data24Y = data24['GJY_student']
data24P = data24['GJP_student']
data25X = data25['GJX_student']
data25Y = data25['GJY_student']
data25P = data25['GJP_student']
data26X = data26['GJX_student']
data26Y = data26['GJY_student']
data26P = data26['GJP_student']
data27X = data27['GJX_student']
data27Y = data27['GJY_student']
data27P = data27['GJP_student']
data28X = data28['GJX_student']
data28Y = data28['GJY_student']
data28P = data28['GJP_student']
data29X = data29['GJX_student']
data29Y = data29['GJY_student']
data29P = data29['GJP_student']
data30X = data30['GJX_student']
data30Y = data30['GJY_student']
data30P = data30['GJP_student']
data31X = data31['GJX_student']
data31Y = data31['GJY_student']
data31P = data31['GJP_student']
data32X = data32['GJX_student']
data32Y = data32['GJY_student']
data32P = data32['GJP_student']
data33X = data33['GJX_student']
data33Y = data33['GJY_student']
data33P = data33['GJP_student']
data34X = data34['GJX_student']
data34Y = data34['GJY_student']
data34P = data34['GJP_student']
data35X = data35['GJX_student']
data35Y = data35['GJY_student']
data35P = data35['GJP_student']
data36X = data36['GJX_student']
data36Y = data36['GJY_student']
data36P = data36['GJP_student']
data37X = data37['GJX_student']
data37Y = data37['GJY_student']
data37P = data37['GJP_student']
data38X = data38['GJX_student']
data38Y = data38['GJY_student']
data38P = data38['GJP_student']
data39X = data39['GJX_student']
data39Y = data39['GJY_student']
data39P = data39['GJP_student']
data40X = data40['GJX_student']
data40Y = data40['GJY_student']
data40P = data40['GJP_student']
data41X = data41['GJX_student']
data41Y = data41['GJY_student']
data41P = data41['GJP_student']
data42X = data42['GJX_student']
data42Y = data42['GJY_student']
data42P = data42['GJP_student']
data43X = data43['GJX_student']
data43Y = data43['GJY_student']
data43P = data43['GJP_student']
data44X = data44['GJX_student']
data44Y = data44['GJY_student']
data44P = data44['GJP_student']
data45X = data45['GJX_student']
data45Y = data45['GJY_student']
data45P = data45['GJP_student']
data46X = data46['GJX_student']
data46Y = data46['GJY_student']
data46P = data46['GJP_student']
data47X = data47['GJX_student']
data47Y = data47['GJY_student']
data47P = data47['GJP_student']
data48X = data48['GJX_student']
data48Y = data48['GJY_student']
data48P = data48['GJP_student']
data49X = data49['GJX_student']
data49Y = data49['GJY_student']
data49P = data49['GJP_student']
data50X = data50['GJX_student']
data50Y = data50['GJY_student']
data50P = data50['GJP_student']
data51X = data51['GJX_student']
data51Y = data51['GJY_student']
data51P = data51['GJP_student']
data52X = data52['GJX_student']
data52Y = data52['GJY_student']
data52P = data52['GJP_student']
data53X = data53['GJX_student']
data53Y = data53['GJY_student']
data53P = data53['GJP_student']
data54X = data54['GJX_student']
data54Y = data54['GJY_student']
data54P = data54['GJP_student']
data55X = data55['GJX_student']
data55Y = data55['GJY_student']
data55P = data55['GJP_student']
data56X = data56['GJX_student']
data56Y = data56['GJY_student']
data56P = data56['GJP_student']
data57X = data57['GJX_student']
data57Y = data57['GJY_student']
data57P = data57['GJP_student']
data58X = data58['GJX_student']
data58Y = data58['GJY_student']
data58P = data58['GJP_student']
data59X = data59['GJX_student']
data59Y = data59['GJY_student']
data59P = data59['GJP_student']
data60X = data60['GJX_student']
data60Y = data60['GJY_student']
data60P = data60['GJP_student']
data61X = data61['GJX_student']
data61Y = data61['GJY_student']
data61P = data61['GJP_student']
data62X = data62['GJX_student']
data62Y = data62['GJY_student']
data62P = data62['GJP_student']
data63X = data63['GJX_student']
data63Y = data63['GJY_student']
data63P = data63['GJP_student']
data64X = data64['GJX_student']
data64Y = data64['GJY_student']
data64P = data64['GJP_student']
data65X = data65['GJX_student']
data65Y = data65['GJY_student']
data65P = data65['GJP_student']
data66X = data66['GJX_student']
data66Y = data66['GJY_student']
data66P = data66['GJP_student']
data67X = data67['GJX_student']
data67Y = data67['GJY_student']
data67P = data67['GJP_student']
data68X = data68['GJX_student']
data68Y = data68['GJY_student']
data68P = data68['GJP_student']
data69X = data69['GJX_student']
data69Y = data69['GJY_student']
data69P = data69['GJP_student']
data70X = data70['GJX_student']
data70Y = data70['GJY_student']
data70P = data70['GJP_student']
data71X = data71['GJX_student']
data71Y = data71['GJY_student']
data71P = data71['GJP_student']
data73X = data73['GJX_student']
data73Y = data73['GJY_student']
data73P = data73['GJP_student']
data72X = data72['GJX_student']
data72Y = data72['GJY_student']
data72P = data72['GJP_student']
data75X = data75['GJX_student']
data75Y = data75['GJY_student']
data75P = data75['GJP_student']
data76X = data76['GJX_student']
data76Y = data76['GJY_student']
data76P = data76['GJP_student']
data77X = data77['GJX_student']
data77Y = data77['GJY_student']
data77P = data77['GJP_student']
data78X = data78['GJX_student']
data78Y = data78['GJY_student']
data78P = data78['GJP_student']
data79X = data79['GJX_student']
data79Y = data79['GJY_student']
data79P = data79['GJP_student']
data80X = data80['GJX_student']
data80Y = data80['GJY_student']
data80P = data80['GJP_student']
data81X = data81['GJX_student']
data81Y = data81['GJY_student']
data81P = data81['GJP_student']
data82X = data82['GJX_student']
data82Y = data82['GJY_student']
data82P = data82['GJP_student']
data89X = data89['GJX_student']
data89Y = data89['GJY_student']
data89P = data89['GJP_student']

data1 = np.concatenate((data1X[0:1290001:100], data1Y[0:1290001:100], data1P[0:1290001:100]), axis=1)
data2 = np.concatenate((data2X[0:1290001:100], data2Y[0:1290001:100], data2P[0:1290001:100]), axis=1)
data3 = np.concatenate((data3X[0:1290001:100], data3Y[0:1290001:100], data3P[0:1290001:100]), axis=1)
data5 = np.concatenate((data5X[0:1290001:100], data5Y[0:1290001:100], data5P[0:1290001:100]), axis=1)
data6 = np.concatenate((data6X[0:1290001:100], data6Y[0:1290001:100], data6P[0:1290001:100]), axis=1)
data7 = np.concatenate((data7X[0:1290001:100], data7Y[0:1290001:100], data7P[0:1290001:100]), axis=1)
data8 = np.concatenate((data8X[0:1290001:100], data8Y[0:1290001:100], data8P[0:1290001:100]), axis=1)
data9 = np.concatenate((data9X[0:1290001:100], data9Y[0:1290001:100], data9P[0:1290001:100]), axis=1)
data10 = np.concatenate((data10X[0:1290001:100], data10Y[0:1290001:100], data10P[0:1290001:100]), axis=1)
data11 = np.concatenate((data11X[0:1290001:100], data11Y[0:1290001:100], data11P[0:1290001:100]), axis=1)
data12 = np.concatenate((data12X[0:1290001:100], data12Y[0:1290001:100], data12P[0:1290001:100]), axis=1)
data13 = np.concatenate((data13X[0:1290001:100], data13Y[0:1290001:100], data13P[0:1290001:100]), axis=1)
data14 = np.concatenate((data14X[0:1290001:100], data14Y[0:1290001:100], data14P[0:1290001:100]), axis=1)
data15 = np.concatenate((data15X[0:1290001:100], data15Y[0:1290001:100], data15P[0:1290001:100]), axis=1)
data16 = np.concatenate((data16X[0:1290001:100], data16Y[0:1290001:100], data16P[0:1290001:100]), axis=1)
data17 = np.concatenate((data17X[0:1290001:100], data17Y[0:1290001:100], data17P[0:1290001:100]), axis=1)
data18 = np.concatenate((data18X[0:1290001:100], data18Y[0:1290001:100], data18P[0:1290001:100]), axis=1)
data19 = np.concatenate((data19X[0:1290001:100], data19Y[0:1290001:100], data19P[0:1290001:100]), axis=1)
data20 = np.concatenate((data20X[0:1290001:100], data20Y[0:1290001:100], data20P[0:1290001:100]), axis=1)
data21 = np.concatenate((data21X[0:1290001:100], data21Y[0:1290001:100], data21P[0:1290001:100]), axis=1)
data22 = np.concatenate((data22X[0:1290001:100], data22Y[0:1290001:100], data22P[0:1290001:100]), axis=1)
data23 = np.concatenate((data23X[0:1290001:100], data23Y[0:1290001:100], data23P[0:1290001:100]), axis=1)
data24 = np.concatenate((data24X[0:1290001:100], data24Y[0:1290001:100], data24P[0:1290001:100]), axis=1)
data25 = np.concatenate((data25X[0:1290001:100], data25Y[0:1290001:100], data25P[0:1290001:100]), axis=1)
data26 = np.concatenate((data26X[0:1290001:100], data26Y[0:1290001:100], data26P[0:1290001:100]), axis=1)
data27 = np.concatenate((data27X[0:1290001:100], data27Y[0:1290001:100], data27P[0:1290001:100]), axis=1)
data28 = np.concatenate((data28X[0:1290001:100], data28Y[0:1290001:100], data28P[0:1290001:100]), axis=1)
data29 = np.concatenate((data29X[0:1290001:100], data29Y[0:1290001:100], data29P[0:1290001:100]), axis=1)
data30 = np.concatenate((data30X[0:1290001:100], data30Y[0:1290001:100], data30P[0:1290001:100]), axis=1)
data31 = np.concatenate((data31X[0:1290001:100], data31Y[0:1290001:100], data31P[0:1290001:100]), axis=1)
data32 = np.concatenate((data32X[0:1290001:100], data32Y[0:1290001:100], data32P[0:1290001:100]), axis=1)
data33 = np.concatenate((data33X[0:1290001:100], data33Y[0:1290001:100], data33P[0:1290001:100]), axis=1)
data34 = np.concatenate((data34X[0:1290001:100], data34Y[0:1290001:100], data34P[0:1290001:100]), axis=1)
data35 = np.concatenate((data35X[0:1290001:100], data35Y[0:1290001:100], data35P[0:1290001:100]), axis=1)
data36 = np.concatenate((data36X[0:1290001:100], data36Y[0:1290001:100], data36P[0:1290001:100]), axis=1)
data37 = np.concatenate((data37X[0:1290001:100], data37Y[0:1290001:100], data37P[0:1290001:100]), axis=1)
data38 = np.concatenate((data38X[0:1290001:100], data38Y[0:1290001:100], data38P[0:1290001:100]), axis=1)
data39 = np.concatenate((data39X[0:1290001:100], data39Y[0:1290001:100], data39P[0:1290001:100]), axis=1)
data40 = np.concatenate((data40X[0:1290001:100], data40Y[0:1290001:100], data40P[0:1290001:100]), axis=1)
data41 = np.concatenate((data41X[0:1290001:100], data41Y[0:1290001:100], data41P[0:1290001:100]), axis=1)
data42 = np.concatenate((data42X[0:1290001:100], data42Y[0:1290001:100], data42P[0:1290001:100]), axis=1)
data43 = np.concatenate((data43X[0:1290001:100], data43Y[0:1290001:100], data43P[0:1290001:100]), axis=1)
data44 = np.concatenate((data44X[0:1290001:100], data44Y[0:1290001:100], data44P[0:1290001:100]), axis=1)
data45 = np.concatenate((data45X[0:1290001:100], data45Y[0:1290001:100], data45P[0:1290001:100]), axis=1)
data46 = np.concatenate((data46X[0:1290001:100], data46Y[0:1290001:100], data46P[0:1290001:100]), axis=1)
data47 = np.concatenate((data47X[0:1290001:100], data47Y[0:1290001:100], data47P[0:1290001:100]), axis=1)
data48 = np.concatenate((data48X[0:1290001:100], data48Y[0:1290001:100], data48P[0:1290001:100]), axis=1)
data49 = np.concatenate((data49X[0:1290001:100], data49Y[0:1290001:100], data49P[0:1290001:100]), axis=1)
data50 = np.concatenate((data50X[0:1290001:100], data50Y[0:1290001:100], data50P[0:1290001:100]), axis=1)
data51 = np.concatenate((data51X[0:1290001:100], data51Y[0:1290001:100], data51P[0:1290001:100]), axis=1)
data52 = np.concatenate((data52X[0:1290001:100], data52Y[0:1290001:100], data52P[0:1290001:100]), axis=1)
data53 = np.concatenate((data53X[0:1290001:100], data53Y[0:1290001:100], data53P[0:1290001:100]), axis=1)
data54 = np.concatenate((data54X[0:1290001:100], data54Y[0:1290001:100], data54P[0:1290001:100]), axis=1)
data55 = np.concatenate((data55X[0:1290001:100], data55Y[0:1290001:100], data55P[0:1290001:100]), axis=1)
data56 = np.concatenate((data56X[0:1290001:100], data56Y[0:1290001:100], data56P[0:1290001:100]), axis=1)
data57 = np.concatenate((data57X[0:1290001:100], data57Y[0:1290001:100], data57P[0:1290001:100]), axis=1)
data58 = np.concatenate((data58X[0:1290001:100], data58Y[0:1290001:100], data58P[0:1290001:100]), axis=1)
data59 = np.concatenate((data59X[0:1290001:100], data59Y[0:1290001:100], data59P[0:1290001:100]), axis=1)
data60 = np.concatenate((data60X[0:1290001:100], data60Y[0:1290001:100], data60P[0:1290001:100]), axis=1)
data61 = np.concatenate((data61X[0:1290001:100], data61Y[0:1290001:100], data61P[0:1290001:100]), axis=1)
data62 = np.concatenate((data62X[0:1290001:100], data62Y[0:1290001:100], data62P[0:1290001:100]), axis=1)
data63 = np.concatenate((data63X[0:1290001:100], data63Y[0:1290001:100], data63P[0:1290001:100]), axis=1)
data64 = np.concatenate((data64X[0:1290001:100], data64Y[0:1290001:100], data64P[0:1290001:100]), axis=1)
data65 = np.concatenate((data65X[0:1290001:100], data65Y[0:1290001:100], data65P[0:1290001:100]), axis=1)
data66 = np.concatenate((data66X[0:1290001:100], data66Y[0:1290001:100], data66P[0:1290001:100]), axis=1)
data67 = np.concatenate((data67X[0:1290001:100], data67Y[0:1290001:100], data67P[0:1290001:100]), axis=1)
data68 = np.concatenate((data68X[0:1290001:100], data68Y[0:1290001:100], data68P[0:1290001:100]), axis=1)
data69 = np.concatenate((data69X[0:1290001:100], data69Y[0:1290001:100], data69P[0:1290001:100]), axis=1)
data70 = np.concatenate((data70X[0:1290001:100], data70Y[0:1290001:100], data70P[0:1290001:100]), axis=1)
data71 = np.concatenate((data71X[0:1290001:100], data71Y[0:1290001:100], data71P[0:1290001:100]), axis=1)
data72 = np.concatenate((data72X[0:1290001:100], data72Y[0:1290001:100], data72P[0:1290001:100]), axis=1)
data73 = np.concatenate((data73X[0:1290001:100], data73Y[0:1290001:100], data73P[0:1290001:100]), axis=1)
data75 = np.concatenate((data75X[0:1290001:100], data75Y[0:1290001:100], data75P[0:1290001:100]), axis=1)
data76 = np.concatenate((data76X[0:1290001:100], data76Y[0:1290001:100], data76P[0:1290001:100]), axis=1)
data77 = np.concatenate((data77X[0:1290001:100], data77Y[0:1290001:100], data77P[0:1290001:100]), axis=1)
data78 = np.concatenate((data78X[0:1290001:100], data78Y[0:1290001:100], data78P[0:1290001:100]), axis=1)
data79 = np.concatenate((data79X[0:1290001:100], data79Y[0:1290001:100], data79P[0:1290001:100]), axis=1)
data80 = np.concatenate((data80X[0:1290001:100], data80Y[0:1290001:100], data80P[0:1290001:100]), axis=1)
data81 = np.concatenate((data81X[0:1290001:100], data81Y[0:1290001:100], data81P[0:1290001:100]), axis=1)
data82 = np.concatenate((data82X[0:1290001:100], data82Y[0:1290001:100], data82P[0:1290001:100]), axis=1)
data89 = np.concatenate((data89X[0:1290001:100], data89Y[0:1290001:100], data89P[0:1290001:100]), axis=1)
dataFile401 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test101.mat'
dataFile402 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test102.mat'
dataFile403 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test103.mat'
dataFile404 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test104.mat'
dataFile405 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test105.mat'
dataFile406 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test106.mat'
dataFile407 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test107.mat'
dataFile408 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test108.mat'
dataFile409 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test109.mat'
dataFile410 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test110.mat'
dataFile411 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test111.mat'
dataFile413 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test113.mat'
dataFile414 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test114.mat'
dataFile416 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test116.mat'
dataFile417 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test117.mat'
dataFile418 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test118.mat'
dataFile419 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test119.mat'
dataFile420 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test120.mat'
dataFile421 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test121.mat'
dataFile426 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test126.mat'
dataFile427 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test127.mat'
dataFile428 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test128.mat'
dataFile429 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test129.mat'
dataFile430 = '/Users/lansenn/Desktop/extract/extr_fill_data_Test130.mat'

fdata1 = scipy.io.loadmat(dataFile401)
fdata2 = scipy.io.loadmat(dataFile402)
fdata3 = scipy.io.loadmat(dataFile403)
fdata4 = scipy.io.loadmat(dataFile404)
fdata5 = scipy.io.loadmat(dataFile405)
fdata6 = scipy.io.loadmat(dataFile406)
fdata7 = scipy.io.loadmat(dataFile407)
fdata8 = scipy.io.loadmat(dataFile408)
fdata9 = scipy.io.loadmat(dataFile409)
fdata10 = scipy.io.loadmat(dataFile410)
fdata11 = scipy.io.loadmat(dataFile411)
fdata13 = scipy.io.loadmat(dataFile413)
fdata14 = scipy.io.loadmat(dataFile414)
fdata16 = scipy.io.loadmat(dataFile416)
fdata17 = scipy.io.loadmat(dataFile417)
fdata18 = scipy.io.loadmat(dataFile418)
fdata19 = scipy.io.loadmat(dataFile419)
fdata20 = scipy.io.loadmat(dataFile420)
fdata21 = scipy.io.loadmat(dataFile421)
fdata26 = scipy.io.loadmat(dataFile426)
fdata27 = scipy.io.loadmat(dataFile427)
fdata28 = scipy.io.loadmat(dataFile428)
fdata29 = scipy.io.loadmat(dataFile429)
fdata30 = scipy.io.loadmat(dataFile430)

fdata1X = fdata1['GJX_student']
fdata1Y = fdata1['GJY_student']
fdata1P = fdata1['GJP_student']
fdata2X = fdata2['GJX_student']
fdata2Y = fdata2['GJY_student']
fdata2P = fdata2['GJP_student']
fdata3X = fdata3['GJX_student']
fdata3Y = fdata3['GJY_student']
fdata3P = fdata3['GJP_student']
fdata4X = fdata4['GJX_student']
fdata4Y = fdata4['GJY_student']
fdata4P = fdata4['GJP_student']
fdata5X = fdata5['GJX_student']
fdata5Y = fdata5['GJY_student']
fdata5P = fdata5['GJP_student']
fdata6X = fdata6['GJX_student']
fdata6Y = fdata6['GJY_student']
fdata6P = fdata6['GJP_student']
fdata7X = fdata7['GJX_student']
fdata7Y = fdata7['GJY_student']
fdata7P = fdata7['GJP_student']
fdata8X = fdata8['GJX_student']
fdata8Y = fdata8['GJY_student']
fdata8P = fdata8['GJP_student']
fdata9X = fdata9['GJX_student']
fdata9Y = fdata9['GJY_student']
fdata9P = fdata9['GJP_student']
fdata10X = fdata10['GJX_student']
fdata10Y = fdata10['GJY_student']
fdata10P = fdata10['GJP_student']
fdata11X = fdata11['GJX_student']
fdata11Y = fdata11['GJY_student']
fdata11P = fdata11['GJP_student']
fdata13X = fdata13['GJX_student']
fdata13Y = fdata13['GJY_student']
fdata13P = fdata13['GJP_student']
fdata14X = fdata14['GJX_student']
fdata14Y = fdata14['GJY_student']
fdata14P = fdata14['GJP_student']
fdata16X = fdata16['GJX_student']
fdata16Y = fdata16['GJY_student']
fdata16P = fdata16['GJP_student']
fdata17X = fdata17['GJX_student']
fdata17Y = fdata17['GJY_student']
fdata17P = fdata17['GJP_student']
fdata18X = fdata18['GJX_student']
fdata18Y = fdata18['GJY_student']
fdata18P = fdata18['GJP_student']
fdata19X = fdata19['GJX_student']
fdata19Y = fdata19['GJY_student']
fdata19P = fdata19['GJP_student']
fdata20X = fdata20['GJX_student']
fdata20Y = fdata20['GJY_student']
fdata20P = fdata20['GJP_student']
fdata21X = fdata21['GJX_student']
fdata21Y = fdata21['GJY_student']
fdata21P = fdata21['GJP_student']
fdata26X = fdata26['GJX_student']
fdata26Y = fdata26['GJY_student']
fdata26P = fdata26['GJP_student']
fdata27X = fdata27['GJX_student']
fdata27Y = fdata27['GJY_student']
fdata27P = fdata27['GJP_student']
fdata28X = fdata28['GJX_student']
fdata28Y = fdata28['GJY_student']
fdata28P = fdata28['GJP_student']
fdata29X = fdata29['GJX_student']
fdata29Y = fdata29['GJY_student']
fdata29P = fdata29['GJP_student']
fdata30X = fdata30['GJX_student']
fdata30Y = fdata30['GJY_student']
fdata30P = fdata30['GJP_student']

fdata1 = np.concatenate((fdata1X[0:1290001:100], fdata1Y[0:1290001:100], fdata1P[0:1290001:100]), axis=1)
fdata2 = np.concatenate((fdata2X[0:1290001:100], fdata2Y[0:1290001:100], fdata2P[0:1290001:100]), axis=1)
fdata3 = np.concatenate((fdata3X[0:1290001:100], fdata3Y[0:1290001:100], fdata3P[0:1290001:100]), axis=1)
fdata4 = np.concatenate((fdata4X[0:1290001:100], fdata4Y[0:1290001:100], fdata4P[0:1290001:100]), axis=1)
fdata5 = np.concatenate((fdata5X[0:1290001:100], fdata5Y[0:1290001:100], fdata5P[0:1290001:100]), axis=1)
fdata6 = np.concatenate((fdata6X[0:1290001:100], fdata6Y[0:1290001:100], fdata6P[0:1290001:100]), axis=1)
fdata7 = np.concatenate((fdata7X[0:1290001:100], fdata7Y[0:1290001:100], fdata7P[0:1290001:100]), axis=1)
fdata8 = np.concatenate((fdata8X[0:1290001:100], fdata8Y[0:1290001:100], fdata8P[0:1290001:100]), axis=1)
fdata9 = np.concatenate((fdata9X[0:1290001:100], fdata9Y[0:1290001:100], fdata9P[0:1290001:100]), axis=1)
fdata10 = np.concatenate((fdata10X[0:1290001:100], fdata10Y[0:1290001:100], fdata10P[0:1290001:100]), axis=1)
fdata11 = np.concatenate((fdata11X[0:1290001:100], fdata11Y[0:1290001:100], fdata11P[0:1290001:100]), axis=1)
fdata13 = np.concatenate((fdata13X[0:1290001:100], fdata13Y[0:1290001:100], fdata13P[0:1290001:100]), axis=1)
fdata14 = np.concatenate((fdata14X[0:1290001:100], fdata14Y[0:1290001:100], fdata14P[0:1290001:100]), axis=1)
fdata16 = np.concatenate((fdata16X[0:1290001:100], fdata16Y[0:1290001:100], fdata16P[0:1290001:100]), axis=1)
fdata17 = np.concatenate((fdata17X[0:1290001:100], fdata17Y[0:1290001:100], fdata17P[0:1290001:100]), axis=1)
fdata18 = np.concatenate((fdata18X[0:1290001:100], fdata18Y[0:1290001:100], fdata18P[0:1290001:100]), axis=1)
fdata19 = np.concatenate((fdata19X[0:1290001:100], fdata19Y[0:1290001:100], fdata19P[0:1290001:100]), axis=1)
fdata20 = np.concatenate((fdata20X[0:1290001:100], fdata20Y[0:1290001:100], fdata20P[0:1290001:100]), axis=1)
fdata21 = np.concatenate((fdata21X[0:1290001:100], fdata21Y[0:1290001:100], fdata21P[0:1290001:100]), axis=1)
fdata26 = np.concatenate((fdata26X[0:1290001:100], fdata26Y[0:1290001:100], fdata26P[0:1290001:100]), axis=1)
fdata27 = np.concatenate((fdata27X[0:1290001:100], fdata27Y[0:1290001:100], fdata27P[0:1290001:100]), axis=1)
fdata28 = np.concatenate((fdata28X[0:1290001:100], fdata28Y[0:1290001:100], fdata28P[0:1290001:100]), axis=1)
fdata29 = np.concatenate((fdata29X[0:1290001:100], fdata29Y[0:1290001:100], fdata29P[0:1290001:100]), axis=1)
fdata30 = np.concatenate((fdata30X[0:1290001:100], fdata30Y[0:1290001:100], fdata30P[0:1290001:100]), axis=1)

D = np.array(
    [fdata1.T, fdata2.T, fdata3.T, fdata4.T,fdata5.T, fdata6.T, fdata7.T, fdata8.T, fdata9.T,fdata10.T, fdata11.T,
     fdata13.T,fdata14.T, fdata16.T, fdata17.T, fdata18.T, fdata19.T,fdata21.T,
     fdata26.T, fdata27.T, fdata28.T, fdata29.T,fdata30.T, ])
A = np.array(
    [data1.T, data2.T, data3.T, data7.T, data9.T, data12.T, data13.T, data16.T, data17.T, data18.T, data19.T, data23.T,
     data26.T, data27.T, data30.T, data32.T, data35.T, data38.T, data41.T, data45.T, data46.T, data55.T, data63.T,
     data68.T, data71.T, data76.T, data77.T, data80.T, data81.T, data89.T])
B = np.array(
    [data33.T, data34.T, data39.T, data42.T, data43.T, data47.T, data48.T, data49.T, data50.T, data51.T, data52.T,
     data53.T, data57.T, data58.T, data60.T, data62.T, data66.T, data67.T, data70.T, data72.T, data73.T, data75.T,
     data78.T, data79.T, data82.T])
C = np.array([data5.T, data6.T, data8.T, data10.T, data11.T, data14.T, data15.T, data20.T, data21.T, data22.T, data24.T,
              data25.T, data28.T, data29.T, data31.T, data36.T, data37.T, data40.T, data44.T, data54.T, data56.T,
              data59.T, data61.T, data64.T, data65.T, data69.T])
D1 = A.transpose(1, 2, 0)
D2 = B.transpose(1, 2, 0)
D3 = C.transpose(1, 2, 0)
D = D.transpose(1, 2, 0)

nTRs = D.shape[1]
nSubj = D.shape[2]
Result = np.zeros(shape=(D.shape[2],18))
#test_ = np.array([340, 1530, 2300, 3600, 4790, 5290, 7000, 7540, 8380, 8610,8800, 9290, 9650, 10260, 10600, 11130, 11810, 12450])
#test_=np.array([290, 1480, 2250, 3550, 4740, 5240, 6950, 7490, 8330, 8560,8750, 9240, 9600, 10210, 10550, 11080, 11760, 12400])
test_=np.array([390, 1580, 2350, 3650, 4840, 5340, 7050, 7590, 8430, 8660,8850, 9340, 9700, 10310, 10650, 11180, 11860, 12500])

for i in range(D.shape[2]):
    subj_id_test = i
    subj_id_train = [
        subj_id for subj_id in range(nSubj)
        if subj_id not in [subj_id_test]
    ]
    D_train = D[:, :, subj_id_train]
    xbou_ = np.zeros(shape=(D_train.shape[2],len(test_)))
    ybou_ = np.zeros(shape=(D_train.shape[2],len(test_)))
    pbou_ = np.zeros(shape=(D_train.shape[2],len(test_)))
    D_test = D[:, :, subj_id_test]
    D_test1 = stats.zscore(D_test, axis=1, ddof=1)

    for m in range(D_train.shape[2]):
        D_train1=D_train[:,:,m]
        D_train1 = stats.zscore(D_train1, axis=1, ddof=1)

        for n in range(len(test_)):
            xbou_[m,n] = np.mean(np.corrcoef(D_test1[0,:][test_[n]-50:test_[n]+50],
                                            D_train1[0,:][test_[n]-50:test_[n]+50]))
            ybou_[m,n] = np.mean(
                np.corrcoef(D_test1[1, :][test_[n]-50:test_[n]+50],
                            D_train1[1, :][test_[n]-50:test_[n]+50]))
            pbou_[m,n] = np.mean(
                np.corrcoef(D_test1[2, :][test_[n]-50:test_[n]+50],
                            D_train1[2, :][test_[n]-50:test_[n]+50]))
    Result[i]=np.mean((xbou_+ybou_+pbou_)/3,axis=0)