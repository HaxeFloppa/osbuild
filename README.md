<h1 align="center">osbuild</h1>
OSBuild: a linker styled programming language created by HaxeFloppa.
<h2><i><b>I/O stream</b></i></h2>
To print a string, use the following lines to do so:





    BOOTLOADER_PRINT
    {
        DISPLAY HELLO, WORLD!
    }




You can type whatever you want within the "HELLO, WORLD!" part. And no, the string to print doesn't need to be all caps. I'm just trying to look cool.

<h2><i><b>Strings</b></i></h2>
To define a string, write first the type, in this case "STR", then the value.




    BOOTLOADER_PRINT
    {
        STR Hello, world!
    }




To call a string, you'll need to call it by address as all variables are saved to dicts and each dict are classified by type. To do so, the following snippet will present how:




    BOOTLOADER_PRINT
    {
        STR Hello, world!
        STINT 0
    }
