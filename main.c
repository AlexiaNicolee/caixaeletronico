#include <stdio.h>
#include <stdlib.h>
int qtdnotas(int valor){
    int nota50,nota100,nota5,nota1,nota10;
    if(valor < 10  || valor > 600){
        printf("Valor invalido");
        return 0;
    }

    nota100 = valor/ 100;
    valor -= nota100*100;
    nota50 = valor/ 50;
    valor -= nota50*50;
    nota10 = valor/ 10;
    valor -= nota10*10;
    nota5 = valor/ 5;
    valor -= nota5*5;
    nota1 = valor/ 1;
    valor -= nota1*1;

    printf("Notas de 100: %d\n", nota100);
    printf("Notas de 50: %d\n", nota50);
    printf("Notas de 10: %d\n", nota10);
    printf("Notas de 5: %d\n", nota5);
    printf("Notas de 1:  %d\n", nota1);
    return 1;

}


int main()
{
    int valor,nota50,nota100,nota5,nota1,nota10;
    printf("Qual valor voce quer sacar?");
    scanf("%d",&valor);
    qtdnotas(valor);

return 1;



}
