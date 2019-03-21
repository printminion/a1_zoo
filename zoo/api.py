# -*- coding: utf-8 -*-

import requests


class ZooApi:
    base_url = None
    cache_dir = "/tmp/"

    def __init__(self, base_url, cache_dir="/tmp/"):

        self.cache_dir = cache_dir

        if base_url is None or base_url == '':
            raise Exception('Required parameter base_url is empty')

        self.base_url = base_url

    def get_animals(self, local_filename=None):
        if local_filename:
            return self.download_file("/animals", self.cache_dir + local_filename)
        else:
            return self.do_get_request("/animals")

    def get_food(self, local_filename=None):
        if local_filename:
            return self.download_file("/food", self.cache_dir + local_filename)
        else:
            return self.do_get_request("/food")

    def get_zookeeper(self, local_filename=None):

        if local_filename:
            return self.download_file("/zookeeper", self.cache_dir + local_filename)
        else:
            return self.do_get_request("/zookeeper")

    def do_get_request(self, url):
        response = requests.get(self.base_url + url)

        if response.status_code != 200:
            raise Exception('Failed to get ' + url)

        return response.content

    def do_post_request(self, url, data=None):
        response = requests.post(self.base_url + url, data=data)

        if response.status_code != 200:
            raise Exception('Failed to get ' + url)

        return response.text

    def download_file(self, url, local_filename):
        """
        Stream response content to local file system
        :param local_filename:
        :return:
        """
        # NOTE the stream=True parameter below
        with requests.get(self.base_url + url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        # f.flush()
        return local_filename

    def report_to_director(self, most_expensive_compound):
        """

        :param expensive_compound:
        :type most_expensive_compound: string
        :return:
        :rtype: string
        """
        result = self.do_post_request("/director", {"compound": most_expensive_compound})

        return str(result)
