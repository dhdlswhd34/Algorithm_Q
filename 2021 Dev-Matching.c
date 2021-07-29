#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// enroll_len은 배열 enroll의 길이입니다.
// referral_len은 배열 referral의 길이입니다.
// seller_len은 배열 seller의 길이입니다.
// amount_len은 배열 amount의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.

int Amount_10per(float money)
{  
    int temp=0;
    temp = (money*0.1);
    if( (money - temp) >= 0.5)
    {
        temp = money + 0.5;
    }
    return temp;
}




int* solution(const char* enroll[], size_t enroll_len, const char* referral[], size_t referral_len, const char* seller[], size_t seller_len, int amount[], size_t amount_len) {
    
    int temp = 0;
    int money= 0;
    int data[10000]= {0,};
    int sell[100000] = {0,};

    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*enroll_len);
    
    
    for(int i = 0; i <  enroll_len ; i ++)
    {
        //데이터 확인
        for(int j =0 ; j < referral_len; j++ )
        {
            if(!strcmp(enroll[i],referral[j]))
            {
                data[j]=i;
            }
           
        }
        //seller 비교
        for(int j = 0 ; j< seller_len ; j++)
        {
            if(!strcmp(enroll[i],seller[j]))
            {
                sell[j]=i;
            }
        }
    }
    

    for(int i = 0;  i < seller_len ; i++)
    {
          money =  amount[i] * 100;
          temp  =  Amount_10per(money);
      for(;;)
      {  
         answer[sell[i]] += (money-temp);
         referral(sell[i]);
      }     
        
    }
      
    
    
    
    
    
    return answer;
}
