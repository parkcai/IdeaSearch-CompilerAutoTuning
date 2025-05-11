# IdeaSearch-CompilerAutoTuning


GCC optimization flags: https://gcc.gnu.org/onlinedocs/gcc-13.1.0/gcc/Optimize-Options.html
可以在这个网站上选一些flags尝试

Benchmark:
该文件夹下存放用于调优的程序集
运行某个程序的命令：
gcc -O3 -c -I {your positition}/utilities {your positition}/utilities/polybench.c {your positition}/datamining/correlation/*.c

gcc -o a.out -O3 -lm *.o

./a.out

Algorithm
该文件夹下存放一些用于调优的算法，后续会继续补充
The `RIO.py` is the code for **Random Iterative Optimization**. For example, if you want to use it to tune program `correlation`, you can input command `python RIO.py --log_file=correlation_rio.log --source_path=/home/user/polybench-code/datamining/correlation --gcc_path=gcc --flag_path=/home/user/flag.txt`.
In this command, `--log_file` is your log file name, `--source_path` is your program path, `--gcc_path` is your compiler path, and `--flag_path` is for your tuning optimization flags. Moreover, if your program has parameters, you need to input `--exec_param`. 


The `CompTuner.py` is the code for **Compiler Autotuning through Multiple Phase Learning**. For example, if you want to use it to tune program `correlation`, you can input command `python CompTuner.py --log_file=correlation_comptuner.log --source_path=/home/user/polybench-code/datamining/correlation --gcc_path=gcc --flag_path=/home/user/flag.txt`.
In this command, `--log_file` is your log file name, `--source_path` is your program path, `--gcc_path` is your compiler path, and `--flag_path` is for your tuning optimization flags. Moreover, if your program has parameters, you need to input `--exec_param`. 