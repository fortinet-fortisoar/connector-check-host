"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end

"""
import requests
from connectors.core.connector import get_logger, ConnectorError
logger = get_logger('check-host')


class CheckHost(object):

    def __init__(self, config):
        self.server_url = config.get('server_url','').strip('/')
        self.headers = {'accept': 'application/json'}
        if not self.server_url.startswith('https://') and not self.server_url.startswith('http://'):
            self.server_url = 'https://' + self.server_url

    def make_api_call(self, endpoint=None, method='GET', headers=None, health_check=False):
        url = self.server_url + endpoint
        logger.debug('RESP API Endpoint: {0}'.format(url))
        if headers:
            self.headers.update(headers)
        try:
            logger.debug('Making a request with {0} method and {1} headers.'.format(method, self.headers))
            response = requests.request(method, url, headers=self.headers)
            if response.status_code in [200]:
                if health_check:
                    return response.json()
                try:
                    logger.debug(
                        'Converting the response into JSON format after returning with status code: {0}'.format(
                            response.status_code))
                    response_data = response.json()
                    return {'status': response_data['status'] if 'status' in response_data else 'Success',
                            'data': response_data}
                except Exception as e:
                    response_data = response.content
                    logger.error('Failed with an error: {0}. The response details are: {1}'.format(e, response_data))
                    return {'status': 'Failure', 'data': response_data}
            else:
                logger.error('Failed with response {0}'.format(response.text))
                raise ConnectorError(
                    {'status': 'Failure', 'status_code': str(response.status_code), 'response': response.text})
        except Exception as e:
            logger.exception(str(e))
            raise ConnectorError(str(e))


def ping_check(config, params):
    obj = CheckHost(config)
    endpoint = f"/check-ping?host={params.get('host')}&max_nodes={params.get('max_nodes')}"
    return obj.make_api_call(endpoint=endpoint, health_check=True)


def http_check(config, params):
    obj = CheckHost(config)
    endpoint = f"/check-http?host={params.get('host')}&max_nodes={params.get('max_nodes')}"
    return obj.make_api_call(endpoint=endpoint, health_check=True)


def tcp_connection_check(config, params):
    obj = CheckHost(config)
    endpoint = f"/check-tcp?host={params.get('host')}&max_nodes={params.get('max_nodes')}"
    return obj.make_api_call(endpoint=endpoint, health_check=True)


def dns_address_check(config, params):
    obj = CheckHost(config)
    endpoint = f"/check-dns?host={params.get('host')}&max_nodes={params.get('max_nodes')}"
    return obj.make_api_call(endpoint=endpoint, health_check=True)


def check_result_by_request_id(config, params):
    obj = CheckHost(config)
    return obj.make_api_call(endpoint=f"/check-result/{params.get('request_id')}", health_check=True)


def _check_health(config):
    try:
        obj = CheckHost(config)
        obj.make_api_call(endpoint='/check-http?host=check-host.net&max_nodes=3', health_check=True)
        return True
    except Exception as err:
        logger.exception('Health check failed with: {0}'.format(err))
        raise ConnectorError('Health check failed with: {0}'.format(err))


operations = {
    'ping_check': ping_check,
    'check_result_by_request_id': check_result_by_request_id,
    'http_check': http_check,
    'tcp_connection_check': tcp_connection_check,
    'dns_address_check': dns_address_check
}
