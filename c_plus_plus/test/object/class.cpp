/* ######## Abstract Code
 *
 * class Class_name 
 * {
 *     private:
 *          data member
 *          function
 *     public:
 *          data member
 *          function
 *  };
 *
 *  ######## Inside code there are data member and variable member, private and public are access control
 *
 *  class Person
 *  {
 *  private:
 *      int age;
 *      string name;
 *  public:
 *      double bw;
 *      int show();
 *  };
 *
 *  ######## if you remove the private part like this:
 *
 *  class Person
 *  {
 *      int age;     // part from here will be private
 *      string name;
 *      
 *  public:          // part from here will be public
 *      double vw;
 *      int show();
 *  };
 *
 * ######## function inside class will be defined outside class and connect to the class by "::(scope resolution operator)" . With this the speed of calling 
 * ######## the function and return value will be a little bit slower but the program size will be smaller, if you define function inside class it will be faster but 
 * ######## the program will be longer. And there is inline that will help that when the compiler run the function attach to inline (being short enough) will be 
 * ######## considered as defined inside a class and have lower cost when you call out the function "inline type ClassName::functionName(argument) {...}"
