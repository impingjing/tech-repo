#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& arr,int left,int mid,int right){
	// Create a temporary array to store the merged result
	vector<int>temp(right-left+1);

	int i=left; // Left half start index
        int j=mid+1;// Right half start index
	int k=0;   // Temporary array index
	
	// Compare the two subarrays and copy the smaller value into temp
	while(i<=mid && j<=right){
		if(arr[i]<arr[j]){
			temp[k++]=arr[i++];
		}
		else{
			temp[k++]=arr[j++];
		}
	}
	// Copy the remaining elements into temp
	while(i<=mid){
		temp[k++]=arr[i++];
	}
	while(j<=right){
		temp[k++]=arr[j++];
	}

	// Copy the merged result back to the original array
	for(int i=0;i<temp.size();i++){
		arr[left+i]=temp[i];
	}
}
// Recursive merge sort function
void merge_sort(vector<int>& arr,int left,int right){
	// Handle empty arrays or arrays with one element
	if(left>=right) return;

	int mid=left+(right-left)/2;
	merge_sort(arr,left,mid); // Sort the left half
	merge_sort(arr,mid+1,right); // Sort the right half
	// Merge the two sorted halves
	merge(arr,left,mid,right);
}

int main(){
	vector<int>arr={24,13,56,23,58,13,29};
	cout << "Before sorting:" << endl;
	for(int num:arr) cout << num << " ";
        cout << endl;

	merge_sort(arr,0,arr.size()-1);
	cout << "After sorting:" << endl;
	for(int num:arr) cout << num << " ";
	cout << endl;

	return 0;
}
