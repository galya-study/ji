using System;
					
public class Program
{
	public static void Main()
	{
        string nString;
		nString = Console.ReadLine();
		int n = Int32.Parse(nString);
		
		if ((n < 1) || (n > 40))
		{
			Console.WriteLine("{0}", n);
		}
		else
		{
			int[] f = new int[n+1];
			f[0] = 0;
			f[1] = 1;
			
			for (int i = 2; i < n+1; i++)
			{
				f[i] = f[i - 1] + f[i - 2];
			}
			
			Console.WriteLine("{0}", f[n]);
		}		
	}
}
//на вход - число n
//на выход - число Фибонначи в позиции n