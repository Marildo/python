from flask import Flask, make_response
from task import test_count
app = Flask('Test-celery')

app.config['CELERY_BROKER_URL'] = 'https://sqs.us-east-1.amazonaws.com/315403747144/TestQueue.fifo'
app.config['CELERY_TASK_DEFAULT_QUEUE'] = 'TestQueue.fifo'


@app.route('/')
def index():
    return make_response({'msg': 'Server is running...'}, 200)


@app.route('/test/<int:duration>')
def test(duration):
    for i in range(0, 2):
        test_count.delay(duration)
    return make_response({'msg': 'Processing...'}, 200)


app.run(debug=True, port=3300)
