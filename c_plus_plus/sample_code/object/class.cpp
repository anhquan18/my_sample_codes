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
 * ### function inside class will be defined outside class and connect to the class by "::(scope resolution operator)" 
 *
 * ### With this the speed of calling the function and return value will be a little bit slower 
 * but the program size will be smaller, if you define function inside class it will be faster 
 * but the program will be longer 
 *
 * ### Inline function will help the compiler run the function attach to inline (being short enough) 
 * will be considered as defined inside a class and have lower cost when you call out the function 
 * Ex: "inline type ClassName::functionName(argument) {...};"
 *
 * ### Dot('.') operator access the members of plain data structures
 * Ex: "class_name.member_name(member function name);"
 *
 * ### Constructor: special class members called by an constructor every time an object of that class is isntantiated.
 * Constructors have the same name as the class and may be defined outside or inside the class definition.
 * There are 3 types of constructors: Default, Parametrized, Copy
 * Copy:a class member function which intializes an object using another object of the same class
 * Copy Constructor is called in following cases:
 * 1.When an object of the class is returned by value
 * 2.When an object of the class is passed(to a function) by values as an argument
 * 3.When an object is constructed based on another object of the same class
 * 4.When the compiler generates a temporary object
 * However there are certain cases Copy Constructor is not called(Ex: https://en.wikipedia.org/wiki/Copy_elision#Return_value_optimization)
 *
 * ### Destructors
