import java.net.Socket;
import java.io.IOException;

public class MyClient { 

    public static void main(String[] args) {
        try {
            if(args.length < 2)  {
                System.err.println("modo de usar: java MyClient <nome-do-host> <porta>");
                System.exit(-100);
            }
            String hostname = args[0];
            Integer port = Integer.parseInt(args[1]);
            Socket myClient = new Socket( hostname, port);
            myClient.close();
        }
        catch (Exception e) {
            System.out.println(e);
            e.printStackTrace();
        }
    }
}