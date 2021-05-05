from celery import Celery
import time
from datetime import datetime
from csv import writer
import logging

#rabbit_broker_url = 'amqps://rgucyrcv:YB-vf1UaOswtAkrXl_QZg5lcLJEFYEpx@prawn.rmq.cloudamqp.com/rgucyrcv'
aws_access_key = 'AKIAUS34HH5EIZWXDBQQ'
aws_secret_key = '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'

broker_url = f'sqs://{aws_access_key}:{aws_secret_key}@'

celery = Celery('tasks', broker=broker_url)
celery.conf["broker_transport_options"] = {
    'region': 'sa-east-1',
    'visibility_timeout': 43200
}
celery.conf["task_default_queue"] = 'TestQueue.fifo'


@celery.task(name='test_count')
def test_count(duration):
    try:
        filename = f"task-{datetime.strftime(datetime.now(), '%d-%m-%Y-%H-%M-%S')}.csv"
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            pointer = writer(file)
            for i in range(duration):
                print(i)
                pointer.writerow([str(i), str(datetime.today())])
                time.sleep(2)

        return 'finish'
    except Exception as error:
        logging.error(error)

