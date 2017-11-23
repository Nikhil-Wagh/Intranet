#include<unistd.h>
#include<stdio.h>
#include<fcntl.h>
#include<sys/stat.h>
#include<sys/types.h>
int main()
{
	char buf[1024],fname[10];
	int fd,fd1;
	system("touch test.txt");
	fd=open("test.txt",O_WRONLY);
	printf("\nEnter the message::");
	gets(buf);
	write(fd,buf,sizeof(buf));
	close(fd);
	printf("\nEnter the filename to read::");
	scanf("%s",fname);
	fd1=open(fname,O_RDONLY);
	if(fd1!=3)
	{
		printf("File does not exist\n");
		exit(0);
	}
	read(fd1,buf,sizeof(buf));
	printf("\nFile contents are -> %s\n",buf);
	close(fd1);
	return 0;
}
