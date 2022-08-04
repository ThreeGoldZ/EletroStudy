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
       