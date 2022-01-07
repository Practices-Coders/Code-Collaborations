import java.util.Scanner;

class Ejercicio16 {
	public static void main (String... args){
		
		System.out.println("Ingrese los productos delimitados por una coma");
		//Pedimos los productos y lo almacenamos en la variable 'productos'
		String productos = new Scanner(System.in).nextLine();
		//Ahora remplazamos todas las comas (que estén antecedidas y seguidas por 0 o más espacios en blanco) por saltos de linea.
		System.out.println(productos.replaceAll( "\\s*,\\s*", "\n" ));

	
	}

}
