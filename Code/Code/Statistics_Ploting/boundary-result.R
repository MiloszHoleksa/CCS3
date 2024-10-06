library(tidyverse)
library(dabestr)
library(reshape2)
library(ggplot2)
library(patchwork)
library(ggpmisc)
library(bruceR)
library(stats)
library(readr)
library(ggpubr)
library(readxl)
################################################################################
#fig2
################################################################################
mydata2a<- read_excel("~/Desktop/Boundary/Result/Commercial Movie/Figure2a_pupil size.xlsx")
my.data2a  <- reshape2::melt(mydata2a,id.vars = c('SubID','Group'),variable.name = 'Time')
my.data_mean2a<-aggregate(my.data2a[,4],by=list(Time=my.data2a$Time),FUN = mean)
p2a<-ggplot(my.data_mean2a,aes(x=Time,y=x,group=1)) +
  geom_point(size=3,col='#DCE6E7')+
  geom_line(size=2,col="#53868B")+
  labs(y='pupil size')+
  theme(panel.background = element_rect(fill=NA),
        panel.grid.major = element_line(colour = '#DCE6E7'),
        panel.ontop = T)
mydata2c <- read_excel("~/Desktop/Boundary/Result/STEM Course/Figure2c_pupil size.xlsx")
my.data2c  <- reshape2::melt(mydata2c,id.vars = c('SubID','Group'),variable.name = 'Time')
my.data_mean2c<-aggregate(my.data2c[,4],by=list(Time=my.data2c$Time),FUN = mean)
p2c<-ggplot(my.data_mean2c,aes(x=Time,y=x,group=1)) +
  geom_point(size=3,col='#DCE6E7')+
  geom_line(size=2,col="#FFA500")+
  labs(y='pupil size')+
  theme(panel.background = element_rect(fill=NA),
        panel.grid.major = element_line(colour = '#DCE6E7'),
        panel.ontop = T)
mydata2e <- read_excel("~/Desktop/Boundary/Result/STEM Course/Figure2e_pupil size.xlsx")
mydata2e <- reshape2::melt(mydata2e,id.vars = c('SubID','Strength'),variable.name = 'Time')
mydata2e<-aggregate(mydata2e[,4],by=list(Time=mydata2e$Time,strength=mydata2e$Strength),FUN = mean)
p2e<-ggplot(mydata2e,aes(x=Time,y=x,group=strength,col=strength)) +
  geom_point(size=3,col='#DCE6E7')+
  geom_line(size=2)+
  scale_colour_manual(values = c("#FCB391","#F1F6E5","#F6D9C0"))+
  labs(y='pupil size')+
  theme(panel.background = element_rect(fill=NA),
        panel.grid.major = element_line(colour = '#DCE6E7'),
        panel.ontop = T)
mydata2b<- read_excel("~/Desktop/Boundary/Result/Commercial Movie/Figure2b_speed.xlsx")
my.data2b  <- reshape2::melt(mydata2b,id.vars = c('SubID','Group'),variable.name = 'Time')
shared.control <-
  my.data2b %>%
  dabest(Time,value,
         idx = c('-2', "-1",'0','1','2'),
         paired = FALSE
  )

shared.control.mean_diff <- shared.control %>% mean_diff()

p2b<-plot(shared.control.mean_diff,
         rawplot.ylabel = "speed",
         palette = c("#53868B","#53868B", "#53868B","#53868B","#53868B"),
         rawplot.markersize = 1,
         rawplot.groupwidth = 0.4
)
mydata2d <- read_excel("~/Desktop/Boundary/Result/STEM Course/Figure2d_speed.xlsx")
my.data2d  <- reshape2::melt(mydata2d,id.vars = c('SubID','Group'),variable.name = 'Time')
shared.control <-
  my.data2d %>%
  dabest(Time,value,
         idx = c('-2', "-1",'0','1','2'),
         paired = FALSE
  )

shared.control.mean_diff <- shared.control %>% mean_diff()

