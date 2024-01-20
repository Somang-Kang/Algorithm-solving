#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string s) {
    string answer = "";
    for(int i =0;i<s.length();i++){
        if(i==0){
            if(s[i]>='a' and s[i]<='z') answer+=s[i]-32;
            else answer+=s[i];
        }
        else{
            if(s[i]==' ') answer+=s[i];
            else if(s[i-1]==' '){
                if(s[i]>='a' and s[i]<='z') answer+=s[i]-32;
                else answer+=s[i];
            }
            else{
                if(s[i]>='a' and s[i]<='z') answer+=s[i];
                else answer+=s[i]+32;
            }
        }
    }
    //첫글자 -> 숫자면 출력, 소문자면 대문자화, 대문자면 출력
    //공백일때 -> 출력
    //이전글자가 공백일때 -> 소문자면 대문자화, 대문자면 출력
    //else -> 소문자면 출력, 대문자면 소문자화
    
    return answer;
}