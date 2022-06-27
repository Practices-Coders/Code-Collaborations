package enjava.ejercicio3;

import java.util.Scanner;

/*
    Escribir un programa que pregunte el nombre del usuario en la consola y después de que 
    el usuario lo introduzca muestre por pantalla la cadena ¡Hola < nombre>!, donde < nombre> 
    es el nombre que el usuario haya introducido
 */

public class Saludo {

    public static void main(String[] args) {

        // Forma de definir una constante en JAVA 
        final String HOLA = "!Hola ";
       
        // Declaracion de una variable
        String nombreUsuario;

        // Declarando un objeto de tipo Scanner para capturar la informacion del usuario 
        Scanner capturador = new Scanner(System.in);

        // Imprimiendo mensaje desde la consola
        System.out.print("Por favor ingrese el su nombre: ");

        // Capturando la informacion del usuario y almacenandola en la variable
        nombreUsuario = capturador.nextLine();

        // Imprimiendo mensaje desde la consola concatenandolo 
        System.out.println(HOLA + nombreUsuario + "!");

        // Cerrando el obejeto scanner
        capturador.close();
        
    }
}