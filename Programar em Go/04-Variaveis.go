// Programar em Go #04 - Variáveis

package main;

import "fmt";

func main() {
	var inteiro int = 10;
	var _string string = "Eu sou uma string!";
	var semTipo = "Eu continuo a ser uma string!";

	decimal := 10.5;
	booleano := true;

	fmt.Println(inteiro);
	fmt.Println(_string);
	fmt.Println(semTipo);
	fmt.Println(decimal);
	fmt.Println(booleano);
}