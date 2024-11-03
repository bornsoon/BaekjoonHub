import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        OutputStreamWriter osw = new OutputStreamWriter(System.out);
        BufferedWriter bw = new BufferedWriter(osw);
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Map<String, String> hashMap = new HashMap<>();
        
        for (int i=0; i<N; i++) {
            String temp = br.readLine();
            StringTokenizer t = new StringTokenizer(temp);
            String id = t.nextToken();
            String pw = t.nextToken();
            hashMap.put(id, pw);
        }

        for (int i=0; i<M; i++) {
            String id = br.readLine();
            String pw = hashMap.get(id);
            bw.write(pw + "\n");
        }
        br.close();
        isr.close();
        bw.flush();
        bw.close();
        osw.close();
    }
}