import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Single-threaded server socket.
 * Echoes the message from the client and exits.
 * @author pbose
 *
 */
public final class SocketServer
{
	public static final int PORT = 2016;
	public static void main(String[] args)
	{
		// create a server socket
		try(ServerSocket server = new ServerSocket(PORT))
		{
			System.out.println("> Waiting for connection...");
			// wait for connection, this is a blocking call, i.e. waits for new connections
			Socket client = server.accept();
			System.out.println("> Connected to host:" + client.getLocalAddress().getHostName() +
						", port:" + client.getLocalPort());

			// get the client socket I/O streams
			try(BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream())))
			{
				// print the message from the client
				System.out.println("> Client data -> " + in.readLine());
			}

			System.out.println("> Exiting server...");
		}
		catch (IOException e)
		{
			System.out.println("> Lost connection to host due to I/O error.");
			e.printStackTrace();
		}
	}
}
