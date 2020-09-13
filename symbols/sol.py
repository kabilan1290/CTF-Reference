s="@#@@s+#+u(#(#(@n+#(@(@i+#+@k@+@@+a(@@(b@((@i!@!@@l@@(@(l@(@(a#((#n"
l=len(s)
i=0
while(i<l):
    if(s[i]=='!'):
     print('1', end="")
    elif(s[i]=='@'):
     print('2', end="")
    elif(s[i]=='#'):
     print('3', end="")
    elif(s[i]=='$'):
     print('4', end="")
    elif(s[i]=='%'):
     print('5', end="")
    elif(s[i]=='^'):
     print('6', end="")
    elif(s[i]=='&'):
     print('7', end="")
    elif(s[i]=='*'):
     print('8', end="")
    elif(s[i]=='('):
     print('9', end="")
    elif(s[i]==')'):
     print('0', end="")
    else:
     print(s[i], end="")
    i=i+1