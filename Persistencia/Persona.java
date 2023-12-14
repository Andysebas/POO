public class Persona {
    String nombre;
    int edad;
    float estatura;
    String nacionalidad;

    public Persona(String nombre, int edad, float estatura, String nacionalidad) {
        this.nombre = nombre;
        this.edad = edad;
        this.estatura = estatura;
        this.nacionalidad = nacionalidad;

    }
 public String mostrarDatos(){
     return "Nombre: "+nombre+"\nEdad: "+edad+"\nEstatura: "+estatura+"\nNacionalidad: "+nacionalidad+"\n";
 }
  
}
