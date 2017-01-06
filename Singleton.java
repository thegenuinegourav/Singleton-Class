public class MyClass {
    private static MyClass myObject;

    public static MyClass getInstance() {
    
        if(myObject == null)
            myObject = new MyClass();
        
        return myObject;
    }

    public destroy()
    {
    	this.myObject = null
    }

}

/* Now use it anywhere you want

// MyClass myObj = MyClass.getInstance();
// myObj.call(); //call is any method of MyClass
// myObj.destroy;

*/