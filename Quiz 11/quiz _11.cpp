#include <bits/stdc++.h>
using namespace std;

struct Item
{
	float wgt;
	int value;
};

struct Node
{
	int level, prof, bnd;
	float wgt;
};

bool cmp(Item a, Item b)
{
	double r1 = (double)a.value / a.wgt;
	double r2 = (double)b.value / b.wgt;
	return r1 > r2;
}

int bnd(Node u, int n, int W, Item arr[])
{
	if (u.wgt >= W)
		return 0;

	int prof_bnd = u.prof;

	int j = u.level + 1;
	int totwgt = u.wgt;

	while ((j < n) && (totwgt + arr[j].wgt <= W))
	{
		totwgt += arr[j].wgt;
		prof_bnd += arr[j].value;
		j++;
	}

	if (j < n)
		prof_bnd += (W - totwgt) * arr[j].value /
										arr[j].wgt;

	return prof_bnd;
}

void knapsack(int W, Item arr[], int n)
{

	sort(arr, arr + n, cmp);

	queue<Node> Q;
	Node u, v;

	u.level = -1;
	u.prof = u.wgt = 0;
	Q.push(u);

	int maxprof = 0;
	int count = 0;
	while (!Q.empty())
	{
		u = Q.front();
		Q.pop();

		if (u.level == -1)
			v.level = 0;

		if (u.level == n-1)
			continue;

		v.level = u.level + 1;

		v.wgt = u.wgt + arr[v.level].wgt;
		v.prof = u.prof + arr[v.level].value;

		if (v.wgt <= W && v.prof > maxprof)
			maxprof = v.prof;

		v.bnd = bnd(v, n, W, arr);

		if (v.bnd > maxprof){
			Q.push(v);
			count += 1;
		}
			

		v.wgt = u.wgt;
		v.prof = u.prof;
		v.bnd = bnd(v, n, W, arr);
		if (v.bnd > maxprof){
			Q.push(v);
			count += 1;
		}
		
	}
	cout<<"Count of nodes = " << count<< endl;
	cout<<"Maximum prof = " << maxprof;
}

int main()
{
	int W = 13; 
	Item arr[] = {{2, 20}, {5, 30}, {7, 35}, {3, 12}, {1, 3}};
	int n = sizeof(arr) / sizeof(arr[0]);

	knapsack(W, arr, n);

	return 0;
}
