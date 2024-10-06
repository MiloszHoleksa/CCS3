%提取每个被试mat中的数据形成data1(N行5列：1序号，2时间，3注视X坐标，4注视Y坐标，5瞳孔)，data2数据

clc;
clear;
filelist = dir('C:\Users\86159\Desktop\_temp_matlab_R2022a_win64\Matlab\mat\*mat');%存储mat的文件夹
savepath = 'C:\Users\86159\Desktop\_temp_matlab_R2022a_win64\Matlab\data\';        %存储data的文件夹

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%↑以上需修改↑↑以上需修改↑↑以上需修改↑%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



[Nfile,~] = size(filelist);


for nf = 1 : Nfile
load(strcat(filelist(nf).folder,'/',filelist(nf).name));
filename = strsplit(filelist(nf).name,'.');
savename = strcat(savepath,'data_',filename{1,1},'.mat');

    %建立data1数据分析集

t=double(demo.FSAMPLE.time(1,:))';
time=(double(demo.FSAMPLE.time(1,:))-double(demo.FSAMPLE.time(1,1))+1)';
x=double(demo.FSAMPLE.gx(2,:))';
y=double(demo.FSAMPLE.gy(2,:))';
p=double(demo.FSAMPLE.pa(2,:))';
data1=[time,t,x,y,p];

    %建立data2索引集

sttime={demo.FEVENT.sttime}';
entime={demo.FEVENT.entime}';
message={demo.FEVENT.message}';
codestring={demo.FEVENT.codestring}';
data2=[sttime,entime,message,codestring];

    %查找mg_sy,blink在message或者codestring中相应的行号
    
mg_sy = find(strcmp(message, 'PLAY_SOUND'));%%查找messagemg_sy的行号(因为sy在视频下2~3行)
blink = find(strcmp(codestring, 'ENDBLINK'));%查找codestring中所有包含mg_sp的行号
 
    %%%查找mg_sp在message中相应的行号
%i=2;%%这个地方是2的原因是数据结构中一般这个mg_sp在mg_sy前2行，用1容易报错
   % while contains(message(mg_sy-i,:),'mg_sp')==0  %contains一个逻辑判断，当声音往上2行的字符是包含sp时为1
    % i=i+1;
   % end
%mg_sp=mg_sy-i;
    
    %锁定mg_sy,blink,mg_sp对应的sttime和entime
  mg_sy_sttime=cell2mat(data2(mg_sy,1));
  %mg_sp_sttime=cell2mat(data2(mg_sp,1));
  blink_sttime=double(cell2mat(data2(blink,1)));
  blink_entime=double(cell2mat(data2(blink,2)));%blink的结束时间
  
    %保存
  clear demo;
  save(savename);
  
  clear t time x y p  data1;
  clear sttime entime codestring message data2;
  clear mg_sy blink i mg_sp;
  clear mg_sy_sttime mg_sp_sttime blink_sttime blink_entime;
  
end
        









