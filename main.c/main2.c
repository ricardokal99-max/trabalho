#include <stdio.h>

int main() {
    int vetor[5];        // Declara um vetor com 5 elementos inteiros
    int soma = 0;        // Variável para armazenar a soma
    int i;               // Variável de controle do loop

    // Entrada de dados
    printf("Digite 5 numeros inteiros:\n");
    for(i = 0; i < 5; i++) {
        printf("Numero %d: ", i + 1);
        scanf("%d", &vetor[i]);
        soma += vetor[i]; // Soma acumulada
    }

    // Exibição dos elementos do vetor
    printf("\n--- Valores Inseridos ---\n");
    for(i = 0; i < 5; i++) {
        printf("Elemento [%d] = %d\n", i, vetor[i]);
    }

    // Exibição da soma total
    printf("\nSoma total dos elementos = %d\n", soma);

    return 0;
}
