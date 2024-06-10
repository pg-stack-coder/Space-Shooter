#include <iostream>
#include <math.h>
using namespace std;

// // binary/octal to decimal
// int bo_d(int x,int y)
// {int n,sum=0,c=0;
// while (x!=0)
// {n=x%10;
// x=int(x/10);
// sum+=(pow(y,c))*(n);
// c=c+1;}
// return sum;}

// // decimal to binary / octal
// void d_bo(int x,int y)
// {int a[20],c=0,n;
// while (x!=0)
// {n=x%y;
// x=int(x/y);
// a[c]=n;
// c+=1;}
// for (int i=c-1;i>=0;i--)
// cout<<a[i];}

// // octal to binary
// void o_b(int x)
// {int c=0;
// string a[8]={"000","001","010","011","100","101","110","111"},b[20];
// while(x!=0)
// {b[c]=a[x%10];
// x=int(x/10);
// c+=1;}
// for (int j=c;j>=0;j--)
// cout<<b[j];}

// //binary  to octal
// void b_o(int w)
// {int c,a[2],c2=0,sum=0,b[20];
// while (w!=0)
// {c=0;sum=0;
// while (c!=3)
// {a[c]=w%10;
// w=int(w/10);
// c+=1;}
// for (int j=0;j<3;j++)
// {sum+=(pow(2,j))*a[j];}
// b[c2]=sum;
// c2+=1;}
// for (int k=c2-1;k>=0;k--)
// {cout<<b[k];}}

// //decimal to hexadecimal
// void d_h(int x)
// {int c=0;
// string a[16]={"0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","A","B","C","D","E","F"},b[20];
// while(x!=0)
// {b[c]=a[x%16];
// x=int(x/16);
// c+=1;}
// for (int j=c;j>=0;j--)
// cout<<b[j];}

// //hexadecimal to binary
// void h_b(int x)
// {int c=0;string m[6]={"A","B","C","D","E","F"};
// string a[16]={"0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"},b[20];
// while(x!=0)
// {b[c]=a[x%16];
// x=int(x/16);
// c+=1;}
// for (int j=c;j>=0;j--)
// cout<<b[j];}

// //

// main()
// {int x,b,y,d;
// cout<<"Enter a number:";
// cin>>x;
// // cout<<"Enter the base:";
// // cin>>y;
// // b=bo_d(x,y);
// // cout<<b;
// // d_bo(x,y);
// // b_o(x);
// // o_b(x);
// // d_h(x);
// h_b(x);// }

//---------------------------------------------|RECURSION|-------------------------------------------
//---------------------------------------------|ABCDE|-----------------------------------------------
// void display(int c=65)
// {if(c==90)
// cout<<char(c);
// else{cout<<char(c);
// display(c+1);}}
// main()
// {display();}
//---------------------------------------------|FACTORS|----------------------------------------------
// void factors(int p,int x=1)
// {if (p>=x)
// {if (p%x==0)
// cout<<x<<"\n";
// factors(p,x+1);}}
// main()
// {int n=10;
// factors(10);}
//----------------------------------------------|MULTIPLES|--------------------------------------------
// void multiples(int p,int x=1)
// {if ((p*x)<=100)
// {cout<<(p*x)<<"\n";}
// multiples(p,x+1);}
// main()
// {int n;
// cout<<"Enter a number:";
// cin>>n;
// multiples(n);}
//---------------------------------------------|PRIME NUMBERS|---------------------------------------------
// void prime(int p,int x=2)
// {bool check=true;
// if (p!=1) 
// {if (x>int(p/2))
// {if (check)
// {cout<<"Number is prime";
// }}
// else if (p%x!=0)
// {prime(p,x+1);} 
// else if (p%x==0)
// {check=false;
// cout<<"Number is not prime";}}
// else
// {cout<<"Number is not prime";}
// }
void prime(int p,int x=2)
{bool check=true;
if (p!=1) 
{if (x>int(p/2))
{if (check)
{cout<<p<<"\n";
}}
else if (p%x!=0)
{prime(p,x+1);} 
else if (p%x==0)
{check=false;}}
// cout<<"Number is not prime";}}
// else
// {cout<<"Number is not prime";}
}
void range(int p=100)
{if (p!=2)
{prime(p-1);
range(p-1);
}}


main()
{int a=5;
// for(int i=2;i<5;i++)
// {prime(i);}}
range();}















