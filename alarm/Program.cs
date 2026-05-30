using System;
using System.Formats.Asn1;
using System.Media;
using System.Net.Mail;
using System.Security;
using System.Threading;
class Alarm
{
    static SoundPlayer player;
    static void Main()
    {
        player = new SoundPlayer(@"C:\Windows\Media\Alarm01.wav");
        Console.WriteLine("アラームへようこそ！");
        Console.WriteLine("1時間以上はh、1~59分はm、1~59秒はsを押してね！");
        ConsoleKeyInfo key = Console.ReadKey(intercept: true);
        if(key.Key == ConsoleKey.H)
        {
            Console.WriteLine("時間を入力してください");
            int hour = int.Parse(Console.ReadLine());
            int min = setmin();
            int sec = setsec();
            int total = hour * 3600 + min * 60 + sec;
            bootalarm(total);
        }
        else if(key.Key == ConsoleKey.M)
        {
            int min = setmin();
            int sec = setsec();
            int total = min * 60 + sec;
            bootalarm(total);
        }
        else if(key.Key == ConsoleKey.S)
        {
            int sec = setsec();
            int total = sec;
            bootalarm(total);
        }
    }
static int setmin()
    {
        Console.WriteLine("分を入力してください(最大59分まで)");
        int min = int.Parse(Console.ReadLine());
        if(min > 59)
        {
            min = 59;
        }
        return min;
    }
static int setsec()
    {
        Console.WriteLine("秒を入力してください（最大59秒まで)");
        int sec = int.Parse(Console.ReadLine());
        if(sec > 59)
        {
            sec = 59;
        }
        return sec;
    }
static void bootalarm(int total)
        {
            Console.WriteLine($"{total}秒後にタイマーがなります");
            int keeptotal = total;
            int Soon1 = 0;
            while(total > 0)
            {
                total--;
                Thread.Sleep(1000);
                if(keeptotal / 2 >= total && Soon1 == 0)
            {
                Console.WriteLine($"あと{total}秒後になります");
                Soon1 = 1;
            }
            }
            Console.WriteLine("アラームが鳴ったよ");
            player.PlayLooping();
            Console.WriteLine("アラームを止めるにはキーを押してください。");
            Console.ReadKey(intercept: true);
            player.Stop();
            Console.WriteLine($"アラームを繰り返す場合はr 秒数: {keeptotal}、アラームをもう一度設定する場合はy、終了する場合はnを押してください。");
            ConsoleKeyInfo roop = Console.ReadKey(intercept: true);
            if(roop.Key == ConsoleKey.R)
        {
            bootalarm(keeptotal);
        }
        else if(roop.Key == ConsoleKey.Y)
        {
            Main();
        }
        }
}