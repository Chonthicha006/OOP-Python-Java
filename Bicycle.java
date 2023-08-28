/**
* Represents a bicycle
* @author https://docs.oracle.com/javase/tutorial/java/concepts/class.html
*/

public class Bicycle {
//instance variables
private int cadence = 0;
private int speed = 0;
private int gear = 1;
public void changeCadence(int newValue) {
cadence = newValue;
}
public void changeGear(int newValue) {
gear = newValue;
}
public void changeSpeed(int change) {
speed = speed + change;
}
public int getCadence() {
return cadence;
}
public void printGear() {
System.out.println("Gear:" + gear);
}
public String toString() {
return "cadence:" + cadence + " speed:" + speed + " gear:" + gear;
}
}