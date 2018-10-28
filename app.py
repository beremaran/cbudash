#!/usr/bin/env python3
import json
import redis

from celery.schedules import crontab
from flask import Flask
from flask import jsonify, render_template

from cbudash.dash import CBUDash
from cbudash.tasks import make_celery

application = Flask(__name__)

application.config['CELERY_BROKER_URL'] = 'redis://redis:6379'
application.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379'

celery = make_celery(application)
redis_db = redis.StrictRedis('redis', port=6379, db=0)
cbu_dash = CBUDash()


def get_news():
    news = redis_db.get('cbu_news')
    if news is None:
        news = cbu_dash.get(True)
        update_cache.delay()
    else:
        news = json.loads(news.decode('utf-8'))

    return news


@application.route('/')
def index():
    return render_template('index.html', news=get_news())


@application.route('/feed.json')
def feed():
    return jsonify(get_news())


@celery.on_after_configure.connect()
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour='*', minute='*'),
        update_cache.s()
    )


@celery.task()
def update_cache():
    print('Refreshing news sources')
    redis_db.set('cbu_news', json.dumps(cbu_dash.get(True)))
    print('News sources are refreshed.')


if __name__ == '__main__':
    application.run()
