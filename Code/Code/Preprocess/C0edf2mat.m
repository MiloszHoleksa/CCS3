%将EDF转化为MAT并保存

clear;
clc;
filepath='Users\lansenn\Documents\MATLAB\edf'  %汇总EDF的文件夹
savepath = 'Users\lansenn\Documents\MATLAB\mat\'%存储转换EDF后的文件夹

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%↑以上需修改↑↑以上需修改↑↑以上需修改↑%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

cd(filepath)%该程序需要CD到相应的文件夹
filelist = dir([filepath '\*edf']);%中括号可将两者合并
[Nfile,~] = size(filelist);
for nf = 1 : Nfile
    demo = edfmex(strcat(filelist(nf).name));
    filename = strsplit(filelist(nf).name,'.');
    savename = strcat(savepath,filename{1,1},'.mat');
    save(savename,'demo');
    clear demo;
    note= [filelist(nf).name '-ok!'];
    note
end