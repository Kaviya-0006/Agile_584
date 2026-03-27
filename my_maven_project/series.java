import java.util.*;
import java.io.*;

class series{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int tn=0;
        int k=1;
        for(i=0;i<n;i++){
            tn=a+(k*b)+tn;
            k=k+k;
            System.out.print(tn+" ");
        }
        
        }
        
        in.close();
    }
}
