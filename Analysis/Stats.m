clear all
close all

filename ='Study/threshold.csv';
M = csvread(filename,1,0);
j=6
Data = zeros(20,5)
k= 1
for i =1:389
   if M(i,6) == 2
       Data(k,1)=M(i,4)
       Data(k,2)=M(i,5)
       Data(k,3)=M(i,7)
       Data(k,5)=M(i,1)
   end
   if M(i,6) == 3
       Data(k,4)=M(i,8)
       k = k+1
   end
end

writematrix(Data,'Study/threshold_part.csv')

G = findgroups(Data(:,5))

Y = splitapply(@mean,Data,G)

plot((1:20),Y(:,3),'.')
hold on 
plot((1:20),Y(:,4),'.')
hold off 
%boxplot of perception 
boxplot(Data(:,3),Data(:,2))

%boxplot of tolerance 
%boxplot(Data(:,4),Data(:,5))
ylim([0 40])

[p,t,stats1] = anova1(Data(:,3),Data(:,2),"subjects")
[c,m,h] = multcompare(stats1)

%Calculate the mean of perception threshold for each person 
for i = 1:116
    for k=1:20
        %if Data(i,5)=k

        
    end
end

%Calculate the mean of tolerance for each person

       