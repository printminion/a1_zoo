#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging

from zoo import settings
from zoo.api import ZooApi

import os
import sys, getopt

from zoo.calculator import ZooCalculator


def init_logger():
    """
    initialize logger
    """
    logger = logging.getLogger(settings.LOG_LOGGER)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(settings.LOG_FILE)
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

def get_env_config(env_variable):
    if env_variable not in os.environ.keys():
        print("Error: please define %s env variable" % env_variable)
        exit(1)

    print(os.environ[env_variable])


def main(argv):


    try:
        opts, args = getopt.getopt(argv, "hb:m:", ["api_base_url=", "method="])
    except getopt.GetoptError:
        print('calculate.py -b <api_base_url>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('calculate.py -b <api_base_url>')
            sys.exit()

        elif opt in ("-b", "--api_base_url"):
            settings.API_BASE_URL = arg
        elif opt in ("-m", "--method"):
            settings.METHOD = arg

    log = init_logger()

    if settings.API_BASE_URL == '' or settings.API_BASE_URL == None:
        print("No --api_base_url= is set. try to get API_BASE_URL env")
        settings.API_BASE_URL = get_env_config('API_BASE_URL')

    if settings.API_BASE_URL == '' or settings.API_BASE_URL == None:
        print('Please set --api_base_url=')
        sys.exit(2)


    log.info("Begin session")
    log.info("API_BASE_URL: %s" % settings.API_BASE_URL)
    log.info("LOG_LOGGER: %s" % settings.LOG_LOGGER)
    log.info("LOG_FILE: %s" % settings.LOG_FILE)
    log.info("CACHE_DIR: %s" % settings.CACHE_DIR)

    log.info('Start Zoo Session')
    api = ZooApi(settings.API_BASE_URL, settings.CACHE_DIR)

    log.info('Download and save data locally')

    log.info('get animals...')
    api.get_animals("animals.json")
    log.info('done')

    log.info('get food data...')
    api.get_food("food.json")
    log.info('done')

    log.info('get zookeeper data...')
    api.get_zookeeper("zookeeper.json")
    log.info('done')

    calculator = ZooCalculator(
        settings.CACHE_DIR + "animals.json",
        settings.CACHE_DIR + "food.json",
        settings.CACHE_DIR + "zookeeper.json"
    )

    total_amount_per_animal = calculator.calculate_total_animals_cost()

    log.info("total_amount_per_animal: {}".format(total_amount_per_animal))

    total_cost_per_compound = calculator.calculate_total_cost_per_compound()

    log.info("total_cost_per_compound: {}".format(total_cost_per_compound))

    most_expensive_compound = calculator.calculate_total_cost_per_compound(True)

    log.info("most_expensive_compound: {}".format(most_expensive_compound))

    log.info("report to director")
    result = api.report_to_director(most_expensive_compound)
    log.info("directors response: {}:".format(result))

    log.info("done")


if __name__ == "__main__":
    main(sys.argv[1:])
