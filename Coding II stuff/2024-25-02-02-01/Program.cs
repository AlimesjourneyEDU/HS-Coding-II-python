using System.Formats.Asn1;

namespace _2024_25_02_02_01
{
    internal class Program
    {
        // the Main method that All
        // programs MUST have
        // The main entry point


        static void Main(string[] args) //Main entry point
        {
            //DoExample01();
            DoExample02();

        }

        static void DoExample01()
        {

            #region basic var. and data type
            int i = 100; // integer data type
            Console.WriteLine(i);

            bool isTrue = false; // boolean data type
            Console.WriteLine(isTrue);

            char letter = 'a'; // letter data type
            Console.WriteLine(letter);

            float gpa = 80 / 9f; // req. to put 'f' after a float
            Console.WriteLine(gpa);

            string name = "Bonetastic"; // string data type
            Console.WriteLine(name);

            Console.Write("Age: ");
            string? input = Console.ReadLine();
            #endregion

            uint age = 17;

            #region if statements
            if (input != null)
            {
                // this means that it's safe to use the nullable variable
                //why? because it's not null
                Console.WriteLine("You entered " + input);
                try
                {
                    age = uint.Parse(input);
                }
                catch (FormatException e)
                {
                    Console.WriteLine(input + " isn't a valid age!");
                    Console.WriteLine("Defaulting to age = " + age);
                }
                catch (OverflowException e)
                {
                    Console.WriteLine("The age you entered is either too low or too high!");
                    Console.WriteLine("Defaulting to age = " + age);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.ToString());
                }
            }

            if (age <= 5)
            {
                Console.WriteLine("You're a baby");
            }
            else if (age < 13)
            {
                Console.WriteLine("You're a child");
            }
            else if ((age >= 13) && (age < 20))
            {
                Console.WriteLine("You're a teenager");
            }
            else if ((age >= 20) && (age <= 30))
            {
                Console.WriteLine("You're a young adult");
            }
            else
            {
                Console.WriteLine("Over the hill");
            }
            #endregion

            #region switch statement
            Console.Write("Favorite Month? "); // Only 12 months
            input = Console.ReadLine();

            if (input != null)
            {
                switch (input.ToLower())
                {
                    case "january":
                        Console.WriteLine("It's an ok month.");
                        break;

                    case "february":
                        Console.WriteLine("A cool month.");
                        break;
                    case "march":
                        Console.WriteLine("Nice month");
                        break;
                    case "april":
                        Console.WriteLine("I don't enjoy this month");
                        break;
                    case "may":
                        Console.WriteLine("Great month");
                        break;
                    case "june":
                        Console.WriteLine("Eh");
                        break;
                    case "july":
                        Console.WriteLine("Firework go boom.");
                        break;
                    case "august":
                        Console.WriteLine("No more boom.");
                        break;
                    case "september":
                        Console.WriteLine("My month. OH YEAH");
                        break;
                    case "october":
                        Console.WriteLine("Ghost.");
                        break;
                    case "november":
                        Console.WriteLine("Underappreciated month.");
                        break;
                    case "december":
                        Console.WriteLine("Takes all the attention from November.");
                        break;
                    default:
                        Console.WriteLine("You've entered a month that doesn't exist.");
                        break;
                }
            }
            #endregion

            SayBye();
        }

        static void DoExample02()
        {
            // declares and allocates an array with 5 ints (default 0)
            int[] numbers = new int[5];
            numbers[0] = 1;
            numbers[1] = 2;
            numbers[2] = 3;
            numbers[3] = 4;
            numbers[4] = 5;


            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine(numbers[i]);
            }

            int[,] mdNumbers = new int[3, 2];
            mdNumbers[0, 0] = 5;
            mdNumbers[0, 1] = 2;
            mdNumbers[1, 0] = 3;
            mdNumbers[1, 1] = 4;
            mdNumbers[2, 0] = 5;
            mdNumbers[2, 1] = 6;

            for (int i = 0; i < 3; i++)
            {
                for (int j = 0; j < 2; j++)
                {
                    Console.WriteLine(mdNumbers[i, j]);
                }
            }
        }
        static void SayHello()
        {
            Console.WriteLine("hello");
        }

        static void SayBye()
        {
            Console.WriteLine("Goodbye");
        }

        // 1) basics / data -> variables data types
        // 2) intermediate level -> classes, generics, ...
        // 3) advanced parts ...
    }
}

/*  the quick brown fox jumps over the lazy dog
 *  the quick brown fox jumps over the lazy dog
 *  the quikc brown fox jumps over the lazy dog
 *  I can type really fast sometimes
 *  sometimes I type really slowly
 *  I can code really well
 *  the quick brown fox jumps over the lazy dog
 *  the quick brown fox jumps over the lazy dog
 *  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
 *  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
 *  tHe QuiCK BrOwn Fox juMpS OveR tHe LazY DoG
 *  tHe QuiCK BrOwn Fox juMpS OveR tHe LazY DoG
 */