p2d<-plot(shared.control.mean_diff,
         rawplot.ylabel = "speed",
         palette = c("#FFA500","#FFA500","#FFA500","#FFA500","#FFA500"),
         rawplot.markersize = 1,
         rawplot.groupwidth = 0.4
)
mydata2f <- read_excel("~/Desktop/Boundary/Result/STEM Course/Figure2f_speed.xlsx")
my.data2f  <- reshape2::melt(mydata2f,id.vars = c('SubID','Strength'),variable.name = 'Time')
#my.data1f <-my.data1f[my.data1f$strength=='low',]
shared.control <-
  my.data2f %>%
  dabest(Time,value,
         idx = c('-2', "-1",'0','1','2'),
         paired = FALSE
  )

shared.control.mean_diff <- shared.control %>% mean_diff()

p2f<-plot(shared.control.mean_diff,
         rawplot.ylabel = "speed",
         color.column = Strength,
         palette = c("#FCB391","#F6D9C0","#F1F6E5"),
         rawplot.markersize = 1,
         rawplot.groupwidth = 0.4
)
(p2a+p2b)/(p2c+p2d)/(p2e+p2f)+plot_annotation(tag_levels = 'A')#14*14
################################################################################
#fig3
################################################################################
mydata3a<- read_excel("~/Desktop/Boundary/Result/Commercial Movie/Figure3a_similarity.xlsx")
my.data3a <- reshape2::melt(mydata3a,id.vars = c('SubID','Group'),variable.name = 'Time')
shared.control <-
  my.data3a %>%
  dabest(Time,value,
         idx = c('Within Event pre-Bounday', "Between Events","Within Event post-Bounday"),
         paired = FALSE
  )

shared.control.mean_diff <- shared.control %>% mean_diff()

p3a<-plot(shared.control.mean_diff,
          rawplot.ylabel = "pupil degree of similarity",
          palette = c("#53868B","#53868B", "#53868B"),
          axes.title.fontsize = 20,
          rawplot.markersize = 2,
          rawplot.groupwidth = 0.4
)
mydata3b<- read_excel("~/Desktop/Boundary/Result/Commercial Movie/Figure3b_similarity.xlsx")
my.data3b <- reshape2::melt(mydata3b,id.vars = c('SubID','Group'),variable.name = 'Time')
shared.control <-
  my.data3b %>%
  dabest(Time,value,
         idx = c('Within Event pre-Bounday', "Between Events","Within Event post-Bounday"),
         paired = FALSE
  )

shared.control.mean_diff <- shared.control %>% mean_diff()

p3b<-plot(shared.control.mean_diff,
          rawplot.ylabel = "pupil & XY degree of
          similarity",
          palette = c("#53868B","#53868B", "#53868B"),
          axes.title.fontsize = 20,
          rawplot.markersize = 2,
          rawplot.groupwidth = 0.4
)
mydata3c <- read_excel("~/Desktop/Boundary/Result/STEM Course/Figure3c_similarity.xlsx")
my.data3c <- reshape2::melt(mydata3c,id.vars = c('SubID','Group'),variable.name = 'Time')
shared.control <-
  my.data3c %>%
  dabest(Time,value,
         idx = c('Within Event pre-Bounday', "Between Events","Within Event post-Bounday"),
         paired = FALSE
  )

shared.control.mean_diff <- shared.control %>% mean_diff()

p3c<-plot(shared.control.mean_diff,
          rawplot.ylabel = "pupil degree of similarity",
          palette = c("#FFA500","#FFA500","#FFA500"),
          axes.title.fontsize = 20,
          rawplot.markersize = 2,
          rawplot.groupwidth = 0.4
)
mydata3d <- read_excel("~/Desktop/Boundary/Result/STEM Course/Figure3d_similarity.xlsx")
my.data3d <- reshape2::melt(mydata3d,id.vars = c('SubID','Group'),variable.name = 'Time')
shared.control <-
  my.data3d %>%
  dabest(Time,value,
         idx = c('Within Event pre-Bounday', "Between Events","Within Event post-Bounday"),
         paired = FALSE
  )

shared.control.mean_diff <- shared.control %>% mean_diff()

