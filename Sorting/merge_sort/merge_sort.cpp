#include <iostream>
#include <vector>
#include <utility>
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))



using namespace std;


typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> pii;


void mergesort(int *a, int low, int high)
{
    int mid;
    if (low < high)
    {
        mid=(low+high)/2;
        mergesort(a,low,mid);
        mergesort(a,mid+1,high);
        merge(a,low,high,mid);
    }
    return;
}
void merge(int *a, int low, int high, int mid)
{
    int i, j, k, c[50];
    i = low;
    k = low;
    j = mid + 1;
    while (i <= mid && j <= high)
    {
        if (a[i] < a[j])
        {
            c[k] = a[i];
            k++;
            i++;
        }
        else
        {
            c[k] = a[j];
            k++;
            j++;
        }
    }
    while (i <= mid)
    {
        c[k] = a[i];
        k++;
        i++;
    }
    while (j <= high)
    {
        c[k] = a[j];
        k++;
        j++;
    }
    for (i = low; i < k; i++)
    {
        a[i] = c[i];
    }
}

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
