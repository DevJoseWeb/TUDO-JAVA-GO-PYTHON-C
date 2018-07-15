// Programar em Go #06 - Mais sobre as Strings

package main;

import (
	"fmt"
	"strings"
);

func main() {
	primeiroNome, ultimoNome := "Nelson", "Silva";
	idade := 21;

	fmt.Println("Nome:", len(primeiroNome), len(ultimoNome), "\nIdade:", idade);
	fmt.Printf("Nome: %s %s\nIdade: %d", strings.ToUpper(primeiroNome), strings.ToLower(ultimoNome), idade);
}