p3d<-plot(shared.control.mean_diff,
          rawplot.ylabel = "pupil & XY degree of
          similarity",
          palette = c("#FFA500","#FFA500","#FFA500"),
          axes.title.fontsize = 20,
          rawplot.markersize = 2,
          rawplot.groupwidth = 0.4
)
mydata3e <- read_excel("~/Desktop/Boundary/Result/STEM Course/Figure3e_similarity.xlsx")
my.data3e <- reshape2::melt(mydata3e,id.vars = c('SubID','Strength'),variable.name = 'Time')
#my.data1f <-my.data1f[my.data1f$strength=='low',]
shared.control <-
  my.data3e %>%
  dabest(Time,value,
         idx = c('Within Event pre-Bounday', "Between Events","Within Event post-Bounday"),
         paired = FALSE
  )

shared.control.mean_diff <- shared.control %>% mean_diff()

p3e <-plot(shared.control.mean_diff,
          rawplot.ylabel = "pupil degree of similarity",
          color.column = Strength,
          palette = c("#FCB391","#F6D9C0","#F1F6E5"),
          axes.title.fontsize = 20,
          rawplot.markersize = 2,
          rawplot.groupwidth = 0.4
)
mydata3f <- read_excel("~/Desktop/Boundary/Result/STEM Course/Figure3f_similarity.xlsx")
my.data3f <- reshape2::melt(mydata3f,id.vars = c('SubID','Strength'),variable.name = 'Time')
#my.data1f <-my.data1f[my.data1f$strength=='low',]
shared.control <-
  my.data3f %>%
  dabest(Time,value,
         idx = c('Within Event pre-Bounday', "Between Events","Within Event post-Bounday"),
         paired = FALSE
  )

shared.control.mean_diff <- shared.control %>% mean_diff()

p3f <-plot(shared.control.mean_diff,
           rawplot.ylabel = "pupil & XY degree of
           similarity",
           color.column = Strength,
           palette = c("#FCB391","#F6D9C0","#F1F6E5"),
           axes.title.fontsize = 20,
           rawplot.markersize = 2,
           rawplot.groupwidth = 0.4
)
(p3a+p3b)/(p3c+p3d)/(p3e+p3f)#20*20
################################################################################
#fig4
################################################################################
mydata4j <- read_excel("~/Desktop/Boundary/Result/Commercial Movie/Figure4j_K value.xlsx")
my.data4j <- reshape2::melt(mydata4j,id.vars = c('SubID','Group','sequence'),variable.name = 'K')
p4j <- ggplot(data = my.data4j, aes(x = K, y = value, group = 1, color = Group)) +
  geom_jitter(size = 1.5, width = 0.2, height = 0) +
  scale_colour_manual(values = c("#53868B","#53868B","#53868B","#53868B"))+
  theme_classic()+
  theme(
    legend.box.background = element_rect(colour = "grey30"),
    legend.title = element_blank(),
    legend.position = c(2, 1),
    legend.margin = margin(1, 5, 3, 1),
    plot.title = element_text(size = 12, vjust = 10)
  )+
  labs(
    x = 'K value',
    y = "correlation coefficient in the Commercial Movie Dataset"
  )
p4j<-p4j + geom_smooth(method = 'lm', formula = y~x, se = TRUE, show.legend = FALSE) +
  stat_cor(method='pearson',label.x.npc = 'left', label.y.npc = 'top',size = 2.7)
mydata4k <- read_excel("~/Desktop/Boundary/Result/STEM Course/Figure4k_K value.xlsx")
my.data4k <- reshape2::melt(mydata4k,id.vars = c('SubID','Group','sequence'),variable.name = 'K')
p4k <- ggplot(data = my.data4k, aes(x = K, y = value, group = 1, color = Group)) +
  geom_jitter(size = 1.5, width = 0.2, height = 0) +
  scale_colour_manual(values = c("#FFA500"))+
  theme_classic()+
  theme(
    legend.box.background = element_rect(colour = "grey30"),
    legend.title = element_blank(),
    legend.position = c(2, 1),
    legend.margin = margin(1, 5, 3, 1),
    plot.title = element_text(size = 12, vjust = 10)
  )+
  labs(
    x = 'K value',
    y = "correlation coefficient in the STEM Course Dataset"
  )
p4k<-p4k + geom_smooth(method = 'lm', formula = y~x, se = TRUE, show.legend = FALSE) +
  stat_cor(method='pearson',label.x.npc = 'left', label.y.npc = 'top',size = 2.7)

