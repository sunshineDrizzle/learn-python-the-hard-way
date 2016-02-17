from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()
indata = open(from_file).read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

# study drill 1, 2
# 要想精简代码，首先，导入exists这个属性在这个程序中没有实际功能所以有关这个的语句可以省略
# 利用硬编码文件名可以省去使用argv的语句，再省去打印与提示语句、中间变量以及close方法的调用就可以精简成一条语句了

# study drill 4
# 文件或者类文件对象的close方法的作用主要有两个：
# 1. 释放资源。打开一个文件，对文件进行操作，这个过程需要消耗计算机的硬件资源，
# 最主要的就是内存(比如接下来要说的"读写缓冲区")，调用close方法后，文件对象占用的资源就会被释放。
# 2.清空缓冲区。当你打开一个文件向里面写入数据或者从某个url获取远程html想对其进行解析，这时候就会用到缓冲区的概念。
# 比如你要写入文件，你想写入文件的数据并不会直接输出到那个文件中，而是首先被输出到缓冲区，等到缓冲区满或者手动刷新时，
# 才将缓冲区中已有的数据输出到文件中(这样设计的原因是避免了频繁I/O，提高了效率)。因此，close方法的另一个作用就是清空
# 缓冲区中的数据(当然你也可以调用flush这样的方法)

# 如果不调用close方法关闭文件，首先占用的硬件资源被浪费，其次数据可能无法像预期的那样正确输出到文件，
# 可能出现空白文件或者数据输出不完整的情况。此外，由于文件对象未关闭，你仍然可能对它进行操作，
# 误操作的话会给调试惹不少麻烦，也有可能成为一种不安全因素。
