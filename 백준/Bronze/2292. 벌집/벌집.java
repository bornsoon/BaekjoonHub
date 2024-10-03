import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        int i = 1;
        int cnt = 1;
        int answer = 1;
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        
        while(cnt < num){
            cnt += 6 * i;
            i ++;
            answer++;
        }       
        System.out.println(answer);
    }
}