#include <stdio.h>
#include <stdlib.h>  
#include <time.h>
int a[12][6],b[12][6][6];
int Nfaculty=12,Ncourses=12,Nstudents=120,NclassRoom=6;

void getStudentEnrollment(int n){
    printf("Number of studetns in UG1 : %d\n",n/3);
    printf("Number of studetns in UG2 : %d\n",n/3);
    printf("Number of studetns in UG3 : %d\n",n/3);
}

void getCourseOffered(int n){
    printf("Number of courses in UG1 : %d\n",n/3);
    printf("Number of courses in UG2 : %d\n",n/3);
    printf("Number of courses in UG3 : %d\n",n/3);
}
void generateGraph(){
    printf("Faculty         Course\n");
    for(int i=0;i<12;++i){
        printf("faculty %d\t",i+1);
        for(int j=0;j<12;j++){
            if(i==j){
                printf("1\t");
            }else{
                printf("0\t");
            }
        }
        printf("\n");
    }
    printf("Faculty         Course Mapping\n");
    for(int i=0;i<3;++i){
        for(int j=0;j<12;j++){
            if(j<4 && i==0){
                printf("1 ");
            }
            else if(j<8 && i==1 && j>3){
                printf("1 ");
            }
            else if( i==2 && j>8){
                printf("1 ");
            }else{
                printf("0 ");
            }
        }
        printf("\n");
    }
}
void ColorEdges(){
    printf("Faculty         Course\n");
    int p=1;
    for(int i=0;i<12;++i){
        printf("faculty %d\t",i+1);
        for(int j=0;j<12;j++){
            if(i==j){
                printf("%d\t",p);
                p++;
            }
            else{
                printf("0\t");
            }
        }
        printf("\n");
        if(p>4){
            p=1;
        }
    }
    printf("Faculty         Course Mapping\n");
    for(int i=0;i<3;++i){
        int p=1;
        for(int j=0;j<12;j++){
            if(j<4 && i==0){
                printf("%d\t",p);
                p++;
            }
            else if(j<8 && i==1 && j>3){
                printf("%d\t",p);
                p++;
            }
            else if(i==2 && j>7){
                printf("%d\t",p);
                p++;
            }else{
                printf("0\t");
            }
        }
        printf("\n");
    }
}
void getInitialTimeSlot(){
    for(int i=0;i<12;++i){
        printf("Enter Timeslots for faculty : %d\n",i+1);
        for(int j=0;j<6;j++){
            a[i][j]=0 + (rand () % 6);
            printf("%d\t",a[i][j]);
        }
        printf("\n\n");
        
    }
}
void getAvailableTimeSlot(){
    for(int i=0;i<12;++i){
        printf("Enter Freeslots for faculty : %d\n",i+1);
        for(int j=0;j<6;j++){
            int surya = a[i][j];
            for(int k=0;k<6;++k){
                if(surya >0){
                    scanf("%d",&b[i][k][j]);
                    surya--;
                }else{
                    b[i][k][j]=0;
                }
            }
        }
    }
}
int main()
{
    srand (time(0));
    getStudentEnrollment(Nstudents);
    getCourseOffered(Ncourses);
    getInitialTimeSlot();
    getAvailableTimeSlot();
    generateGraph();
    ColorEdges();
    return 0;
}