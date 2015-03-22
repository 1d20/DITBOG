from django.http import HttpResponse
from tasks import add   

def test(request):

    res = add.apply_async((1, 4), task_id='123')

    #res.id = d6b3aea2-fb9b-4ebc-8da4-848818db9114
    #res.state = PENDING -> STARTED -> RETRY -> STARTED -> RETRY -> STARTED -> SUCCESS
    #>>> res.failed() = True
    #>>> res.successful() = False

    # >>> from proj.celery import app
    # >>> res = app.AsyncResult('this-id-does-not-exist')
    # >>> res.state
    # 'PENDING'


    return HttpResponse({'result': 'ok'}, content_type='application/json')

    # cancel task
    # >>> from proj.celery import app
    # >>> app.control.revoke(task_id)
    # or
    # >>> from celery.task.control import revoke
    # >>> revoke(task_id, terminate=True)
