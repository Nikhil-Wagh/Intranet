#include<unistd.h>
#include<pthread.h>
#include<stdio.h>
#include<semaphore.h>
sem_t empty,full;
pthread_mutex_t m;
int buff[5];
void *producer(void *arg)
{
	printf("\nProducer thread created");
	sleep(5);
	int item,i=0;
	while(1)
	{
		sem_wait(&empty);
		item=random()%10;
		pthread_mutex_lock(&m);
		buff[i++]=item;
		printf("\n%d item is inserted at %d location\n",item,i-1);
		if(i==5)
			i=0;
		sleep(1);
		pthread_mutex_unlock(&m);
		sem_post(&full);
	}
	
}
void *consumer(void *arg)
{
	printf("\nConsumer thread created");
	sleep(5);
	int key,i=0;
	while(1)
	{
		sem_wait(&full);
		pthread_mutex_lock(&m);
		key=buff[i++];
		printf("\n%d key is extracted from %d location\n",key,i-1);
		if(i==5)
			i=0;
		sleep(1);
		pthread_mutex_unlock(&m);
		sem_post(&empty);
	}
}
int main()
{
	sem_init(&empty,0,5);
	sem_init(&full,0,0);
	pthread_mutex_init(&m,NULL);
	pthread_t pid,cid;
	pthread_create(&pid,NULL,producer,NULL);
	sleep(1);
	pthread_create(&cid,NULL,consumer,NULL);
	sleep(1);
	pthread_join(pid,NULL);
	pthread_join(cid,NULL);
	printf("\nMain thread terminated\n");
}
