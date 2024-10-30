import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        String[] nk = br.readLine().split(" ");
        int N = Integer.parseInt(nk[0]);
        int K = Integer.parseInt(nk[1]);
        int count = 0;
        int[] coin = new int[N];
        
        for (int i=0; i<N; i++) {
            coin[i] = Integer.parseInt(br.readLine());
        }
        br.close();

        for (int i=N-1; i>=0; i--) {
            if (coin[i] <= K) {
                int temp = K / coin[i];
                count += temp;
                K -= temp * coin[i];
            }
            if (K == 0) break;
        }

        System.out.println(count);
        br.close();
        isr.close();
    }
}