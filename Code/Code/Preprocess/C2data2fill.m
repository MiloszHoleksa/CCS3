%由于眼动数据在刺激呈现前还会再记录一段时间，因此本代码首先将数据从头切齐
%再找到眨眼填充为NAN并插值，找到异常值填充为NAN并插值。

clc;
clear;
filelist2 = dir('C:\Users\86159\Desktop\_temp_matlab_R2022a_win64\Matlab\data\*mat');%存储data的文件夹
savepath2 = 'C:\Users\86159\Desktop\_temp_matlab_R2022a_win64\Matlab\fill\';         %存储填充之后的文件夹
start=16;%从mg_sp后多久开始截取，初始大概在16行，start=16的原因是在制作视频材料时前面有1帧（60hz）的白屏

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%↑以上需修改↑↑以上需修改↑↑以上需修改↑%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[Nfile2,~] = size(filelist2);
for nf2 = 1 : Nfile2

load(strcat(filelist2(nf2).folder,'/',filelist2(nf2).name));
filename = strsplit(filelist2(nf2).name,'.');
savename = strcat(savepath2,'fill_',filename{1,1},'.mat');

%切掉前面没呈现刺激前的时间
ss=find(data1(:,2)==mg_sy_sttime);%找到mg_sp开始的行位置
eye_x=x(ss+start:end,:);
eye_y=y(ss+start:end,:);
eye_p=p(ss+start:end,:);

%将blink替换为NAN
len=length(blink);

for i=1:len
     %眨眼开始点不能小于100
     zhayandian_start=blink_sttime(i,:)-mg_sy_sttime-start+1;%眨眼的相对时间减去刺激开始时的相对时间，得到开始后的绝对时间,在去掉裁去的16行
    if zhayandian_start<101
        zhayandian_start=101;
    end
     %眨眼结束点不能大于eye_x行数的倒数100
     zhayandian_end=blink_entime(i,:)-mg_sy_sttime-start+1;
    if zhayandian_end>size(eye_x,1)-100
        zhayandian_end=size(eye_x,1)-100;
    end
 eye_x((zhayandian_start-100):(zhayandian_end+100),:)=nan;
 eye_y((zhayandian_start-100):(zhayandian_end+100),:)=nan;
 eye_p((zhayandian_start-100):(zhayandian_end+100),:)=nan;
end

%将NAN进行线性插值
EYE_X= fillmissing(eye_x,'linear');
EYE_Y= fillmissing(eye_y,'linear');
EYE_P= fillmissing(eye_p,'linear');

% % 使用filloutliers对异常值进行替换(弃用)
% YCX=filloutliers(EYE_X,'linear');
% YCY=filloutliers(EYE_Y,'linear');
% YCP=filloutliers(EYE_P,'linear');
YCX=EYE_X;
YCY=EYE_Y;
YCP=EYE_P;

%查找过界值并进行替换
GJ=[find(YCX>1280|YCX<=0);find(YCY>1024|YCY<=0);find(YCP<=0)];
len2=length(GJ);
for j=1:len2
%防止yichangzhi异常值在头导致报错
    yichangdian=GJ(j,:);
    if yichangdian<101
        yichangdian=101;
    end
    %防止yichangzhi异常值在尾导致报错
    if yichangdian>size(eye_x,1)-100
        yichangdian=size(eye_x,1)-100;
    end
    
YCX((yichangdian-100):(yichangdian+100),:)=nan;
YCY((yichangdian-100):(yichangdian+100),:)=nan;
YCP((yichangdian-100):(yichangdian+100),:)=nan;
end

%将NAN进行线性插值
GJX= fillmissing(YCX,'linear');
GJY= fillmissing(YCY,'linear');
GJP= fillmissing(YCP,'linear');


 save(savename,'EYE_X','EYE_Y','EYE_P', 'YCX', 'YCY', 'YCP','GJX', 'GJY','GJP' );
clear eye_x eye_y eye_p ss len2 GJ EYE_X EYE_Y EYE_P YCP YCX YCY GJX GJY GJP yichangdian
end



%clearvars -except savename EYE_X EYE_Y EYE_P

