public class CastingTest 
{
    public static void main(String[] args)
    {
        //Widening Casting. Convert int to double data type, this convert is automatic
        int a = 9;
        double b = a;

        //Narrowing Casting. Convert double to int data type, we need to manual casting. 
        double c=9.81;
        int d = (int) c;
        
        System.out.println("Integer:" +a);
        System.out.println("After convert to double:" +b);
        System.out.println("Double:" +c);
        System.out.println("After converting to int:" +d);
    }
}
