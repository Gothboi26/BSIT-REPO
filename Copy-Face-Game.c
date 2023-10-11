#include <stdio.h>
#include <stdlib.h>
#include <time.h>


#define HAPPY 1
#define SAD 2
#define ANGRY 3
#define PLAYER1_WIN 1
#define PLAYER2_WIN 2

void menu(){
    int sel;
    printf("**********************************************\n");
    printf("\t\tC O P Y F A C E\n");
    printf("**********************************************\n\n");
    printf("\t\tSTART (x)\n");
    printf("\t\tINSTRUCTION (i)\n");
    printf("\t\tPRESS ANY KEY TO QUIT \n");
    printf("\t\t-----> ");
    scanf("%c",&sel);
    printf("\n**********************************************\n");
    switch (sel){
    case'x' :
    case 'X':
        printf("\n\t\t   GAME START\n");
        break;
    case 'i' :
    case 'I':
        printf("\n\t\t   INSTRUCTION\n");
        printf("\nThere will be three choices to win this game.");
        printf("\nPress 1 For Happy, Press 2 For Sad, and 3 For Angry.");
        printf("\nYou must guess what the AI choose among the three.\n");
        printf("\n**********************************************\n");
        return;



    default :
        printf("\n\t    THANK YOU FOR PLAYING!\n");
        printf("\n**********************************************\n");
        exit(0);


    }
}
int winCondition(int player1, int player2){
    int result;

    if(player1 == HAPPY && player2 == HAPPY) {
        result = PLAYER1_WIN;
    }
    else if (player1 == SAD && player2 == SAD){
        result = PLAYER1_WIN;
    }
    else if(player1 == ANGRY && player2 == ANGRY) {
        result = PLAYER1_WIN;
    }
    else{
            result = PLAYER2_WIN;
    }
    return result;

}

int get_user_input(){
    int choice;

    do{
        printf("\n");
        printf("\t\t**************** \n");
        printf("\t\t|1.   HAPPY    |\n");
        printf("\t\t|2.    SAD     |\n");
        printf("\t\t|3.   ANGRY    |\n");
        printf("\t\t****************\n");
        printf("\t\tYour Choice: ");
        scanf("%d", &choice);
        if (! (choice >=1 && choice <=3 )){
            printf("\nERROR -- Invalid input, should be 1 or 2 or 3\n\n");
        }
    }while( !(choice >=1 && choice <=3));

    return choice;
}

void printWord(int displayChoice){
    if(displayChoice == HAPPY){
        printf("HAPPY!\n\n");
    }
    else if (displayChoice == SAD) {
        printf("SAD!\n\n");
    }
    else if (displayChoice == ANGRY){
        printf("ANGRY!\n\n");
    }

}

int main()
{
    menu();
    int userScore = 0;
    int computerScore = 0;
    srand(time(NULL));

    int quit = 0;
    while(!quit){

        int user_input = get_user_input();
        int computer_choice = (rand() % 3) + 1;
        printf("\nComputer chose: ");
        printWord(computer_choice);
        printf("User chose: ");
        printWord(user_input);

        int result = winCondition(user_input, computer_choice);
        if (result == PLAYER1_WIN){
            printf("User wins and Computer lost the round\n");
            userScore++;
        }
        else if (result == PLAYER2_WIN){
            printf("Computer wins and User lost the round\n");
            computerScore++;
        }
        printf("\n");
        printf("-----------------------------------\n");
        printf("User score: %d\n", userScore);
        printf("Computer score: %d\n", computerScore);
        printf("-----------------------------------\n");
        printf("\n\n");
        printf("If you want to continue input any integer, 0 to terminate. ");
        int response;
        scanf("%d", &response);
        if(response == 0){
            quit = 1;
        }
    }

    printf("\nFINAL SCORE...\n");
    printf("\n");
    printf("-----------------------------------\n");
    printf("User score: %d\n", userScore);
    printf("Computer score: %d\n", computerScore);
    printf("-----------------------------------\n");
    printf("\n\n");
    if (userScore == computerScore){
        printf("-----------------------------------\n");
        printf("GAME WAS DRAW\n");
        printf("-----------------------------------\n");
    }
    else if (userScore > computerScore){
        printf("-----------------------------------\n");
        printf("USER WINS THE GAME\n");
        printf("-----------------------------------\n");
    }
    else{
        printf("-----------------------------------\n");
        printf("COMPUTER WINS THE GAME\n");
        printf("-----------------------------------\n");
    }
     printf("\nThis game was made by:\n\n");
        printf("\t Jan Ashley Tinao\n");
        printf("\t Edan Raymundo\n");
        printf("\t Maricel Bautista\n");
        printf("\t Abe Mae Saavedra\n");
        printf("\t Alliah Mae Yaba\n");
        printf("-----------------------------------\n");
        printf("\t December 5, 2021\n");
        printf("-----------------------------------\n");
        printf("\tTHANK YOU FOR PLAYING!\n");
        printf("-----------------------------------\n");
}
