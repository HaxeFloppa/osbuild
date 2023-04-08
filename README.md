<h1 align="center">osbuild</h1>
<p align="center"><i>OSBuild: a linker styled programming language created by HaxeFloppa.</i></p>
<h2><i><b>I/O stream</b></i></h2>
To print a string, use the following lines to do so:





    BOOTLOADER_PRINT
    {
        DISPLAY HELLO, WORLD!
    }




You can type whatever you want within the "HELLO, WORLD!" part. And no, the string to print doesn't need to be all caps. I'm just trying to look cool.

<h2><i><b>Strings</b></i></h2>
To define a string, write first the type, in this case "STR_DEF", then the value.




    BOOTLOADER_PRINT
    {
        STR_DEF Hello, world!
    }




To call a string, you'll need to call it by address as all variables are saved to dicts and each dict are classified by type. To do so, the following snippet will present how:




    BOOTLOADER_PRINT
    {
        STR_DEF Hello, world!
        STRING_CALL 0
    }




<h2><i><b>Integers</b></i></h2>
To define an integer, it works the same way as defining a string does:




    BOOTLOADER_PRINT
    {
        INT_DEF 69
    }




To call said integer, again, it works exactly the same as calling strings:




    BOOTLOADER_PRINT
    {
        INT_DEF 69
        INT_CALL 0
    }



<h2><i><b>Exceptions</b></i></h2>
If you wish to throw an error to the terminal for something that you consider wrong, yet the compiler doesn't, you can use the throw command and type a string to show as the cause of said error, for example:




    BOOTLOADER_PRINT
    {
        THROW haxefloppa knew you'd rush B
    }