#include<iostream>

using namespace std;

int findMax(int *arr, int size) {
  //int len = *(&arr + 1) - arr;

  int start = 0, end = size - 1;
  
  while (start < end) {
    int mid = start + (end - start) / 2;
    if (arr[mid] > arr[mid + 1]) 
      end = mid;
    else 
      start = mid + 1;
  }
  return arr[start];
}

int main() {
  int arr[] = {1, 3, 8, 12, 4, 2};
  //int size = sizeof(arr)/sizeof(arr[0]);
  int size = *(&arr + 1) - arr;
  cout << findMax(arr, size) << endl;

}

