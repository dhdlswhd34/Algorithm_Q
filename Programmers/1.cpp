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
        for(int j = 0 ; j < board.size() ; j++)
        {
            temp = board[j][moves[i]-1];
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
                board[j][moves[i]-1] = 0;
                break;
            }
        }    
    }
    return answer;
}