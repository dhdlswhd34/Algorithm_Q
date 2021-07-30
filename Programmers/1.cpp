#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> board,vector <int> moves) {
    
    int answer = 0;
    int temp;
    vector<int> bk;
    
    bk.push_back(0);
    
    for(int i = 0; i < moves.size(); i++)
    {           
        for( ;  0 == (board[moves[i]-1].empty()) ;)
        {
            temp = board[moves[i]-1].back();
            board[moves[i]-1].pop_back();
            if(temp)
            {
                if(temp == bk.back())
                {
                    bk.pop_back();
                    answer +=2;
                }    
                else
                {
                    bk.push_back(temp);
                }
                
                cout << bk;
                break;
            }
        }    
    }
    return answer;
}