
#include<iostream>

using namespace std;

int maxNum(int s, int m , int e, int * arr)
{
    int result = arr[s];
    int temp;
	for(int i = s+1 ; i <= e ; i++ )
    {
    	if(  result < arr[i]  && i != m )
        {
            result = arr[i];
        }
    }
	return result;
}


int main(int argc, char** argv)
{
	int i;
	int T;
	int B[1000] = {0,};
    int Tcase[10] = {0,};
    int temp[2] = {0,};
    int result=0;

    for(int tc = 1 ; tc <= 10 ; tc++ )
    {
       	cin>>T;
 		result=0;

        for(i = 0 ; i < T; i++)
        {		
           cin >> B[i];               
        }

        temp[0] = 2;
        temp[1] = B[2];
        //cout << temp[0] << " "<< temp[1] << " "<< B[98];


        for(i = 2 ;  ; )
        {	
            if( i > T )
                break;

            if( temp[1] <= B[i]  )
            {
                temp[0] = i;
                temp[1] = B[i];
            }

            if( temp[0]+2 == i )
            {
                 //printf("%d %d %d %d\n",i, temp[0], temp[1], maxNum(temp[0]-2 , temp[0] , temp[0]+2 , B) );
                if( (temp[1] - maxNum(temp[0]-2 , temp[0] , temp[0]+2 , B)) > 0 )
                {
                    result = result + ( temp[1] - maxNum(temp[0]-2 , temp[0] , temp[0]+2 , B) );
                   //printf("%d %d \n", temp[0], temp[1]);
                }
             //  printf("%d \n", i);
                //i += ;
                temp[0]  = i;
                temp[1]  = B[i];
                //printf("%d %d %d \n",i, temp[0], temp[1]);
            }
            else
            {
                i++;
            }        
         }

        printf("#%d %d\n",tc,result);
    }
	return 0;
}
