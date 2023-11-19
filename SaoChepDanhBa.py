# Đọc dữ liệu từ tệp SOTAY.txt
with open('SOTAY.txt', 'r') as sotay_file:
    sotay_data = sotay_file.readlines()
sotay_file.close()

contacts = []
res=""
for line in sotay_data:
    arr=line.split()
    if arr[0]=="Ngay":
        s=""
        res=arr[1]
    else:
        if len(arr)==1:
            s=s+arr[0]+" "+res          
            contacts.append(s)
            s=""
        else:
            t=""
            for i in range(len(arr)):
                t+=arr[i]
                if i!=len(arr)-1:
                    t+=" "
            s=t+": "


sorted_contacts = sorted(contacts)

for x in contacts:
    print(x[0])

# Ghi dữ liệu đã sắp xếp vào tệp DIENTHOAI.txt
with open('DIENTHOAI.txt', 'w') as dienthoai_file:
    for contact in sorted_contacts:
        dienthoai_file.write(contact+"\n")
dienthoai_file.close()
   
