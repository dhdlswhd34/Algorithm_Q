#include <stdio.h>
int main(void)
{
	int test_case;
	int T =  0;

	 int f = 0;
     int s = 0;

	setbuf(stdout, NULL);
	scanf("%d", &T);
    
	for (test_case = 0; test_case < T; ++test_case)
	{
		/////////////////////////////////////////////////////////////////////////////////////////////
		scanf("%d %d", &f, &s);  
        if(  f > 9   ||  s  > 9)
        {
        	printf("#%d -1\n",test_case+1);
        }
        else
        {
        	printf("#%d %d\n",test_case+1,s*f);
        }
 
		/////////////////////////////////////////////////////////////////////////////////////////////

	}

	return 0; //정상종료시 반드시 0을 리턴해야 합니다.
}