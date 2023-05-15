#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int solve(vector<int>& nums) {
    int count = 0;

    for(int j = nums.size()-1; j >= 0; j--){

        for(int i = 0; i < j; i++){
            if(nums[i] > nums[i+1]){
                swap(nums[i], nums[i+1]);
                count++;
            }
        }
    }
    return count;
   
}

int main()
{

    return 0;
}