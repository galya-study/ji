using System;
					
public class Program
{
	public static void Main()
	{
		string nString;
		nString = Console.ReadLine();
		int n = Int32.Parse(nString);
		
		if ((n < 1) || (n > Math.Pow(10, 7)))
		{
			Console.WriteLine("{0}", n);
		}
		else
		{
			int F0 = 0;
			int F1 = 1;
			int FSum = (F0  + F1) % 10;
			
			F0 = F1;
			F1 = FSum;
			
			for (int i = 3; i < n+1; i++)
			{
				FSum = (F0  + F1) % 10;

				F0 = F1;
				F1 = FSum;
			}
			
			Console.WriteLine("{0}", FSum);
		}		
	}
}
//на вход - число n
//на выход - последняя цифра в числе Фибонначи в позиции n