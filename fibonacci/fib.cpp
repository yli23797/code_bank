#include <iostream>
#include <vector>
#include <utility>
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))



using namespace std;


typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

//calculate fibonacci number by recursion
ll fib_rec( int n)
{
	int fib = 1;
	return fib;
}

//calculate fibonacci number interatively
ll fib_itr( int n)
{
	//O(n) running time
	int temp = 0;
	int fib = 1;
	int cur_fib = 1;
	For(i, 0, n-1)
	{	
		temp = fib;
		fib = cur_fib;
		cur_fib = temp + cur_fib;
	}
	return fib;
}
//calculate fibonacci number using dynamic programming
ll fib_dym( int n)
{
	int fib = 1;
	return fib;
}
//calcuate fibonacci number by eqation
ll fib_eqa( int n)
{
	int fib = 1;
	return fib;
}

int main()
{
	cout << fib_itr(12) << endl;
	
	return 0;
}
