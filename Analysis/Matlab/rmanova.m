
filename ='Study/threshold_23.csv';
data = csvread(filename,1,0);

re= find(data(:,1)==1)
loc1_min=[]
loc2_min=[]
loc3_min=[]
loc4_min=[]
loc5_min=[]
loc6_min=[]
loc1_max=[]
loc2_max=[]
loc3_max=[]
loc4_max=[]
loc5_max=[]
loc6_max=[]
p_number =[]
i =1
while i<121
    p_number = [p_number data(i,1)]
    i = i+6
end
%get update from pranavi about subject gender
Gender = ['F' 'F' 'F' 'F' 'F' 'F' 'F' 'F' 'M' 'M' 'M' 'M' 'M' 'M' 'M' 'M''F''F''F''F'];
for i=1:120
    if  data(i,4)==1
        loc1_min=[loc1_min data(i,6)]
    end
    if  data(i,4)==2
        loc2_min=[loc2_min data(i,6)]
    end
    if  data(i,4)==3
        loc3_min=[loc3_min data(i,6)]
    end
    if  data(i,4)==4
        loc4_min=[loc4_min data(i,6)]
    end
    if  data(i,4)==5
        loc5_min=[loc5_min data(i,6)]
    end
    if  data(i,4)==6
        loc6_min=[loc6_min data(i,6)]
    end
end




for i=1:120
    if  data(i,4)==1
        loc1_max=[loc1_max data(i,7)]
    end
    if  data(i,4)==2
        loc2_max=[loc2_max data(i,7)]
    end
    if  data(i,4)==3
        loc3_max=[loc3_max data(i,7)]
    end
    if  data(i,4)==4
        loc4_max=[loc4_max data(i,7)]
    end
    if  data(i,4)==5
        loc5_max=[loc5_max data(i,7)]
    end
    if  data(i,4)==6
        loc6_max=[loc6_max data(i,7)]
    end
end
%p_number=p_number[7:17]

Location=[1 2 3 4 5 6]';

t_min = table(p_number',loc1_min',loc2_min',loc3_min',loc4_min',loc5_min',loc6_min','VariableNames',{'SubjectNumber','l1','l2','l3','l4','l5','l6'});
rm_min = fitrm(t_min,'l1-l6 ~ SubjectNumber','WithinDesign',Location,'WithinModel','orthogonalcontrasts')

T_min = multcompare(rm_min,'Time')
ranovatbl_min = ranova(rm_min)

t_max = table(p_number',loc1_max',loc2_max',loc3_max',loc4_max',loc5_max',loc6_max','VariableNames',{'SubjectNumber','l1','l2','l3','l4','l5','l6'});
rm_max = fitrm(t_max,'l1-l6 ~ SubjectNumber','WithinDesign',Location,'WithinModel','orthogonalcontrasts')

T_max = multcompare(rm_max,'Time')
ranovatbl_max = ranova(rm_max)
%[ranovatbl,A,C,D] = ranova(rm,'WithinModel',Location)
%multcompare(ranovatbl)
