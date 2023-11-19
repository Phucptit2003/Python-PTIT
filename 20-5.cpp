#include<bits/stdc++.h>
using namespace std;

int main(){
    int test;
    cin>>test;
    while(test--){
        string s;
        cin>>s;
        stack<int>st,st1;
        st.push(1);
        int dem=2;
        vector<int>v;
        for(char i:s){
            if(i=='D'){
                while(!st1.empty()){
          //          v.push_back(st1.top());
                    st.push(st1.top());
                    st1.pop();
                }
                st.push(dem);
                dem++;
            }
            else if(i=='I'){
                while(!st.empty()){
                    v.push_back(st.top());
                    st.pop();
                }
                st1.push(dem++);
            }
        }
        while(!st1.empty()){
            v.push_back(st1.top());
            st1.pop();
        }
        while(!st.empty()){
            v.push_back(st.top());
            st.pop();
        }
        // while(!st.empty()){
        //     cout<<st.top();
        //     st.pop();
        // }

        for(auto x:v){
            cout<<x;
        }

        cout<<endl;
    }
}