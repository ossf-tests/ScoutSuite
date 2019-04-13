from ScoutSuite.providers.aws.facade.base import AWSFacade
from ScoutSuite.providers.aws.resources.base import AWSResources


class ParameterGroups(AWSResources):
    def __init__(self, facade: AWSFacade, region: str, **kwargs):
        self.facade = facade
        self.region = region

    async def fetch_all(self, **kwargs):
        raw_parameter_groups = await self.facade.elasticache.get_parameter_groups(self.region)
        for raw_parameter_group in raw_parameter_groups:
            name, resource = self._parse_parameter_group(raw_parameter_group)
            self[name] = resource

    def _parse_parameter_group(self, raw_parameter_group):
        raw_parameter_group['name'] = raw_parameter_group.pop('CacheParameterGroupName')
        return raw_parameter_group['name'], raw_parameter_group
