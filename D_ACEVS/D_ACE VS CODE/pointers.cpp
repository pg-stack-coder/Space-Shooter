#include <iostream>
using namespace std;
// // int main()
// // {int x=20,y=10;
// // int *p,*q;int **a;const char c=2;
// // p=&x;q=&y;
// // cout<<&y<<"\n"<<q<<"\n";
// // cout<<&x<<"\n"<<p;
// // cout<<sizeof(x);
// // a=&p;
// // cout<<p<<"\n"<<**a;
// // cout<<(&x);
// // return c;}


// {int x[5]={3,2,5,4,7},*y;
// y=x;
// for(int i=0;i<6;i++)
// {cout<<*y;y++;}}
void d(int p)
{if (p==10)
cout<<10;
else
{cout<<p;d(--p);}}
main()
{d(1);}