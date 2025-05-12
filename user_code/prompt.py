__all__ = [
    "prologue_section",
    "epilogue_section",
]


system_prompt = (
    "你是一位软件工程领域的专家，拥有丰富的文法知识，掌握许多测试用例生成的技术。"
    "现在，你需要帮助我们生成 SysY 语言（C语言的一个教学用子集）的若干测试用例，"
    "你马上就会了解到什么是 SysY 语言，在那以后你会认真地帮助我们完成任务，生成若干"
    "符合要求、覆盖率高、趣味盎然的测试用例，并且你在生成测试用例之余绝不说多余的话。"
)


prologue_section_lv5 = (
    "你好！我希望在你的帮助下，完成SysY语言的测试用例生成工作，希望我们合作愉快！\n"
    "SysY语言是一个用于教学的简单语言，它是C语言的一个真子集，具体来说，它不支持for循环，不支持浮点类型及更多类型，"
    "但支持while循环，支持整型（int）及其计算，支持整型的一维及多维数组，支持基本的变量与常量，"
    "这些内容已经使它图灵完备，可以完成多样的内容。\n"
    "现在，我手头有很多的SysY编译器，但是我不知道它们是对是错，我希望你生成一些测试用例来测试它们。"
    "眼下，我希望你生成SysY语言的一个真子集中的测试用例，这个简单真子集仅由一个main函数组成，仅仅支持"
    "整型的若干表达式运算、变量和常量、语句与作用域，其他内容都不支持。具体来说，描述这个真子集的文法如下："
    'CompUnit      ::= FuncDef;\n'
    'Decl          ::= ConstDecl | VarDecl;\n'
    'ConstDecl     ::= "const" BType ConstDef {"," ConstDef} ";";\n'
    'BType         ::= "int";\n'
    'ConstDef      ::= IDENT "=" ConstInitVal;\n'
    'ConstInitVal  ::= ConstExp;\n'
    'VarDecl       ::= BType VarDef {"," VarDef} ";";\n'
    'VarDef        ::= IDENT | IDENT "=" InitVal;\n'
    'InitVal       ::= Exp;\n'
    'FuncDef       ::= FuncType IDENT "(" ")" Block;\n'
    'FuncType      ::= "int";\n'
    'Block         ::= "{" {BlockItem} "}";\n'
    'BlockItem     ::= Decl | Stmt;\n'
    'Stmt          ::= LVal "=" Exp ";"\n'
    '                | [Exp] ";"\n'
    '                | Block\n'
    '                | "return" [Exp] ";";\n'
    'Exp           ::= LOrExp;\n'
    'LVal          ::= IDENT;\n'
    'PrimaryExp    ::= "(" Exp ")" | LVal | Number;\n'
    'Number        ::= INT_CONST;\n'
    'UnaryExp      ::= PrimaryExp | UnaryOp UnaryExp;\n'
    'UnaryOp       ::= "+" | "-" | "!";\n'
    'MulExp        ::= UnaryExp | MulExp ("*" | "/" | "%") UnaryExp;\n'
    'AddExp        ::= MulExp | AddExp ("+" | "-") MulExp;\n'
    'RelExp        ::= AddExp | RelExp ("<" | ">" | "<=" | ">=") AddExp;\n'
    'EqExp         ::= RelExp | EqExp ("==" | "!=") RelExp;\n'
    'LAndExp       ::= EqExp | LAndExp "&&" EqExp;\n'
    'LOrExp        ::= LAndExp | LOrExp "||" LAndExp;\n'
    'ConstExp      ::= Exp;\n'
    "请你帮我生成一些测试用例！不过，"
    "你可以先看看以下这些现有的例子，Score是它们的得分，Info（若有）是对它们的评语！\n"
)

epilogue_section_lv5 = (
    "看了以上例子，相信你已经明白该怎样生成合法的且优秀的测试用例了！"
    "请注意，我们的希望是，在满足文法要求的前提下，尽可能探索文法的结构，但决不能和现有的例子过分重复。"
    "此外，我们希望测试用例以如下header开头：\n"
    "'******.c******'\n"
    "请你生成，一个即可！请不要生成多个测试用例，也请不要说多余的话，你的回答仅应该包含"
    "一个满足格式要求（以header开头）的测试用例！\n"
)

