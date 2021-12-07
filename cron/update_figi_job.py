import asyncio

from cron import subscriber_job
from cron.update_figi import main
from db.models.subscribed_user_model import SubscribedUserModel


asyncio.run(main())

users = SubscribedUserModel.select(SubscribedUserModel.user_id)
result = users.execute()
for i in result:
    subscriber_job.main(i.user_id)
