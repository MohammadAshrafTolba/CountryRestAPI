from locust import HttpUser, between, TaskSet, task
import random


countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina',
             'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
             'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Botswana',
             'Brazil', 'Brunei', 'Bulgaria', 'Burkina', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
             'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Croatia', 'Cuba', 'Cyprus',
             'Denmark', 'Ecuador', 'Egypt', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon',
             'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'usa']

keys = ['name', 'capital', 'area', 'borders','topLevelDomain', 'region']

class MyTaskSet(TaskSet):

    @task(3)
    def task1(self):
        self.client.get('/')

    @task(2)
    def task2(self):
        country_name = random.choice(countries)
        request = '/country/name/{country_name}/'.format(country_name=country_name)
        self.client.get(request)

    @task(2)
    def task3(self):
        country = random.choice(countries)
        key = random.choice(keys)
        request = '/country/name/{country_name}/keys/{key}'.format(country_name=country, key=key)
        self.client.get(request)

    @task(1)
    def stop(self):
        self.interrupt()

class User(HttpUser):
    wait_time = between(5, 15)
    tasks = [MyTaskSet]