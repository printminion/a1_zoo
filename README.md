A1 Zoo 🐼
========================

To run as docker image with composer
```bash
#build image
docker-compose build
```


```bash
#run with cli 
docker-compose run cli python calculate.py --api_base_url=http://prod.example.de:8020
```
 

To run as docker container with composer
```bash
docker build . -t a1_zoo
docker run -it --rm a1_zoo python calculate.py --api_base_url=http://prod.example.de:8020
```

Configurable via CLI arguments or via ENV


API_BACKEND=http://prod.example.de:8020

python calculate.py --api_base_url=http://prod.example.de:8020

```
$ docker-compose run cli python calculate.py --api_base_url=http://prod.example.de:8020
2019-03-21 21:19:23,521 - a1_zoo - INFO - Begin session
2019-03-21 21:19:23,521 - a1_zoo - INFO - API_BASE_URL: http://prod.example.de:8020
2019-03-21 21:19:23,521 - a1_zoo - INFO - LOG_LOGGER: a1_zoo
2019-03-21 21:19:23,522 - a1_zoo - INFO - LOG_FILE: a1_zoo.log
2019-03-21 21:19:23,522 - a1_zoo - INFO - CACHE_DIR: /tmp/a1_zoorjabveu5/
2019-03-21 21:19:23,522 - a1_zoo - INFO - Start Zoo Session
2019-03-21 21:19:23,522 - a1_zoo - INFO - Download and save data locally
2019-03-21 21:19:23,522 - a1_zoo - INFO - get animals...
2019-03-21 21:19:23,570 - a1_zoo - INFO - done
2019-03-21 21:19:23,571 - a1_zoo - INFO - get food data...
2019-03-21 21:19:23,641 - a1_zoo - INFO - done
2019-03-21 21:19:23,642 - a1_zoo - INFO - get zookeeper data...
2019-03-21 21:19:23,686 - a1_zoo - INFO - done
2019-03-21 21:19:23,740 - a1_zoo - INFO - total_amount_per_animal: 2027.7142857142856
2019-03-21 21:19:23,745 - a1_zoo - INFO - total_cost_per_compound: compound
alligators    472.857143
big_cat       790.285714
bird          256.571429
water_bird    508.000000
Name: total_cost_per_day_per_animal, dtype: float64
2019-03-21 21:19:23,749 - a1_zoo - INFO - most_expensive_compound: big_cat
2019-03-21 21:19:23,749 - a1_zoo - INFO - report to director
2019-03-21 21:19:23,793 - a1_zoo - INFO - directors response: You made it!
================================

Yay, you helped the zoo having a future plan.
Due to your awesomeness the zoo director recommends you to send a message
with the code word "Jumpstart" and the code you wrote
to example@example.com.
:
2019-03-21 21:19:23,793 - a1_zoo - INFO - done
```