#include<bits/stdc++.h>

using namespace std;

// Given an array 'A' of sorted integers and another non-negative integer B, find if there exist 2 indices i and j such that A[i] - A[j] = k, i != j.
// Return 0 / 1 ( 0 for false, 1 for true ) for this problem
// Try doing this in less than linear space complexity.


// Problem Constraints
// 1 <= |A| <= 106
// 0 <= B <= 109


// Input Format
// The first argument is an integer array A.
// The second argument is an integer B.


// Output Format
// Return an integer, 0 / 1 ( 0 for false, 1 for true ) for this problem

int diffpossibility(vector<int> &A, int B){
    int low = 0;
    int high = 1;

    while(low < A.size() && high < A.size()){
        if(low != high && A[high] - A[low] == B){
            return 1;
        }
        else if(A[high] - A[low] < B){
            high++;
        }
        else{
            low++;
        }
    }
}