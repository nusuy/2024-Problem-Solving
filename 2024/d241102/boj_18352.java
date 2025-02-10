package d241102;

import java.io.*;
import java.util.*;

public class boj_18352 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        ArrayList<Integer>[] edges = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) edges[i] = new ArrayList<Integer>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            edges[a].add(b);
        }
        new boj_18352().solution(n,k,x,edges);
    }

    private void solution(int n, int k, int x, List<Integer>[] edges) throws Exception {
        int[] cities = new int[n+1];
        cities[x] = 1;
        Queue<Integer> q = new LinkedList<>();
        q.add(x);
        while (!q.isEmpty()) {
            int c = q.poll();
            for (int e : edges[c]) {
                if (cities[e] == 0) {
                    cities[e] = cities[c] + 1;
                    q.add(e);
                }
            }
        }

        boolean flag = false;
        for (int i = 0; i < cities.length; i++) {
            if (cities[i] == k+1){ 
                System.out.println(i);
                flag = true;
            }
        }
        if (!flag)
            System.out.println(-1);
    }
}