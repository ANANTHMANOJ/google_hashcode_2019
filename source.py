in_file=open('a_example.txt',"r")
out_file=open('a_example_out.txt',"w")
r=int(in_file.readline())
#print(r)
i=1
pic_hv={}
line=[]
spec={}
slides=0
ver=0
slide_show=[]
#upd_key=
nxt_pic=0




def add_pic(pic,i):
    #print(slide_show)
    slide_show.append(pic)
    if i==1:
       slide_show.append('\n')        
    else:
        slide_show.append(' ')
  
    
    
def check_ver(pic,pr_spec):
    global nxt_slide
    temp=0
    flag=0
    for i in pic_hv:
        #print(i)
        if 'V' in pic_hv[i] and pic_hv[i][0]==1:
            temp=i
            if i in spec[pr_spec]:
                nxt_slide=i
                return 1
            flag=1
    if flag==1:
        nxt_slide=temp
        return 1
    else:
        return 0   
        


def sel_nxt_spec(pic,prev_spec):
    m=0
    selected=-1
    for i in spec:
        if pic in spec[i] and i!=prev_spec and int(m)<len(spec[i]):
            for j in spec[i]:
                if pic_hv[j][0]==1:
                    m=len(spec[i])
                    selected=i
                    
                    break
                    
    if selected!=-1:
        
        pick_pic(selected)
#    else:
#       print(slide_show)
    
    

def sel_nxt_pic(pr_spec):
    m=0
    selected=-1
    
    global ver,slides,nxt_slide
    for i in spec[pr_spec]:
        if pic_hv[i][0]==1 and int(pic_hv[i][2])>int(m):
            selected=i
            m=pic_hv[i][2]
    if selected!=-1:
        if pic_hv[selected][1]=='H':
             nxt_slide=selected
             slides+=1
             pic_hv[selected][0]=0
             add_pic(nxt_slide,1)
             sel_nxt_spec(nxt_slide,pr_spec)
        else:
            pic_hv[selected][0]=0
            if check_ver(selected,pr_spec):
                   #print(selected)
                   if ver%2==0:
                       ver=1
                       add_pic(selected,0)
                       #print(nxt_pic)
                       add_pic(nxt_pic,1)
                       sel_nxt_spec(nxt_pic,pr_spec)
                   else:
                       ver=0
                       slides+=1
                       add_pic(selected,1)
            else:
                sel_nxt_pic(pr_spec)
               
                       
            
            
                
            
        
    
    

def pick_pic(sel_spec):
    global slides,ver
    for i in spec[sel_spec]:
       if pic_hv[i][0]==0 :
           continue
       else:
           if pic_hv[i][1]=='H':
               pic_hv[i][0]=0
               slides+=1
               add_pic(i,1)
               sel_nxt_pic(sel_spec)
           else:
               pic_hv[i][0]=0
               if check_ver(i,sel_spec):
                   
                   if ver%2==0:
                       ver=1
                       slides+=1
                       add_pic(i,0)
                       add_pic(nxt_slide,1)
                       sel_nxt_spec(nxt_slide,sel_spec)
                   else:
                       ver=0
                       slides+=1
                       add_pic(i,1)
                       #print(i)
                #else select new pic
                       
       


while i<=r:
    line=(in_file.readline().split(' '))
    line=[i.split('\n')[0] for i in line]
    pic_hv.setdefault(i-1,[])
    pic_hv[i-1].append(1)
    pic_hv[i-1].append(line[0])
    pic_hv[i-1].append(line[1])
    j=1
    
    while j<int(line[1])+1:
        key=line[(1+j)]
        spec.setdefault(key, [])
        spec[key].append(i-1)
        j+=1
    i+=1
#print (spec)
#print(pic_hv)

m=0
max_spec=0
for i in spec:
    if(m<len(spec[i])):
        m=len(spec[i])
        max_spec=i
#print(m,max_spec)

pick_pic(max_spec)
#add (max_spec)
out_file.write(str(slides))
out_file.write('\n')

#for i in slide_show:
    
print(slides)
for i in slide_show:
    out_file.write(str(i))
#print(slide_show)
out_file.close()
in_file.close()
