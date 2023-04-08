BOOTLOADER_PRINT
{
    INT_DEF 69
    INT_CALL 0
    STR_DEF Hi, I'm gonna place error.
    STRING_CALL 0
    THROW This is error I refer to.
}