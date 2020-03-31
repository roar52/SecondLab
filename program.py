file=open('conf.txt','r')
dic={}
for line in file:
    if line[0]!='#' and line[0]!=';' and line[0]!='\n':
        string_line=line.split(maxsplit=1)
        if len(string_line)>1:
            key=string_line[0]
            dic[key]=string_line[1]
        else:
            dic[string_line[0]]='null'
file.close()
flag=True
while flag:
    inquiry=input('Введите запрос в формате(get param ...): ')
    s=inquiry.split()
    for key in dic:
        if s[2]==key:
            if dic[key]!='null':
                print(key,':',dic[key])
            else:
                print(key,':')
    while True:
        str_cont=input('Продолжить?(Да/Нет): ')
        if str_cont.lower()=='да':
            break;
        elif str_cont.lower()=='нет':
            flag=False
            break