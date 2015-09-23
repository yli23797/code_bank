#include <iostream>
#include <vector>
#include <utility>
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))



using namespace std;


typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> pii;



int main()
{
	int i = 0;
	int j = 0;

	j = i++;
	cout << i <<" " << j << endl;

	i = 0;
	j = 0;
	j = ++i;
	cout << i << " "  << j << endl;
	
	return 0;
}
