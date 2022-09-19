import random

letters_string= 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,!,@,#,$,%,^,&,*,(,)'
letters_nostring=letters_string.split(',')

pr=int(input('How many charecters would you like in your password ?: '))

password= ''.join(random.sample(letters_nostring, pr))
print(password)