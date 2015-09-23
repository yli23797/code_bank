#include <iostream>
#include <vector>
#include <utility>
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))



using namespace std;


typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

void quick_sort(int *arr, int left, int right)
{
	int i = left; 
	int j = right;
	int temp = 0;
	int pivot = arr[(left+right)/2];

	while (i <= j)
	{
		while (arr[i] < pivot )
			i++;
		while (arr[j] > pivot )
			j--;
		if( i <= j)
		{
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			i++;
			j--;
		}
	}
	if(left < j)
		quick_sort(arr, left, j);
	if(i < right)
		quick_sort(arr, i, right);

}

int main()
{
	int arr[10] = {4, 5, 6, 7, 10, 1, 3, 9, 2, 8};
	quick_sort(arr, 0, 10);
	For(i, 0, 10)
	{
		cout << arr[i] << " " ;
	}
	cout << endl;
	/*int i = 0;
	int j = 0;
	j = i++;
	cout << i << " " << j << endl;


	i = 0;
	j = 0;
	j = ++i;
	cout <<i <<" " << j;
	cout << endl;*/
	return 0;
}
