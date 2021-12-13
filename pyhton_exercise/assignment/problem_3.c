#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int main(void)
{
    int sum = 0, i,len1,len2,len3;
    char string_a[100];
    char string_b[100];
    char result_a[]={};
    int var1;
    int a_as_int,b_as_int,adding,temp=0;
    
    printf("Enter the string1 : ");
    scanf("%s", string_a);
    printf("Enter the string2 : ");
    scanf("%s", string_b); //An array to store data

    len1=strlen(string_a);
    len2=strlen(string_b);
    
    // printf("%d\n",len1);
    // printf("%d\n",len2);
    if(strlen(string_a)>=strlen(string_b)){
        for(int i=(strlen(string_a)-1);i>=0;i--)
            {   
                len2--;
                a_as_int = (int) string_a[i] -48;
                b_as_int = (int) string_b[len2] -48;
                if(b_as_int<0){
                    b_as_int=0;
                }
                adding=a_as_int+b_as_int+temp;
                // printf("%dtemp\n",temp);
                // printf("%d add\n",adding);
                if(adding>=10){
                    // printf("afad\n");
                    temp=adding/10;
                    // if(b_as_int>0){
                        // add_temp=adding%10;
                    printf("%d",adding%10);
                    result_a[i]=adding%10;
                    // printf("adf");
                    // }
                    /*
                    else{
                        temp=0;
                    }
                    */
                }
                else{
                    // printf("%d\n",temp);
                    if(b_as_int>0){
                        printf("%d",adding+temp);
                        result_a[i]=adding+temp;
                    // printf("fdsfs");
                        }
                    else{
                        printf("%d",a_as_int+temp);
                        result_a[i]=a_as_int;
                    // printf("afdaf");
                    }
                if(adding>10){
                    temp=temp;
                }
                else{
                    temp=0;
                }
                }
                
            }
        /*    
        len3=strlen(result_a);
        for (int i = len3-1; i >= 0; i--) {     
        printf("%d ", result_a[i]);     
    } */   
    }
    else{
        printf("%c",'a');
    }
    
}