prologue_section_lv9 = (
    "你好！我希望在你的帮助下，完成SysY语言的测试用例生成工作，希望我们合作愉快！\n"
    "SysY语言是一个用于教学的简单语言，它是C语言的一个真子集，具体来说，它不支持for循环，不支持浮点类型及更多类型，"
    "但支持while循环，支持整型（int）及其计算，支持整型的一维及多维数组，支持基本的变量与常量，"
    "这些内容已经使它图灵完备，可以完成多样的内容。\n"
    "现在，我手头有很多的SysY编译器，但是我不知道它们是对是错，我希望你生成一些测试用例来测试它们。"
    "下面我会告诉你关于SysY语言的更多信息。\n"
    "首先，SysY语言支持的注释与C语言一致：\n"
    "1. 单行注释: 以序列 // 开始, 直到换行符结束, 不包括换行符.\n"
    "2. 多行注释: 以序列 /* 开始, 直到第一次出现 */ 时结束, 包括结束处 */.\n"
    "其次，SysY的完整文法如下所示：\n"
    'CompUnit      ::= [CompUnit] (Decl | FuncDef);\n'
    'Decl          ::= ConstDecl | VarDecl;\n'
    'ConstDecl     ::= "const" BType ConstDef {"," ConstDef} ";";\n'
    'BType         ::= "int";\n'
    'ConstDef      ::= IDENT {"[" ConstExp "]"} "=" ConstInitVal;\n'
    'ConstInitVal  ::= ConstExp | "{" [ConstInitVal {"," ConstInitVal}] "}";\n'
    'VarDecl       ::= BType VarDef {"," VarDef} ";";\n'
    'VarDef        ::= IDENT {"[" ConstExp "]"}\n'
    '                | IDENT {"[" ConstExp "]"} "=" InitVal;\n'
    'InitVal       ::= Exp | "{" [InitVal {"," InitVal}] "}";\n'
    'FuncDef       ::= FuncType IDENT "(" [FuncFParams] ")" Block;\n'
    'FuncType      ::= "void" | "int";\n'
    'FuncFParams   ::= FuncFParam {"," FuncFParam};\n'
    'FuncFParam    ::= BType IDENT ["[" "]" {"[" ConstExp "]"}];\n'
    'Block         ::= "{" {BlockItem} "}";\n'
    'BlockItem     ::= Decl | Stmt;\n'
    'Stmt          ::= LVal "=" Exp ";"\n'
    '                | [Exp] ";"\n'
    '                | Block\n'
    '                | "if" "(" Exp ")" Stmt ["else" Stmt]\n'
    '                | "while" "(" Exp ")" Stmt\n'
    '                | "break" ";"\n'
    '                | "continue" ";"\n'
    '                | "return" [Exp] ";";\n'
    'Exp           ::= LOrExp;\n'
    'LVal          ::= IDENT {"[" Exp "]"};\n'
    'PrimaryExp    ::= "(" Exp ")" | LVal | Number;\n'
    'Number        ::= INT_CONST;\n'
    'UnaryExp      ::= PrimaryExp | IDENT "(" [FuncRParams] ")" | UnaryOp UnaryExp;\n'
    'UnaryOp       ::= "+" | "-" | "!";\n'
    'FuncRParams   ::= Exp {"," Exp};\n'
    'MulExp        ::= UnaryExp | MulExp ("*" | "/" | "%") UnaryExp;\n'
    'AddExp        ::= MulExp | AddExp ("+" | "-") MulExp;\n'
    'RelExp        ::= AddExp | RelExp ("<" | ">" | "<=" | ">=") AddExp;\n'
    'EqExp         ::= RelExp | EqExp ("==" | "!=") RelExp;\n'
    'LAndExp       ::= EqExp | LAndExp "&&" EqExp;\n'
    'LOrExp        ::= LAndExp | LOrExp "||" LAndExp;\n'
    'ConstExp      ::= Exp;\n'
    "请你仔细阅读以上文法、认真思考，请注意，一些常见的错误点在于：\n"
    "1. SysY语言不支持三目运算符 condition ? expr1 : expr2，这在SysY语言里是错误的\n"
    "2. SysY语言不支持for循环，不支持浮点类型及更多类型（只支持int），不支持指针和取地址操作\n"
    "3. SysY语言不支持a += 1或a++这样的语法糖，必须写成a = a + 1才能正确解析\n"
    "4. SysY语言不支持&、|这样的逐比特运算符，仅支持&&、||这样的逻辑运算符，并且在语义上短路地处理逻辑运算符！\n"
    "5. SysY语言中的常量const int和C语言中的不一样！C语言中，常量仅表示定义后不可修改；"
    "但是，SysY语言中，常量必须在编译期即可求值。具体而言，以下语句：\n"
    "int a = 1;\n"
    "const b = a;\n"
    "在SysY语言中是非法的（因此你不该生成这样的测试用例）！"
    "但是，在C语言中，只要接下来b的值不被修改，就是合法的。\n"
    "6. SysY语言中，shadow行为（作用域内的变量覆盖作用域外的同名变量）是允许的，并且我们鼓励你"
    "适当生成包含shadow行为的代码，来测试编译器符号表的正确性。但是，请不要生成以下这种corner case：\n"
    "...\n"
    "int x = getint();\n"
    "int i = 0;\n"
    "int arr[3] = {1, 2, 3};\n"
    "{\n"
    "    {\n"
    "        int x = x + 1; // Don't generate this!\n"
    "        int i = arr[i]; // Don't generate this either!\n"
    "        putint(x);\n"
    "    }\n"
    "}\n"
    "...\n"
    "具体来说，我们不希望在同一个语句里同时出现变量的声明和使用，哪怕变量实质上可以tricky地理解为分属为两个作用域的不同同名变量。"
    "尽管在一些标准里，这个corner case并非未定义行为，但是gcc会认为这段代码中x和i在使用前未被定义。\n"
    "7. 如果SIZE是一个常整数，那么用其定义数组int array[SIZE];可能是一个常见的行为，"
    "但是对于SysY语言，我们不希望你这样做！\n"
    "8. 常数数组不可以作为参数传入接收数组参数的函数中！\n"
    "9. 用于初始化常数数组的ConstInitVal中，不可以出现变量、对数组的引用和函数调用；"
    "用于初始化可变数组的InitVal中，可以出现变量和对数组的引用，但不能出现函数调用，因为函数调用的求值顺序是未定义行为！\n"
    "此外，SysY语言有一些默认可用的库函数，在使用这些库函数前你无需手动定义它们，也不用include，"
    "我们的测试系统会自动帮你链接。譬如，下面的SysY程序：\n"
    'int main() {\n'
    '    return getint();\n'
    '}\n'
    "完全没有定义getint，也没有引入头文件，但它是合法的，因为getint是SysY的库函数。\n"
    "SysY的库函数一共有下面这些：\n"
    "1. int getint()   从标准输入读取一个整数, 返回对应的整数值. 如果未能读取到任何整数 (例如遇到了 EOF), 则返回值未定义.\n"
    "2. int getch()   从标准输入读取一个字符, 返回字符对应的 ASCII 码值. 如果读取到了 EOF, 则返回 -1.\n"
    "3. int getarray(int[])   从标准输入读取一串整数, 其中第一个整数代表后续出现整数的个数, 该数值通过返回值返回; 后续的整数通过传入的数组参数返回\n"
    "4. void putint(int)   输出一个整数的值.\n"
    "5. void putch(int)   将整数参数的值（0~255）作为 ASCII 码, 输出该 ASCII 码对应的字符.\n"
    "6. void putarray(int, int[])    第 1 个参数指定了输出整数的个数 (假设为 N), 第 2 个参数指向的数组中包含 N 个整数. putarray 在输出时会在整数之间安插空格.\n"
    "7. void starttime()   开启计时器. 此函数应和 stoptime() 联用.【请注意，函数starttime有特殊用途，你生成的测试用例不应包含这一库函数！】\n"
    "8. void stoptime()   停止计时器. 此函数应和 starttime() 联用.【请注意，函数stoptime有特殊用途，你生成的测试用例不应包含这一库函数！】\n"
    "无须额外操作，测试用例就可以方便地使用这些函数。但是，请注意，也正因如此，"
    "为避免混乱你不应该在测试用例中定义和库函数同名的函数。\n"
    "请你帮我生成一些测试用例！不过，"
    "你可以先看看以下这些现有的例子，Score是它们的得分（满分为100分），Info（若有）是对它们的评语！\n"
)

epilogue_section_lv9 = (
    "看了以上例子，相信你已经明白该怎样生成合法的且优秀的测试用例了！"
    "请注意，我们的希望是，在满足文法要求的前提下，尽可能探索文法的结构，除了main函数可以多多定义函数，也请多多使用库函数，"
    "但决不能和现有的例子过分重复。\n"
    "此外，我们鼓励你在测试用例中多写注释（单行&多行！），甚至是用测试用例完成一个意图明确的功能！"
    "最后，我们希望测试用例以如下header开头：\n"
    "'******.c******'\n"
    "如果测试用例使用了getch、getint等库函数、需要有输入，请在.c部分结束后输出input section的header：\n"
    "'******.in******'\n"
    "然后再写测试用例的输入。\n"
    "注意，测试用例的输入是可选的，不是必须的。如果不需要输入，请不要打input section header！\n"
    "现在，你可以生成测试用例了，一个即可！请不要生成多个测试用例，也务必不要说多余的话；请注意，你的回答仅应该包含"
    "一个满足格式要求的测试用例！\n"
)


prologue_section = prologue_section_lv9
epilogue_section = epilogue_section_lv9