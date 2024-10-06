%对于fill后的数据，截取出某一时间段数据保存。

clc;
clear;

student_extr_start=5001;%注意此处剪视频时留下的1帧白屏已经再C2代码中切去了
student_extr_end=58000; %选取中间764000的时间点

filelist_student = dir('C:\Users\86159\Desktop\_temp_matlab_R2022a_win64\Matlab\fill\*mat');
savepath_student = 'C:\Users\86159\Desktop\_temp_matlab_R2022a_win64\Matlab\extract\';

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%↑以上需修改↑↑以上需修改↑↑以上需修改↑%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%截取学生数据

[Nfile3,~] = size(filelist_student);

for nf3 = 1 : Nfile3
    
load(strcat(filelist_student(nf3).folder,'/',filelist_student(nf3).name));
filename_student = strsplit(filelist_student(nf3).name,'.');
savename_student = strcat(savepath_student,'extr_',filename_student{1,1},'.mat');

GJP_student=GJP(student_extr_start:student_extr_end,:);
GJX_student=GJX(student_extr_start:student_extr_end,:);
GJY_student=GJY(student_extr_start:student_extr_end,:);

save(savename_student,'GJP_student', 'GJX_student', 'GJY_student');
clear  GJP  GJX  GJY  YCP  YCX  YCY

end